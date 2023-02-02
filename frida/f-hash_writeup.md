First we try to understand why the program doesn't end (where is it stuck)
perhaps at some recursive calls flow that takes forever

aero@AERO-PC:~/tools/frida/ctf$ frida-discover f-hash
Tracing 1 threads. Press ENTER to stop.
^C
f-hash
        Calls           Function
        360463          sub_12a0   
        360433          sub_13b0

sub_12a0: note that it's called more times than sub_13b0 

We will go into IDA/Ghidra and see that sub_13b0 is the recursion entry point and it has two conditional calls to  sub_12a0:

struct res_struct {
  int64_t a;
  int64_t b;
  int64_t c;
};

result *__fastcall outer_recursive_func(result *result, int a2, __int64 a3, __int64 a4)
{
  __int64 res_B; // rax
  __int64 v7; // rdx
  __int64 res_A; // rax
  __int64 v10; // rdx
  __int64 v11; // r13
  __int128 v12; // rax
  __int128 v13; // rax
  __int128 v14; // rcx
  result res_C; // [rsp+0h] [rbp-78h] BYREF
  result res_D; // [rsp+20h] [rbp-58h] BYREF
  unsigned __int64 canary; // [rsp+48h] [rbp-30h]

  canary = __readfsqword(0x28u);
  if ( a2 == 1 )
  {
    res_A = inner_heavy_math(a3, a4);
    result->c = 0LL;
    result->a = res_A;
    result->b = v10;
  }
  else if ( a2 == 2 )
  {
    res_B = inner_heavy_math(a3 ^ 1, a4);
    result->c = 1LL;
    result->a = res_B;
    result->b = v7;
  }
  else
  {
    outer_recursive_func(&res_C, a2 - 1, a3, a4);
    outer_recursive_func(&res_D, a2 - 2, a3, a4);
    v11 = res_C.c + res_D.c;
    *(_QWORD *)&v12 = inner_heavy_math((res_C.c + res_D.c) ^ a3, a4);
    v13 = *(_OWORD *)&res_C.a + *(_OWORD *)&res_D.a + v12;
    v14 = *(_OWORD *)(qword_203138 + 16LL * a2);
    if ( *((_QWORD *)&v14 + 1) <= *((_QWORD *)&v13 + 1) )
    {
      if ( *((_QWORD *)&v14 + 1) >= *((_QWORD *)&v13 + 1) )
        goto LABEL_11;
      do
      {
        do
          v13 -= v14;
        while ( *((_QWORD *)&v14 + 1) < *((_QWORD *)&v13 + 1) );
        if ( *((_QWORD *)&v14 + 1) > *((_QWORD *)&v13 + 1) )
          break;
LABEL_11:
        ;
      }
      while ( (unsigned __int64)v14 < (unsigned __int64)v13 );
    }
    *(_OWORD *)&result->a = v13;
    result->c = v11;
  }
  return result;
}


Trying to use Interceptor.replace will take effect only once
aero@AERO-PC:~/tools/frida/ctf$ frida --runtime=v8 -l frida_trace.js ./f-hash
     ____
    / _  |   Frida 16.0.8 - A world-class dynamic instrumentation toolkit
   | (_| |
    > _  |   Commands:
   /_/ |_|       help      -> Displays the help system
   . . . .       object?   -> Display information about 'object'
   . . . .       exit/quit -> Exit
   . . . .
   . . . .   More info at https://frida.re/docs/home/
   . . . .
   . . . .   Connected to Local System (id=local)
Spawned `./f-hash`. Resuming main thread!
[Local::f-hash ]->  the_recursive_function(a1: 0x7ffd682e96d0, a2: 256, a3: 7163385811044755000, a4: 2336936577195974700)
[Local::f-hash ]->
[Local::f-hash ]->

Note that using frida -l JS_FILE BINARY_PATH , will keep the binary process running even after 
frida exists. so make sure to kill the process when debugging (pkill / frida-kill)g even afte




shorter solution:
(writeU64 & readU64 can be replaced with S64 version )
var base = ptr(Process.enumerateModulesSync()[0].base)
var recursive_func_ptr = base.add(0x13b0)

var mem = {}
Interceptor.attach(recursive_func_ptr, {
    onEnter: function (args) {
        this.buf = args[0]
        this.hash = args[1] + '-' + args[2] + '-' + args[3]
        if (mem[this.hash] !== undefined) {
            args[1] = ptr(1)
        }
    },
    onLeave: function (retval) {
        if (mem[this.hash] === undefined) {
            mem[this.hash] = [this.buf.readU64(), this.buf.add(8).readU64(), this.buf.add(16).readU64()]
        } else {
            this.buf.writeU64(mem[this.hash][0])
            this.buf.add(8).writeU64(mem[this.hash][1])
            this.buf.add(16).writeU64(mem[this.hash][2])
        }
    }
})
// Interceptor.attach(Module.getExportByName(null, 'open'), {
//     onEnter: function (args) {
//       send({
//         type: 'open',
//         path: Memory.readUtf8String(args[0])
//       });
//     }
//   });

var char = -1
var char_i = -1
var is_correct = -1

const BINARY_NAME = "beginners_rev"
const PRE_CALL_CHECK_OFFSET = 0x31c4; //address of movsx   edi, byte ptr [r13+rax+0]
const POST_CALL_CHECK_OFFSET= 0x31CF; //test    eax, eax
const modules = Process.enumerateModules();
const m = modules[0];//@TODO change
// const m = Process.findModuleByName(BINARY_NAME)
// const check_address_str = DebugSymbol.fromName("check")["address"]; //offset of 0x31CA
// console.log(modules);
// console.log('Tracing...'); //is it safe here?
// console.log(m)
// console.log('Base address: ' + m.base);


Interceptor.attach(ptr(m.base.add(PRE_CALL_CHECK_OFFSET)),
    function(args) {
        char = Memory.readU8(this.context.r13.add(this.context.rax))
        var rsi = this.context.rsi //second param is the char index within the flag
        char_i = parseInt(rsi)
    }
);

Interceptor.attach(ptr(m.base.add(POST_CALL_CHECK_OFFSET)),
    function(args) {
        var rax = this.context.rax
        is_correct = parseInt(rax)
        // console.log([char, char_i, is_correct])
        if (is_correct == 1){
            send([char, char_i, is_correct]);
        }
    }
);
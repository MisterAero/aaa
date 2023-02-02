// Intercepts the recursive function
var mem = new Object(); // Cache object ,TODO: use different type?

var b = Process.getModuleByName("f-hash").base;
var recursive_func_ptr = b.add(0x13b0); 
var recursive_func = new NativeFunction(recursive_func_ptr, 'void', ['pointer', 'int64', 'int64', 'int64']);

function deref64(address) {
  return Memory.readS64(ptr(address))
}

function p(s) {
console.log(s);
}

// hash parameters in order to store in memoization cache
function hash_args(args) {
  return args[1] + "_" + args[2] + "_" + args[3];
};

Interceptor.attach(recursive_func_ptr, {
  onEnter: function(args) {
    this.a1 = parseInt(args[0]); // get the address pointed by the result struct (a1)
                                //The only prefix that parseInt() recognizes is 0x or 0X for hexadecimal values
                                //numbers in JS are 64bit
                                // console.log(
                                //   Number.isSafeInteger(parseInt(0x7ffd682e96d0)),
                                //   parseInt(0x7ffd682e96d0));
    this.hash = hash_args(args);
    // this.already_in_cache = false 
            // If already in cache, don't do recursive call
        // (we will replace the result in the OnLeave hook)
    if (typeof mem[this.hash] !== 'undefined') {
        // this.already_in_cache = true
        args[1] = ptr(1); // we use the value of 1 in order to prevent falling into the recursive calls section 
                          //it might be also possible to jump straight to the return statement.... 
      }
  },

  onLeave: function(retval) {
    // if (this.already_in_cache ){
    if (typeof mem[this.hash] === 'undefined') {
        // We have never seen this.. Memoize!
        mem[this.hash] = [deref64(this.a1), deref64(this.a1+8), deref64(this.a1+16)];
    } else {
        // Just replace the fake result with the memoized one (because we made it run the recursion stoppage case)
        var prev_results = mem[this.hash]
        ptr(this.a1).writeS64(prev_results[0])
        ptr(this.a1+8).writeS64(prev_results[1])
        ptr(this.a1+16).writeS64(prev_results[2])
    }
  }
});



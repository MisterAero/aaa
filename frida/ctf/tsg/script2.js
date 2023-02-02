const is_correct_addr = DebugSymbol.fromName("is_correct").address; 
console.log(is_correct_addr)
     
var isCorrectFunction = new NativeFunction(is_correct_addr, "int", ["int","int"]);

function testChar(c,i) {
    var retval=isCorrectFunction(c,i);
    return retval;
}

rpc.exports = {
    testchar: testChar // all lowercase export name
};

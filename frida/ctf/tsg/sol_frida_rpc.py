import frida
import sys
import string
import codecs 

with codecs.open('./script2.js', 'r', 'utf-8') as f:
    agent = f.read()

# with open("script2.js", "r") as f:
#     agent = f.read()

device = frida.get_local_device()
# pid = device.spawn("./beginners_rev")
pid = device.spawn("./PATCHED")
print('pid: %d' % pid)
session = device.attach(pid)
session = frida.attach("PATCHED")
script = session.create_script(agent, runtime="v8")
script.load()
api = script.exports

flag= ["*"]*32
# we can do the loop here
for i in range(32):
    for c in string.printable:
        if(api.testchar(ord(c),i) == 1): 
            # print(f"char found: {i}:{c}")
            flag[i] = c
            # print(flag)
            break

session.detach()
print(''.join(flag))
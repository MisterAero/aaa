import threading
import string
# https://github.com/frida/frida-tools/blob/main/frida_tools/reactor.py
from frida_tools.application import Reactor
import pdb
import frida

SHELL_COMMAND = "./beginners_rev TSG{AAAAAAAAAAAAAAAAAAAAAAAAAAA}"


with open("script.js", "r") as f:
    script_content = f.read()
    
class Application:
    def __init__(self):
        # private fields (names are made up...)
        self._stop_requested = threading.Event() #https://superfastpython.com/thread-event-object-in-python/
                                                 #https://docs.python.org/3/library/threading.html
                                                 
        # Run the given function until return in the main thread (or the thread of
        # the run method) and in a background thread receive and run additional tasks.                               
        #  threading.Event().wait() : blocks until the flag is true
        self._reactor = Reactor(run_until_return=lambda reactor: self._stop_requested.wait()) #wait for the event to finish?

        self._device = frida.get_local_device()
        self._sessions = set()
        
        # define callbacks / event handlers for device
        # Reactor.schedule(): append a function to the tasks queue of the reactor, optionally with a delay in seconds
        self._device.on("child-added", lambda child: self._reactor.schedule(lambda: self._on_child_added(child)))
        # self._device.on("child-removed", lambda child: self._reactor.schedule(lambda: self._on_child_removed(child)))
        self._device.on("output", lambda pid, fd, data: self._reactor.schedule(lambda: self._on_output(pid, fd, data)))

    def run(self):
        self._reactor.schedule(lambda: self._start()) #entry point
        self._reactor.run() #run _start()

    def _start(self):
        argv = ["/bin/sh", "-c", SHELL_COMMAND] #or [program, argv1,arg2,....]
        
        # Not really needed.... @TODO
        env = {
            # "BADGER": "badger-badger-badger",
            # "SNAKE": "mushroom-mushroom",
        }
        # print(f"✔ spawn(argv={argv})") # maybe refereing to the args of spawn()
        
        # @TODO why stdio="pipe" (forwarding/connection input an output fd's?)?....
        # Spawn a process into an attachable state
        pid = self._device.spawn(argv, env=env, stdio="pipe") # Spawn a process into an attachable state
        
        self._instrument(pid) #need to instrument the first process (enable child gating)

    def _stop_if_idle(self):
        if len(self._sessions) == 0:
            self._stop_requested.set() #Set the internal flag to true. All threads waiting for it to become true are awakened




    def _instrument(self, pid):
        # print(f"✔ attach(pid={pid})")
        session = self._device.attach(pid) #   Attach to a process
        
        # no reason to define signal callback for detach if process wasn't started (that's why it's here)
        session.on("detached", lambda reason: self._reactor.schedule(lambda: self._on_detached(pid, session, reason)))
        # print("✔ enable_child_gating()")
        
        #implementation unavailable: https://github.com/frida/frida-python/blob/main/src/_frida.c
        session.enable_child_gating() 
        # From that point on, any child process is going to end up suspended, and you will be responsible for calling resume() with its PID.
        # The Device object now also provides a signal named delivered which you should attach a callback to in 
        # order to be notified of any new children that appear. 
        # That is the point where you should be applying the desired instrumentation, if any, before calling resume(). 
        # The Device object also has a new method named enumerate_pending_children() which can be used to get a full list of pending children.
        # Processes will remain suspended and part of that list until they’re resumed by you, or eventually killed.

        # print("✔ create_script()")
        # script = session.create_script("""\ """)
        script = session.create_script(script_content)
        # script(session.create_script_from_bytes())
        script.on("message", lambda message, data: self._reactor.schedule(lambda: self._on_message(pid, message)))
        # print("✔ load()")
        script.load()
        # print(f"✔ resume(pid={pid})")
        self._device.resume(pid) # Resume a process from the attachable state
        self._sessions.add(session) #add to set

    def _on_child_added(self, child):
        # print(f"⚡ child_added: {child}")
        self._instrument(child.pid)

    def _on_child_removed(self, child):
        # print(f"⚡ child_removed: {child}")
        pass
    def _on_output(self, pid, fd, data):
        # print(f"⚡ output: pid={pid}, fd={fd}, data={repr(data)}")
        pass
    def _on_detached(self, pid, session, reason):
        # print(f"⚡ detached: pid={pid}, reason='{reason}'")
        self._sessions.remove(session) #remove from set
        self._reactor.schedule(self._stop_if_idle, delay=0.5)

# This is our main interest for the exercise
    def _on_message(self, pid, message):
        if "payload" not in message:
            print("* Special message: {}".format(message))
            pdb.breakpoint()
            return
        
        # print(f"⚡ message: pid={pid}, payload={message['payload']}")
        # try:
        #     if message.type == 'send':
        #         char_i = message["payload"][1]
        #         results[char_i] = message["payload"]
        # except:
        #     print(type(message))
        char_i = message["payload"][1]
        results[char_i] = message["payload"]
        
flag = ["?"] * 32
for c in string.printable:
    # input_data = "".join([c] * 32)
    
    input_data = c * 32
    SHELL_COMMAND = f"./beginners_rev {input_data}"
    results = [None] * 32

    # all processes are checking their input independetly 
    app = Application()
    app.run()

    for result in results:
        #check the return value of check(flag_char)
        
        if result != None and result[2] == 1:
            flag[result[1]] = chr(result[0])
            print("".join(list(c for c in flag)))

print("".join(flag))
# app = Application()
# app.run()

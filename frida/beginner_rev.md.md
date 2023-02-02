

    aero@AERO-PC:~$ frida -h
    usage: frida [options] target
    
    positional arguments:
      args                  extra arguments and/or target
    
    optional arguments:
      -h, --help            show this help message and exit
      -D ID, --device ID    connect to device with the given ID
      -U, --usb             connect to USB device
      -R, --remote          connect to remote frida-server
      -H HOST, --host HOST  connect to remote frida-server on HOST
      --certificate CERTIFICATE
                            speak TLS with HOST, expecting CERTIFICATE
      --origin ORIGIN       connect to remote server with “Origin” header set to ORIGIN
      --token TOKEN         authenticate with HOST using TOKEN
      --keepalive-interval INTERVAL
                            set keepalive interval in seconds, or 0 to disable (defaults to -1 to auto-select based on
                            transport)
      --p2p                 establish a peer-to-peer connection with target
      --stun-server ADDRESS
                            set STUN server ADDRESS to use with --p2p
      --relay address,username,password,turn-{udp,tcp,tls}
                            add relay to use with --p2p
      -f TARGET, --file TARGET
                            spawn FILE
      -F, --attach-frontmost
                            attach to frontmost application
      -n NAME, --attach-name NAME
                            attach to NAME
      -N IDENTIFIER, --attach-identifier IDENTIFIER
                            attach to IDENTIFIER
      -p PID, --attach-pid PID
                            attach to PID
      -W PATTERN, --await PATTERN
                            await spawn matching PATTERN
      --stdio {inherit,pipe}
                            stdio behavior when spawning (defaults to “inherit”)
      --aux option          set aux option when spawning, such as “uid=(int)42” (supported types are: string, bool, int)
      --realm {native,emulated}
                            realm to attach in
      --runtime {qjs,v8}    script runtime to use
      --debug               enable the Node.js compatible script debugger
      --squelch-crash       if enabled, will not dump crash report to console
      -O FILE, --options-file FILE
                            text file containing additional command line options
      --version             show program's version number and exit
      -l SCRIPT, --load SCRIPT
                            load SCRIPT
      -P PARAMETERS_JSON, --parameters PARAMETERS_JSON
                            parameters as JSON, same as Gadget
      -C USER_CMODULE, --cmodule USER_CMODULE
                            load CMODULE
      --toolchain {any,internal,external}
                            CModule toolchain to use when compiling from source code
      -c CODESHARE_URI, --codeshare CODESHARE_URI
                            load CODESHARE_URI
      -e CODE, --eval CODE  evaluate CODE
      -q                    quiet mode (no prompt) and quit after -l and -e
      -t TIMEOUT, --timeout TIMEOUT
                            seconds to wait before terminating in quiet mode
      --pause               leave main thread paused after spawning program
      -o LOGFILE, --output LOGFILE
                            output to log file
      --eternalize          eternalize the script before exit
      --exit-on-error       exit with code 1 after encountering any exception in the SCRIPT
      --auto-perform        wrap entered code with Java.perform
      --auto-reload         Enable auto reload of provided scripts and c module (on by default, will be required in the
                            future)
      --no-auto-reload      Disable auto reload of provided scripts and c module




    usage: frida-trace [options] target
    
    positional arguments:
      args                  extra arguments and/or target
    
    optional arguments:
      -h, --help            show this help message and exit
      -D ID, --device ID    connect to device with the given ID
      -U, --usb             connect to USB device
      -R, --remote          connect to remote frida-server
      -H HOST, --host HOST  connect to remote frida-server on HOST
      --certificate CERTIFICATE
                            speak TLS with HOST, expecting CERTIFICATE
      --origin ORIGIN       connect to remote server with “Origin” header set to ORIGIN
      --token TOKEN         authenticate with HOST using TOKEN
      --keepalive-interval INTERVAL
                            set keepalive interval in seconds, or 0 to disable (defaults to -1 to auto-select based on
                            transport)
      --p2p                 establish a peer-to-peer connection with target
      --stun-server ADDRESS
                            set STUN server ADDRESS to use with --p2p
      --relay address,username,password,turn-{udp,tcp,tls}
                            add relay to use with --p2p
      -f TARGET, --file TARGET
                            spawn FILE
      -F, --attach-frontmost
                            attach to frontmost application
      -n NAME, --attach-name NAME
                            attach to NAME
      -N IDENTIFIER, --attach-identifier IDENTIFIER
                            attach to IDENTIFIER
      -p PID, --attach-pid PID
                            attach to PID
      -W PATTERN, --await PATTERN
                            await spawn matching PATTERN
      --stdio {inherit,pipe}
                            stdio behavior when spawning (defaults to “inherit”)
      --aux option          set aux option when spawning, such as “uid=(int)42” (supported types are: string, bool, int)
      --realm {native,emulated}
                            realm to attach in
      --runtime {qjs,v8}    script runtime to use
      --debug               enable the Node.js compatible script debugger
      --squelch-crash       if enabled, will not dump crash report to console
      -O FILE, --options-file FILE
                            text file containing additional command line options
      --version             show program's version number and exit
      -I MODULE, --include-module MODULE
                            include MODULE
      -X MODULE, --exclude-module MODULE
                            exclude MODULE
      -i FUNCTION, --include FUNCTION
                            include [MODULE!]FUNCTION
      -x FUNCTION, --exclude FUNCTION
                            exclude [MODULE!]FUNCTION
      -a MODULE!OFFSET, --add MODULE!OFFSET
                            add MODULE!OFFSET
      -T INCLUDE_IMPORTS, --include-imports INCLUDE_IMPORTS
                            include program's imports
      -t MODULE, --include-module-imports MODULE
                            include MODULE imports
      -m OBJC_METHOD, --include-objc-method OBJC_METHOD
                            include OBJC_METHOD
      -M OBJC_METHOD, --exclude-objc-method OBJC_METHOD
                            exclude OBJC_METHOD
      -j JAVA_METHOD, --include-java-method JAVA_METHOD
                            include JAVA_METHOD
      -J JAVA_METHOD, --exclude-java-method JAVA_METHOD
                            exclude JAVA_METHOD
      -s DEBUG_SYMBOL, --include-debug-symbol DEBUG_SYMBOL
                            include DEBUG_SYMBOL
      -q, --quiet           do not format output messages
      -d, --decorate        add module name to generated onEnter log statement
      -S PATH, --init-session PATH
                            path to JavaScript file used to initialize the session
      -P PARAMETERS_JSON, --parameters PARAMETERS_JSON
                            parameters as JSON, exposed as a global named 'parameters'
      -o OUTPUT, --output OUTPUT
                            dump messages to file
   


        usage: frida-discover [options] target
    
    positional arguments:
      args                  extra arguments and/or target
    
    optional arguments:
      -h, --help            show this help message and exit
      -D ID, --device ID    connect to device with the given ID
      -U, --usb             connect to USB device
      -R, --remote          connect to remote frida-server
      -H HOST, --host HOST  connect to remote frida-server on HOST
      --certificate CERTIFICATE
                            speak TLS with HOST, expecting CERTIFICATE
      --origin ORIGIN       connect to remote server with “Origin” header set to ORIGIN
      --token TOKEN         authenticate with HOST using TOKEN
      --keepalive-interval INTERVAL
                            set keepalive interval in seconds, or 0 to disable (defaults to -1 to auto-select based on transport)
      --p2p                 establish a peer-to-peer connection with target
      --stun-server ADDRESS
                            set STUN server ADDRESS to use with --p2p
      --relay address,username,password,turn-{udp,tcp,tls}
                            add relay to use with --p2p
      -f TARGET, --file TARGET
                            spawn FILE
      -F, --attach-frontmost
                            attach to frontmost application
      -n NAME, --attach-name NAME
                            attach to NAME
      -N IDENTIFIER, --attach-identifier IDENTIFIER
                            attach to IDENTIFIER
      -p PID, --attach-pid PID
                            attach to PID
      -W PATTERN, --await PATTERN
                            await spawn matching PATTERN
      --stdio {inherit,pipe}
                            stdio behavior when spawning (defaults to “inherit”)
      --aux option          set aux option when spawning, such as “uid=(int)42” (supported types are: string, bool, int)
      --realm {native,emulated}
                            realm to attach in
      --runtime {qjs,v8}    script runtime to use
      --debug               enable the Node.js compatible script debugger
      --squelch-crash       if enabled, will not dump crash report to console
      -O FILE, --options-file FILE
                            text file containing additional command line options
      --version             show program's version number and exit

> Written with [StackEdit](https://stackedit.io/).



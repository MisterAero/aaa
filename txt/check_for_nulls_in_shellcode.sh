#!/bin/bash
grep -Pa '\x00' payload
# get retval into a variable
retval=$?
# 1 - no null bytes
# 0 - null bytes found
if [ $retval -eq 1 ]; then
    echo "No null bytes found"
else
    echo "Null bytes found"
    #xxd
    hexdump -C payload
fi
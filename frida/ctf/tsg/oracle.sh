#!/bin/bash
strace -f ./beginners_rev "$1" 2>&1 | grep correct | wc -l
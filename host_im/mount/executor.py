#!/usr/bin/python3

import os
import sys

for i in sys.argv[1:]:
    # initial compiler commands
    var = i
    # print(var)
    os.system("wine ~/.wine/drive_c/Python27/Scripts/pyinstaller.exe --onefile {}".format(var))

    # a bunch of edits to var to trim it to the compiled file name
    # would take in any file name destination
    var = var.split('/')
    var = str(var[-1])
    var = 'dist/' + str(var[:-3]) + '.exe'
    # print(var)
    os.system("python3 /root/mount/malware-classification-master/checkpe.py {}".format(var))
    
    # Simulate user interaction
    exec(open(i).read())
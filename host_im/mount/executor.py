#!/usr/bin/python3

import os
import sys

for i in sys.argv[1:]:
    exec(open(i).read())
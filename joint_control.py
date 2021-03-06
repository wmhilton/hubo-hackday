#!/usr/bin/python
# /*
# Copyright (c) 2013, William Hilton
# All rights reserved.
# */

import sys
from hubo import *

hubo = Hubo()
jointmap = {"LSP":LSP, "RSP":RSP, "LEB":LEB, "REB":REB}
hubo.updateState()
ref = hubo.getState()

# Inform nodejs what the current slider values should be
print "LSP ",ref[LSP]
print "RSP ",ref[RSP]
print "LEB ",ref[LEB]
print "REB ",ref[REB]
sys.stdout.flush()

while 1:
    line = sys.stdin.readline()
    if line == '\n':
        break;
    try:
        print len(line)
        [j, v] = line.split()
        print "j = ",j
        print "v = ",v
        print "ji = ",jointmap[j]
        ref[jointmap[j]] = float(v)
        hubo.setRef(ref)
        hubo.updateRef()
        sys.stdout.flush()
    except:
        pass


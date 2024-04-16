#!/usr/bin/env python

from random import choice
from sys import stdout as o
from time import sleep

cols_normal = ['\033[30m', '\033[31m', '\033[32m', '\033[33m',
               '\033[34m', '\033[35m', '\033[36m', '\033[37m']
cols_bold = ['\033[30;1m', '\033[31;1m', '\033[32;1m', '\033[33;1m',
             '\033[34;1m', '\033[35;1m', '\033[36;1m', '\033[37;1m']
cols = cols_normal + cols_bold
endcol = '\033[0;0m'
l = ''
ch = "10 "

while True:
    l = "%s%s" % (choice(cols), choice(ch))
    o.flush()
    o.write(l)
    o.write(endcol)
    sleep(0.0001)

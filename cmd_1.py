#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
    python-version:3.6
    date:2018/8/14
    author:yafei9 
"""


from cmd import Cmd
import os
import sys

class Cli (Cmd):

    def __init__(self):
        Cmd.__init__(self)

    def do_hello(self, line):
        print('hello', line)

if __name__ == '__main__':
    cli = Cli()
    cli.cmdloop()

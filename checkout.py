#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
from builtins import input  # pip install future
import sys
import codecs
from _common.shell import Shell
from _common.color import Colors

if __name__ == '__main__':
    cmd = 'git branch';
    if len(sys.argv) > 1:
        cmd = 'git branch -a | grep %s' % sys.argv[1]
    branch_str = Shell.execute(cmd)[0]
    branches = branch_str.strip().split('\n')
    cur_branch = -1
    for i, branch in enumerate(branches):
        if branch.find('*') == -1:
            print(' %d. %s' % (i + 1, branch.strip()))
        else:
            cur_branch = i
            print(' %d. %s%s%s' % (i + 1, Colors.GREEN, branch.replace('*', '').strip(), Colors.DEFAULT))
    try:
        select = int(input('\n which branch do you want to checkout? '))
        if 1 <= select and select <= len(branches):
             if select != cur_branch + 1:
                 Shell.execute('git checkout %s' % branches[select - 1].replace('remotes/origin/', ''))
    except ValueError:
        print(':(')

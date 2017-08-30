#! /usr/bin/env python


from _common._linux.shell import Shell
from _common.color import Colors

if __name__ == '__main__':
    branch_str = Shell.execute('git branch')[0]
    branches = branch_str.strip().split('\n')
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
                Shell.execute('git checkout %s' % branches[select - 1])
    except ValueError:
        print(':(')

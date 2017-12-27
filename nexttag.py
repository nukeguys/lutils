#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from _common._linux.shell import Shell
from _common.color import Colors

def nextVersion(version, cipher):
    versions=version.split('.')
    versions[cipher]=str(int(versions[cipher])+1)
    return '.'.join(versions)
if __name__ == '__main__':
    versionRegEx='"v([0-9]+[.]?){4}$"'
    bashCommand='git tag --sort=-v:refname | grep -E '+versionRegEx
    tags=Shell.execute(bashCommand, wantToError=False).split('\n')
    latestVersion=tags[0]

    if latestVersion:        
        print("Latest Version is %s%s%s" % (Colors.GREEN, latestVersion, Colors.DEFAULT))
    else:
        print("%sCan't find version tags.%s" % (Colors.RED, Colors.DEFAULT))
        exit(0)

    answer = input('0. Master, 1. Major, 2. Minor, 3. patch : ')
    if answer!='0' and answer!='1' and answer!='2' and answer!='3':
        print("%sWrong input.%s" % (Colors.RED, Colors.DEFAULT))
        exit(0)

    nextVersion='v'+nextVersion(latestVersion[1:], int(answer))
    answer = input('Do you want to create & push tag "%s%s%s"? [y/n] ' % (Colors.GREEN, nextVersion, Colors.DEFAULT))
    if answer.lower() == 'y':
        bashCommand = 'git tag -a %s -m %s' % (nextVersion, nextVersion)
        #Shell.execute(bashCommand)
        #bashCommand = 'git push --tags'
        #Shell.execute(bashCommand)
    else:
        print('%s:(%s' % (Colors.RED, Colors.DEFAULT))

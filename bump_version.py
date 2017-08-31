#! /usr/bin/env python


import fileinput
import re
from _common.util import Util
from _common.color import Colors

if __name__ == '__main__':
    versionFiles = Util.filesByName('.', 'AssemblyInfo.cs')
    versionRegx = re.compile('^\[assembly: Assembly(File)?Version\("(?P<version>[0-9](.[0-9]{1,2}){2,3})"\)\]')
    for filePath in versionFiles:
        if '\\Test\\' in filePath:  # skip test project
            continue
        with fileinput.FileInput(filePath, openhook=fileinput.hook_encoded('utf-8')) as file:
            for line in file:
                m = versionRegx.match(line)
                if m is not None:
                    print(filePath + ' - ' + m.group('version'))

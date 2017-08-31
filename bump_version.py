#! /usr/bin/env python


import fileinput
import re
from terminaltables.other_tables import UnixTable
from _common.util import Util
from _common.color import Colors

if __name__ == '__main__':
    versionFiles = Util.findFiles('.', 'AssemblyInfo.cs')
    versionRegx = re.compile('^\[assembly: Assembly(File)?Version\("(?P<version>[0-9](.[0-9]{1,2})*)"\)\]')
    assemblyVersions = []
    assemblyFileVersions = []

    for filePath in versionFiles:
        if '\\Test\\' in filePath:  # skip test project
            continue
        with fileinput.FileInput(filePath, openhook=fileinput.hook_encoded('utf-8')) as file:
            for line in file:
                m = versionRegx.match(line)
                if m is not None:
                    if 'File' in line:
                        assemblyFileVersions.append(m.group('version'))
                    else:
                        assemblyVersions.append(m.group('version'))

    tableHeader = [['file', 'assemblyVersion', 'asssemblyFileVersion']]
    table = UnixTable(tableHeader + list(zip(versionFiles, assemblyVersions, assemblyFileVersions)))
    print(table.table)


#print(filePath.split('\\')[1] + ' - ' + filePath + ' - ' + m.group('version'))

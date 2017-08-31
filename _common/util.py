# -*- coding: utf-8 -*-
import os


class Util:
    def enum(*sequential, **named):
        enums = dict(zip(sequential, range(len(sequential))), **named)
        reverse = dict((value, key) for key, value in enums.items())
        enums['reverse_mapping'] = reverse
        return type('Enum', (), enums)


    def filesByName(rootDir, fileName):
        if not os.path.isdir(rootDir):
            raise EnvironmentError('root is not directory')

        foundFiles = []
        for root, subDirs, files in os.walk(rootDir):
            if fileName in files:
                foundFiles.append(os.path.join(root, fileName))
        return foundFiles

# -*- coding: utf-8 -*-

from __future__ import print_function
import subprocess
import sys
# https://stackoverflow.com/questions/4760215/running-shell-command-from-python-and-capturing-the-output

class Shell:

    @staticmethod
    def execute(command, wantToError=True):
        output, err = '', ''
        if sys.version_info >= (3, 5):
            result = subprocess.run(
                command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, err = result.stdout, result.stderr
        else:
            process = subprocess.Popen(
                command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, err = process.communicate()


        if wantToError:
            return output.decode('utf-8'), err.decode('utf-8')
        else:
            return output.decode('utf-8')

if __name__ == '__main__':
	print('### TEST - {0} ###'.format(__file__))
	cmd = 'ls -l'
	print('> run \'{0}\''.format(cmd))
	out, err = Shell.execute(cmd)
	print('[ OUTPUT ]')
	print(out)
	print('[ ERROR ]')
	print(err)
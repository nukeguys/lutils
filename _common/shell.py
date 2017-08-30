import subprocess
import sys

class Shell:
    @staticmethod
    def execute(bashCommand, wantToError=True):
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, err = process.communicate()
        if wantToError == True:
            if sys.version_info.major >= 3:
                return str(output, 'utf-8'), str(err, 'utf-8') 
            else:
                return str(output), str(err) 
        else:
            if sys.version_info.major >= 3:
                return str(output, 'utf-8')
            else:
                return str(output)

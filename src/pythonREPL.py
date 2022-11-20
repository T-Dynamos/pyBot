import sys
import os
import subprocess
from timeit import default_timer as timer
import random
import string
import _thread

PYTHON_PATH = os.path.realpath(sys.executable)

class CodeExecuter():
    
    def __init__(self,code:str):
        self.output = []
        self.final_output = []
        self.temp_dir = os.path.realpath(os.path.join("/tmp/","".join(random.choices(string.ascii_lowercase,k=10))))
        self.file_path = os.path.join(self.temp_dir,"temp_run.py")
        os.mkdir(self.temp_dir)
        os.chdir(self.temp_dir)
        with open(self.file_path,"w") as file:
            file.write(code)
            file.close()

    def execute_code(self):
        process = subprocess.run([PYTHON_PATH,self.file_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        self.output = ["".join(process.stderr.decode()),process.stdout.decode()]
        self.execution_end = timer()
        os.remove(self.file_path)
        os.removedirs(self.temp_dir)
        self.final_output = [abs(self.execution_start-self.execution_end),self.output,process.returncode]

    def execute_python(self):
        self.execution_start = timer()
        _thread.start_new_thread(self.execute_code,())
        while abs(self.execution_start-timer()) < 10 and self.final_output == []:
            continue

        if len(self.final_output) == 0:
            return [10,["Timeout!","Code cannot run for more than 10 secs"],1]
        else:
            return self.final_output


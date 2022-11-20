import sys
import os
import subprocess
from timeit import default_timer as timer
import random
import string

PYTHON_PATH = os.path.realpath(sys.executable)

def execute_python(code:str,PYTHON_PATH=PYTHON_PATH) -> list:
    output = []
    temp_dir = os.path.realpath(os.path.join("/tmp/","".join(random.choices(string.ascii_lowercase,k=10))))
    file_path = os.path.join(temp_dir,"temp_run.py")

    os.mkdir(temp_dir)
    os.chdir(temp_dir)
    with open(file_path,"w") as file:
        file.write(code)
        file.close()

    execution_start = timer()
    process = subprocess.run([PYTHON_PATH,file_path],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    output = ["".join(process.stderr.decode()),process.stdout.decode()]
    execution_end = timer()

    os.remove(file_path)
    os.removedirs(temp_dir)

    return [abs(execution_start-execution_end),output,process.returncode]



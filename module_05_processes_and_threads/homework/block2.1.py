from flask import Flask
import shlex, subprocess
import os
import signal


result = subprocess.run(["lsof", "-i", ":5000"], stdout=subprocess.PIPE)
k=str(result.stdout.decode('ascii'))
j=k.split('\n')
j.pop()
b=[]
for line in j:
    field=line.split()
    b.append(field[1])
    print(field[1])
b.pop(0)
print(b)
for i in b:
    os.kill(int(i), signal.SIGTERM)  # or signal.SIGKILL


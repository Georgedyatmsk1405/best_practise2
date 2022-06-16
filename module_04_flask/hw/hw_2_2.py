"""
Напишите GET flask endpoint с url /uptime,
    который в ответ на запрос будет возвращать как долго текущая машина не перезагружалась
        (в виде строки f"Current uptime is '{UPTIME}'"
            где UPTIME - uptime системы. Это можно сделать с помощью команды uptime
            (https://www.opennet.ru/man.shtml?topic=uptime&category=1&russian=4)
        )

Напомним, что вызвать программу из python можно с помощью модуля subprocess:
"""
from typing import List, Optional

from flask import Flask, request

app = Flask(__name__)
import shlex, subprocess
@app.route("/uptime", methods=["POST","GET"])
def uptime():

    command_str = f"uptime"
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)
    final=(result.stdout.decode('cp866')).split(',')[0]
    return f"Current uptime is '{result}'"
if __name__ == "__main__":
    app.run(debug=True)

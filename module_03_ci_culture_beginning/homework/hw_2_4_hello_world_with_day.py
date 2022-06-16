"""
Напишите  hello-world endpoint , который возвращал бы строку "Привет, <имя>. Хорошей пятницы!".
Вместо хорошей пятницы, endpoint должен уметь желать хорошего дня недели в целом, на русском языке.
Текущий день недели можно узнать вот так:

"""

import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/hello-world/<username>")
def hello_world(username) -> str:
    day=datetime.datetime.today().weekday()
    normalday=''
    if day==0:
        normalday='понедельника'
    elif day==1:
        normalday = "вторника"
    elif day == 2:
        normalday = "среды"
    elif day == 3:
        normalday = "четверга"
    elif day == 4:
        normalday = "пятницы"
    elif day == 5:
        normalday = "субботы"
    elif day == 6:
        normalday ="воскресенья"


    return "привет " +str(username)+"хорошей "+str(normalday)




if __name__ == "__main__":
    app.run(debug=True)

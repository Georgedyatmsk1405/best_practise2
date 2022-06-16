from flask import Flask
from random import choice
import datetime

app=Flask(__name__)
countt=int()

@app.route('/hello_world')
def hello():
    return 'Привет мир'

@app.route('/cars')
def cars():
    return 'Chevrolet, Renault, Ford, Lada'


@app.route('/cats')
def cats():
    a=['корниш рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']

    return choice(a)


@app.route('/get_time/future')
def gettimefuture():
    currenttime=str(datetime.datetime.now())
    futuretime=str(datetime.datetime.now()+datetime.timedelta(hours=1))
    return 'будущее время '+futuretime


@app.route('/get_time/now')
def gettimenow():
    currenttime = str(datetime.datetime.now())
    return 'Точное время ' + currenttime

@app.route('/get_random_word')
def randomword():
   j=choice(open("war_and_peace.txt", encoding='utf-8').read().split())

   return j

@app.route('/counter')
def counter():
   global countt
   countt+=1

   return str(countt)




if __name__ == '__main__':
    app.run(debug=True)



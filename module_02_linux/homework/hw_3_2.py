"""
Давайте напишем свое приложение для учета финансов.
Оно должно уметь запоминать, сколько денег мы потратили за день,
    а также показывать затраты за отдельный месяц и за целый год.

Модифицируйте  приведенный ниже код так, чтобы у нас получилось 3 endpoint:
/add/<date>/<int:number> - endpoint, который сохраняет информацию о совершённой за какой-то день трате денег (в рублях, предполагаем что без копеек)
/calculate/<int:year> -- возвращает суммарные траты за указанный год
/calculate/<int:year>/<int:month> -- возвращает суммарную трату за указанный месяц

Гарантируется, что дата для /add/ endpoint передаётся в формате
YYYYMMDD , где YYYY -- год, MM -- месяц (число от 1 до 12), DD -- число (от 01 до 31)
Гарантируется, что переданная дата -- корректная (никаких 31 февраля)
"""
from flask import Flask

app = Flask(__name__)

storage = {}
numb=0

@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    year=int(date[0:4])
    month = int(date[4:6])
    day = int(date[6:8])
    global numb
    numb+=1
    storage[numb]={'year':year,'month':month,'day':day,'finance':number}
    return 'ok'





@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    a=0
    for key in storage:
        if storage[key]['year'] == year:
            a += storage[key]['finance']

    print(a)
    return str(a)


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    # поиск по месяцу
    bb = 0
    for key in storage:
        if storage[key]['year'] == year and storage[key]['month'] == month:
            bb += storage[key]['finance']
    print(bb)
    return str(bb)




if __name__ == "__main__":
    app.run(debug=True)

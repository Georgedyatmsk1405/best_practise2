"""
Юный натуралист Петя решил посетить Юнтоловский заказник на рассвете и записать журнал всех птиц,
    которых он увидел в заказнике. Он написал программу, но, в процессе написания,
    так устал, что уснул на клавиатуре, отчего пол-программы стёрлось.

Наш юный натуралист точно помнит, что программа позволяла добавить в БД новую птицу и говорила ему,
    видел ли он такую птицу раньше.

Помогите восстановить исходный код программы ЮНат v0.1 ,
    реализовав функции log_bird (добавление новой птицы в БД) и check_if_such_bird_already_seen
    (проверка что мы уже видели такую птицу)

Пожалуйста помогите ему, реализовав функцию log_bird .
    При реализации не забудьте про параметризацию SQL запроса!
"""
# table_bird добавлена в модуле test.py
import datetime
import sqlite3


def log_bird(
        c: sqlite3.Cursor,
        bird_name: str,
        date_time: str,
) -> None:
    sql_req = """INSERT INTO table_bird (birdname, birdtime )  VALUES (?,?);"""
    c.execute(sql_req, (bird_name,date_time))



def check_if_such_bird_already_seen(c: sqlite3.Cursor, bird_name: str) -> bool:
    sql_req = """SELECT * FROM table_bird WHERE birdname=?;"""
    c.execute(sql_req, (bird_name,))
    result=c.fetchone()
    print(result)
    if result:
        return True
    return False


if __name__ == "__main__":
    print("Программа помощи ЮНатам v0.1")
    name = input("Пожалуйста введите имя птицы\n> ")
    count_str = input("Сколько птиц вы увидели?\n> ")
    count = int(count_str)
    right_now = datetime.datetime.utcnow().isoformat()

    with sqlite3.connect("hw.db") as connection:
        cursor = connection.cursor()


        if check_if_such_bird_already_seen(cursor, name):
            print("Такую птицу мы уже наблюдали!")
        log_bird(cursor, name, right_now)

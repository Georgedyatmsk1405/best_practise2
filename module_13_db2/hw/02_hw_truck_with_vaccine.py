"""
Пожалуйста, запустите скрипт generate_hw_database.py прежде, чем приступать к выполнению практической работы. После выполнения скрипта у вас должен появиться файл базы hw.db и в нем таблица table_truck_with_vaccine
Грузовик перевозит очень важную вакцину.

Условия хранения этой вакцины весьма необычные -- в отсеке должна быть температура  -18±2 градуса.
    Если температурный режим был нарушен - вакцина считается испорченной.

Для проверки состояния вакцины применяется датчик, который раз в час измеряет температуру внутри контейнера.
    Если в контейнере было хотя бы 3 часа с температурой, которая находится вне указанного выше диапазона -
    температурный режим считается нарушенным.

Пожалуйста, реализуйте функцию `check_if_vaccine_has_spoiled`,
    которая по номеру грузовика определяет, не испортилась ли вакцина.
"""
import sqlite3


def check_if_vaccine_has_spoiled(c: sqlite3.Cursor,truck_number: str,) -> bool:
    c=c.cursor()
    sql_req="""SELECT temperature_in_celsius from table_truck_with_vaccine where truck_number=? """
    c.execute(sql_req,(truck_number,))
    request_result, *_ = c.fetchone()
    if request_result <16 or request_result>20:
        print('испортилась')
        return 'испортилась'
    print('норм')
    return 'норм'





if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        truck_number='в034рн11'


        check_if_vaccine_has_spoiled(conn,truck_number)

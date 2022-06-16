"""
В 20NN году оккультному автосалону "Чёртово колесо" исполняется ровно 13 лет.
    В честь этого они предлагает своим клиентам уникальную акцию:
    если вы обращаетесь в автосалон в пятницу тринадцатое и ваш автомобиль
    чёрного цвета и марки "Лада" или "BMW", то вы можете поменять колёса со скидкой 13%.
Младший менеджер "Чёртова колеса" слил данные клиентов в интернет,
    поэтому мы можем посчитать, как много клиентов автосалона могли воспользоваться
    скидкой (если бы они об этом знали). Давайте сделаем это!

Реализуйте функцию, c именем get_number_of_luckers которая принимает на вход курсор и номер месяца,
    и в ответ возвращает число клиентов, которые могли бы воспользоваться скидкой автосалона.
    Таблица с данными называется `table_occult_car_repair`
"""
import datetime
import sqlite3


def friday(
        c: sqlite3.Cursor,
        mounth_number: str,

) -> None:

    sql_req = """SELECT  COUNT(*)  FROM table_occult_car_repair WHERE strftime('%m', timestamp)=? and (car_type="BMW" or car_type="Лада") and  strftime('%w', timestamp)=4 and strftime('%d', timestamp)=13 ;"""
    c.execute(sql_req,(mounth_number,))
    result=c.fetchall()
    print(result)

if __name__ == "__main__":
    mounth_number=int(input())
    mounth_number=str(mounth_number).zfill(2)
    print(mounth_number)
    with sqlite3.connect("hw.db") as connection:
        cursor = connection.cursor()
        friday(cursor, mounth_number)


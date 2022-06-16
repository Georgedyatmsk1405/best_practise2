"""
Иван Совин - эффективный менеджер.
Когда к нему приходит сотрудник просить повышение з/п -
    Иван может повысить её только на 10%.

Если после повышения з/п сотрудника будет больше з/п самого
    Ивана Совина - сотрудника увольняют, в противном случае з/п
    сотрудника повышают.

Давайте поможем Ивану стать ещё эффективнее,
    автоматизировав его нелёгкий труд.
    Пожалуйста реализуйте функцию которая по имени сотрудника
    либо повышает ему з/п, либо увольняет сотрудника
    (удаляет запись о нём из БД).

Таблица с данными называется `table_effective_manager`
"""
import sqlite3
import sqlite3


def ivan_sovin_the_most_effective(
        c: sqlite3.Cursor,
        name: str,
) -> None:

    sql_req = """SELECT * FROM table_effective_manager WHERE name='Иван Совин';"""
    sql_req2="""SELECT * FROM table_effective_manager WHERE name=?;"""
    c.execute(sql_req)
    #c.execute(sql_req)
    result=c.fetchone()
    c.execute(sql_req2,(name,))
    result2=c.fetchone()
    #print(c.execute("""SELECT * FROM table_effective_manager """).fetchall())
    if result2:
        if 1.1*result2[2]>=result[2]:
            c.execute("""DELETE FROM table_effective_manager WHERE name=?""",(name,))

        else:
            c.execute("""UPDATE table_effective_manager SET salary=? WHERE name=?""",(1.1*result2[2],name,))
    else:
        print('uvolen')

    print(result)
    print(result2)
if __name__ == "__main__":
    name=str(input())

    with sqlite3.connect("hw.db") as connection:
        cursor = connection.cursor()
        ivan_sovin_the_most_effective(cursor, name)



#Яковлев З.Ц.
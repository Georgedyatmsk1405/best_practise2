"""
Иногда бывает важно сгенерировать какие то табличные данные по заданным характеристикам.
К примеру, если вы будете работать тестировщиками, вам может потребоваться добавить
    в тестовую БД такой правдоподобный набор данных (покупки за сутки, набор товаров в магазине,
    распределение голосов в онлайн голосовании).

Давайте этим и займёмся!

Представим, что наша FrontEnd команда делает страницу сайта УЕФА с жеребьевкой команд
    по группам на чемпионате Европы.

Условия жеребьёвки такие:
Есть N групп.
В каждую группу попадает 1 "сильная" команда, 1 "слабая" команда и 2 "средние команды".

Задача: написать функцию generate_data, которая на вход принимает количество групп (от 4 до 16ти)
    и генерирует данные, которыми заполняет 2 таблицы:
        1. таблицу со списком команд (столбцы "номер команды", "Название", "страна", "сила команды")
        2. таблицу с результатами жеребьёвки (столбцы "номер команды", "номер группы")

Таблица с данными называется `uefa_commands` и `uefa_draw`
"""
import sqlite3
import random

def generate_test_data(c: sqlite3.Cursor, number_of_groups: int) -> None:
    k = 0
    numb = 16
    c.execute("""DELETE FROM
    uefa_commands""")
    c.execute("""DELETE FROM
        uefa_draw""")
    # c.execute(
    #     """ALTER TABLE uefa_commands ADD command_number_new INTEGER""")
    for i in range(4, number_of_groups+1, 4):
        list1=list(range(i+1))[-4:]
        print("делаем четверки")
        c.execute("""INSERT INTO uefa_commands (command_number_new,command_name, command_country,command_level) VALUES (?,'strongteam','sss','strong')""",(list1[0],))

        c.execute(
            """INSERT INTO uefa_commands (command_number_new,command_name, command_country,command_level) VALUES (?,'weakteam','sss','weak')""",(list1[1],))
        c.execute(
            """INSERT INTO uefa_commands (command_number_new,command_name, command_country,command_level) VALUES (?,'midleteam','sss','midle')""",(list1[2],))
        c.execute(
            """INSERT INTO uefa_commands (command_number_new,command_name, command_country,command_level) VALUES (?,'midleteam2','sss','midle')""",(list1[3],))
        # сюда же инсертим то же самое только во вторую таблицу и с присвоением группы i//4 для каждой четверки своя группа
        c.execute(
            """INSERT INTO uefa_draw (command_number,group_number) VALUES (?,?)""",
            (list1[3],i//4))
        c.execute(
            """INSERT INTO uefa_draw (command_number,group_number) VALUES (?,?)""",
            (list1[2], i // 4))
        c.execute(
            """INSERT INTO uefa_draw (command_number,group_number) VALUES (?,?)""",
            (list1[1], i // 4))
        c.execute(
            """INSERT INTO uefa_draw (command_number,group_number) VALUES (?,?)""",
            (list1[0], i // 4))

    print("завершаем с остатками")
    last_group=((number_of_groups//4)+1)
    if number_of_groups % 4 == 0:
        k = 0
        print(k)
    elif number_of_groups % 4 == 1:
        k = 1
        print(k)
        c.execute(
            """INSERT INTO uefa_commands (command_number_new,command_name, command_country,command_level) VALUES (?,'strongteam','sss','strong')""",
            (number_of_groups,))
        c.execute(
            """INSERT INTO uefa_draw (command_number,group_number) VALUES (?,?)""",
            (number_of_groups, last_group,))
    elif number_of_groups % 4 == 2:
        k = 2
        c.execute(
        """INSERT INTO uefa_commands (command_number_new,command_name, command_country,command_level) VALUES (?,'strongteam','sss','strong')""",
        (number_of_groups-1,))
        c.execute(
            """INSERT INTO uefa_commands (command_number_new,command_name, command_country,command_level) VALUES (?,'weakteam','sss','weak')""",
            (number_of_groups,))
        c.execute(
            """INSERT INTO uefa_draw (command_number,group_number) VALUES (?,?)""",
            (number_of_groups-1, last_group,))
        c.execute(
            """INSERT INTO uefa_draw (command_number,group_number) VALUES (?,?)""",
            (number_of_groups, last_group,))
    elif number_of_groups % 4 == 3:
        k = 3
        c.execute(
            """INSERT INTO uefa_commands (command_number_new,command_name, command_country,command_level) VALUES (?,'strongteam','sss','strong')""",
            (number_of_groups - 2,))
        c.execute(
            """INSERT INTO uefa_commands (command_number_new,command_name, command_country,command_level) VALUES (?,'weakteam','sss','weak')""",
            (number_of_groups-1,))
        c.execute(
            """INSERT INTO uefa_commands (command_number_new,command_name, command_country,command_level) VALUES (?,'midleteam','sss','midle')""",
            (number_of_groups ,))
        c.execute(
            """INSERT INTO uefa_draw (command_number,group_number) VALUES (?,?)""",
            (number_of_groups - 2, last_group,))
        c.execute(
            """INSERT INTO uefa_draw (command_number,group_number) VALUES (?,?)""",
            (number_of_groups - 1, last_group,))
        c.execute(
            """INSERT INTO uefa_draw (command_number,group_number) VALUES (?,?)""",
            (number_of_groups, last_group,))





if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        generate_test_data(cursor,17)
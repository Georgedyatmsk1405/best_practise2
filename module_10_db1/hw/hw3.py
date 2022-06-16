import sqlite3


with sqlite3.connect("hw_3_database.db") as conn:
    cursor=conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM table_1 UNION SELECT COUNT(*) FROM table_2 UNION SELECT COUNT(*) FROM table_3 ")

    result=cursor.fetchall()
    print(result)

with sqlite3.connect("hw_3_database.db") as conn:
    cursor=conn.cursor()
    cursor.execute("SELECT COUNT(DISTINCT value) FROM table_1 ")

    result=cursor.fetchall()
    print(result)

with sqlite3.connect("hw_3_database.db") as conn:
    cursor=conn.cursor()
    cursor.execute("SELECT COUNT(*) from table_1, table_2 where table_1.id=table_2.id ")

    result=cursor.fetchall()
    print(result)

with sqlite3.connect("hw_3_database.db") as conn:
    cursor=conn.cursor()
    cursor.execute("SELECT COUNT(*) from table_1, table_2, table_3 where table_1.id=table_2.id and table_1.id=table_3.id")

    result=cursor.fetchall()
    print(result)


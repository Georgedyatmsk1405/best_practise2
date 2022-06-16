import sqlite3


with sqlite3.connect("hw_5_database.db") as conn:
    cursor=conn.cursor()
    cursor.execute("SELECT colour, COUNT(colour) from (SELECT table_phones.id, name, colour, price FROM table_phones INNER JOIN table_checkout ON table_phones.id=phone_id) as foo GROUP BY colour ")

    result=cursor.fetchall()
    print(result)
    #1 ответ синий
    #2 синий
    #3 золотой
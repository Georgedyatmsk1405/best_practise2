import sqlite3

with sqlite3.connect("hw_2_database.db") as conn:
    cursor=conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM salaries WHERE salary<5000 ")

    result=cursor.fetchall()
    print(result)
with sqlite3.connect("hw_2_database.db") as conn:
    cursor=conn.cursor()

    cursor.execute("SELECT AVG(salary) FROM salaries")
    result=cursor.fetchall()
    print(result)
with sqlite3.connect("hw_2_database.db") as conn:
    cursor=conn.cursor()

    #cursor.execute("SELECT salary as sa FROM salaries WHERE (SELECT COUNT(id) FROM salaries WHERE salary<=sa)=(SELECT COUNT(id) FROM salaries WHERE salary>sa)")
    result=cursor.fetchall()
    print(result)


with sqlite3.connect("hw_2_database.db") as conn:
    cursor=conn.cursor()

    cursor.execute("SELECT SUM(salary) FROM (SELECT * FROM salaries ORDER BY salary DESC LIMIT 0.1*(SELECT COUNT(id) FROM salaries )) AS foo UNION SELECT SUM(salary) FROM (SELECT * FROM salaries ORDER BY salary LIMIT 0.9*(SELECT COUNT(id) FROM salaries )) AS foo")
    result=cursor.fetchall()
    print(result)
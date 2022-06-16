import sqlite3


with sqlite3.connect('C:\python\python_advanced\module_16_db3\homework\hw.db') as conn:
    cursor = conn.cursor()
    cursor.execute("""SELECT customer.customer_id, customer.full_name from customer left join oorder on oorder.customer_id=customer.customer_id
    where oorder.customer_id is null""")
    all_room = cursor.fetchall()
    print(all_room)
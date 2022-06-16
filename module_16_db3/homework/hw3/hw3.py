import sqlite3


with sqlite3.connect('C:\python\python_advanced\module_16_db3\homework\hw.db') as conn:
    cursor = conn.cursor()
    cursor.execute("""SELECT customer.full_name, oorder.order_no  from customer join oorder on oorder.customer_id=customer.customer_id
    where customer.manager_id is null""")
    all_room = cursor.fetchall()
    print(all_room)
import sqlite3

# with sqlite3.connect("hw.db") as conn:
# 	cursor=conn.cursor()

# 	cursor.execute("""SELECT * FROM table_truck_with_vaccine""")
# 	result=c.fetchall()

# 	for i in result:
# 		print(i)
#
# list1=[]
# with open('wrong_fees.csv') as f:
# 	line=f.readlines()
#
# 	for i in line:
# 		i=i.split(',')
# 		i[1]=i[1].replace('\n','')
# 		list1.append(i)
# 		print(i)
# print(list1)
#
# with sqlite3.connect("hw.db") as conn:
# 	cursor=conn.cursor()
# 	for i in list1:
# 		sql_req="""DELETE * FROM table_fees  WHERE truck_number=? AND timestamp=?;"""
# 		cursor.execute(sql_req,(str(i[0]),str(i[1])))
		
# generate_hw_2_sql = """
# DROP TABLE IF EXISTS `table_bird`;
#
# CREATE TABLE `table_bird` (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     birdname VARCHAR(100) NOT NULL,
#     birdtime VARCHAR(100) NOT NULL
# );
# """
# with sqlite3.connect("hw.db") as conn:
# 	cursor=conn.cursor()
# 	cursor.executescript(generate_hw_2_sql)
# у455мт77
# 2021-10-31T22:55:31
#print(list(range(0,13,4)))
# k=0
# numb=12
# for i in range(4,numb+1,4):
# 	print("делаем четверки")
#
# if numb % 4 == 0:
# 	k = 0
# 	print(k)
# elif numb % 4 == 1:
# 	k = 1
# 	print(k)
# elif numb % 4 == 2:
# 	k = 2
# 	print(k)
# elif numb % 4 == 3:
# 	k = 3
# 	print(k)
# 	k=4
# 	print("s"+str(k))
#print(list(range(9))[-4:])
print(3//4)



# with sqlite3.connect("hw.db") as conn:
# 	cursor=conn.cursor()
# 	cursor.executescript("""SELECT * FROM uefa_draw""")
# 	result=cursor.fetchall()
# 	print(result)
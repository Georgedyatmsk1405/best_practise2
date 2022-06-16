import sqlite3

file=open('doc.txt', 'r', encoding='utf-8')
list=[]
print(str(file))

for i in file:
    i=i.replace('`','')
    i=i.split('\n')
    for ii in i:
        ii=ii.split(',')
        list.append(ii)

for i in list:
    if i==['']:
        list.remove(i)
print(list)
with sqlite3.connect("hw_1_database.db") as conn:
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM table_people")
    result=cursor.fetchall()
    print(result)
    #cursor.executescript("""CREATE TABLE TABLE_CARR(Id, nomer, car, vladelez, description);""")
    id=0
    for i in list:
        id+=1

        print(i[0],i[1],i[2],i[3])
        cursor.executescript("""INSERT INTO TABLE_CARR VALUES('{id}','{nomer}','{name}','{vladelez}','{description}')""".format(id=id,
                                                                                                                                nomer=str(i[0]),name=str(i[1]),
                                                                                                                                vladelez=str(i[2]),
                                                                                                                                description=str(i[3])))


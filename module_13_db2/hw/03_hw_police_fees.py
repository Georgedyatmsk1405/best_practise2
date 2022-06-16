"""
Вы работаете программистом в IT отделе ГИБДД.
    Ваш отдел отвечает за обслуживание камер,
    которые фиксируют превышения скорости и выписывают автоматические штрафы.
За последний месяц к вам пришло больше тысячи жалоб на ошибочно назначенные штрафы,
    из которых около 100 были признаны и правда ошибочными.

Список из дат и номеров автомобилей ошибочных штрафов прилагается к заданию,
    пожалуйста удалите записи об этих штрафах из таблицы `table_fees`
"""
import sqlite3


def delete_wrong_fees(c: sqlite3.Cursor, wrong_fees_file: str) -> None:
    list1=[]
    with open(wrong_fees_file) as f:
        line=f.readlines()
        
        for i in line:
            i=i.split(',')
            i[1]=i[1].replace('\n','')
            list1.append(i)
            print(i)


    
       
        for i in list1:
            sql_req="""DELETE FROM table_fees  WHERE truck_number=? AND timestamp=?;"""
            c.execute(sql_req,(str(i[0]),str(i[1])))



if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()

        delete_wrong_fees(cursor, "wrong_fees.csv")

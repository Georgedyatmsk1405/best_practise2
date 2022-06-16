"""
Напишите функцию, которая будет по output команды ls возвращать средний размер файла в папке.
$ ls -l ./
В качестве аргумента функции должен выступать путь до файла с output команды ls
"""
import os


def get_mean_size(ls_output_path: str) -> float:
    a=os.listdir()
    spisok=[]
    for i in a:
        c=os.path.getsize(ls_output_path+str(i))
        spisok.append(c)
    print(spisok)
    return(sum(spisok)/len(spisok))


    """Put your code here"""


if __name__ == "__main__":
    print(get_mean_size("/home/george/PycharmProjects/advanced/python_advanced/module_02_linux/homework/"))

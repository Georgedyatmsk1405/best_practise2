"""
В своей работе программист должен часто уметь решать рутинные задачи.

Хорошим примером такой задачи является вычисление суммарного размера директории.

Пожалуйста реализуйте функцию, которая на вход принимает путь до папки
    в виде стрки или объекта Path
и возвращает суммарный объём директории в байтах.

В случае, если на вход функции передаётся несуществующий путь или НЕ директория,
    функция должна выкинуть исключение ValueError с красивым описание ошибки
"""

from pathlib import Path
from typing import Union
import subprocess
import os
def calculate_directory_size(directory_path: str) -> int:
    a=os.path.exists(directory_path)
    if a:
        size=subprocess.check_output(['du','-sh',directory_path]).split()[0].decode('utf-8')
        print(size)
        return size
    raise ValueError('not right way')

calculate_directory_size('/home/george/PycharmProjects/pythonProject/python_advanced/module_08_deploy')
#def calculate_directory_size(directory_path: Union[str, Path] = ".") -> int:
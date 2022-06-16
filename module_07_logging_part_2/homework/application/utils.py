from typing import Union, Callable
from operator import sub, mul, truediv, add
from datetime import datetime
import logging.config
from five import dict_config
root_logger = logging.getLogger()
logging.config.dictConfig(dict_config)

module_logger = logging.getLogger('module_logger')
#задание 5 импортируем дикт конфиг который сохраняет от инфо и выше

# Пишем штуку которая постоянно проверяет что логи на 10 часов не застоялись в этом файле
with open("five.log", 'r') as f:
    lines=f.readlines()
    print(lines)
with open("five.log", 'w') as f:
    for i in lines:
        pos=i.split('|')
        print(pos)
        timestr=pos[2].strip().split(',')[0]
        print(timestr)
        time=datetime.strptime(timestr, '%Y-%m-%d %H:%M:%S')
        today = datetime.now()
        print(today)
        result=(today-time)
        result=result.total_seconds()/60
        print(result)

        print(result)
        if result < 600:
            f.write(i)





OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}

Numeric = Union[int, float]


def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    """
    Convert string to arithmetic function
    :param value: basic arithmetic function
    """
    if not isinstance(value, str):
        print("wrong operator type", value)
        raise ValueError("wrong operator type")

    if value not in OPERATORS:
        print("wrong operator value", value)
        raise ValueError("wrong operator value")

    return OPERATORS[value]

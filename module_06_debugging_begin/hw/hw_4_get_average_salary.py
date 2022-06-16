"""
Вы работаете программистом на предприятии.
К вам пришли из бухгалтерии и попросили посчитать среднюю зарплату по предприятию.
Вы посчитали, получилось слишком много, совсем не реалистично.
Вы подумали и проконсультировались со знакомым из отдела статистики.
Он посоветовал отбросить максимальную и минимальную зарплату.
Вы прикинули, получилось что-то похожее на правду.

Реализуйте функцию get_average_salary_corrected,
которая принимает на вход непустой массив заработных плат
(каждая -- число int) и возвращает среднюю з/п из этого массива
после отбрасывания минимальной и максимальной з/п.

Задачу нужно решить с алгоритмической сложностью O(N) , где N -- длина массива зарплат.

Покройте функцию логгированием.
"""
import sys
from typing import List
import logging
logger=logging.getLogger('salary')
k=[1,5,2,4]

def get_average_salary_corrected(salaries: List[int])->float:
    summ=0
    maximum = 0
    minimum=9999999999999999999

    for i in salaries:
        summ+=i

        if i > maximum:
            maximum = i
        if minimum>i:
            minimum=i
    logger.warning(maximum)
    logger.warning(minimum)
    logger.warning(summ)
    summ=summ-maximum-minimum
    answer=summ/(len(salaries)-2)
    logger.warning(answer)
    return answer









print(get_average_salary_corrected(k))
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Вы пытаетесь поссчитать зарплату")


"""
Давайте немного отойдём от логирования.
Программист должен знать не только computer science, но и математику.
Давайте вспомним школьный курс математики.

Итак, нам нужно реализовать функцию, которая принимает на вход
list из координат точек (каждая из них - tuple с x и y).

Напишите функцию, которая определяет, лежат ли все эти точки на одной прямой или не лежат
"""
from typing import List, Tuple


def check_is_straight_line(coordinates: List[Tuple[float, float]]) -> bool:
    answer=False
    for i in range(len(coordinates)-1):
        for j in range(1):
            if coordinates[i][j]==0:
                print("не выполняется условие коллинеарности")
                answer=False
            elif coordinates[i][j]/coordinates[i+1][j]==coordinates[i][j+1]/coordinates[i+1][j+1]:
                answer= True
    print(answer)
    return answer

print(check_is_straight_line([(1,3),(2,4)]))

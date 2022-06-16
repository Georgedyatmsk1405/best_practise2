import typing


def find_insert_position(array: typing.List[int], value: int) -> int:
    count=0
    for i in array:
        if i<value:
            count+=1
    return count
    print(count)

A = [1, 2, 3, 3, 3,3, 5]
x = 4

assert A == sorted(A)
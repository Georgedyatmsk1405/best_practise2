"""
Вася решил передать Пете шифрограмму.
Поскольку о промышленных шифрах Вася ничего не знает,
он решил шифровать сообщение следующим образом: он посылает Пете строку.

1) Каждый символ строки - либо буква, либо пробел, либо точка ".", либо две точки "..".
2) если после какой-то буквы стоит точка, значит мы оставляем букву без изменений
    (об 1ой точке Вася задумался чтобы усложнить расшифровку). Саму точку при этом надо удалить
3) если после какой-то буквы стоит две точки, то предыдущий символ надо стереть.
    Обе точки при этом тоже нужно удалить
4) возможна ситуация, когда сообщение после расшифровки будет пустым.
    В качестве результата можно вернуть просто пустую строку

Помогите Пете написать программу для расшифровки.

Примеры шифровок-расшифровок:
абра-кадабра. -> абра-кадабра
абраа..-кадабра -> абра-кадабра
абраа..-.кадабра -> абра-кадабра
абра--..кадабра -> абра-кадабра
абрау...-кадабра -> абра-кадабра (сначала срабатывает правило 2х точек, потом правило 1ой точки)
абра........ -> <пустая строка>
абр......a. -> a
1..2.3 -> 23
. -> <пустая строка>
1....................... -> <пустая строка>

"""
import math

def decrypt(s: str) -> str:

    a = s.split('.')
    a = [x if x != '' else 1 for x in a]
    vv = []
    for i in range(len(a)):
        if a[i] != 1:
            vv.append(i)

    lena = len(a)

    sresspisok = []
    for i in range(len(vv)):
        if i == 0:
            pass
        else:
            sres = vv[i] - 1 - (vv[i - 1])
            sresspisok.append(sres)
    sreskonez =len(a) - vv[-1] - 2

    sresspisok.append(sreskonez)


    for i in list(a):
        if i == 1:
            a.remove(i)


    uniq_and_fifa = dict(zip(a, sresspisok))
    for item in uniq_and_fifa:
        if uniq_and_fifa[item]==0:
            uniq_and_fifa[item]=0
        else:
            uniq_and_fifa[item] = math.ceil(uniq_and_fifa[item] / 2)
    uniq_and_fifa
    final = []
    for item in uniq_and_fifa:
        slovo = item

        dellen = len(slovo) - uniq_and_fifa.get(item)

        if dellen < 0:
            dellen = 0
            slovored = slovo[0:dellen]
            final.append(slovored)

        else:
            dellen = dellen
            slovored = slovo[0:dellen]
            final.append(slovored)

    final = " ".join(final)
    print(final)
decrypt('..kavalll...kk..kkk....g.')



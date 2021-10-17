import string
import random


def gen(n):
    length = ""
    for i in range(n):
        length += (random.choice(string.ascii_letters))
    return length


def counter(length):
    lows = 0
    caps = 0
    for i in length:
        if i in string.ascii_lowercase:
            lows += 1
        elif i in string.ascii_uppercase:
            caps += 1
    if caps > lows:
        return 1
    elif caps < lows:
        return -1
    return 0


def func(list_1):
    kol_1 = 0
    kol_0 = 0
    for i in list_1:
        c = counter(i)
        if c == 1:
            kol_1 += 1
        elif c == 0:
            kol_0 += 1
    print('Процент количества строк, в которых больше заглавных букв: ',
          round(kol_1 * 100 / len(list_1), 1), "%", sep="")
    print('Процент количества строк, в которых больше маленьких букв: ',
          round((len(list_1) - kol_1 - kol_0) * 100 / len(list_1), 1), "%", sep="")
    print('Процент количества строк, в которых одинаковое число заглавных и маленьких букв: ',
          round(kol_0 * 100 / len(list_1), 1), "%", sep="")

stroka = [gen(3), gen(3), gen(3)]
print(stroka)
func(stroka)
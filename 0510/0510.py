import random


def gen(a, b, c, n):
    i = 0
    while i < n:
        yield random.choice(a)  + random.choice(b) + random.choice(c)
        i += 1


for i in gen(["super", "evil"], ["Arthas", "maks", "ghoul"], ["122", "322", "1337"], 5):
    print(i)


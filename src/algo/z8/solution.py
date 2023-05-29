import random
"""
Słowa sklejamy z sylab w następujący sposób:

słowo:

"abac"

... trzeba złożyć z 2-literowych "sylab"
ab←→ba -> aba
aba←→ac -> abac

(czyli dołączana sylaba 2-literowa ma mieć taką pierwszą literę, jak ostatnia litera słowa do którego jest dołączana)

"""


def split_to_syllables(word: str) -> list[str]:
    #todo: your solution here
    length = len(word)
    length = (length*2)**length
    n = 2
    warms = []
    while(length != 0):
        worms = ''.join((random.choice(word) for i in range(2)))
        warms.append(worms)
        length -= 1
    setted = set(warms)
    return list(setted)



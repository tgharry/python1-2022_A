import re
"""
Słowa sklejamy z sylab w następujący sposób:

słowo:

"abac"

... trzeba złożyć z 2-literowych "sylab"
ab←→ba -> aba
aba←→ac -> abac

(czyli dołączana sylaba 2-literowa ma mieć taką pierwszą literę, jak ostatnia litera słowa do którego jest dołączana)

Zadanie -- mamy dostępny zbiór sylab, oraz pewne słowo `word`; pytanie -- czy przy użyciu tych sylab
(każdą można użyć dowolną liczbę razy, również 0) można utworzyć dane słowo.

"""


def construct_word(syllables: set[str], word: str) -> bool:
    #todo: your solution here
    #sylaby: A E I O U Y, wo/rd
    """""
    for item in syllables:
        if item in word:
            return True
        else:
            return False
    """""
    line = re.findall('..?', word)
    sylable = list(syllables)
    print(f"Line: {line}")
    print(f"Sylables: {sylable}")

    for item in line:
        for items in sylable:
            if items in item:
                return True
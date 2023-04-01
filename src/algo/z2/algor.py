"""""
problem do rozwiązania:
mamy dane dwie listy liczb tej samej wielkości, np. a = [2,5,7,9], b=[4,8,18,27]
dla każdej liczby z tablicy "a" sprawdzić ile jest takich liczb z tablicy "b" które się przez nią dzielą; zwrócić te krotności jako listę
czyli tutaj -- wynik = [3,0,0,2]
"""""

from datetime import datetime
import matplotlib.pyplot as plt
from random import seed, randint

def algor(a, b):
    a1 = set(a)
    wyniks = []
    count = 0
    for a1,b2 in zip(a,b):
        if(a1/b2 == 0):
            wyniks.append((a1/b2))
        else:
            wyniks.append(count)

def solve(a, b):
    a1 = set(a)
    wyniks = []

    for item in a:
        count = 0
        for items in b:
            if item % items == 0:
                count += 1
        wyniks[item] = count

    wynik = [wyniks[item] for item in a]
    return wynik
def generate_data(data_size):
    seed(111)
    mx_num = 10 ** 4
    a = [randint(0, mx_num) for _ in range(data_size)]
    b = [randint(0, mx_num) for _ in range(data_size)]
    return {"a": a, "b": b}


if __name__ == '__main__':
    x, y = run_tests(generate_data, solve, max_size=10**4)
    visualize(x, y)
    # print(solve([2, 5, 7, 9, 2], [4, 8, 18, 27]))


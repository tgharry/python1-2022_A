"""""
napisać funkcje def largetst_sum_10_percet(a: list[int]) => int
która dla danej listy liczb całkowitych (o długości podzielnej prz 10, np 11030) znajdzie największą
sumę ciągłej podlisty długości len(a)/10 podlisty len(a)/10


"""""
from random import seed, randint

from src.algo.z2.algor import solve
from src.algo.z2.gen import run_tests, visualize


def largest_sum_10_percent (a: list[int]):
     N = len(a)
     n = N // 10
     best = sum(a[:n])
     for start in range(0, N - n):
         best = max(best, sum(a[start: start + n]))
     return best

def generate_data(data_size):
    seed(111)
    mx_num = 10 ** 4
    data_a = [randint(0, mx_num) for _ in range(data_size)]
    return {"a": data_a}

if __name__ == '__main__':
    x, y = run_tests(generate_data, solve, max_size=10**4)
    visualize(x, y)
    # print(solve([2, 5, 7, 9, 2], [4, 8, 18, 27]))
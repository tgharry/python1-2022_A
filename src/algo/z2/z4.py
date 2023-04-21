"""""
napisać funkcje def largetst_sum_10_percet(a: list[int]) => int
która dla danej listy liczb całkowitych (o długości podzielnej prz 10, np 11030) znajdzie największą
sumę ciągłej podlisty długości len(a)/10 podlisty len(a)/10


"""""
from random import seed, randint
from src.algo.z2.algor import solver
from src.algo.z2.gen import run_tests, visualize
from src.algo.z2.automat import run_tests, visualize


def largest_sum_10_percent (data: list[int]) -> int:
    piece = len(data) // 10
    max_sum = sum(data[:piece])
    sums = max_sum
    result = []
    for item in range(1,10):
        start = item * piece
        end = start + piece
        if sum(data[start:end]) > sums:
            sums = sum(data[start:end])
            result.append(data[start:end])
        max_sum = max(max_sum, sums)
    return max_sum, result[-1]


def generate_data(data_size):
    seed(12345)
    mx_num = 10 ** 4
    data_a = [randint(0, mx_num) for _ in range(data_size)]
    return {"a": data_a}
#Nie odpalać
print(largest_sum_10_percent(generate_data(100)["a"]))
#if __name__ == '__main__':
#    x, y = run_tests(generate_data, solver, max_size=10**4)
#    visualize(x, y)

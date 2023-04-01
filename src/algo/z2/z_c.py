from random import seed, randint

from src.algo.z2.algor import solve
from src.algo.z2.gen import run_tests, visualize
from random import seed, randint

"""""
zadanie 🇨 Mamy daną tablicę liczb całkowitych; wybieramy dwie różne pozycje w tej tablicy, czyli liczby ix, iy; 
proszę napisać funkcję def best_multiply(a: list[int]) -> int która zwróci 
największą możliwą wartość iloczynu a[ix] * a[iy]
przykład
a=[1,2,3]
wynik: 6
------ 
a=[2,2,-3,-3]
wynik: 9

a = [2,2,-3,-3]
z = len(a)
x = int(input())
y = int(input())

def best_multiply(x, y):
    if (x<z and y < z):
        return a[x] * a[y]
    else:
        return -1

b = best_multiply(x,y)
print(b)
"""
def best_multiply(a: list[int]) -> int:
    x = int(input())
    y = int(input())
    z = len(a)
    while(True):
        if x < z or y < z:
            wynik = a[x] * a[y]
        else:
            wynik = -1
    return wynik
def generate_data(data_size):
    seed(111)
    mx_num = 10 ** 4
    data_a = [randint(0, mx_num) for _ in range(data_size)]
    return {"a": data_a}

if __name__ == '__main__':
    x, y = run_tests(generate_data, solve, max_size=10**4)
    visualize(x, y)
    # print(solve([2, 5, 7, 9, 2], [4, 8, 18, 27])){{{{{
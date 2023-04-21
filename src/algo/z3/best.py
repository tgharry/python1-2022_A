from random import seed, randint
from datetime import datetime

from src.algo.z2.automat import run_tests, visualize

#no
def best_mult(a: list[int]):
    x = datetime.now().timestamp()
    sort = sorted(a)
    result = sort[-2] * sort[-1]
    y = datetime.now().timestamp()
    time_1 = y - x
    print(time_1)
    return result
def solve_time(a: list[int]) -> int:
    time_now = datetime.now().timestamp()
    max_result = 0
    for i in range(len(a)-1):
        res = a[i] * a[i+1]
        if res > max_result:
            max_result = res
    time_end = datetime.now().timestamp()
    time_2 = time_end - time_now
    print(time_2)
    return max_result
def generate_data(data_size):
    seed(111)
    mx_num = 10 ** 4
    data_a = [randint(0, mx_num) for _ in range(data_size)]
    return data_a

print(best_mult(generate_data(10 ** 4)))
print(solve_time(generate_data(10 ** 4)))

# if __name__ == '__main__':
#     x, y = run_tests(generate_data, solve, max_size=10**4)
#     visualize(x, y)
from datatime import datatime
from random import seed, randint
import matplotlib.pyplot as plt
def generator(data_size):
    seed(111)
    return [randint(0, 10**6) for _ in range(data_size)]
def solve_problem(data):
    pass
def run_test(generator, solver):
    size = 10
    sizes = []
    times = []
    while(size<10000):
        repetitons = 200
        time_sum = 0
        for i in range(repetitons):
            st = datatime.now().timestamp()
            ret = solver(data)
            en = datatime.now().timestamp()
            time_sum +=(en-st)
        size.append(size)
        times.append(time_sum/repetitons*10**6)
        #


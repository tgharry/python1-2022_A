from datetime import datetime
import matplotlib.pyplot as plt
from random import seed, randint

"""""
problem do rozwiązania:
mamy dane dwie listy liczb tej samej wielkości, np. a = [2,5,7,9], b=[4,8,18,27]
dla każdej liczby z tablicy "a" sprawdzić ile jest takich liczb z tablicy "b" które się przez nią dzielą; zwrócić te krotności jako listę
czyli tutaj -- wynik = [3,0,0,2]
"""""
wynik = []
def generate_data(data_size):
    a=[randint(1,100) for _ in range(data_size)]
    b=[randint(1,100) for _ in range(data_size)]
    data = (a, b)
    return data

def solver(data):
    x = data[0], y = data[1]
    for item in x:
        counter = 0
        for items in y:
            if items % item == 0:
                counter+=1
            else:
                pass
        wynik.append(counter)
    return wynik

def run_tests(generator, solver):
    size = 10
    sizes = []
    times = []
    while size < 1281:
        print(f'testing solver for {size=}')
        data = generator(size)
        REPETITIONS = 400
        time_sum = 0
        for i in range(REPETITIONS):
            st = datetime.now().timestamp()
            ret = solver(data)
            en = datetime.now().timestamp()
            time_sum += (en - st)

        sizes.append(size)
        times.append(time_sum / REPETITIONS * 10 ** 6)
        size *= 2

    return sizes, times

#nie włączać, zabija laptopa, na przyszłość sprawdzić jak działa na linuxie
if __name__ == '__main__':
    x, y = run_tests(generate_data, solver)

    plt.plot(x, y)
    plt.xlabel("Rozmiar danych")
    plt.ylabel("Czas wykonania (usec)")
    plt.show()
from gen_train_data import generate_data
from collections import Counter
from random import randint, seed
import random
N_CITIES = 100
seed(111)
def generate_data(data_size):
    res = []
    for i in range(data_size):
        res.append((randint(0, N_CITIES - 1), randint(0, N_CITIES - 1)))
    return res
"""
zadanie1:
 Mając dany "rozkład jazdy (z pliku gen_train_data.py), wyświetlić miasto z którego jest najwięcej
 połączeń wychodzących.

"""
def get_city_most_connections(train_data: list[tuple[int,int]]) -> int:
    list = [];
    maxs = 0
    listest = []
    for tupla in train_data:
        a, b = tupla
        list.append(b)
        listest.append(tupla)
    couns = Counter(list)
    lst = Counter(listest)
    #print(list)
    #print(couns.most_common(3))
    print(lst.most_common(3))
    return lst


""""""
##Mając dany "rozkład jazdy (z pliku gen_train_data.py), wyświetlić miasto z którego jest najwięcej
#połączeń wychodzących.
def get_city_most_conection(train_data: list[tuple[int,int]]) -> int:
    destination = {}
    extractios = {}
    for start, end in train_data:
        if start in destination:
            destination[start] += 1
        else:
            destination[start] = 1
        if end in extractios:
            extractios[end] +=1
        else:
            extractios[end] = 1
    return destination, extractios
""""""


def trip(train_data: list[tuple[int,int]]) -> int:
    its = random.choice((train_data))
    x, y = its
    locations = []
    print(f"Starting location: {its}")
    for location in train_data:
        s_T, e_T = location

        if(y<s_T):
            locations.append(location)
            x, y = s_T, e_T
        else:
            break;
    for places in locations:
        print(places)
    print(f'Finish line: {places[-1]}')

trip(generate_data(100))
#Mając dany "rozkład jazdy" (z pliku gen_train_data.py), napisać funkcję która sprawdzi czy można dojechać
#z miasta "a" do miasta "b" (bez przesiadek).
def connected(train_data: list[tuple[int,int]], a: int, b: int) -> bool:
    for start, end in train_data:
        if (start == a) and (end == b):
            return True;
        else: return False;

if __name__ == '__main__':
    start = int(input())
    end = int(input())
    train_schedule = generate_data(40)

    if connected(train_schedule, start, end):
        print("Exist")
    else:
        print()


#Mając dany "rozkład jazdy" (z pliku gen_train_data.py), napisać funkcję która sprawdzi czy można dojechać
#z miasta "a" do miasta "b" z dokładnie jedną przesiadką, czyli czy istnieje para połączeń typu (a,c),(c,b).
# a, b = tupla 1, c,d = tupla 2, jeśli b=c istnieje, więc gdy < or >, end

def one_stop(train_data: list[tuple[int, int]], a: int, b: int) -> bool:
    begin = []
    stopped = []
    for item in train_data:
        if item[0] == a:
            begin.append(item)
        if item[1] == b:
            stopped.append(item)
    for items in range(len(begin)):
        for itemz in range(len(stopped)):
            if begin[items][1] == stopped[itemz][0]:
                return True
"""""
z = int(b) - int(a)
        if(z < 0):
            z = z*-1
            if(maxs < z):
                maxs = z
                finale = f'{tupla} : {maxs}'
            else:
                list.append(f'{tupla} : {z}')
        elif (z>0):
            if (maxs < z):
                maxs = z
                finale = f'{tupla} : {maxs}'
            else:
                list.append(f'{tupla} : {z}')
    print(f'{list}\n------------\n{finale}')
"""""
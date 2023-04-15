from gen_train_data import generate_data
from collections import Counter
import random
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

#get_city_most_connections(generate_data(200))

def get_city_most_conection(train_data: list[tuple[int,int]]) -> int:
    destination = get_city_most_connections(train_data)
    extractios = get_city_most_connections(train_data)

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
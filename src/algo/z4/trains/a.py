from gen_train_data import generate_data
from collections import Counter
"""
zadanie1:
 Mając dany "rozkład jazdy (z pliku gen_train_data.py), wyświetlić miasto z którego jest najwięcej
 połączeń wychodzących.

"""

def get_city_most_connections(train_data: list[tuple[int,int]]) -> int:
    list = [];
    maxs = 0
    for tupla in train_data:
        a, b = tupla
        list.append(b)
    couns = Counter(list)
    print(list)
    print(couns.most_common(3))



get_city_most_connections(generate_data(10))

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
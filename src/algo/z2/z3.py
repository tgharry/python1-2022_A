a = [2,5,7,9]
b=[4,8,18,27]
wynik = []
count = 0;
vaue = 0;
"""""
problem do rozwiązania:
mamy dane dwie listy liczb tej samej wielkości, np. a = [2,5,7,9], b=[4,8,18,27]
dla każdej liczby z tablicy "a" sprawdzić ile jest takich liczb z tablicy "b" które się przez nią dzielą; zwrócić te krotności jako listę
czyli tutaj -- wynik = [3,0,0,2]
"""""

wyniks = []
count = 0
for a1,b2 in zip(a,b):
    if(a1/b2 == 0):
        wyniks.append((a1/b2))
    else:
        wyniks.append(count)
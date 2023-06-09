"""""
Zadania na dziś (wieczorem.... /sad)
Dany będzie napis składający się ze znaków < oraz >
np s=<>>>><><>
🇦 Znaleźć długość najdłuższego kawałka składającego się z takich samych znaków; np. <<> -> 2; <> -> 1, <>>><< -> 3
🇧 Znaleźć (jakąś) tablicę liczb całkowitych a kompatybilną z napisem s w tym sensie, że tablica s opisuje relacje między kolejnymi elementami tablicy a
przykład
s = <<>
możliwe rozwiązanie a=[2,8,10,7]
albo a=[4,5,9,-1]
----
przykład 2
s = <><>
możliwe rozwiązanie
a=[2,10,5,8,3]
----
rozwiązania plz na branchach wychodzących z
"""""

def longest_combination(combination: str) -> int:
    #todo: your solution here
    result = 1
    temp = 1
    for item in range(1,len(combination)):
        if (combination[item] == combination[item-1]) :
            temp+=1
        else :
            result = max(result,temp)
            temp = 1


    result = max(result, temp)
    return result

def compatibility(string: str) -> list[int]:
    result = []
    current_value = 0
    for symbol in string:
        if symbol == '<':
            current_value -= 1
        elif symbol == '>':
            current_value += 1
        result.append(current_value)
    return result




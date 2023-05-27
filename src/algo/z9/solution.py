"""
Zadanie: mamy daną tablicę liczb całkowitych "a"; chcemy potencjalnie stworzyć inną tablicę
tej samej długości, "b", gdzie
b[i] = a[i] lub a[i] - a[j],
przy czym "j" może być inne dla każdego "i".

Chcemy by ostatecznie wszystkie elementy tablicy "b" miały tą samą parzystość... czyli by były wszystkie
parzyste, lub wszystkie nieparzyste. Dodatkowo wszystkie liczby tablicy "a" i "b" mają być > 0.

Przykład:

a = [1, 5, 6]
można wykorzystać do budowy
b = [1, 5, 5]  (wszystkie są nieparzyste, przy czym a[0]=b[0], a[1]=b[1], b[2] = a[2] - a[0])
lub
b = [1, 5, 1]  (teraz na ostatniej pozycji odjęliśmy 5, czyli a[1])



"""


def equalize_parity(a: list[int]) -> bool:
    b = []
    j = 2 #user defined
    try:
        for item in a:
            if item > 0:
                continue
            else:
                return False
        b = a
        c = (a[j] - a[0])
    except:
        return False
    else:
        print(f'{c} || {b}')
        if (c > 0):
            b[-1] = c
            print(b)
        else:
            return False
        b_sum = sum(b)
        print(f'|| {b_sum}')
        v = b_sum % 2
        print(v)
        if (v == 0 or v == 1 or b[-1]%2==1):
            return True
        else:
            return False
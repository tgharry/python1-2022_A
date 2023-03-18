from random import seed, randint
a = [5,1,9,7,2]
s = sorted(a)

def gen_r_ints(count: int, seed_number: int):
    seed(seed_number)
    return [randint(0, 10 ** 6) for _ in range(count)]

def sort_numbers(nums: list([int])) -> list[int]:
    def sort_numbers(nums: list[int]) -> list[int]:
        ret = sorted(nums)
        return ret
#
"""""
count time
5     0.7
"""""

dane = [
    5, 0.7,
    10, 0.75,
    100, 2.4,
    200, 4.9,
    400, 11,
    800, 29,
    1600, 86,
    3200, 224,
    6400, 497,
    12800, 1092]

# zadanie -- wszystkie elementy na parzystych elementach --> do listy "x", pozostae do listy "y"
"""""
x, y = [], []
for item in dane:
        if (item%2==0):
            x.append(item);
        else:
            y.append(item);
print(y)
print(x)
"""""
x,y = dane[::2], dane[1::2]



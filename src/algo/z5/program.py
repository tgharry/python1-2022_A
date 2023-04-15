from collections import defaultdict

w = [1,2,3,3,1,2]

s = set(w)
#print(s)

w = list(set(w))
#print(w)

d = dict()

d[1] = 'akabra'
d[2] = 'xxx'
#print(d)

dd = defaultdict(lambda : [])

dd[1].append(1)
dd[1].append(2)
dd[3].append(3)
#print(dd)


s=['aa', 'a', 'c', 'bb', 'aa']


def unique(x):
    return set(x)

def non_duped(x):
    a= len(x) != len(set(x))
    return a

def non_dupeds(x):
    dupe = []
    status = True
    for item in x:
        if x.count(item) > 1:
            dupe.append(item)
            status = False
    if status == True:
        return "No duplicates"
    else:
        return f"Duplicates: {set(dupe)} \nWhole array: {dupe}"

print(unique(s))
print(non_dupeds(s))
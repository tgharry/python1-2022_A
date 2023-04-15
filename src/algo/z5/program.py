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
    dup = []
    status = True
    for item in x:
        if x.count(item) > 1:
            dup.append(item)
            status = False
    if status == True:
        return "No duplicates"
    else:
        return f"Duplicates: {set(dup)} \nWhole array: {dup}"

print(unique(s))
print(non_dupeds(s))

namesz = [(5,'Adam'), (3,'Jane'), (5, 'Xiao'), (2,'Jane')]

ids = []
names = []
dupe = []
def xyz(array):
    for id, name in array:
        if id not in ids:
            ids.append(id)
        else:
            dupe.append(id)
            return id, name
#print(xyz(namesz))

def zyx(array):
    for id, name in array:
        if name not in names:
            names.append(name)
        else:
            dupe.append(name)
            return id, name
print(zyx(namesz))
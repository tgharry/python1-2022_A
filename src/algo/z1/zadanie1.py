import math
#square and cube
def square(x):
    return x*x;
def cube(x):
    return math.pow(x,3);

def calculator(operation,argument):
    return operation(argument);

print(square(5))
print(cube(3))

#calculator
def Add(x,y):
    return x+y;
def Mul(x,y):
    return x*y;

def Calculator(func, x, y):
    if func == 'Add':
        return print(Add(x,y));
    elif func == 'Mul':
        return print(Mul(x,y));
#test
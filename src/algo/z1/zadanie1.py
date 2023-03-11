# This is a sample Python script.
import math


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def square(x):
    return x*x;
def cube(x):
    return math.pow(x,3);

def calculator(operation,argument):
    return operation(argument);

print(square(5))
print(cube(3))
print(calculator(cube, 3))

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
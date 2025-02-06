# Welcome to my basic Python calculator
# Please follow the input instructions carefully:
# For SoloLearn, input all values 
# in the following order, separated by line breaks:
# 1. Operation number (1 for Sum, 2 for Subtraction,
# 3 for Multiplication, 4 for Division, 5 to Exit)
# 2. First number to operate (only if Operation number is 1-4)
# 3. Second number to operate (only if Operation number is 1-4)
# Example input: 1 5 3 (This will select Sum and add 5 and 3)
# Example input: 5 (This will exit the program)
# If you want to perform multiple operations, input them sequentially:
# Example input: 1 5 3 2 10 4 4 12 3 5
# (This will perform Sum, Subtraction, Multiplication, then Exit)

print('Welcome to my basic Python calculator ')
exit = False


def sum(a, b):
    result = a + b
    return result


def sub(a, b):
    result = a - b
    return result


def mul(a, b):
    result = a * b
    return result


def div(a, b):
    result = a / b
    return result


while exit is False:
    print('——————>')
    print('''Menu
    1 - Sum
    2 - Subtraction
    3 - Multiplication
    4 - Division
    5 - Exit
  ''')

    print('——————>')
    option = int(input('Enter the operation you want to perform [1 - 5]: '))
    if option == 1:
        a = int(input('First number to operate: '))
        b = int(input('Second number to operate: '))
        print(f'Result = {sum(a, b)}')

    elif option == 2:
        a = int(input('First number to operate: '))
        b = int(input('Second number to operate: '))
        print(f'Result = {sub(a, b)}')

    elif option == 3:
        a = int(input('First number to operate: '))
        b = int(input('Second number to operate: '))
        print(f'Result = {mul(a, b)}')

    elif option == 4:
        a = int(input('First number to operate: '))
        b = int(input('Second number to operate: '))
        print(f'Result = {div(a, b)}')

    elif option == 5:
        exit = True
        print(' Thanks to test our program, see ya later')



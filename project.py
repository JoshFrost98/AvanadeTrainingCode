"""
1. Add a menu to a console application to manage activities.
2. Run a selected function.
3. Clear the output
4. Display the menu again or exit if done is selected
"""

import sys
from os import system
import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}


def menu(menu):
    for k, function in menu.items():
        print(k, ':', function.__name__)


def calc():
    print("you have selected menu option the calculator") # Simulate function output.
    while True:
        try:
            value1 = int(input('please input the first number (an integer):  '))
        except:
            print('That is not an real number, try again')
            continue
        break
    while True:
        operation = input('please input the operation to be performed (*, /, +, -):  ')
        if operation == 'x' or operation == '/' or operation == '+' or operation == '-':
            break
        print('that was not an option, try again')
    while True:
        try:
            value2 = int(input('please input the second number (an integer):   '))
        except:
            print('That is not an integer, try again')
            continue
        break
    ans = ops[operation](value1, value2)
    print('The answer is: '+ str(ans))
    input('press any key')
    system('cls')  # clears stdout


def two():
    print("you have selected menu option two") # Simulate function output.
    input("Press Enter to Continue\n")
    system('cls')  # clears stdout


def three():
    print("you have selected menu option three") # Simulate function output.
    input("Press Enter to Continue\n")
    system('cls')  # clears stdout


def exit():
    system('cls')  # clears stdout
    print("Goodbye")
    sys.exit()


def main():
    # Create a menu dictionary where the key is an integer number and the
    # value is a function name.
    system('cls')
    functions_names = [calc, two, three, exit]
    menu_items = dict(enumerate(functions_names, start=1))

    while True:
        menu(menu_items)
        selection = int(
            input("Please enter your selection number: "))  # Get function key
        selected_value = menu_items[selection]  # Gets the function name
        selected_value()  # add parentheses to call the function


if __name__ == "__main__":
    main()
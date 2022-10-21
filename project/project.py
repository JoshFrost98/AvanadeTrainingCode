"""
1. Add a menu to a console application to manage activities.
2. Run a selected function.
3. Clear the output
4. Display the menu again or exit if done is selected
"""

import sys
from os import system
import operator
import time
import random

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
        if operation == '*' or operation == '/' or operation == '+' or operation == '-':
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

def fb(i, j, k):
    if i % j == 0 and i % k == 0:
        return 'foobar'
    if i % j == 0:
        return 'foo'
    if i % k == 0:
        return 'bar'
    return i

def foobar():
    print("you have selected foobar") # Simulate function output.
    max = int(input("Enter the number you wish to generate foobar up to:  "))
    timestep = float(input('Enter the number of seconds between each subsequent generation:  '))
    j = int(input('Enter the number where multiples become foo:  '))
    k = int(input('Enter the number where multiples become bar:  '))
    for i in range(max):
        print(fb(i, j, k))
        time.sleep(timestep)
    
    input('Press any key to exit to main menu')


    system('cls')  # clears stdout


def compliments():
    comps = ['You have a lovely smile', 'Thats a great hairstyle', 'I wish I was as articulate as you,']
    print("you have selected the compliment generator") # Simulate function output.
    name = input("Please input your name:  ")
    index = random.randint(0,2)
    print(comps[index], name)
    input('Press any key to exit to main menu')
    system('cls')  # clears stdout


def exit():
    system('cls')  # clears stdout
    print("Goodbye")
    sys.exit()


def main():
    system('cls')
    functions_names = [calc, foobar, compliments, exit]
    menu_items = dict(enumerate(functions_names, start=1))

    while True:
        menu(menu_items)
        selection = int(
            input("Please enter your selection number: "))  # Get function key
        selected_value = menu_items[selection]  # Gets the function name
        selected_value()  # add parentheses to call the function


if __name__ == "__main__":
    main()
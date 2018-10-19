#!/usr/bin/env python3

# basic if-elif-else demo

x = int(input('Enter a number:'))

if x == 5:
    print('x is 5')
elif x == 10:
    print('x is 10')
else:
    print('I do not know this number')

y = input('Enter your name:')

if y == 'Shiv':
    print('I know your first name is Shiv')
elif y == 'Dayal':
    print('That is your last name Dayal')
else:
    print('I do not know you')

z = int(input('Enter another number'))

if x == 0 and z == 0:
    print('Both the numbers are zero')
elif not(x == 0 or z == 0):
    print('At least one of the numbers is not zero')
else:
    print('Noth the numbers are non-zero')

# if elif and else can be nested

if x == 0:
    if z == 0:
        print('Both the numbers are zero')
    else:
        print('x is zero and z is non-zero')
elif z == 0:
    if x != 0:
        print('x is non-zero and z is zero')
else:
    print('Both the numbers are non-zero')
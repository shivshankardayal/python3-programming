#!/usr/bin/env python3

x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

y = int(input("Please enter another integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


if x == 5 and y == 5:
    print('Both are 5')
elif x > 0 or y > 0:
    print('Both are positive')
else:
    print('Both are negative')

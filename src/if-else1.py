#!/usr/bin/env python3

# false values
#
# constants defined to be false: None and False.
# zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
# empty sequences and collections: '', (), [], {}, set(), range(0)
# everything else is True(this is the symbol)


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


if x == 5:
    if y == 5:
        print('Both are 5')
elif x > -1 or y > -1:
    print('Both are positive or zero')
else:
    print('Both are negative')

#!/usr/bin/env python3

# loops and range function demo

x = range(0, 5)

print(type(x))

# range(a, b) is half-closed half-open interval i.e. it includes a but excludes b i.e. values are a through b-1

for i in x:
    print(i)

i = 0

while not i:
    print('i is False, you need to make it true to exit this loop')
    i = int(input('Enter i:'))

for i in range(1, 11):
    print('\nTable for ' + str(i) + '\n')
    for j in range(1,11):
        print(i, '*', j , '=', i*j)
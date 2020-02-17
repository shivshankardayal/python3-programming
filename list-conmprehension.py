#!/usr/bin/env python

'''
L = [1, 2, 3, 4, 5]

for i in range(len(L)):
    L[i] += 10

print(L)


L = [1, 2, 3, 4, 5]

L = [x + 10 for x in L if x>2]

print(L)

'''
L = [x + y for x in 'abc' for y in 'def']

print(L)

# Manual iteration

I = iter(L)

while True:
    try:
        X = next(I)
    except StopIteration:
        break

    print(X, end=' ')
print()


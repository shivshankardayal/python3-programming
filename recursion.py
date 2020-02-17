#!/usr/bin/env python

'''
def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])

print(mysum([1, 2, 3, 4, 5]))


def fib(a, b, n):
    if n:
        a, b = b, a + b

        print(b)

        fib(a, b, n - 1)


fib(1, 1, 20)

'''
def fact(n):
    if n > 0:
        return n * fact(n - 1)
    else:
        return 1

print(fact(20))



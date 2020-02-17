#!/usr/bin/env python

def f(n):
    '''
    Function f
    '''

    a = 1
    b = 1

    while n:
        a, b = b, a+b
        n = n -1

    print(b)
        


if __name__ == "__main__":
    f(5)

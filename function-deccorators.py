#!/usr/bin/env python

def f(func):
    def wrapper(*args, **kwargs):
        print('Do decorator stuff')
        return func(*args, **kwargs)

    return wrapper

@f
def g(*args, **kwargs):
    print(args, kwargs)
    

g(1,2,3)

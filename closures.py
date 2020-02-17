#!/usr/bin/env python

# We must have a nested function.
# The nested function must refer to a value defined in the enclosing function.
# The enclosing function must return the nested function.


def f():
    def g():
        print('In g')

    return g

x = f()
x()

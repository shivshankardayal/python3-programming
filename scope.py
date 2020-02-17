#!/usr/bin/env python

# order of arguments: positional, default, list, keyword
'''
def f(y=10, x, *var_list, **var_dict):
    print(x, y)

    for i in var_list:
        print('List item is', i)

    for k,v in var_dict.items():
        print('Dictionary items is ', k, v)

f(5, 10, 16, k1=10)
'''
# The enclosing module is a global scope.
# The global scope spans a single file only.
# Assigned names are local unless declared global or nonlocal.
# All other names are enclosing function locals, globals, or built-ins.
# Each call to a function creates a new local scope.

# Local, Enclosing, Global, Built-in

# Global scope

'''
X = 99


def func(Y):
    # Local scope
    X = 90

print(func(1), X) # result is 100



import builtins

print(dir(builtins))


def hider():
    open = 1

    open('scope.py')

hider()



X = 88 # Global X


def func():
    X = 99 # Local X: hides global
    print('Inside func %d' % X)

func()
print(X)



# ways to access global variable

var = 99

def local():
    var = 0 # Change local var


def glob1():
    global var
    var += 1 # Declare global (normal)


def glob2():
    var = 0
    import scope
    scope.var += 1

def glob3():
    var = 0
    import sys
    glob = sys.modules['scope']
    glob.var += 1

def test():
    print('In test %d' % var)

    local(); glob1(); glob2(); glob3()
    print('In test %d' % var)

'''

def f():
    print('In f')
    X = 10
    def g():
        nonlocal X
        X = X + 1
        print('In g')

    g()
    print(X)

f()

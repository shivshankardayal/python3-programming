#!/usr/bin/env python

# lambda is an expression, not a statement.
# lambda's body is a single expression, not a block of statements

def add(x, y): return x + y

print(add(2, 3))

f = lambda x, y: x + y

print(f(2, 3))

# Defaults work on lambda arguments, just like in a def.

x = (lambda a="This", b="is", c="world": a + b + c)

print(x('It'))

def teachers():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)
    return action

act = teachers()
msg = act('Shiv')

print(msg)

# lambda is also commonly used to code jump tables, which are lists or dictionaries of
# actions to be performed on demand.

L = [lambda x: x ** 2,
     lambda x: x ** 3,
     lambda x: x ** 4]

for f in L:
    print(f(2))

print(L[0](3))

def f1(x): return x ** 2
def f2(x): return x ** 3
def f3(x): return x ** 4

L = [f1, f2, f3]
for f in L:
    print(f(2))

print(L[0](3))

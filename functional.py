#!/usr/bin/env python

sum = (lambda x: (lambda y: x + y))
add = sum(99)
print(add(3))


my_list = [1, 2, 3, 4]
my_updated_list = []

for i in my_list:
    my_updated_list.append(i + 10)

print(my_updated_list)

def add_10(i): return i + 10

my_new_list = list(map(add_10, my_list))
print(my_new_list)

my_new_list = list(map((lambda x: x + 10), my_list))
print(my_new_list)

def mymap(func, seq):
    res = []
    for x in seq: res.append(func(x))
    return res

my_new_list = mymap(add_10, my_list)
print(my_new_list)

print(list(range(0, 10)))

print(list(filter((lambda x: x > 5), range(0, 10))))

res = []
for x in range(0, 10):
    if x > 5:
        res.append(x)

g = (x for x in range(0, 10) if x > 5)

for i in g:
    print(i)

from functools import reduce

print(reduce((lambda x, y: x + y), [1, 2, 3, 4]))

L = [1,2,3,4]
res = L[0]
for x in L[1:]:
    res = res + x

print(res)

def myreduce(function, sequence):
    term = sequence[0]
    for next in sequence[1:]:
        term = function(term, next)
    return term

print(myreduce((lambda x, y: x + y), [1, 2, 3, 4, 5]))

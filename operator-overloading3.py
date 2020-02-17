#!/usr/bin/env python

'''
class Counter:
    numOfInstances = 0

    def __init__(self):
        Counter.numOfInstances += 1

    @classmethod
    def printNumOfInstances(cls):
        print("Number of instances is {}".format(cls.numOfInstances))

    
    def __del__(self):
        print('Deleting object ', Counter.numOfInstances)
        Counter.numOfInstances -= 1

x = Counter()
x.printNumOfInstances()
y = Counter()
y.printNumOfInstances()
z = Counter()
x.printNumOfInstances()
y.printNumOfInstances()
z.printNumOfInstances()

x = Counter()
x.printNumOfInstances()

'''

class Called:
    def __call__(self, *args, **kwargs):
        print('Object called ', args, kwargs)


x = Called()
x(1, 2, 3, k=8)


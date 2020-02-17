#!/usr/bin/env python


class Counter:
    numOfInstances = 0

    def __init__(self):
        Counter.numOfInstances += 1

    @classmethod
    def printNumOfInstances(cls):
        print("Number of instances is {}".format(cls.numOfInstances))


x = Counter()
x.printNumOfInstances()
y = Counter()
y.printNumOfInstances()
z = Counter()
x.printNumOfInstances()
y.printNumOfInstances()
z.printNumOfInstances()


class Counter2:
    numOfInstances = 0

    def __init__(self):
        Counter2.numOfInstances += 1

    @staticmethod
    def printNumOfInstances():
        print("Number of instances is {}".format(Counter2.numOfInstances))


x = Counter2()
x.printNumOfInstances()
y = Counter2()
y.printNumOfInstances()
z = Counter2()
x.printNumOfInstances()


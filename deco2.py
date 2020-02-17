#!/usr/bin/env python3

import functools


def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Inside decorator.")
        func(*args, **kwargs)
    return wrapper


def hello(name):
    print("Hello " + name)

hello1 = my_decorator(hello)

hello1('Shiv')
print(hello1.__name__)

#!/usr/bin/env python3


def my_decorator(func):
    def wrapper():
        print("Before execution of func.")
        func()
        print("After execution of func.")
    return wrapper

@my_decorator
def hello():
    print("Hello world!")


hello()

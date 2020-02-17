#!/usr/bin/env/python3

import functools


def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat

    if _func is None:
        return decorator_repeat

    return decorator_repeat(_func)


@repeat(num_times=5)
def hello(name):
    print('Hello ' + name)

@repeat
def say_hello():
    print('Hello')


say_hello()

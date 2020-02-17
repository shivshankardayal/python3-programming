#!/usr/bin/env/python3

import functools


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper_repeat
    return decorator_repeat


@repeat(num_times=5)
def hello(name):
    print('Hello ' + name)


hello('Shiv')

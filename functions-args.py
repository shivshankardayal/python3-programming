#!/usr/bin/env python

def f(x, y=0, *var_arg, **var_dict):
    '''
    Prints the supplied argument.
    '''
    print(x, y)

'''
    for i in var_arg:
        print(i)

    for i in var_dict.items():
        print(i)
'''


if __name__ == "__main__":
    f(5, k1='v1')


#!/usr/bin/env python3

"""
print('I like to be a module.')
if __name__ == '__main__':
    print('module being run directly')
else:
    print('module being imported')
"""

""" importing_module.py - an example of a Python module """

NAME = 'ryan'

__counter = 0


def suml(ls):
    global __counter
    __counter += 1
    total = 0
    for e in ls:
        total += e
    return total

def prodl(ls):
    global __counter
    __counter += 1
    prod = 1
    for e in ls:
        prod *= e
    return prod


def fn(n):
    return n + 1

if __name__ == '__main__':
    print('I prefer to be a module but I can do some tests for you.')
    ls = [i + 1 for i in range(5)]
    print( suml(ls) == 15 )
    print( prodl(ls) == 120 )
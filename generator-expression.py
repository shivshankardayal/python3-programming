#!/usr/bin/env python

print([x ** 2 for x in range(10)])

print((x ** 2 for x in range(10)))


g = (x ** 2 for x in range(10))

print(next(g))
print(next(g))
print(next(g))
print(next(g))

# As iterables, generator expressions can appear in for loops, sum, map, sorted etc just
# like the result of a generator function call.


print(' '.join(x.upper() for x in 'Hello,world!'.split(',')))


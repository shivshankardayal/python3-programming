#!/usr/bin/env python

'''
class Indexer:
    def __getitem__(self, value):
        if isinstance(value, int):
            print('Indexing')
        else:
            print('Slicing', value, value.start, value.stop, value.step)

    def __setitem__(self, index, value):
        if isinstance(value, int):
            print('Indexing setitem')


X = Indexer()
X[5]
X[1:2:6]
X[0] = 5



class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]


X = StepperIndex()
X.data = 'Spam'

for item in X:
    print(item)

print('p' in X)
print([i for i in X])
print(list(map(str.upper, X)))


class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


for i in Squares(1, 5):
    print(i)

X = Squares(1, 3)
I = iter(X)
print(next(I))
print(next(I))
print(next(I))
#print(next(I))

X = Squares(1, 5)

print([n for n in X])
print([n for n in X])

print(36 in Squares(1, 10))
a, b, c = Squares(1, 3)
print(a, b, c)
print(':'.join(map(str, Squares(1, 5))))

'''
class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped)

class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0
    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 1
            return item

alpha = 'abcdef'
skipper = SkipObject(alpha)

for x in skipper:
    for y in skipper:
        print(x + y, end=' ')


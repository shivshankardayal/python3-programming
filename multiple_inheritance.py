#!/usr/bin/env python3


class A:
    def __init__(self):
#        print('A')
        super().__init__()
        self.a = 1

class B(A):
    a = 6
    def __init__(self):
#        print('B')
        super().__init__()
        self.a = 2

class X:
    def __init__(self):
#        print('X')
        super().__init__()
        self.a = 3

class Forward(B, X):
    def __init__(self):
#        print('Forward')
        super().__init__()
        print(self.a)
        print(B.mro()[0].a)

class Backward(X, B):
    def __init__(self):
#        print('Backward')
        super().__init__()
        print(self.a)


#a = A()
#b = B()
#x = X()
f = Forward()
b = Backward()

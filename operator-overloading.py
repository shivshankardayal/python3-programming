#!/usr/bin/env python3

# __init__ Constructor Object creation: X = Class(args)
# __del__ Destructor Object reclamation of X
# __add__ Operator + X + Y , X += Y if no __iadd__
# __or__ Operator | (bitwise OR) X | Y , X |= Y if no __ior__
# __repr__ , __str__ Printing, conversions print(X) , repr(X) , str(X)
# __call__ Function calls X(*args, **kargs)
# __getattr__ Attribute fetch X.undefined
# __setattr__ Attribute assignment X.any = value
# __delattr__ Attribute deletion del X.any
# __getattribute__ Attribute fetch X.any
# __getitem__ Indexing, slicing, iteration X[key] , X[i:j] , for loops and other iterations if no __iter__
# __setitem__ Index and slice assignment X[key] = value , X[i:j] = iterable
# __delitem__ Index and slice deletion del X[key] , del X[i:j]
# __len__ Length len(X) , truth tests if no __bool__
# __bool__ Boolean tests bool(X) , truth tests (named __nonzero__ in 2.X)
# __lt__ , __gt__ ,
# __le__ , __ge__ ,
# __eq__ , __ne__ Comparisons X < Y , X > Y , X <= Y , X >= Y , X == Y , X != Y(or else __cmp__ in 2.X only)
# __radd__ Right-side operators Other + X
# __iadd__ In-place augmented operators X += Y (or else __add__ )
# __iter__ , __next__ Iteration contexts I=iter(X) , next(I) ; for loops, in if no __contains__ , all comprehensions, map(F,X) , others
# ( __next__ is named next in 2.X)
# __contains__ Membership test item in X (any iterable)
# __index__ Integer value hex(X) , bin(X) , oct(X) , O[X] , O[X:] (replaces 2.X__oct__ , __hex__ )
# __enter__ , __exit__ Context manager with obj as var:
# __get__ , __set__ , __delete__ Descriptor attributes X.attr, X.attr = value, del X.attr
# __new__ Creation  Object creation, before __init__


class Time:

    def __init__(self, hour, minute, sec):
        self.hour = hour
        self.minute = minute
        self.sec = sec

    def __eq__(self, value):
        if self.hour == value.hour and self.minute == value.minute and self.sec == value.sec:
            return True
        else:
            return False

    def __lt__(self, value):
        if self.hour < value.hour:
            return True
        elif self.hour > value.hour:
            return False
        else:
            if self.minute < value.minute:
                return True
            elif self.minute > value.minute:
                return False
            else:
                if self.sec < value.sec:
                    return True
                elif self.sec > value.sec:
                    return False
                else:
                    return False


x = Time(10, 20, 30)
y = Time(10, 20, 30)
z = Time(11, 22, 33)

print(x==y, x==z)
print(x<z)

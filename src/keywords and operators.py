#!/usr/bin/env python3

# keywords and operators

import keyword

print(keyword.kwlist)

'''

The Operators:

+   Addition for numbers and concatenation for strings
-   Subtration of numbers
*   Multiplication of numbers. Repitition string if one of the operands is string
/   Division.
%   Remainder
x << y
    Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is 
    the same as multiplying x by 2**y. 
x >> y
    Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y. 
x & y
    Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0. 
x | y
    Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1. 
~ x
    Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. This is the same 
    as -x - 1. 
x ^ y
    Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 
    0, and it's the complement of the bit in x if that bit in y is 1. 
and logical and
or  logical or
not logical not
==  equality operator
!=  inequality operator

Keywords:

False       Boolean
None        None type
True        Boolean
as          For importing modules/names as a different name
assert      For assertions
break       Breaking out of loop
class       Class keyword for object oriented programming
continue    For skipping rest of loop
def         For defining a function
del         Deletes an element from a container or a name
elif        Else if
else        Else part of if control statement
except      Exception part of try/except/finally
finally     Finally block of try/except/finally
for         For loop
from        For importing from modules
global      For overriding scoping
if          If part of if/elif/else statements
import      For importing a module
in          Member test in a container
is          Kind of equality test
lambda      Anonymous function
nonlocal    For avoiding scoping tule
pass        Do nothing
raise       Raise an exception
return      Return from a function
try         try part of try/except/finally
while       while loop
with        For working with unmanaged resource
yield       For defining generators

'''
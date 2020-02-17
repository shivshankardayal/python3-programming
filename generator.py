#!/usr/bin/env python

# Generator functions (available since 2.3) are coded as normal def statements, but
# use yield statements to return results one at a time, suspending and resuming their
# state between each.

# Generator expressions (available since 2.4) are similar to the list comprehensions
# of the previous videos, but they return an object that produces results on demand
# instead of building a result list.

# Generator functions may also have a return statement that, along with falling off the
# end of the def block, simply terminates the generation of values-technically, by raising
# a StopIteration exception after any normal function exit actions. From the caller's
# perspective, the generator's __next__ method resumes the function and runs until either
# the next yield result is returned or a StopIteration is raised.

def generate_squares(n):
    for i in range(n):
        yield i ** 2 # Resume here later

'''
for i in generate_squares(5): # Resume the function
    print(i, end=' : ') # Print last yielded value


x = generate_squares(3)

print(type(x))

print(next(x))
print(next(x))
print(next(x))
print(next(x))

# Generators saves memory and can have higher performance in large programs.
# Generators can provide a simpler alternative to manually saving the state between
# iterations in class objects.
# With generators, variables accessible in the function's scopes are saved and
# restored automatically.

'''
def gen():
    for i in range(10):
        X = (yield i) + 10
        print(X)

g = gen()
print(next(g))
print(g.send(20))
#print(next(g))

# The send method advances to the next item in the series of results, just like __next__ , but also
# provides a way for the caller to communicate with the generator, to affect its operation.
# Technically, yield is now an expression form that returns the item passed to send , not
# a statement (though it can be called either way-as yield X , or A = (yield X) ). The
# expression must be enclosed in parentheses unless it's the only item on the right side
# of the assignment statement. For example, X = yield Y is OK, as is X = (yield Y) + 10 .
# send method can be used, for example, to code a generator that its caller can terminate
# by sending a termination code, or redirect by passing a new position in data
# being processed inside the generator.


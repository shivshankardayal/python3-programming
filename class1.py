#!/usr/bin/env python

# Three powerful aspects of OOP in Python

# Inheritance
# Composition
# Polymorphism

# A class's Distiction with other forms of code

# Multiple Instances
# Customization via Inheritance
# Operator Overloading

# Class objects

# The class statement creates a class object and assigns it a name.
# Assignments inside class statements make class attributes.
# Class attributes provide object state and behavior.

# Objects of class

# Calling a class object like a function makes a new instance object.
# Each instance object inherits class attributes and gets its own namespace.
# Assignments to attributes of self in methods make per-instance attributes.

'''
class MySimpleClass:
    """A simple example class"""
    i = 10

    def __init__(self, name):
        self.name = name
    def f(self):
        return self.name


x = MySimpleClass('Shiv')

print(x.i)
print(x.f())

'''
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return u"Name is {} and age is {}".format(self.name, self.age)

    def __str__(self):
        return "Name is {} and age is {}".format(self.name, self.age)

    def f(self):
        return 'Hello from Person'


x = Person('Shiv', 20)
print(x)


class Employee(Person):

    def __init__(self, name, age, position):
        super().__init__(name,age)
        self.position = position

    def __str__(self):
        return "Name is {}, age is {} and position is {}.".format(self.name, self.age, self.position)

    def __repr__(self):
        return u"Name is {}, age is {} and position is {}.".format(self.name, self.age, self.position)

    def f(self):
        return 'Hello from Employee'


y = Employee('Shiv', 20, 'Manager')
print(y)
print(y.f())



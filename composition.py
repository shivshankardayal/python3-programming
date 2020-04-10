#!/usr/bin/env python3

class Person:
    def __init__(self, name: str):
        self.name = name


class Address:
    def __init__(self, street: str, state: str, country: str, zipcode: int):
        self.street = street
        self.state = state
        self.country = country
        self.zipcode = zipcode

class Employee:
    def __init__(self, person: Person, address: Address):
        self.person = person
        self.address = address
        


p = Person('Shiv')
a = Address('abcd', 'NA', 'US', '123456')

e = Employee(p, a)

print(e.person.name)
print(e.address.street)

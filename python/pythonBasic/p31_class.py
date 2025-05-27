#!/usr/bin/env python

class Person(object) :
    total = 10

    def __init__(self, name, age) :
        self.name = name
        self.age = age

    def getName(self) :
        return self.name

    def getAge(self) :
        return self.age

my = Person('Lee', 28)
print(my.name)
print(my.age)
print(my.getName())
print(my.getAge())
print(my.total)

you = Person('Moon', 23)
print(you.getName())
print(you.getAge())
print(you.total)

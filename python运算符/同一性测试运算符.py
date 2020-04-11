#!/usr/bin/python3
#coding = UTF-8

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Tony', 18)
p2 = Person('Tony', 18)

print(p1 == p2)     #False
print(p1 is p2)     #False

print(p1 != p2)     #True
print(p1 is not p2) #True
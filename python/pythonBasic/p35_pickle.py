#!/usr/bin/env python

import pickle

class SmartPhone(object) :
    def __init__(self, brand, detail, price) :
        self.brand = brand
        self.detail = detail
        self.price = price

    def __str__(self) :
        return f'str:{self.brand} - {self.detail} - {self.price}'

object = SmartPhone('IPhone', 'Apple', 10000)
f = open("test.pickle", 'wb')
pickle.dump(object, f)
f.close()

f = open("test.pickle", 'rb')
object2 = pickle.load(f)
print(object2)

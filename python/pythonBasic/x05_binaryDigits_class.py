#!/usr/bin/env python

import random

class BinaryDigits(object) :
    def __init__(self, num, lists) :
        self.num = num
        self.lists = lists

    def binaryDigits(self) :
        q = self.num // 2
        r = self.num % 2
        self.lists.append(r)
        if q == 0 :
            self.lists.reverse()
            return self.lists
        else :
            self.num = q
            return self.binaryDigits()
    
lists = []
num = random.randint(4, 20)

bd = BinaryDigits(num, lists)

print(f'{num} binary number is : {bd.binaryDigits()}')
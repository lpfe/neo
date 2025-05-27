#!/usr/bin/env python

class GCD(object) :
    def __init__(self, a, b) :
        self.a = a
        self.b = b
    
    def gcd(self) :
        print(f'gcd({self.a}, {self.b})')

        while self.b != 0 :
            r = self.a % self.b
            self.a = self.b
            self.b = r
        return self.a
    
x = int(input("Input first number : "))
y = int(input("Input second number : "))

gcd1 = GCD(x, y)
print(f'gcd({x}, {y}) = {gcd1.gcd()}')
#!/usr/bni/env python

class Factorial(object) :
    def __init__(self, n) :
        self.n = n

    def factorial(self) :
        if self.n == 0 :
            return 1
        else :
            return self.n + self.factorial(self.n - 1)
        # else : 
        #     n = self.n
        #     self.n -= 1
        #     return n * self.factorial()
            
a = int(input("Enter a number : "))

factorial1 = Factorial(a)
print(f'{a} factorial is : {factorial1.factorial()}')
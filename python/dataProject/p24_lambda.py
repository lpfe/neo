#!/usr/bin/env python

i = int(input("Enter the number : "))
j = int(input("Enter another number : "))

a = lambda i, j : i + j

print(f'{i} + {j} = {a(i, j)}')

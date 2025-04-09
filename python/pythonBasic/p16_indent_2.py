#!/usr/bin/env python

n = 0

while True :
    n += 1

    if n > 10 :
        break
    if((n % 2)) :           # 나머지가 있으면 이라는 뜻  or  if(n % 2 == 1) :
        print(n)

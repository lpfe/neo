#!/usr/bin/env python

arr = [1, 2, 3, 4]

print("arr가 저장된 id = ", id(arr))

print("arr type = ", type(arr))

print("10 type = ", type(10))

print("[1,2] type = ", type([1,2]))

print("(타입의 타입은 타입이다~) (10 type = type) = ", type(type(10)))

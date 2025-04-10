#!/usr/bin/env python

somelist = ['김의찬', '유만식', '이영철', '심수련', '윤기석', '노윤철', '황우철']

print(somelist)

print(somelist[4])
print(somelist[-2])
print(somelist[1:4])
print(somelist[4:])

length = len(somelist)
print(f'lentgh of list : {length}')

# 0 2 4 출력
print(somelist[:length:2])

# 1 3 5 출력
print(somelist[1:length:2])

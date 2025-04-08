#!/usr/bin/env python

num = 1
prev = 0
cur = 1

while num < 10:
    next = cur + prev
    print("%3d : %d" % (num, next))
    prev = cur
    cur = next
    num += 1
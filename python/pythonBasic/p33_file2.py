#!/usr/bin/env python

f = open('out.txt', 'w')
f.write("This file is %s \n" % "out.txt")
f.write("End of file")
f.close()

f = open('out.txt', 'r')
line = 1
while line :
    line = f.readline()
    print(line)
f.close()

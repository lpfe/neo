#!/usr/bin/env python

while True :
    i = input("Input the number(q:quit) : ")

    if i == 'q' or i == "Q" :
        break
    elif i.isalpha() :
        print('Please enter a valid input')
        continue
    else :
        if int(i) > 0 :
            print("This is Positive number")
        elif int(i) < 0 :
            print("This is Negative number")
        else :
            print("This is Zero")
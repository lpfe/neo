#!/usr/bin/env python

import datetime

def datetime_deco(func) :
    def decorated() :
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
        print()
    return decorated

@datetime_deco
def func1() :
    print("Main Function1 Start")

@datetime_deco
def func2() :
    print("Main Function1 Start")

@datetime_deco
def func3() :
    print("Main Function1 Start")

func1()
func2()
func3()
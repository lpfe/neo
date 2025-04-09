#!/usr/bin/env python

def division_function(a, b) :
    try :
        print(a / b)
    except Exception as e :         # Exception이 더 큰 개념이라 얘한테 다 걸림
        print('First')
    except TypeError as e :
        print('Second')
    except ZeroDivisionError as e :
        print('Third')

division_function("a", 1)
division_function(1, 0)
division_function(4, 2)


#!/usr/bin/env python

me = {"name" : "Lee", "age" : 28, "gender" : "male"}
print(me)

myname = me["name"]
print(myname)

me["age"] = 29
print(me)

dict = {}
print(dict)

me[10] = 10
print(me)

me['10'] = 10
print(me)

me['job'] = 'student'
print(me)

me['list'] = [1,2,3,4,5]
print(me)
print(me['list'])

me[(1,2)] = 'This is value'
print(me)

me[3] = (3, 'aa', 5)
print(me)

print("=" * 50)
print(f'me[list] : {me["list"]}')
print(f'me[(1,2)] : {me[(1,2)]}')
print(f'me[3] : {me[3]}')

print(f'me[(1,2)] : {me[(1,2)]}')
me[(1,2)] = 'This is real value'
print(f'me[(1,2)] : {me[(1,2)]}')

dict = {'a' : 1234, 'b' : "blog", 'c' : 3333}

# in
if 'b' in dict:
    print('b is exist')
else:
    print('b is not exist')

# key()
print(dict.keys())

for k in dict.keys():
    print(f'key : {k}')

# values
print(dict.values())

if 'blog' in dict.values():
    print('value is exist')
else :
    print('value is not exist')

for v in dict.values():
    print(f'value : {v}')

# items()
print(dict.items())

for i in dict.items():
    print(f'all : {[i]}')
    print(f'key : {i[0]}')
    print(f'value : {i[1]}')
    print()

# get()
v1 = dict.get('b')
print(f'dict.get("b") : {v1}')

v2 = dict.get('z')
print(f'dict.get("z") : {v2}')

# del
print(f'before : {dict}')

del dict['c']

print(f'after : {dict}')

# clear
dict.clear()
print(f'dict : {dict}')
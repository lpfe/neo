import numpy as np
from pandas import DataFrame as df

myindex = ["LEE", "KIM", "KANG", "KWANG", "YUN"]
mycolumns = ["서울", "부산", "광주", "목포", "경주"]
mylist = list(10 * onedata for onedata in range(1, 26))
print(mylist)

myframe = df(np.reshape(mylist, (5, 5)), index = myindex, columns = mycolumns)
print(myframe)

print("\n1 row data read of series")
result = myframe.iloc[1]
print(type(result))
print(result)
print("-" * 50)

print("\n1 row data read of series")
result = myframe.iloc[::2]
print(type(result))
print(result)
print("-" * 50)

print("\n1 row data read of series")
result = myframe.loc[['LEE', 'KIM']]
print(type(result))
print(result)
print("-" * 50)

print(myframe.index)
print("-" * 50)

print("\n1 row data read of series")
result = myframe.loc[['LEE'], ["광주"]]
print(type(result))
print(result)
print("-" * 50)

print("\n1 row data read of series")
result = myframe.iloc[0:3, 0:4]
# == result = myframe.loc['LEE':"KANG", "서울" : "광주"]        iloc / loc
print(type(result))
print(result)
print("-" * 50)

print("\nBoolean Data Processing")
result = myframe.loc[[False, True, True, False, True]]
print(result)
print("-" * 50)
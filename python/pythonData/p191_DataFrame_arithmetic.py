import numpy as np
from pandas import Series, DataFrame

myindex = ["강호연", "유재준", "신동진"]
mylist = [30, 40, 50]

myseries = Series(data = mylist, index = myindex)
print("\n # data of series")
print(myseries)

myindex = ["강호연", "유재준", "이수진"]
mycolumns = ['서울', '부산', '경주']
mylist = list(10 * onedata for onedata in range(1,10))

myframe = DataFrame(np.reshape(np.array[mylist], (3, 3)), index = myindex, columns = mycolumns)
print(myframe)
print("-" * 50)


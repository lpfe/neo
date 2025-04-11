from pandas import Series

print("\n Unique and Count and isin")
mylist = ['라일락','코스모스', '코스모스', '백일홍', '코스모스', '코스모스', '들장미', '들장미', '라일락', '라일락']
myseries = Series(data = mylist)
print(myseries)

print("\n Unique")
myunique = myseries.unique()
print(myunique)
print("-" * 50)

print("\n value_counts()")
mycount = myseries.value_counts()
print(mycount)
print("-" * 50)

print("\n isin")
mask = myseries.isin(['라일락', '들장미'])
print(mask)
print("-" * 50)

print(myseries[mask])
print("-" * 50)
print("Done")
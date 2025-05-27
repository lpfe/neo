import pandas as pd
import numpy as np
from pandas import Series, DataFrame

print("\n # Series의 누락 데이터 처리")
print("\n # 원본 Series")
myseries = Series(['강감찬', '이순신', np.nan, '광해군'])
print(myseries)
print("-" * 50)

print("\n # isnull() 함수 : NaN 이면 True")
print(myseries.isnull())
print("-" * 50)

print("\n # notnull() 이용해서 참인 항목만 출력")
print(myseries[myseries.notnull()])
print("-" * 50)

print("\n # dropna() 이용 누락 데이터 처리")
print(myseries.dropna())
print("-" * 50)


filename = 'excel02.csv'
myframe = pd.read_csv(filename, index_col = '이름', encoding = 'utf-8')
print("\n", myframe)
print("-" * 50)

print("\n # dropna() 이용 누락 데이터 처리")
cleaned = myframe.dropna(axis=0)
print(cleaned)
print("-" * 50)

print("\n # how='all' 이용 누락 데이터 처리")
cleaned = myframe.dropna(axis = 0, how='all')
print(cleaned)
print("-" * 50)

print("\n # how='any' 이용 누락 데이터 처리")
cleaned = myframe.dropna(axis = 0, how='any')
print(cleaned)
print("-" * 50)

print("\n # [영어] 누락 데이터 처리")
# ~


print("\n # columns 기준, how='any' 이용 누락 데이터 처리")
cleaned = myframe.dropna(axis = 1, how = 'any')
print(cleaned)
print("-" * 50)


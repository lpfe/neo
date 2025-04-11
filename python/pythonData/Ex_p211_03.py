import numpy as np
import pandas as pd
from pandas import Series

filename = 'fruitsell.csv'
df = pd.read_csv(filename, index_col = '과일명', encoding = 'utf-8')
print(df)
print("-" * 50)

print("\n 구입액과 수입량의 소계")
print(df.sum(axis = 0))
print("-" * 50)

print("\n 과일별 구입액과 수입량의 소계")
print(df.sum(axis = 1))
print("-" * 50)

print("\n 구입액과 수입량의 평균")
print(np.round(df.mean(axis =0), 2))
print("-" * 50)

print("\n 과일별 평균")
print(np.round(df.mean(axis = 1), 2))
print("-" * 50)
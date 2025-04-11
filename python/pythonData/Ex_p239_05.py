import pandas as pd
from pandas import Series
import matplotlib
import matplotlib.pyplot as plt

# print([f.fname for f in matplotlib.font_manager.fontManager.ttflist])
plt.rcParams['font.family'] = 'NanumBarunGothic'

filename = 'ex802.csv'
myframe = pd.read_csv(filename, encoding = 'utf-8')
print(myframe)

myframe.plot(title = '지역별 차종 교통량', kind = 'line', legend = True, rot = 0)

filename = "p239_DataframeGraph01.png"
plt.savefig(filename, dpi = 400, bbox_inches = 'tight')
print(filename + ' saved')
plt.show()
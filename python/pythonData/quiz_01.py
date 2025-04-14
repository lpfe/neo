from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

plt.rcParams['font.family'] = 'NanumBarunGothic'

html = open('/work/neo/html/source/5/ex5-10.html', 'r', encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
body = soup.select_one('body')
ptag = body.find('p')

body_tag = soup.findAll('td')
print(body_tag)
print("-" * 50)

list = []
for td in body_tag :
    list.append(td.text)
    print(td)

print(list)

# list = np.array(list)
# print(list)

mycolumns = ['이름', '국어', '영어']

myframe = DataFrame(np.reshape(np.array(list), (4, 3)), columns = mycolumns)
myframe = myframe.set_index('이름')
print(myframe)

print("-" * 50)

myframe.astype(float).plot(title='Score', kind = 'line', legend = True)
filename = 'quiz_01_scoreGraph.png'
plt.savefig(filename, dpi = 400, bbox_inches = 'tight')
print(filename + ' saved')
plt.show()
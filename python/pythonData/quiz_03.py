#!/usr/bin/env python

from urllib.request import urlopen
from bs4 import BeautifulSoup

import os
from pandas import DataFrame
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.family'] = 'NanumBarunGothic'

myparser = 'html.parser'
myurl = 'https://www.moviechart.co.kr/rank/boxoffice'
response = urlopen(myurl)
soup = BeautifulSoup(response, myparser)

body = soup.select_one('tbody')
ptag = body.find('td')

infos = soup.findAll('tr')
# print(infos)
# print("-" * 50)


# infos = soup.findAll('div', attrs = {'class' : 'wArea space title'})

# print("-" * 50)
# print(infos)
# print("-" * 50)

no = 0
result = []
for info in infos :
    no += 1
    mytitle = info.find('td', attrs = {'class' : 'title'})
    title = mytitle
    # title = title.string

    myopen = info.find('td', attrs = {'class' : 'date'})
    open = myopen

    myaudience = info.find('td', attrs = {'class' : 'audience'})
    audience = myaudience
    # audience = myaudience.find('span').string

    mycumulative = info.find('td', attrs = {'class' : 'cumulative'})
    cumulative = mycumulative

    mysales = info.find('td', attrs = {'class' : 'sales'})
    sales = mysales

    # result.append([no, title, grade, num])
    result.append([no, title, open, audience, cumulative, sales])

# print(result)
# print("-" * 50)

mycolumn = ['순위', '제목', '개봉일', '관객수', '누적관객수', '누적매출액']

myframe = DataFrame(result, columns=mycolumn)
newdf = myframe.set_index(keys = ['순위'])
print(newdf)

# filename = 'quiz_02_cgvMovie.csv'
# myframe.to_csv(filename, encoding = 'utf-8', index = False)
# print(filename + ' saved')


# '''
# # dfmovie = myframe.reindex(columns = ['제목', '평점', '예매율'])
# # print(dfmovie)

# # mygroup0 = dfmovie['제목']
# # mygroup1 = dfmovie['평점']
# # mygroup1 = mygroup1.str.replace('%', '')
# # mygroup1 = mygroup1.str.replace('?', '0')
# # mygroup2 = dfmovie['예매율']
# # mygroup2 = mygroup2.str.replace('%', '')
# # mygroup2 = mygroup2.str.replace('?', '0')

# # df = pd.concat([mygroup1, mygroup2], axis = 1)
# # df =df.set_index(mygroup0)
# # df.columns = ['평점', '예매율']
# # print(df)

# # df.astype(float).plot(kind = 'barh', title = '영화별 평점과 예매율', rot = 0)
# # filename = 'quiz_02_cgvMovie.png'
# # plt.savefig(filename, dpi = 400, bbox_inches = 'tight')
# # print(filename + ' saved')
# # plt.show()
# '''


# myframe = myframe.reindex(columns = ['제목', '평점', '예매율'])

# myframe['평점'] = myframe['평점'].str.replace('%', '').str.replace('?', '0')
# myframe['예매율'] = myframe['예매율'].str.replace('%', '').str.replace('?', '0')

# myframe = myframe.set_index(keys = ['제목'])
# myframe.columns = ['평점', '예매율']

# # # matplotlib row bar
# myframe.astype(float).plot(kind = 'barh', rot = 0, title = '영화별 평점과 예매율')

# filename = 'quiz_02_cgvMovie.png'
# plt.savefig(filename, dpi = 400, bbox_inches = 'tight')
# print(filename + ' saved')
# plt.show()
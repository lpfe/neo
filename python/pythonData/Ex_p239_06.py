from pandas import Series
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'NanumBarunGothic'

mylist = [30, 20, 40, 30, 60]
myindex = ['강감찬', '김유신', '이순신', '안익태', '윤동주']
myseries = Series(data = mylist, index = myindex)
myseries.plot(kind = 'bar', rot = 0, use_index = True, grid = False, Talbe = False, color = ['r','g','b','y','c'])

plt.slaebl['학생이름']
plt.ylabel('점수')
plt.title('학생별 시험 점수')

for idx in range(myseries.size) :
    value = str(myseries.iloc[idx]) + '건'
    ratioval = '%.1f' % ratio.iloc[idx]

    plt.text(x = idx, y = myseries.iloc[idx] + 1 , s = value, ha = 'center', va ='bottom')
    plt.text(x = idx, y = myseries.iloc[idx] / 2 , s = value, ha = 'center', va ='bottom')

meanval = myseries.mean()
print(meanval)
print('-' * 50)

average = '평균 : %d건' % meanval
plt.axhline(y = meanval, color = 'r', linestyle = '--')

plt.text(x = 2, y = meanval + 5, s = average, ha = 'center', va = 'bottom')
filename = 
plt.show())
    
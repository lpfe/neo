import re

mylist = ['abc123', 'cd456', 'ef789', 'abc12']

# 문자열2개 숫자3개 정규식
regex = '[a-z]{2}\d{3}'
pattern = re.compile(regex)

print("# 문자열2개, 숫자3개 패턴 찾기")
totallist = []
for item in mylist :
    if pattern.match(item) :
        print(item, '은(는) 조건에 적합')
        totallist.append(item)
    else :
        print(item, '은(는) 조건에 부적합')
print("\n조건에 적합한 항목들")
print(totallist)
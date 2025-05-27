# from itertools import count
# from p340_ChickenUtil import ChickenStore

# brandName = 'pelicana'
# base_url = "https://www.pelicana.co.kr/store/store_search.html"

# def getData() :
#     saveData = []

#     for page_idx in count() :
#         url = base_url + "?page=" + str(page_idx + 1)
#         print(url)
#         chickenStore = ChickenStore(brandName, url)
#         soup = chickenStore.getSoup()

#         mytable = soup.find('table', attrs = {'class' : 'info_box'})
#         # mytbody = mytable.find('tbody')
#         print(mytable)

# print(brandName + " 매장 크롤링 시작")
# getData()
# print(brandName + " 매장 크롤링 완료")








from itertools import count
from p340_ChickenUtil import ChickenStore

brandName = 'pelicana'
base_url = 'https://www.pelicana.co.kr/store/store_search.html'

def getData():
    savedData = []

    for page_idx in count():
        # url = base_url + '?page=' + str(page_idx + 1)
        # print( url )
        chknStore = ChickenStore(brandName, base_url)
        soup = chknStore.getSoup()

        mytbody = soup.find('tbody')
        # print(mytbody)

        shopExists = False
        for mytr in mytbody.find_all('tr') :
            shopeExists = True
            mylist = list(mytr.strings)
            # print(mylist)

            imsiphone = mytr.select_one('td:nth-of-type(3)').string
            if imsiphone != None:
                phone = imsiphone.strip()
            else:
                phone = ""

            store = mylist[1]
            address = mylist[3]

            if len(address) >= 2:
                imsi = address.split()
                sido = imsi[0]
                gungu = imsi[1]

            mydata = [brandName, store, sido, gungu, address, phone]
            savedData.append(mydata)

        if shopExists == False:
            chknStore.save2csv(savedData)
            break


print(brandName + ' 매장 크롤링 시작')
getData()
print(brandName + ' 매장 크롤링 끝')
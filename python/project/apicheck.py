import requests

url = 'https://apis.data.go.kr/6260000/BusanCommercialHistoryService/getCommercialHistoryList'
params ={'serviceKey'='z3vCca%2FaCJ%2FU%2FPVs%2Bz4bS%2Be%2Ba6sOBLhXEQQR2BITqZlDdpheoB1%2BUnLhFIjqzWfAmgX1lNhY9YHtQEksaVurDw%3D%3D', 'pageNo' = 1, 'numOfRows' =1}

response = requests.get(url, params=params)
print(response.content)
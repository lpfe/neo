import json, requests
import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import os.path
from fastapi import FastAPI

BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath('./')))
secret_file = os.path.join(BASE_DIR, '../../secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = "Set the {} environment variable.".format(setting)
        return errorMsg
        
app = FastAPI()

@app.get('/') 
async def healthcheck():
    return {"status": "ok"}

@app.get('/hello') 
async def hello():
    return {"massage": "Hello World~!!"}

@app.get('/getdata') 
async def getData():



params = '?serviceKey=' + get_secret('data_apiKey')
params += '&pageNo=1'
params += '&numOfRows=500'
params += '&apiType=JSON'
params += '&status_dt=' + str(today)

url += params
print(url)

response = requests.get(url)
print(response)
print("-" * 50)

contents = response.text
print(type(response))
print(response)
print("-" * 50)

dict = json.loads(contents)
print(type(dict))
print(dict)
print("-" * 50)

items = dict['items'][0]
print(type(items))
print(items)
print("-" * 50)

df = pd.DataFrame.from_dict(items, orient = 'index').rename(columns = {0: 'result'})
print(type(df))
print(df)
print("-" * 50)

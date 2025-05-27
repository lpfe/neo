from fastapi import FastAPI
from pydantic import BaseModel

class HellowWorldRequest(BaseModel):
    name : str
    age : int

app = FastAPI()

@app.get('/')
async def HealthCheck() :
    return {"status": "ok"}

@app.get(path='/hello')
async def Hello_with_querystring(name:str):
    return "Hellow with name. your name is " + name

@app.get('/hello/{name}')
async def Hello_with_name(name : str) :
    return "Hellow with name. your name is " + name


@app.post(path = 'hello/post')
async def Hello_post(request: HellowWorldRequest):
    return "Hello with post. your name is {} and your age is {}".format(request.name, request.age)
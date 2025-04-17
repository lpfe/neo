from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def HealthCheck() :
    return {"status": "ok"}

@app.get('/hello')
async def Hello() :
    return {"mmessage": "Hellow World"}

@app.get('/random')
async def Random(max = None) :
    import random

    if max in None :
        max = 10
    else :
        max = int(max)
    return {"random number": random.randint(1, max)}
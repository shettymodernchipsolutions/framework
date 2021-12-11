from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/name/{name}')
async def name(name: str):
    return f'Hello Woeld {name}'

if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1",port=8000)

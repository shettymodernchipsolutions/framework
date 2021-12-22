# from typing import Optional
#
# from fastapi import FastAPI
# import uvicorn
#
# app = FastAPI()
#
#
# @app.get("/a")
# def read_root():
#     return {"Hello": "World"}
#
# if __name__ == "__main__":
#     uvicorn.run(app)

# from typing import Optional
#
# from fastapi import  FastAPI
# import uvicorn
#
# app = FastAPI()
#
#
# @app.get('/')
# def read_root():
#     return {"Hello":"World"}
#
#
# @app.get('/items/{item_id}')
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": "q"}
#
#
# if __name__=="__main__":
#     uvicorn.run(app, host="127.0.0.1",port=8000)


# from fastapi import FastAPI, Depends
# import uvicorn
# from pydantic import BaseModel
#
# app = FastAPI()
#
#
# @app.get('/home')
# def get():
#     return 'Hello Bhavesh'
#
#
# @app.get('/home/{name}')
# def get(name):
#     return f'Hello {name}'
#
#
# class Item(BaseModel):
#     name: str
#     number: int
#
#
# @app.post('/home/post')
# def post(game: Item):
#     # game ---> Item ---> game = {'name':'name', 'number':12}
#     new_name = game.name
#     new_number = game.number
#     return f'Hello {new_name} you are in {new_number}'
#

# @app.get('/base')
# def base_fun(db : Session = Depends(get_db())):


# if __name__ == '__main__':
#     uvicorn.run(app, host="localhost", port=5000)

# from typing import Optional
# from fastapi import FastAPI
# import uvicorn
#
# from pydantic import BaseModel
#
#
# class PackageIn(BaseModel):
#     secret_id: int
#     name: str
#     number: str
#     description: Optional[str] = None
#
#
# class Package(BaseModel):
#     name: str
#     number: str
#     description: Optional[str] = None
#
#
# app = FastAPI()
#
#
# @app.get('/')
# async def hello_world():
#     return {'Hello': 'World'}


# @app.get('/component/{component_id}')  # path parameter
# async def component(component_id: int):
#     return {"component_id": component_id}
#
#
# @app.get('/component/')
# async def read_component(number : int, text : str): # query parameter
#     return {'number': number, 'text': text}
#
#
# @app.get('/component/')
# async def get_component(number : int, text : Optional[str]):
#     return {'number' : number, 'text' : text}


# @app.post('/package/', response_model=Package, response_model_include={'description'})
# async def make_package(package: PackageIn):
#     return package
#
# if __name__ == '__main__':
#     uvicorn.run(app, host="localhost", port=5000)


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import uvicorn


class Todo(BaseModel):
    name: str
    due_date: str
    description: str


app = FastAPI(title="Todo API")

# Concept of Create, Read, Update and Delete

store_todo = []


@app.get('/')
async def home():
    return {'Hello': 'World'}


@app.post('/todo/')
async def create_todo(todo: Todo):
    store_todo.append(todo)
    return todo


@app.get('/todo/', response_model=List[Todo])
async def get_all_todos():
    return store_todo


@app.get('/todo/{id}')
async def get_todo(id: int):
    try:
        return store_todo[id]

    except:
        raise HTTPException(status_code=404, detail='Todo Not Found')


@app.put('/todo/{id}')
async def update_todo(id: int, todo: Todo):
    try:
        store_todo[id] = todo
        return store_todo[id]

    except:
        raise HTTPException(status_code=404, detail='Todo Not Found')


@app.delete('/todo/{id}')
async def delete_todo(id: int):
    try:
        obj = store_todo[id]
        store_todo.pop(id)
        return obj

    except:
        raise HTTPException(status_code=404, detail='Todo Not Found')

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=5000)

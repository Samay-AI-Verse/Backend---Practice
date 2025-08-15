# from fastapi import  FastAPI,Path
# from pydantic import BaseModel

# from typing import List

# class stud(BaseModel):
#     id : int
#     name : str
#     age : int

# list = []


# app = FastAPI()

# @app.get('/')
# def show():
#     return "hello world!"



# @app.get("/data")
# def show():
#     return list



# @app.post("/data")
# def showdata(user:stud):
#     list.append(user)
#     return user


# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# # Request body model
# class Stud(BaseModel):
#     id: int
#     name: str

# # Path parameter + request body
# @app.post("/access/{id}")
# def access(id: int, data: Stud):
#     if data.id == id:
#         return {"message": f"Hello {data.name}!"}
#     else:
#         return {"error": "ID mismatch"}

from fastapi import FastAPI
from pydantic import BaseModel

# get , post , put , delete 




app = FastAPI()

students = {
    1: {"name": "Samay", "age": 21},
    2: {"name": "Aarav", "age": 22}
}

@app.get("/")
def welcome():
    return {"Welcome to the backend lecture...."}


# @app.get("/show")
# def show():
#     return students



@app.get("/show")
def seedata(id : int):
    return students.get(id)

# pydantic 


class Students(BaseModel):
    id:int
    name:str
    age:int


@app.post("/show")
def addData(data:Students):
    students[data.id] = {"name":data.name, "age":data.age}
    return students

@app.get("/seealldata")
def showone():
    return students



@app.put("/show")
def update_method(id:int,data:Students):
    if id in students:
        students[id] = data.dict()
        return "Data is updated"
    return "Id is not found"
    


@app.delete("/show")
def delete(id : int):
    if id in students:
        del students[id]
        return "Deleted the data"



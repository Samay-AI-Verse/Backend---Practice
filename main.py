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








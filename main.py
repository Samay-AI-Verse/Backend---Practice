



@app.get("/data")
def show():
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

# from fastapi import FastAPI
# from pydantic import BaseModel

# # get , post , put , delete 




# app = FastAPI()

# students = {
#     1: {"name": "Samay", "age": 21},
#     2: {"name": "Aarav", "age": 22}
# }

# @app.get("/")
# def welcome():
#     return {"Welcome to the backend lecture...."}


# # @app.get("/show")
# # def show():
# #     return students



# @app.get("/show")
# def seedata(id : int):
#     return students.get(id)

# # pydantic 


# class Students(BaseModel):
#     id:int
#     name:str
#     age:int


# @app.post("/show")
# def addData(data:Students):
#     students[data.id] = {"name":data.name, "age":data.age}
#     return students

# @app.get("/seealldata")
# def showone():
#     return students



# @app.put("/show")
# def update_method(id:int,data:Students):
#     if id in students:
#         students[id] = data.dict()
#         return "Data is updated"
#     return "Id is not found"
    


# @app.delete("/show")
# def delete(id : int):
#     if id in students:
#         del students[id]
#         return "Deleted the data"


# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import List



# class student(BaseModel):
#     id : int
#     name : str
#     age : int


# MyList : List[student] = []

# app = FastAPI()

# @app.post("/show")
# def addData(stud:student):
#     MyList.append(stud)
#     return f"Data is added successfully {stud}"


# @app.get("/show")
# def show():
#     return MyList

# @app.put("/show")
# def update(input_id:int, Updated:student):
#     for index,data in enumerate(MyList):
#         if data.id == input_id:
#             MyList[index] = Updated
#             return Updated
#     return "Faild"


# @app.delete("/show")
# def deletedata(id:int):
#     for index,data in enumerate(MyList):
#         if data.id == id:
#             MyList.pop(index)
#             return "List deleted successfullly"
#         return "not found"


# @app.post("/student")
# def create_student(student: student):
#     return {"message": "Student created", "data": student}





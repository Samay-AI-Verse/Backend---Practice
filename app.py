from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# students = {
#     1: {"name": "Samay", "age": 21},
#     2: {"name": "Aarav", "age": 22},
#     3: {"name": "Shivam", "age": 22},
# }

# # get post delete put 


# @app.get("/")
# def show():
#     return students





# class main(BaseModel):
#     name : str
#     age : int


# list1 = []



# @app.post("/send")
# async def send(student:main):
#     list1.append(student)
#     return "data added "

# @app.get("/show")
# def getdata():
#     return list1


list1 = [{"id":1,"name":"samay","age":19 },{"id":1,"name":"samay","age":19 }]


class student(BaseModel):
    id:int
    name:str
    age:int


@app.get("/")
def show():
    return {"welcome":f"{list1}"}


@app.post("/insert")
def addData(student:student):
    list1.append(student.dict())
    return {"message":"Data insterted...."}

@app.put("/update")
async def update(id:int , student:student):
    pass







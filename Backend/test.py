from fastapi import FastAPI,Path,Query
from pydantic import BaseModel

app = FastAPI()

list1 = [
 {
    "id": 1,
        "name": "Samay",
        "age": 19,
        "marks": 78.9
    }
]

class Students(BaseModel):
    id :int
    name:str
    age:int
    marks:float




@app.get("/")
def show():
    return list1

@app.post("/")
def show(students:Students):
    list1.append(students)
    return list1


@app.get("/show")
def showdata(id:int):
   for x , data in enumerate(list1):
       if data["id"] == id:
           return list1[x]
   return {"Message":"Data not found"}


    
        


@app.put("/show/{id}")
def show(id:int, updated_data:Students):
    for x ,data in enumerate(list1):
        if data["id"] == id:
            list1[x] = updated_data
            return updated_data
    return {"Message":"Data not found"}




@app.delete("/show/{id}")
def show(id:int):
    for x , data in enumerate(list1):
        if data["id"] == id:
            del list1[x]
            return {"Data is deleted"}
    return {"Data is not delted"}

@app.get("/data")
def show(id:int):
    return {"Data is find"}





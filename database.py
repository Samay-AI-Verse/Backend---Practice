from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()



client = MongoClient("mongodb://localhost:27017/")
db = client["MydataBase"]
collection = db["Mydata"]


@app.get("/")
def show():
    return "connection is work...."


@app.post("/insert")
async def insert(email:str, password:str):
       user = {"mail":email, "pass":password}
       new_data = collection.insert_one(user)
       return {"message": "User added!"}

@app.get("/getAllData")
def getdata():
      list1 = []
      for u in collection.find():
            list1.append({
                  "id":str(u["_id"]),
                  "mail":u["mail"], 
                  "pass":u["pass"]
           } )
      return list1
      

@app.get("/getoneData")
def getdata(email:str):
      user = collection.find_one({"mail": email})
      if user:
            return {
            "id": str(user["_id"]),
            "mail": user["mail"],
            "pass": user["pass"]
        }
      return {"message": "User not found"}
      
      

@app.put("/getoneData")
def getdata(email:str):
      user = collection.update_one({"mail": email})
      return {"message": "User updated"}
      
      


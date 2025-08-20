
from fastapi import FastAPI,Path,Query

app = FastAPI()

dict = {

    1:{"Name":"Samay","age":19,"roll":12},
    2:{"Name":"Nandini","age":17,"roll":13},
    3:{"Name":"Shivam","age":18,"roll":14},
    4:{"Name":"aryan","age":19,"roll":15}

}

# print(dict)


@app.get('/')
def root():
    return {"Message":"Welcome to backend lecture"}

@app.get('/show/data')
async def showData():
    return dict

# input parameters 

# path / Query 

@app.get('/my')
def showMy(a:int,b:str,c:float):
    return {"Message":f"value of a  = {a}, Value of b = {b}, value of c = {c}"}




@app.get("/read/{userid}/{Name}")
def getdata(Name:str = Path(..., description="Enter user ID here: ", example="1"),userid:int = Path(..., description="Enter user ID here: ", example="1")):
    return dict[userid]



@app.get("/mydata")
def showdata(list : int = Query(..., description="Enter list elements", example="[1,2,3,4]")):
    return dict


@app.get("/natural/{number}")
def natural(number:int):
     result = 0
     for x in range(1,number + 1 ):
         result = result + x 
     return result
     





# def natural(number:int):
#      result = 0
#      for x in range(1,number + 1):
#          result = result + x
#          print(result)

     

# natural(3)
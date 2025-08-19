
from fastapi import FastAPI,Path,Query

app = FastAPI()

data = []

@app.get("/")
def show():
    return data


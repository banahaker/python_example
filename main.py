from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class People(BaseModel):
  age: int
  name: str


# Basic GET Router
@app.get("/")
def root_router():
  return "hello, world!"

# Basic POST Method
@app.post("/{id}")
def id_get(id: int, user: People):
  return {"id": id, "age":  user.age}

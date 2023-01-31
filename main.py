from fastapi import FastAPI
from pydantic import BaseModel
from algorithm import lazpPleaseYou
from algorithm import isPrime
from algorithm import GCD

app = FastAPI()

class People(BaseModel):
  age: int
  name: str


# Basic GET Router
@app.get("/")
def root_router():
  return "hello, world!"

# Basic Router Parm and Body usage
@app.get("/people/{id}")
def id_get(id: int, user: People):
  return {"id": id, "age":  user.age}


@app.get("/query/")
def request_with_query(a: int = 0, b: str = "aaa"):
  return {"a": a, "b": b}



"""API with Algorithm"""
@app.post("/lazp")
def lazp(CupA: str, CupB: str):
  return lazpPleaseYou(CupA, CupB)

@app.get("/prime")
def prime(n: int):
  return isPrime(n)

@app.get("/gcd")
def gcd(x: int, y:int):
  return GCD(x, y)
from typing import Union

from fastapi import FastAPI

app = FastAPI()

users = {
    "a": "aaa",
    "b": "bbb"
}

@app.get("/")
def read_root():
    return {"Hello": "World", "world": "hello"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/user/")
def get_user(user_id: str):
    if user_id in users:
        return {"user_id": users[user_id]}
    return {"user_id": "user not found"}

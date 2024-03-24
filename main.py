from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from app import gpu_info, sys_info

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float

@app.get("/gpu_info")
async def read_gpu():
    return gpu_info.get_gpu_info()

@app.get("/sys_info")
async def read_sys():
    return sys_info.get_sys_info()

'''
@app.post("/items/")
async def create_item(item: Item):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    result = {"item_id": item_id, **item.dict()}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"deleted": item_id}
'''
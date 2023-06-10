from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    item_id: int
    title: str
    Description: str

items=[]


@app.get("/items/")
async def read_items(limit:int=10):
    return items[:limit]

@app.post("/create_item/")
async def create_item(item: Item):
    items.append(item)
    return item

@app.post("/delete_item/{item}")
async def delete_item(item:int):
    res = dict()
    for idx, val in enumerate(items):
        res[idx+1] = val
    poped_item=items.pop(items.index(res.pop(item)))
    return poped_item


@app.post("/update_item/{selected_item}")
async def update_item(selected_item:int,item:Item):
    res = dict()
    for idx, val in enumerate(items):
        res[idx+1] = val
    index=items.index(res.pop(selected_item))    
    poped_item=items.pop(index)    
    items.insert(index,item)
    return items


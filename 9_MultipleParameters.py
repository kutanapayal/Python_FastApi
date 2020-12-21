#MultipleParameters

from fastapi import FastAPI, Path, Body
import uvicorn
from pydantic import BaseModel

app=FastAPI(debug=True)

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

class User(BaseModel):
    username: str
    full_name: str = None

@app.put("/items/{item_id}")
async def update_item(
            *,
            item_id: int=Path(...,title="The ID of the item  to get"),
            q: str=None,
            item: Item=None
            ):
            result={"item_id":item_id}
            if q:
                result.update({"q":q})
            if item:
                result.update({"item":item})
            return result

@app.put("/items_new/{item_id}")
async def update_item(*,item_id: int, item:Item, user:User , q:int =Body(...,)):
    result={"item_id":item_id,"item":item,"q":q,"user":user}
    return result

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)
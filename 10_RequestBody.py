#RequestBody parameter specification

from fastapi import FastAPI, Body
import uvicorn
from pydantic import BaseModel,Field

app=FastAPI(debug=True)

class Item(BaseModel):
    name: str
    des: str=Field(None,title="Description of item",max_length=250)
    price: float=Field(...,gt=0,le=100,description="The price of item")
    tax: float=None

@app.put("/items/{item_id}")
async def update_item(*,item_id:int, item: Item=Body(...,embed=True,example={
                        "name":"Foo",
                        "description":"A very good item",
                        "price":35.4,
                        "tax":3.2,
                    },)):
    results={"item_id":item_id,"item":item}
    return results

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)
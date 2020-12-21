import uvicorn
from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI(debug=True)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

#fastapi has automatic support of async so it's work fine with async
@app.get("/items/{item_id}")
async def read_item(item_id: int , q: Optional[str] = None):
    return {"item_id": item_id,"q": q}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)


#  Command to run --> uvicorn FastApi:app --reload
#  Browse http://127.0.0.1:8000/item/5?q=hello
#  Browse this to get automatic document http://127.0.0.1:8000/docs
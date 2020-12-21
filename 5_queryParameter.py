#Query parameter

import uvicorn
from fastapi import FastAPI

app =FastAPI(debug=True)

app.get("/item/")
async def read_item(skip : int=0, limit: int=1):
    return {"skip":skip,"limit":limit}

@app.get("/items/{item_id}")
async def read_item(item_id: int , q: str = None):
    if q:
        return {"item_id": item_id,"q": q}
    return {"item_id": item_id}

@app.put("/getitems/{item_id}")
async def read_item(item_id: int, q: str=None, short: bool=False):
    item={"item_id":item_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"short":"false"})
    return item

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
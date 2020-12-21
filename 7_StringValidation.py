#String Validaion of path parameter

from fastapi import FastAPI, Query
import uvicorn
from typing import List

app=FastAPI(debug=True)

@app.get("/prodect/")
async def get_product(product_id:str=Query(None,max_length=10,min_length=2,alias="product-id",regex='^p\d{1,6}')):
    return product_id

#@app.get("/item/")
#async def create_item(item_id:List[str]=Query(...,max_length=10,min_length=2)):
 #   return item_id

@app.get("/item/")
async def create_item(item_id:List[str]=Query(["pencil","pen"],title="Item list",max_length=10,min_length=2,
                                              deprecated=True,description="list of items to be returned")):
    results = {"item_id":item_id}
    return results

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)
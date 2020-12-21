#Number Validation

from fastapi import FastAPI,Query,Path
import uvicorn

app=FastAPI(debug=True)

app.get("/items/")
async def read_items(item_id: str= Query(...,min_length=2,max_length=10,regex="Item\d{1,6}")):
    results = {"items":[{"item_id":"pen"},{"item_id":"pencil"}]}
    results.update({"New item":item_id})
    return results

#@app.get("/items/{item_id}")
#async def read_items(item_id: str= Path(...,title="Item_id",description="Id for item you want to retrieve.",min_length=3),
 #                       item: str=Query(...,min_length=2,max_length=10)):
  #  return{"item_id":item_id,"item":item}


@app.get("/items/{item_id}")
async def read_items(item: int =Query(None,gt=2,le=10),
                        item_id: float= Path(...,title="Item_id",description="Id for item you want to retrieve.",ge=3,le=10)
                        ):
    return{"item_id":item_id,"item":item}

if __name__=="__main__":
   uvicorn.run(app,host="127.0.0.1",port=8000)
from fastapi import FastAPI, Body
import uvicorn
from pydantic import BaseModel,Field,HttpUrl
from typing import List, Set, Dict

app=FastAPI(debug=True)

class Image(BaseModel):
    name:str
    url:HttpUrl

class Item(BaseModel):
    name: str
    description: str=Field(None,title="Description of item",max_length=250)
    price: float=Field(...,gt=0,le=100,description="The price of item")
    tax: float=None
#    tags:list=[]
    tags: List[int]=None      #List use for Data  type indication
    shape: Set[str]=[]      #Set removes Duplication
    image:List[Image]=None

class offer(BaseModel):
    name:str
    description:str=Field(None)
    price:float
    items:List[Item]

@app.put("/items/{item_id}")
async def update_item(*,item_id:int, item: Item=Body(...,embed=True)):
    results={"item_id":item_id,"item":item}
    return results


@app.put("/offers/{offer_id}")
async def update_offer(*,offer_id:int, offers: List[offer]):
    results={"offer-id":offer_id,"Offers":offers}
    return results

@app.put("/dictExample/")
async def get_weight(*,weight:Dict[str,float]):
    return weight


if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)
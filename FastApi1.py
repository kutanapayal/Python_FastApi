import uvicorn
from fastapi import FastAPI
from typing import Optional


app = FastAPI(debug=True)

#fastapi has automatic support of async so it's work fine with async
@app.get("/")
async def msg():
    return "hello welcome "

@app.get("/items/{item_id}")
async def read_item(item_id: int , q: Optional[str] = None):
    return {"item_id": item_id,"q": q}

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)


#  Command to run --> uvicorn FastApi:app --reload
#  Browse http://127.0.0.1:8000/item/5?q=hello
#  Browse this to get automatic document http://127.0.0.1:8000/docs
from fastapi import FastAPI, Header
import uvicorn

app=FastAPI(debug=True)

@app.get("/items/")
async def read_items(*,ads_id: str =Header("ads")):
    return {"ads_id":ads_id}

@app.get("/itemsOne/")
async def read_items(*,user_agent: str =Header(None)):
    return {"user-Aget":user_agent}

@app.get("/itemsTwo/")
async def read_items(*,strange_header: str =Header(None,convert_underscores=False)):
    return {"strager_header":strange_header}

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)

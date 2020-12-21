#path parameter

from enum import Enum
import uvicorn
from fastapi import FastAPI

app=FastAPI()

class ModelName(str,Enum):
    telnet: "telnet"
    ftp: "ftp"
    tcp: "tcp"

@app.get("/model/{model_name}")
async def read_model(model_name:ModelName):
    if model_name==ModelName.telnet:
        return "ModelName : telnet"
    if model_name.value =="ftp":
        return "ModelName : ftp"
    if model_name==ModelName.tcp:
        return "ModelName : tcp"
    return "it's not defined"

@app.get("/file/{file_path:path}")
async def read_file(file_path:str):
    return "filepath :" + file_path


if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)

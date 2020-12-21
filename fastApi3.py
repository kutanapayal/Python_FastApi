import uvicorn
from fastapi import FastAPI
from typing import Optional

app = FastAPI(debug=True)

#fastapi has automatic support of async so it's work fine with async
@app.get("/users/me")
async def read_user():
    return {"hi it's me!"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/users/{filepath:path}")
async def read_filepath(filepath: str):
    return {"filepath": filepath}
if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)

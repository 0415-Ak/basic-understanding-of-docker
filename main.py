from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app=FastAPI()

class calcop(BaseModel):
    a:float
    b:float
    op:str

@app.post("/api/calculate")
def calculation(req:calcop):
    if req.op=="add":
        result=req.a+req.b
    elif req.op=="sub":
        result=req.a-req.b
    elif req.op=="mul":
        result=req.a*req.b
    elif req.op=="div":
        if req.b==0:
            raise HTTPException(status_code=400, detail="Cannot divide by zero")
        result=req.a/req.b
    else:
        raise HTTPException(status_code=400, detail="Invalid operation")
    return {"result": result}


app.mount("/", StaticFiles(directory="static", html=True), name="static")
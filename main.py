# main.py
from fastapi import FastAPI
from gravitydatabase import GravityDatabase
from pydantic import BaseModel, HttpUrl
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/update")
def update_url():
    test = GravityDatabase()
    output = test.update()
    return json.dumps({"console output": output.split("\n")})

@app.get("/enable/{adlist_comment}")
async def enable_url(adlist_comment: str):
    test = GravityDatabase(comment=adlist_comment)
    return {"message": test.toggle(is_enabled=True)}
    # add proper documentation and status codes from 

@app.get("/disable/{adlist_comment}")
async def disable_url(adlist_comment: str):
    test = GravityDatabase(comment=adlist_comment)
    return {"message": test.toggle(is_enabled=False)}

@app.get("/status/{adlist_comment}")
async def status(adlist_comment: str):
    test = GravityDatabase(comment=adlist_comment)
    return {"message": test.status()}

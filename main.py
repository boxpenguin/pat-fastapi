# main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from gravitydatabase import GravityDatabase
from pydantic import BaseModel, HttpUrl

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/update", response_class=PlainTextResponse)
def update_url():
    test = GravityDatabase()
    output = test.update()
    return output.replace("\u001b[K", "")

@app.get("/enable/{adlist_comment}")
async def enable_url(adlist_comment: str):
    test = GravityDatabase(comment=adlist_comment)
    return {"message": test.enable_adlist()}
    # add proper documentation and status codes from 

@app.get("/disable/{adlist_comment}")
async def disable_url(adlist_comment: str):
    test = GravityDatabase(comment=adlist_comment)
    return {"message": test.disable_adlist()}

@app.get("/status/{adlist_comment}")
async def status(adlist_comment: str):
    test = GravityDatabase(comment=adlist_comment)
    return {"message": test.status()}

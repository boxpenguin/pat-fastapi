# main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse, RedirectResponse
from gravitydatabase import GravityDatabase

app = FastAPI()

@app.get("/", response_class=RedirectResponse)
async def root():
    return "/pat-fastapi/"

@app.get("/pat-fastapi/")
async def root():
    return {"message": "Hello World"}

@app.get("/pat-fastapi/update", response_class=PlainTextResponse)
def update_url():
    test = GravityDatabase()
    return test.update()

@app.get("/pat-fastapi/enable/{adlist_comment}")
async def enable_url(adlist_comment: str):
    test = GravityDatabase(comment=adlist_comment)
    return {"message": test.enable_adlist()}
    # add proper documentation and status codes from 

@app.get("/pat-fastapi/disable/{adlist_comment}")
async def disable_url(adlist_comment: str):
    test = GravityDatabase(comment=adlist_comment)
    return {"message": test.disable_adlist()}

@app.get("/pat-fastapi/status/{adlist_comment}")
async def status(adlist_comment: str):
    test = GravityDatabase(comment=adlist_comment)
    return {"message": test.status()}

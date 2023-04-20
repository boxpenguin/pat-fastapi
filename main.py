# main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
from gravitydatabase import GravityDatabase
from app_stdout import app_stdout_router

app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse("/pat-fastapi/")

@app.get("/pat-fastapi/")
async def root():
    return {"message": "Hello World"}

@app.get("/pat-fastapi/update", response_class=PlainTextResponse)
def update_url():
    test = GravityDatabase()
    output = test.update()
    return output

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

app.include_router(app_stdout_router, prefix='/stdout')
# main.py
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import PlainTextResponse, RedirectResponse
from gravitydatabase import GravityDatabase
from pydantic import BaseModel, HttpUrl

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
    return output.replace("\u001b[K", "")

@app.get("/pat-fastapi/enable/{adlist_comment}")
async def enable_url(adlist_comment: str):
    test = GravityDatabase(comment=adlist_comment)
    return {"message": test.enable_adlist()}

@app.get("/pat-fastapi/disable/{adlist_comment}")
async def disable_url(adlist_comment: str):
    test = GravityDatabase(comment=adlist_comment)
    return {"message": test.disable_adlist()}

@app.get("/pat-fastapi/status/{adlist_comment}")
async def status(adlist_comment: str):
    test = GravityDatabase(comment=adlist_comment)
    result = test.status()
    if result is None:
        raise HTTPException(status_code=404, detail=f"Adlist with comment '{comment}' not found.")
    return {"message": result}

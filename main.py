# main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import PlainTextResponse
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

#broken code????
from fastapi import APIRouter
from my_class import PiholeGravity

router = APIRouter()

# create an instance of the PiholeGravity class
pihole_gravity = PiholeGravity()

@router.get("/run-gravity-script")
async def run_gravity_script():
    return await pihole_gravity.run_gravity_script()
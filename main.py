# main.py
from fastapi import FastAPI
from gravitydatabase import GravityDatabase
from pydantic import BaseModel, HttpUrl

app = FastAPI()

class Status(BaseModel):
    address: HttpUrl
    status: bool
    updated: str


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/update")
def update_url():
    test = GravityDatabase()
    output = test.update()
    return output

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

# we can have the api perform a python code thing and then do some server side code and reply as a json

"""
How will this work?
UX:
user accesses website to enable
SRV:
perform sqlite3 operation to enable

UX:
user accesses website to disable
SRV:
perform sqlite3 operation to disable

UX: 
User accesses website to check status of adlist
SRV:
perform sqlite3 operation to return "enable" status (could also return datestamp)

TODO:
perform gravity update using /etc/.pihole/gravity.sh
add correct http responses and additional output perhaps?
"""
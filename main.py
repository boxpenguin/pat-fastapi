# main.py
from fastapi import FastAPI
from gravitydatabase import GravityDatabase

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/update")
def update_url():
    test = GravityDatabase(comment="scheduled")
    output = test.update()
    return {"message": output}

@app.get("/enable")
async def enable_url():
    test = GravityDatabase(comment="scheduled")
    return {"message": test.toggle(is_enabled=True)}
    # add proper documentation and status codes from 

@app.get("/disable")
async def disable_url():
    test = GravityDatabase(comment="scheduled")
    return {"message": test.toggle(is_enabled=False)}

@app.get("/status")
async def status():
    test = GravityDatabase(comment="scheduled")
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
from fastapi import APIRouter
from import_asyncio import PiholeGravity

app_stdout_router = APIRouter()

# create an instance of the PiholeGravity class
pihole_gravity = PiholeGravity()

@app_stdout_router.get("/run-gravity-script")
async def run_gravity_script():
    return await pihole_gravity.run_gravity_script()
import asyncio
import sys
import os

class PiholeGravity:
    async def read_subprocess_output(self, cmd):
        # create a subprocess
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )

        # read output
        while True:
            output = await process.stdout.readline()
            if output == b'' and process.poll() is not None:
                break
            if output:
                print(output.strip().decode())

        # close subprocess
        await process.communicate()
        return process.returncode

    async def run_gravity_script(self):
        # execute gravity.sh command
        command = ['/etc/.pihole/gravity.sh']
        return await self.read_subprocess_output(command)
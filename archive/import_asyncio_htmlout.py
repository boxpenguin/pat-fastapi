import asyncio
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi import APIRouter

stdout_router = APIRouter()

class AsyncSubprocessReader:
    def __init__(self, cmd):
        self.cmd = cmd
        self.process = None

    async def read_subprocess_output(self):
        self.process = await asyncio.create_subprocess_shell(
            self.cmd, stdout=asyncio.subprocess.PIPE
        )
        while True:
            line = await self.process.stdout.readline()
            if line:
                yield line.decode().strip()
            else:
                break

    async def stop_subprocess(self):
        self.process.terminate()
        await self.process.communicate()

@stdout_router.get("/")
async def index():
    return HTMLResponse("""
        <html>
            <body>
                <h1>Subprocess output:</h1>
                <pre id="output"></pre>
                <script>
                    async function fetchOutput() {
                        const response = await fetch('/output');
                        const reader = response.body.getReader();
                        const decoder = new TextDecoder('utf-8');
                        let output = '';
                        while (true) {
                            const {done, value} = await reader.read();
                            if (done) break;
                            output += decoder.decode(value);
                            document.getElementById('output').textContent = output;
                        }
                    }
                    fetchOutput();
                </script>
            </body>
        </html>
    """)

@stdout_router.get("/output", response_class=PlainTextResponse)
async def output():
    reader = AsyncSubprocessReader("/etc/.pihole/gravity.sh")
    async for line in reader.read_subprocess_output():
        yield line + "\n"
    await reader.stop_subprocess()

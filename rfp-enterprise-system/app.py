
from fastapi import FastAPI, UploadFile
from core.orchestrator import Orchestrator

app = FastAPI()
orch = Orchestrator()

@app.post("/rfp")
async def rfp(file: UploadFile):
    return await orch.run(file)

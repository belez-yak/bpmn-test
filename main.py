from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
DIAGRAM_PATH = BASE_DIR / "diagrams" / "sample.bpmn"

app = FastAPI()

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def read_index():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/diagram")
def get_diagram():
    return FileResponse(DIAGRAM_PATH, media_type="application/xml")

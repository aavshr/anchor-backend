from deta import Deta
from fastapi import FastAPI 
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
deta = Deta()
db = deta.Base("anchor")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"]
)

class Anchor(BaseModel):
    anchor_id: str
    html: str

@app.get("/")
def index():
    return "ok"

@app.get("/v1/anchors/{anchor_id}")
def get_anchor(anchor_id: str):
    item = db.get(anchor_id)
    return item["html"]

@app.post("/v1/anchors", status_code=201)
def post_anchor(anchor: Anchor):
    db.put({
        "key": anchor.anchor_id,
        "html": anchor.html
    })
    return "created" 
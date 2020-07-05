from deta import Deta
from flask import Flask, request 
from flask_cors import CORS

app = Flask(__name__) 
cors = CORS(app)

@app.route("/")
def index():
    return "ok"

@app.route("/v1/anchors/<anchor_id>", methods = ["GET"])
def get_anchor(anchor_id: str):
    deta = Deta()
    db = deta.Base("anchor")
    item = db.get(anchor_id)
    if (not item):
        return "not found", 404
    return item["html"]

@app.route("/v1/anchors", methods = ["POST"])
def post_anchor():
    deta = Deta()
    db = deta.Base("anchor")
    db.put({
        "key": request.json["anchor_id"],
        "html": request.json["html"] 
    })
    return "created", 201 
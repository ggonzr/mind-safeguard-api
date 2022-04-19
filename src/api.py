"""
App's entrypoint
"""
from fastapi import FastAPI
from src.schema.prediction import Prediction

# App object
app = FastAPI(
    title="DASS model deployment",
    version=1.0
)


# Views
@app.get("/")
async def index():
    return {"msg": "Hello world"}


@app.post("/")
async def prediction(pred: Prediction):
    return pred
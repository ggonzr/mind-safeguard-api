"""
App's entrypoint
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.schema.prediction import Prediction
from src.model.model import predict

# App object
app = FastAPI(
    title="DASS model deployment",
    version=1.0
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Views
@app.get("/")
async def index():
    return {"msg": "Hello world"}


@app.post("/")
async def prediction(pred: Prediction):
    return predict(pred.to_dataframe())

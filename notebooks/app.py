from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from inference import run_pipeline, run_pipeline_batch

app = FastAPI(title="Comment Sentiment API")


class CommentRequest(BaseModel):
    text: str


class BatchCommentRequest(BaseModel):
    texts: List[str]


@app.get("/")
def root():
    return {"status": "ok"}


@app.post("/predict")
def predict(payload: CommentRequest):
    return run_pipeline(payload.text)


@app.post("/predict/batch")
def predict_batch(payload: BatchCommentRequest):
    return run_pipeline_batch(payload.texts)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import base64
import joblib
import pandas as pd

from pydantic import BaseModel
from typing import Dict, List
from fastapi import FastAPI, Request, HTTPException, Depends
from datetime import datetime

from app.get_image import get_image
from app.predict import predict

core = joblib.load("/opt/ml/model.joblib")

class Payload(BaseModel):
    url : str
    id_foragido : str

@app.get("/health")
def root(req: Request):
    """
    Retorna status de saude da API
    """
    return {"status": "ok"}

@app.post("/predict")
async def predict(payload: Payload):
    """

    """
    try:
        prediction = predict(payload, core)
        return prediction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


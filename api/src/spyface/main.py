#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import base64
import joblib
import pandas as pd
import cv2
import os
import numpy as np
from statistics import mean

from pydantic import BaseModel
from typing import Dict, List
from fastapi import FastAPI, Request, HTTPException, Depends
from datetime import datetime

from spyface.Reconhecer import reconhecedor_eigen

from fastapi import FastAPI, File, Form

app = FastAPI()

class Payload(BaseModel):
    id : str
    documento_id : str

@app.get("/health")
def root(req: Request):
    """
    Retorna status de saude da API
    """
    return {"status": "ok"}

@app.post("/predict")
async def predict(file: bytes = File(...), id: str = Form(...)):
    """
    Retorna o score relativo a detecção da face
    """
    try:
        prediction = reconhecedor_eigen(file)
        return prediction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


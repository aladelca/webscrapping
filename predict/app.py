import os
from fastapi import FastAPI
from pydantic import BaseModel


from main_predict import main_predict


app = FastAPI()

class Text(BaseModel):
    text: str

@app.post("/predict/")
async def predict(input: Text):
    print(input)
    prediction = main_predict(input.text)
    return {'prediction': str(prediction)}

import uvicorn
uvicorn.run(app, host="0.0.0.0", port=8000)
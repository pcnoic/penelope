"""
Peneloge - Batch Translation Engine
License: MIT
"""
import fastapi as fa
from apimodels import data

# Controllers
app = fa.FastAPI()


# Endpoints
# All endpoints are unprotected. Please use a proxy if you want to add authentication.

@app.post("/translate", status_code=200)
async def translate(input_data: data.Data, response: fa.Response):
    print("hello", data)

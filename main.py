from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for now)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/data")
def get_data():
    url = "https://docs.google.com/spreadsheets/d/17B4IEGfyIwoWGwEsdadqFzwXvn5LNW5-8E8ZeGvZKrE/gviz/tq?tqx=out:json"
    res = requests.get(url)
    data = json.loads(res.text[47:-2])
    
    rows = data['table']['rows']
    result = []

    for row in rows:
        cols = row['c']
        
        result.append({
            "symbol": cols[5]['v'],
            "cmp": cols[6]['v'],
            "shares": cols[7]['v'],
            "dividend_per_share": cols[8]['v'],
            "expected_dividend": cols[7]['v'] * cols[8]['v']
        })

    return result
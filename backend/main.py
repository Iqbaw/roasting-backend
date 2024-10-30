from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/roast/")
def get_social_data(username: str):
    return {"username": username, "roast": "Kamu eksis banget disini, padahal real-life nya nolep wkwk."}

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],    
)
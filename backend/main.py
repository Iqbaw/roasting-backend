from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://roasting-frontend-l8me41vhp-iqbalalbatmis-projects.vercel.app"],  # Pastikan domain sesuai dengan URL frontend kamu
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/roast")
@app.get("/roast/")
def get_social_data(username: str):
    return {"username": username, "roast": "Kamu terlalu eksis di sini, padahal IRL sepi banget."}

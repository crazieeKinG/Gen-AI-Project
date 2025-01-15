from app.feature.app_user_guide import main as app_user_guide

from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


# Bind the router for each feature
app.include_router(app_user_guide.router)


@app.get("/")
def root():
    return {"message": "Successfully connected to the server"}

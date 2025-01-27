from app.feature.app_user_guide import main as app_user_guide
from app.feature.language_translation import main as language_translate

from fastapi import FastAPI

app = FastAPI()


# Bind the router for each feature
app.include_router(app_user_guide.router)
app.include_router(language_translate.router)


@app.get("/")
def root():
    return {"message": "Successfully connected to the server"}

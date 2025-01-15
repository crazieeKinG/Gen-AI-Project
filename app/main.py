from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Successfully connected to the server"}

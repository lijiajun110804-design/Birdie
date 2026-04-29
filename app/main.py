from fastapi import FastAPI

app = FastAPI(title="Birdie Backend API")

@app.get("/health")
def Health_Check():
    return{"status": "ok"}
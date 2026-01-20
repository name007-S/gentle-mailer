from fastapi import FastAPI

app = FastAPI(title="Gentle Mailer")

@app.get("/health")
def health_check():
    return {"status": "ok"}

from fastapi import FastAPI

app = FastAPI(title="Secure AI Document Assistant")

@app.get("/health")
def health_check():
    return {"status": "ok"}

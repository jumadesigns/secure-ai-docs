from fastapi import FastAPI

app = FastAPI(title="Secure AI Document Assistant")

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/")
def root():
    # Simple root endpoint that mirrors the health check for convenience
    return {"status": "ok"}

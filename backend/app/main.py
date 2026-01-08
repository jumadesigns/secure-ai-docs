from fastapi import FastAPI
from backend.app.audit.logger import log_event

app = FastAPI(title="Secure AI Document Assistant", 
              description="Backend API for regulated AI document workflows")

@app.get("/health")
def health_check():
    log_event(
        action="health_check",
        actor="system",
        resource="health_endpoint",
        metadata={"status": "ok"}
    )
    return {"status": "ok"}


@app.get("/")
def root():
    # Simple root endpoint that mirrors the health check for convenience
    return {"status": "ok"}

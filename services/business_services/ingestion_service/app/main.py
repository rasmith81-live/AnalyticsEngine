from fastapi import FastAPI

app = FastAPI(title="Ingestion Service", version="0.1.0")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "ingestion_service"}

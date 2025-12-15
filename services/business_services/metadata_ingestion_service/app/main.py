from fastapi import FastAPI

app = FastAPI(title="Metadata Ingestion Service", version="0.1.0")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "metadata_ingestion_service"}

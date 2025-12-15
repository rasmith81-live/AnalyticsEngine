from fastapi import FastAPI

app = FastAPI(title="Connector Service", version="0.1.0")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "connector_service"}

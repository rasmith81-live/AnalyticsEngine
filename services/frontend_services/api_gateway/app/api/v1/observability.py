from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
import httpx

from ...clients.messaging import MessagingClient
from ..dependencies import get_messaging_client

router = APIRouter()

OBSERVABILITY_SERVICE_URL = "http://observability_service:8000"


@router.get("/health/{service}/history")
async def get_service_health_history(service: str, limit: int = 50):
    """Proxy health history requests to observability service."""
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            response = await client.get(
                f"{OBSERVABILITY_SERVICE_URL}/health/services/{service}/history",
                params={"limit": limit}
            )
            return response.json()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


@router.get("/stats/realtime")
async def get_realtime_stats():
    """Proxy real-time stats requests to observability service."""
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            response = await client.get(f"{OBSERVABILITY_SERVICE_URL}/stats/realtime")
            return response.json()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


@router.get("/stats/traffic")
async def get_service_traffic():
    """Proxy service traffic data requests to observability service."""
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:
            response = await client.get(f"{OBSERVABILITY_SERVICE_URL}/stats/traffic")
            return response.json()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

@router.post("/telemetry")
async def send_telemetry(
    request: Request,
    messaging_client: MessagingClient = Depends(get_messaging_client),
):
    body = await request.json()
    correlation_id = await messaging_client.send_command(
        "commands.observability", "ingest_telemetry", body
    )
    return JSONResponse(
        status_code=202,
        content={
            "status": "accepted",
            "correlation_id": correlation_id,
            "message": "Telemetry data accepted",
        },
    )

@router.get("/logs")
async def get_logs(
    request: Request,
    messaging_client: MessagingClient = Depends(get_messaging_client),
):
    query_params = dict(request.query_params)
    response = await messaging_client.send_query(
        "queries.observability", "get_logs", query_params
    )
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return JSONResponse(content=response["data"])

@router.get("/metrics")
async def get_metrics(
    request: Request,
    messaging_client: MessagingClient = Depends(get_messaging_client),
):
    query_params = dict(request.query_params)
    response = await messaging_client.send_query(
        "queries.observability", "get_metrics", query_params
    )
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return JSONResponse(content=response["data"])

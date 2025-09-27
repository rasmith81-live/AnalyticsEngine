from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import JSONResponse

from ...clients.messaging import MessagingClient
from ..dependencies import get_messaging_client

router = APIRouter()

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

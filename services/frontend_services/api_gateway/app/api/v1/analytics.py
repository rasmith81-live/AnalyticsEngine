from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import JSONResponse

from ...clients.messaging import MessagingClient
from ..dependencies import get_messaging_client

router = APIRouter()

@router.post("/messages")
async def analyze_messages(
    request: Request,
    messaging_client: MessagingClient = Depends(get_messaging_client),
):
    body = await request.json()
    correlation_id = await messaging_client.send_command(
        "commands.business_service_b", "analyze_messages", body
    )
    return JSONResponse(
        status_code=202,
        content={
            "status": "accepted",
            "correlation_id": correlation_id,
            "message": "Analytics request accepted",
        },
    )

@router.get("/reports")
async def get_analytics_reports(
    request: Request,
    messaging_client: MessagingClient = Depends(get_messaging_client),
):
    query_params = dict(request.query_params)
    response = await messaging_client.send_query(
        "queries.business_service_b", "get_reports", query_params
    )
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return JSONResponse(content=response["data"])

@router.get("/dashboard")
async def get_analytics_dashboard(
    request: Request,
    messaging_client: MessagingClient = Depends(get_messaging_client),
):
    query_params = dict(request.query_params)
    response = await messaging_client.send_query(
        "queries.business_service_b", "get_dashboard", query_params
    )
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return JSONResponse(content=response["data"])

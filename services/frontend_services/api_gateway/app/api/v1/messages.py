from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import JSONResponse

from ...clients.messaging import MessagingClient
from ..dependencies import get_messaging_client

router = APIRouter()

@router.post("/")
async def create_message(
    request: Request,
    messaging_client: MessagingClient = Depends(get_messaging_client),
):
    body = await request.json()
    correlation_id = await messaging_client.send_command(
        "commands.business_service_a", "create_message", body
    )
    return JSONResponse(
        status_code=202,
        content={
            "status": "accepted",
            "correlation_id": correlation_id,
            "message": "Message creation request accepted",
        },
    )

@router.get("/{message_id}")
async def get_message(
    message_id: str,
    messaging_client: MessagingClient = Depends(get_messaging_client),
):
    response = await messaging_client.send_query(
        "queries.business_service_a", "get_message", {"message_id": message_id}
    )
    if "error" in response:
        raise HTTPException(status_code=404, detail=response["error"])
    return JSONResponse(content=response["data"])

@router.get("/")
async def list_messages(
    request: Request,
    messaging_client: MessagingClient = Depends(get_messaging_client),
):
    query_params = dict(request.query_params)
    response = await messaging_client.send_query(
        "queries.business_service_a", "list_messages", query_params
    )
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return JSONResponse(content=response["data"])

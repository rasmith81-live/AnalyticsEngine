from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import JSONResponse

from ...clients.messaging import MessagingClient
from ..dependencies import get_messaging_client

router = APIRouter()

@router.post("/data")
async def archive_data(
    request: Request,
    messaging_client: MessagingClient = Depends(get_messaging_client),
):
    body = await request.json()
    correlation_id = await messaging_client.send_command(
        "commands.archive", "archive_data", body
    )
    return JSONResponse(
        status_code=202,
        content={
            "status": "accepted",
            "correlation_id": correlation_id,
            "message": "Archive request accepted",
        },
    )

@router.get("/messages")
async def get_archived_messages(
    request: Request,
    messaging_client: MessagingClient = Depends(get_messaging_client),
):
    query_params = dict(request.query_params)
    response = await messaging_client.send_query(
        "queries.archive", "get_archived_messages", query_params
    )
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return JSONResponse(content=response["data"])

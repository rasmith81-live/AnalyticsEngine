from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import JSONResponse

from ...clients.messaging import MessagingClient
from ..dependencies import get_messaging_client

router = APIRouter()

@router.post("/query")
async def execute_database_query(
    request: Request,
    messaging_client: MessagingClient = Depends(get_messaging_client),
):
    body = await request.json()
    response = await messaging_client.send_query(
        "queries.database", "execute_query", body
    )
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return JSONResponse(content=response["data"])

@router.post("/timeseries")
async def query_timeseries_data(
    request: Request,
    messaging_client: MessagingClient = Depends(get_messaging_client),
):
    body = await request.json()
    response = await messaging_client.send_query(
        "queries.database.timeseries", "timeseries_query", body
    )
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return JSONResponse(content=response["data"])

from fastapi import APIRouter, Request, Depends, HTTPException
from fastapi.responses import JSONResponse

from ...clients.messaging import MessagingClient
from ..dependencies import get_messaging_client

router = APIRouter()

@router.post("/publish")
async def publish_message(
    request: Request,
    messaging_client: MessagingClient = Depends(get_messaging_client),
):
    body = await request.json()
    channel = body.get("channel")
    message = body.get("message")
    if not channel or not message:
        raise HTTPException(status_code=400, detail="Channel and message are required")
    
    await messaging_client.publish(channel, message)
    return JSONResponse(status_code=202, content={"status": "published"})

@router.post("/subscribe")
async def subscribe_to_channel(
    request: Request,
    messaging_client: MessagingClient = Depends(get_messaging_client),
):
    # Note: This is a simplified example. Real-world subscription management
    # would require a more robust mechanism like WebSockets or webhooks.
    body = await request.json()
    channel = body.get("channel")
    if not channel:
        raise HTTPException(status_code=400, detail="Channel is required")
    
    # This is a placeholder for subscription logic.
    # In a real application, you would register a persistent handler.
    return JSONResponse(status_code=200, content={"status": f"subscription to {channel} noted"})

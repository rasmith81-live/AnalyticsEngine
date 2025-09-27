from fastapi import Depends

from ..clients import MessagingClient

def get_messaging_client() -> MessagingClient:
    return MessagingClient()

import logging
from functools import lru_cache
from typing import Optional

from .config import get_settings
from .messaging_client import MessagingClient

logger = logging.getLogger(__name__)

@lru_cache()
def get_messaging_client() -> MessagingClient:
    """
    Returns a singleton instance of the MessagingClient.

    This function is cached using functools.lru_cache to ensure that only one
    instance of the MessagingClient is created and reused throughout the application.
    This is crucial for maintaining a persistent connection to the messaging service
    and for managing event handlers efficiently.

    Returns:
        MessagingClient: The singleton messaging client instance.
    """
    logger.info("Initializing MessagingClient singleton")
    settings = get_settings()
    return MessagingClient(
        base_url=settings.messaging_service_url,
        service_name=settings.service_name
    )

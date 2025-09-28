import logging
from typing import Dict, Any

from .messaging_client import MessagingClient

logger = logging.getLogger(__name__)

class SessionManager:
    def __init__(self, messaging_client: MessagingClient):
        self.messaging_client = messaging_client
        self.current_session = "CLOSED"

    async def start(self):
        """Subscribe to the trading session topic."""
        await self.messaging_client.subscribe(
            topic="TradingSessionChanged",
            callback=self.handle_session_change
        )
        logger.info("Subscribed to 'TradingSessionChanged' topic.")

    async def stop(self):
        """Unsubscribe from the trading session topic."""
        await self.messaging_client.unsubscribe("TradingSessionChanged")
        logger.info("Unsubscribed from 'TradingSessionChanged' topic.")

    async def handle_session_change(self, session_data: Dict[str, Any]):
        """Handle a trading session change message."""
        try:
            new_session = session_data.get('session')
            if not new_session:
                logger.warning("Received a session change message without a session.")
                return

            logger.info(f"Trading session changed to: {new_session}")
            self.current_session = new_session

        except Exception as e:
            logger.error(f"Failed to handle session change: {e}")

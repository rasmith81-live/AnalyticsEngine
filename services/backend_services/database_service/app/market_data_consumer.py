import logging
from datetime import datetime
from typing import Dict, Any

from .messaging_client import MessagingClient
from .database_manager import DatabaseManager
from .base_models import MarketData

logger = logging.getLogger(__name__)

class MarketDataConsumer:
    def __init__(self, messaging_client: MessagingClient, database_manager: DatabaseManager):
        self.messaging_client = messaging_client
        self.database_manager = database_manager

    async def start(self):
        """Subscribe to the market data topic."""
        await self.messaging_client.subscribe(
            topic="market.data.stream",
            callback=self.handle_market_data
        )
        logger.info("Subscribed to 'market.data.stream' topic.")

    async def stop(self):
        """Unsubscribe from the market data topic."""
        await self.messaging_client.unsubscribe("market.data.stream")
        logger.info("Unsubscribed from 'market.data.stream' topic.")

    async def handle_market_data(self, market_data: Dict[str, Any]):
        """Handle an incoming market data message."""
        try:
            if not market_data:
                logger.warning("Received an empty market data message.")
                return

            # Convert timestamp string to datetime object if necessary
            if isinstance(market_data.get('timestamp'), str):
                market_data['timestamp'] = datetime.fromisoformat(market_data['timestamp'])

            async with self.database_manager.get_session() as session:
                db_market_data = MarketData(**market_data)
                session.add(db_market_data)
                await session.commit()
                logger.info(f"Market data for {market_data.get('symbol')} saved to database.")

        except Exception as e:
            logger.error(f"Failed to handle market data message: {e}")

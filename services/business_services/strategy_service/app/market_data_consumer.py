import logging
from typing import Dict, Any

from .messaging_client import MessagingClient
from .asset_profiler import AssetProfiler

logger = logging.getLogger(__name__)

class MarketDataConsumer:
    def __init__(self, messaging_client: MessagingClient, asset_profiler: AssetProfiler):
        self.messaging_client = messaging_client
        self.asset_profiler = asset_profiler

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

            await self.asset_profiler.process_market_data(market_data)

        except Exception as e:
            logger.error(f"Failed to handle market data message: {e}")

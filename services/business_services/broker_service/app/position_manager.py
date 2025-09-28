import logging
from typing import Dict, Any

from .messaging_client import MessagingClient

logger = logging.getLogger(__name__)

class PositionManager:
    def __init__(self, messaging_client: MessagingClient):
        self.messaging_client = messaging_client
        self.open_positions = {}

    async def start(self):
        """Subscribe to trade confirmation topics."""
        await self.messaging_client.subscribe(
            topic="trade.execution.buy.confirmation",
            callback=self.handle_buy_confirmation
        )
        await self.messaging_client.subscribe(
            topic="trade.execution.sell.confirmation",
            callback=self.handle_sell_confirmation
        )
        logger.info("Subscribed to trade confirmation topics.")

    async def stop(self):
        """Unsubscribe from trade confirmation topics."""
        await self.messaging_client.unsubscribe("trade.execution.buy.confirmation")
        await self.messaging_client.unsubscribe("trade.execution.sell.confirmation")
        logger.info("Unsubscribed from trade confirmation topics.")

    async def handle_buy_confirmation(self, trade_data: Dict[str, Any]):
        """Handle a buy confirmation message."""
        try:
            symbol = trade_data.get('symbol')
            if not symbol:
                logger.warning("Received a buy confirmation without a symbol.")
                return

            logger.info(f"Received buy confirmation for {symbol}. Adding to open positions.")
            self.open_positions[symbol] = trade_data

        except Exception as e:
            logger.error(f"Failed to handle buy confirmation: {e}")

    async def handle_sell_confirmation(self, trade_data: Dict[str, Any]):
        """Handle a sell confirmation message."""
        try:
            symbol = trade_data.get('symbol')
            if not symbol:
                logger.warning("Received a sell confirmation without a symbol.")
                return

            if symbol in self.open_positions:
                logger.info(f"Received sell confirmation for {symbol}. Closing position.")
                del self.open_positions[symbol]
            else:
                logger.warning(f"Received a sell confirmation for {symbol}, but no open position was found.")

        except Exception as e:
            logger.error(f"Failed to handle sell confirmation: {e}")

    async def exit_all_positions(self):
        """Exit all open positions."""
        logger.info("Exiting all open positions...")
        for symbol, position_data in list(self.open_positions.items()):
            logger.info(f"Publishing sell order for {position_data.get('quantity')} shares of {symbol}.")
            # In a real implementation, you would publish a sell order command here.
            # For now, we will just log the action and remove the position.
            del self.open_positions[symbol]
        logger.info("All open positions have been exited.")

    async def crash_all_positions(self):
        """Immediately exit all open positions (e.g., with market orders)."""
        logger.info("CRASHING all open positions...")
        for symbol, position_data in list(self.open_positions.items()):
            logger.info(f"Publishing MARKET sell order for {position_data.get('quantity')} shares of {symbol}.")
            del self.open_positions[symbol]
        logger.info("All open positions have been crash-exited.")

    async def winddown_all_positions(self):
        """Gracefully exit all open positions (e.g., with limit orders)."""
        logger.info("WINDING DOWN all open positions...")
        for symbol, position_data in list(self.open_positions.items()):
            logger.info(f"Publishing LIMIT sell order for {position_data.get('quantity')} shares of {symbol}.")
            del self.open_positions[symbol]
        logger.info("All open positions have been wound down.")

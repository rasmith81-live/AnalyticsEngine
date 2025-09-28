import logging
from typing import Dict, Any

from .messaging_client import MessagingClient
from .session_manager import SessionManager

logger = logging.getLogger(__name__)

class OrderManager:
    def __init__(self, messaging_client: MessagingClient, session_manager: SessionManager):
        self.messaging_client = messaging_client
        self.session_manager = session_manager

    async def handle_buy_order(self, order_data: Dict[str, Any]):
        """Handle a buy order command and publish a confirmation."""
        try:
            order_type = order_data.get('order_type', 'market')
            current_session = self.session_manager.current_session

            if order_type == 'market' and current_session != 'MARKET_OPEN':
                logger.warning(f"Market order for {order_data.get('symbol')} rejected: Market is not open.")
                return

            logger.info(f"Executing {order_type} buy order for {order_data.get('symbol')}.")
            # In a real implementation, you would interact with a brokerage API here.

            # Publish a confirmation event
            await self.messaging_client.publish_event(
                event_type="trade.execution.buy.confirmation",
                event_data=order_data
            )
            logger.info(f"Published buy confirmation for {order_data.get('symbol')}.")

        except Exception as e:
            logger.error(f"Failed to handle buy order: {e}")

    async def handle_sell_order(self, order_data: Dict[str, Any]):
        """Handle a sell order command and publish a confirmation."""
        try:
            order_type = order_data.get('order_type', 'market')
            current_session = self.session_manager.current_session

            if order_type == 'market' and current_session != 'MARKET_OPEN':
                logger.warning(f"Market order for {order_data.get('symbol')} rejected: Market is not open.")
                return

            logger.info(f"Executing {order_type} sell order for {order_data.get('symbol')}.")
            # In a real implementation, you would interact with a brokerage API here.

            # Publish a confirmation event
            await self.messaging_client.publish_event(
                event_type="trade.execution.sell.confirmation",
                event_data=order_data
            )
            logger.info(f"Published sell confirmation for {order_data.get('symbol')}.")

        except Exception as e:
            logger.error(f"Failed to handle sell order: {e}")

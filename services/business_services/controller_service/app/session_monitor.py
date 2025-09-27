import asyncio
from datetime import datetime, time
from enum import Enum
import pandas_market_calendars as mcal
import pytz
import logging

logger = logging.getLogger(__name__)

class TradingSession(str, Enum):
    """Enumeration for NYSE trading sessions."""
    PRE_PRE_MARKET = "Pre-PreMarket"
    PRE_MARKET = "Pre-Market"
    MARKET_OPEN = "Market-Open"
    POST_MARKET = "Post-Market"
    CLOSED = "Closed"

class SessionMonitor:
    """Monitors the current NYSE trading session."""

    def __init__(self):
        self.nyse_calendar = mcal.get_calendar('NYSE')
        self.est_tz = pytz.timezone('America/New_York')
        self._current_session = TradingSession.CLOSED
        self._running = False
        self._task = None

    def get_current_session_status(self) -> TradingSession:
        """Determines the current NYSE trading session."""
        now_est = datetime.now(self.est_tz)
        today_str = now_est.strftime('%Y-%m-%d')

        # Get market holidays
        holidays = self.nyse_calendar.holidays().holidays

        # Check if today is a holiday or a weekend
        if now_est.date() in holidays or now_est.weekday() >= 5: # 5=Saturday, 6=Sunday
            return TradingSession.CLOSED

        current_time = now_est.time()

        # Define session times
        pre_pre_market_start = time(4, 0)
        pre_market_start = time(7, 0)
        market_open_start = time(9, 30)
        market_close = time(16, 0)
        post_market_close = time(20, 0)

        if pre_pre_market_start <= current_time < pre_market_start:
            return TradingSession.PRE_PRE_MARKET
        elif pre_market_start <= current_time < market_open_start:
            return TradingSession.PRE_MARKET
        elif market_open_start <= current_time < market_close:
            return TradingSession.MARKET_OPEN
        elif market_close <= current_time < post_market_close:
            return TradingSession.POST_MARKET
        else:
            return TradingSession.CLOSED

    async def _monitor_loop(self):
        """Periodically updates the current session status."""
        while self._running:
            try:
                session = self.get_current_session_status()
                if session != self._current_session:
                    logger.info(f"Trading session changed to: {session.value}")
                    self._current_session = session
                await asyncio.sleep(60)  # Check every minute
            except Exception as e:
                logger.error(f"Error in session monitor loop: {e}", exc_info=True)
                await asyncio.sleep(300) # Wait longer on error

    async def start(self):
        """Start the session monitor background task."""
        if self._running:
            return
        self._running = True
        self._task = asyncio.create_task(self._monitor_loop())
        logger.info("SessionMonitor started.")

    async def stop(self):
        """Stop the session monitor background task."""
        if not self._running:
            return
        self._running = False
        if self._task:
            self._task.cancel()
            try:
                await self._task
            except asyncio.CancelledError:
                pass
        logger.info("SessionMonitor stopped.")

    @property
    def current_session(self) -> TradingSession:
        return self._current_session

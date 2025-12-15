"""
Subscriber Manager for Database Service Stream Publisher
Tracks active subscribers for KPI streams and manages subscription lifecycle
"""
import asyncio
import logging
from typing import Dict, Set, Tuple, Optional
from datetime import datetime
from dataclasses import dataclass, field
from collections import defaultdict

logger = logging.getLogger(__name__)


@dataclass
class Subscription:
    """Represents a single subscription to a KPI stream"""
    subscriber_id: str
    kpi_code: str
    entity_id: str
    period: str  # 'minute', 'hour', 'day'
    created_at: datetime = field(default_factory=datetime.utcnow)
    last_activity: datetime = field(default_factory=datetime.utcnow)
    
    @property
    def stream_key(self) -> str:
        """Generate unique key for this stream"""
        return f"{self.kpi_code}:{self.entity_id}:{self.period}"


class SubscriberManager:
    """
    Manages subscribers for KPI streams
    
    Responsibilities:
    - Track active subscriptions per KPI/entity/period
    - Count subscribers for each stream
    - Notify when first subscriber joins (start publishing)
    - Notify when last subscriber leaves (stop publishing)
    - Handle subscriber timeouts/disconnections
    """
    
    def __init__(self, timeout_seconds: int = 300):
        """
        Initialize subscriber manager
        
        Args:
            timeout_seconds: Time after which inactive subscribers are removed
        """
        self.timeout_seconds = timeout_seconds
        
        # Map: stream_key -> Set[subscriber_id]
        self._subscriptions: Dict[str, Set[str]] = defaultdict(set)
        
        # Map: subscriber_id -> Set[stream_key]
        self._subscriber_streams: Dict[str, Set[str]] = defaultdict(set)
        
        # Map: stream_key -> Subscription details
        self._stream_details: Dict[str, Tuple[str, str, str]] = {}
        
        # Map: subscriber_id -> last_activity
        self._last_activity: Dict[str, datetime] = {}
        
        # Lock for thread-safe operations
        self._lock = asyncio.Lock()
        
        logger.info(f"SubscriberManager initialized with {timeout_seconds}s timeout")
    
    async def add_subscriber(
        self,
        subscriber_id: str,
        kpi_code: str,
        entity_id: str,
        period: str
    ) -> bool:
        """
        Add a subscriber to a KPI stream
        
        Args:
            subscriber_id: Unique identifier for the subscriber
            kpi_code: KPI code to subscribe to
            entity_id: Entity ID for the KPI
            period: Time period ('minute', 'hour', 'day')
            
        Returns:
            True if this is the first subscriber (should start publishing)
            False if stream already has subscribers
        """
        async with self._lock:
            subscription = Subscription(
                subscriber_id=subscriber_id,
                kpi_code=kpi_code,
                entity_id=entity_id,
                period=period
            )
            
            stream_key = subscription.stream_key
            
            # Check if this is the first subscriber
            is_first_subscriber = len(self._subscriptions[stream_key]) == 0
            
            # Add subscription
            self._subscriptions[stream_key].add(subscriber_id)
            self._subscriber_streams[subscriber_id].add(stream_key)
            self._stream_details[stream_key] = (kpi_code, entity_id, period)
            self._last_activity[subscriber_id] = datetime.utcnow()
            
            logger.info(
                f"Added subscriber {subscriber_id} to stream {stream_key}. "
                f"Total subscribers: {len(self._subscriptions[stream_key])}"
            )
            
            return is_first_subscriber
    
    async def remove_subscriber(
        self,
        subscriber_id: str,
        kpi_code: Optional[str] = None,
        entity_id: Optional[str] = None,
        period: Optional[str] = None
    ) -> Set[str]:
        """
        Remove a subscriber from one or all streams
        
        Args:
            subscriber_id: Unique identifier for the subscriber
            kpi_code: Optional - specific KPI to unsubscribe from
            entity_id: Optional - specific entity to unsubscribe from
            period: Optional - specific period to unsubscribe from
            
        Returns:
            Set of stream keys that now have zero subscribers (should stop publishing)
        """
        async with self._lock:
            return await self._remove_subscriber_internal(subscriber_id, kpi_code, entity_id, period)

    async def _remove_subscriber_internal(
        self,
        subscriber_id: str,
        kpi_code: Optional[str] = None,
        entity_id: Optional[str] = None,
        period: Optional[str] = None
    ) -> Set[str]:
        """
        Internal method to remove subscriber (expects lock to be held)
        """
        streams_to_stop = set()
        
        if kpi_code and entity_id and period:
            # Remove from specific stream
            stream_key = f"{kpi_code}:{entity_id}:{period}"
            streams_to_stop = await self._remove_from_stream(subscriber_id, stream_key)
        else:
            # Remove from all streams
            if subscriber_id in self._subscriber_streams:
                stream_keys = self._subscriber_streams[subscriber_id].copy()
                for stream_key in stream_keys:
                    stopped = await self._remove_from_stream(subscriber_id, stream_key)
                    streams_to_stop.update(stopped)
        
        # Clean up subscriber tracking
        if subscriber_id in self._last_activity:
            del self._last_activity[subscriber_id]
        
        if subscriber_id in self._subscriber_streams and not self._subscriber_streams[subscriber_id]:
            del self._subscriber_streams[subscriber_id]
        
        logger.info(
            f"Removed subscriber {subscriber_id}. "
            f"Streams to stop: {len(streams_to_stop)}"
        )
        
        return streams_to_stop
    
    async def _remove_from_stream(self, subscriber_id: str, stream_key: str) -> Set[str]:
        """
        Internal method to remove subscriber from a specific stream
        
        Returns:
            Set containing stream_key if it now has zero subscribers, empty set otherwise
        """
        streams_to_stop = set()
        
        if stream_key in self._subscriptions:
            self._subscriptions[stream_key].discard(subscriber_id)
            
            # If no more subscribers, mark for stopping
            if len(self._subscriptions[stream_key]) == 0:
                streams_to_stop.add(stream_key)
                del self._subscriptions[stream_key]
                if stream_key in self._stream_details:
                    del self._stream_details[stream_key]
        
        if subscriber_id in self._subscriber_streams:
            self._subscriber_streams[subscriber_id].discard(stream_key)
        
        return streams_to_stop
    
    async def update_activity(self, subscriber_id: str) -> None:
        """
        Update last activity timestamp for a subscriber
        
        Args:
            subscriber_id: Unique identifier for the subscriber
        """
        async with self._lock:
            self._last_activity[subscriber_id] = datetime.utcnow()
    
    async def get_subscriber_count(self, kpi_code: str, entity_id: str, period: str) -> int:
        """
        Get number of active subscribers for a stream
        
        Args:
            kpi_code: KPI code
            entity_id: Entity ID
            period: Time period
            
        Returns:
            Number of active subscribers
        """
        stream_key = f"{kpi_code}:{entity_id}:{period}"
        async with self._lock:
            return len(self._subscriptions.get(stream_key, set()))
    
    async def get_active_streams(self) -> Dict[str, int]:
        """
        Get all active streams and their subscriber counts
        
        Returns:
            Dict mapping stream_key to subscriber count
        """
        async with self._lock:
            return {
                stream_key: len(subscribers)
                for stream_key, subscribers in self._subscriptions.items()
            }
    
    async def get_stream_details(self, stream_key: str) -> Optional[Tuple[str, str, str]]:
        """
        Get details for a stream
        
        Args:
            stream_key: Stream key
            
        Returns:
            Tuple of (kpi_code, entity_id, period) or None if not found
        """
        async with self._lock:
            return self._stream_details.get(stream_key)
    
    async def cleanup_inactive_subscribers(self) -> Set[str]:
        """
        Remove subscribers that have been inactive for too long
        
        Returns:
            Set of stream keys that now have zero subscribers
        """
        async with self._lock:
            now = datetime.utcnow()
            inactive_subscribers = []
            
            for subscriber_id, last_activity in self._last_activity.items():
                if (now - last_activity).total_seconds() > self.timeout_seconds:
                    inactive_subscribers.append(subscriber_id)
            
            streams_to_stop = set()
            for subscriber_id in inactive_subscribers:
                logger.warning(f"Removing inactive subscriber: {subscriber_id}")
                stopped = await self._remove_subscriber_internal(subscriber_id)
                streams_to_stop.update(stopped)
            
            if inactive_subscribers:
                logger.info(f"Cleaned up {len(inactive_subscribers)} inactive subscribers")
            
            return streams_to_stop
    
    async def get_stats(self) -> Dict:
        """
        Get statistics about current subscriptions
        
        Returns:
            Dict with subscription statistics
        """
        async with self._lock:
            return {
                "total_streams": len(self._subscriptions),
                "total_subscribers": len(self._subscriber_streams),
                "total_subscriptions": sum(len(subs) for subs in self._subscriptions.values()),
                "streams": {
                    stream_key: {
                        "subscriber_count": len(subscribers),
                        "kpi_code": self._stream_details[stream_key][0],
                        "entity_id": self._stream_details[stream_key][1],
                        "period": self._stream_details[stream_key][2]
                    }
                    for stream_key, subscribers in self._subscriptions.items()
                }
            }

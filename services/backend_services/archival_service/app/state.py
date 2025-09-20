"""
Global state for the archival service.

This module holds shared data structures, such as in-memory dictionaries, to be accessed
by different parts of the application without causing circular imports.
"""

from typing import Dict, Any, Optional
from .messaging_client import MessagingClient

# In-memory dictionary to track the status of archival events
archival_events: Dict[str, Dict[str, Any]] = {}

# Shared messaging client instance
messaging_client: Optional[MessagingClient] = None

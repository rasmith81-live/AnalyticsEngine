"""
Analytics Metadata Service Application Package
"""

from .main import app
from .config import get_settings
from .loader import get_loader

__all__ = ["app", "get_settings", "get_loader"]

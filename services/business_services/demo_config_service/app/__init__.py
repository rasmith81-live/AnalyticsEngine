"""
Demo/Config Service Application Package
"""

from .main import app
from .config import get_settings

__all__ = ["app", "get_settings"]

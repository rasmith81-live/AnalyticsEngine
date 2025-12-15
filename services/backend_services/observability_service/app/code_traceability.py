import os
import time
import logging
import inspect
import functools
import asyncio
from datetime import datetime
from typing import Dict, List, Set, Optional, Any

from .models import CodeUsageData, UnusedFilesResponse

logger = logging.getLogger(__name__)

class CodeTracer:
    """
    Tracks usage of code files, classes, and methods.
    """
    def __init__(self):
        # file_path -> last_usage_timestamp (float)
        self.file_usage: Dict[str, float] = {}
        # file_path -> Set[method_name]
        self.method_usage: Dict[str, Set[str]] = {}

    def track_usage(self, file_path: str, class_name: Optional[str], method_name: str):
        """Log usage of a code element."""
        now = time.time()
        # Normalize file path
        abs_path = os.path.abspath(file_path)
        self.file_usage[abs_path] = now
        
        if abs_path not in self.method_usage:
            self.method_usage[abs_path] = set()
        
        full_name = f"{class_name}.{method_name}" if class_name else method_name
        self.method_usage[abs_path].add(full_name)
        
        # Log it (as per requirement "Implement logging...")
        # Using debug level to avoid spamming production logs, but requirement says "Implement logging"
        logger.info(f"Code Usage: File={abs_path}, Method={full_name}")

    def get_unused_files(self, root_dir: str, period_seconds: int) -> UnusedFilesResponse:
        """
        Identify files not utilized in the given period.
        
        Args:
            root_dir: Root directory to scan for python files.
            period_seconds: Period in seconds. Files not used within (now - period) are considered unused.
        """
        cutoff_time = time.time() - period_seconds
        
        all_py_files = []
        # Walk directory to find all .py files
        if os.path.isdir(root_dir):
            for root, _, files in os.walk(root_dir):
                for file in files:
                    if file.endswith(".py"):
                        full_path = os.path.abspath(os.path.join(root, file))
                        all_py_files.append(full_path)
        else:
            logger.warning(f"Root directory for unused files scan not found: {root_dir}")
        
        unused_files = []
        for file_path in all_py_files:
            last_used = self.file_usage.get(file_path, 0)
            
            # If never used (0) or used before cutoff
            if last_used < cutoff_time:
                unused_files.append(file_path)
                
        return UnusedFilesResponse(
            total_files=len(all_py_files),
            unused_files_count=len(unused_files),
            unused_files=unused_files,
            period_seconds=period_seconds,
            timestamp=datetime.now()
        )

# Global tracer instance
tracer = CodeTracer()

def trace_execution(func):
    """
    Decorator to trace execution of functions/methods.
    """
    def _record_usage(f):
        try:
            file_path = inspect.getfile(f)
            method_name = f.__name__
            # Try to get class name
            class_name = None
            if hasattr(f, '__qualname__'):
                parts = f.__qualname__.split('.')
                if len(parts) > 1:
                    class_name = parts[-2]
            
            tracer.track_usage(file_path, class_name, method_name)
        except Exception as e:
            # Don't fail execution if tracing fails
            logger.debug(f"Failed to trace execution: {e}")

    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        _record_usage(func)
        return await func(*args, **kwargs)

    @functools.wraps(func)
    def sync_wrapper(*args, **kwargs):
        _record_usage(func)
        return func(*args, **kwargs)

    if asyncio.iscoroutinefunction(func):
        return async_wrapper
    else:
        return sync_wrapper

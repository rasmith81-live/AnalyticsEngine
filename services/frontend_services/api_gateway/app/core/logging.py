"""
Logging configuration for the API Gateway service.
Provides structured JSON logging with correlation IDs.
"""
import json
import logging
import sys
import uuid
from datetime import datetime
from typing import Any, Dict, Optional

from app.core.config import settings

class JsonFormatter(logging.Formatter):
    """
    Custom JSON formatter for structured logging.
    Formats log records as JSON objects with standardized fields.
    """
    
    def format(self, record: logging.LogRecord) -> str:
        """
        Format a log record as a JSON string.
        
        Args:
            record: Log record to format
            
        Returns:
            JSON formatted log string
        """
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
            "service": settings.SERVICE_NAME,
        }
        
        # Add correlation ID if available
        if hasattr(record, "correlation_id"):
            log_data["correlation_id"] = record.correlation_id
        
        # Add exception info if available
        if record.exc_info:
            log_data["exception"] = self.formatException(record.exc_info)
        
        # Add extra fields if available
        if hasattr(record, "data") and isinstance(record.data, dict):
            log_data.update(record.data)
        
        return json.dumps(log_data)

def setup_logging() -> None:
    """
    Configure logging for the application.
    Sets up handlers, formatters, and log levels.
    """
    # Get log level from settings
    log_level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)
    
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    
    # Remove existing handlers
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    
    # Create console handler with JSON formatter
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(JsonFormatter())
    root_logger.addHandler(console_handler)
    
    # Set log levels for third-party libraries
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)

class LoggerAdapter(logging.LoggerAdapter):
    """
    Logger adapter that adds correlation ID to log records.
    """
    
    def __init__(self, logger: logging.Logger, correlation_id: Optional[str] = None):
        """
        Initialize the logger adapter.
        
        Args:
            logger: Logger to adapt
            correlation_id: Optional correlation ID
        """
        super().__init__(logger, {})
        self.correlation_id = correlation_id or str(uuid.uuid4())
    
    def process(self, msg: str, kwargs: Dict[str, Any]) -> tuple:
        """
        Process the log record before logging.
        Adds correlation ID to the record.
        
        Args:
            msg: Log message
            kwargs: Additional logging arguments
            
        Returns:
            Processed message and kwargs
        """
        if "extra" not in kwargs:
            kwargs["extra"] = {}
        
        kwargs["extra"]["correlation_id"] = self.correlation_id
        
        return msg, kwargs

def get_logger(name: str, correlation_id: Optional[str] = None) -> LoggerAdapter:
    """
    Get a logger with the given name and correlation ID.
    
    Args:
        name: Logger name
        correlation_id: Optional correlation ID
        
    Returns:
        Logger adapter with correlation ID
    """
    logger = logging.getLogger(name)
    return LoggerAdapter(logger, correlation_id)

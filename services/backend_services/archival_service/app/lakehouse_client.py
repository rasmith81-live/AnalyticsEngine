"""
Lakehouse Client for Azure Data Lake Storage Gen2.

This module provides functionality to interact with Azure Data Lake Storage Gen2
for storing archived TimescaleDB data in a lakehouse format.
"""
import asyncio
import io
import json
import logging
import uuid
from typing import Dict, List, Any, Optional, Union

import pandas as pd
from azure.storage.filedatalake import DataLakeServiceClient
from azure.core.exceptions import AzureError

from .telemetry import trace_method, add_span_attributes, traced_span, inject_trace_context, extract_trace_context

logger = logging.getLogger(__name__)

class LakehouseClient:
    """Client for interacting with Azure Data Lake Storage Gen2."""
    
    def __init__(
        self,
        storage_account: str,
        container_name: str,
        connection_string: str
    ):
        """Initialize the lakehouse client.
        
        Args:
            storage_account: Azure Storage account name
            container_name: Container name for data lake storage
            connection_string: Azure Storage connection string
        """
        self.storage_account = storage_account
        self.container_name = container_name
        self.connection_string = connection_string
        self._service_client = None
        
    @trace_method(name="LakehouseClient._get_service_client", kind="CLIENT")
    async def _get_service_client(self):
        """Get or create the Data Lake service client.
        
        Returns:
            DataLakeServiceClient instance
        """
        # Add span attributes for Azure connection
        add_span_attributes({
            "storage.system": "azure_datalake",
            "storage.operation": "get_service_client",
            "storage.account": self.storage_account,
            "storage.container": self.container_name
        })
        
        if self._service_client is None:
            # Create the service client
            # Note: Azure SDK doesn't have async support for Data Lake Storage,
            # so we'll run this in a thread pool
            loop = asyncio.get_event_loop()
            self._service_client = await loop.run_in_executor(
                None,
                lambda: DataLakeServiceClient.from_connection_string(
                    self.connection_string
                )
            )
        
        return self._service_client
    
    @trace_method(name="LakehouseClient.test_connection", kind="CLIENT")
    async def test_connection(self) -> bool:
        """Test the connection to Azure Data Lake Storage.
        
        Returns:
            True if connection is successful, False otherwise
        """
        # Add span attributes for connection test
        add_span_attributes({
            "storage.system": "azure_datalake",
            "storage.operation": "test_connection",
            "storage.account": self.storage_account,
            "storage.container": self.container_name
        })
        
        try:
            service_client = await self._get_service_client()
            
            # Try to get the file system client (container)
            loop = asyncio.get_event_loop()
            await loop.run_in_executor(
                None,
                lambda: service_client.get_file_system_client(self.container_name)
            )
            
            # Set span status to success
            add_span_attributes({"storage.connection_status": "success"})
            return True
        except AzureError as e:
            # Set span status to error with details
            add_span_attributes({
                "storage.connection_status": "error",
                "error.type": e.__class__.__name__,
                "error.message": str(e)
            })
            logger.error(f"Azure Data Lake connection error: {e}", exc_info=True)
            return False
        except Exception as e:
            # Set span status to error with details
            add_span_attributes({
                "storage.connection_status": "error",
                "error.type": e.__class__.__name__,
                "error.message": str(e)
            })
            logger.error(f"Unexpected error testing connection: {e}", exc_info=True)
            return False
            
    def is_connected(self) -> bool:
        """Check if connected to Azure Data Lake Storage.
        
        Returns:
            True if service client exists, False otherwise.
            Note: This is a synchronous method that doesn't actually test the connection,
            it just checks if the client has been initialized.
        """
        return self._service_client is not None
    
    @trace_method(name="LakehouseClient.write_data", kind="CLIENT")
    async def write_data(
        self, 
        path: str, 
        data: Union[List[Dict[str, Any]], pd.DataFrame],
        format: str = "parquet",
        correlation_id: Optional[str] = None
    ) -> bool:
        """Write data to the data lake.
        
        Args:
            path: Path in the data lake where data will be stored
            data: Data to write, either as a list of dictionaries or a pandas DataFrame
            format: Format to store data in ('parquet', 'delta', 'json')
            correlation_id: Optional correlation ID for distributed tracing
            
        Returns:
            True if write was successful, False otherwise
        """
        # Generate operation ID for tracing
        operation_id = str(uuid.uuid4())
        correlation_id = correlation_id or str(uuid.uuid4())
        
        # Add span attributes for storage operation
        add_span_attributes({
            "storage.system": "azure_datalake",
            "storage.operation": "write_data",
            "storage.account": self.storage_account,
            "storage.container": self.container_name,
            "storage.path": path,
            "storage.format": format,
            "storage.operation_id": operation_id,
            "correlation_id": correlation_id,
            "data.size_rows": len(data) if hasattr(data, "__len__") else "unknown"
        })
        try:
            # Convert data to pandas DataFrame if it's a list
            if isinstance(data, list):
                df = pd.DataFrame(data)
            else:
                df = data
            
            # Get the file system client
            service_client = await self._get_service_client()
            loop = asyncio.get_event_loop()
            file_system_client = await loop.run_in_executor(
                None,
                lambda: service_client.get_file_system_client(self.container_name)
            )
            
            # Create directory structure if needed
            directory_path = "/".join(path.split("/")[:-1])
            if directory_path:
                await loop.run_in_executor(
                    None,
                    lambda: file_system_client.create_directory(directory_path, exist_ok=True)
                )
            
            # Create file client
            file_name = f"{path}.{format}"
            file_client = await loop.run_in_executor(
                None,
                lambda: file_system_client.get_file_client(file_name)
            )
            
            # Convert data to the appropriate format
            buffer = io.BytesIO()
            
            if format == "parquet":
                df.to_parquet(buffer, index=False)
            elif format == "json":
                df.to_json(buffer, orient="records", lines=True)
            else:
                raise ValueError(f"Unsupported format: {format}")
            
            # Reset buffer position
            buffer.seek(0)
            
            # Upload data
            await loop.run_in_executor(
                None,
                lambda: file_client.upload_data(buffer, overwrite=True)
            )
            
            logger.info(f"Successfully wrote data to {file_name}")
            return True
            
        except Exception as e:
            logger.error(f"Error writing data to {path}: {e}", exc_info=True)
            return False
    
    @trace_method(name="LakehouseClient.read_data", kind="CLIENT")
    async def read_data(
        self,
        path: str,
        format: str = "parquet",
        columns: Optional[List[str]] = None,
        correlation_id: Optional[str] = None
    ) -> Optional[pd.DataFrame]:
        """Read data from the data lake.
        
        Args:
            path: Path in the data lake where data is stored
            format: Format of the stored data ('parquet', 'delta', 'json')
            columns: Optional list of columns to read (for parquet only)
            correlation_id: Optional correlation ID for distributed tracing
            
        Returns:
            DataFrame with the data, or None if read failed
        """
        # Generate operation ID for tracing
        operation_id = str(uuid.uuid4())
        correlation_id = correlation_id or str(uuid.uuid4())
        
        # Add span attributes for storage operation
        add_span_attributes({
            "storage.system": "azure_datalake",
            "storage.operation": "read_data",
            "storage.account": self.storage_account,
            "storage.container": self.container_name,
            "storage.path": path,
            "storage.format": format,
            "storage.operation_id": operation_id,
            "correlation_id": correlation_id,
            "columns.requested": ",".join(columns) if columns else "all"
        })
        try:
            # Get the file system client
            service_client = await self._get_service_client()
            loop = asyncio.get_event_loop()
            file_system_client = await loop.run_in_executor(
                None,
                lambda: service_client.get_file_system_client(self.container_name)
            )
            
            # Create file client
            file_name = f"{path}.{format}"
            file_client = await loop.run_in_executor(
                None,
                lambda: file_system_client.get_file_client(file_name)
            )
            
            # Download data
            download = await loop.run_in_executor(
                None,
                lambda: file_client.download_file()
            )
            
            # Read the content
            buffer = io.BytesIO()
            await loop.run_in_executor(
                None,
                lambda: download.readinto(buffer)
            )
            
            # Reset buffer position
            buffer.seek(0)
            
            # Parse data based on format
            if format == "parquet":
                # Use column filtering if provided to reduce data transfer and compute costs
                if columns:
                    return pd.read_parquet(buffer, columns=columns)
                else:
                    return pd.read_parquet(buffer)
            elif format == "json":
                df = pd.read_json(buffer, lines=True)
                # Apply column filtering after reading for JSON
                if columns:
                    return df[columns]
                return df
            else:
                raise ValueError(f"Unsupported format: {format}")
                
        except Exception as e:
            logger.error(f"Error reading data from {path}: {e}", exc_info=True)
            return None
    
    @trace_method(name="LakehouseClient.path_exists", kind="CLIENT")
    async def path_exists(self, path: str, correlation_id: Optional[str] = None) -> bool:
        """Check if a path exists in the data lake.
        
        Args:
            path: Path to check for existence
            correlation_id: Optional correlation ID for distributed tracing
            
        Returns:
            True if the path exists, False otherwise
        """
        # Generate operation ID for tracing
        operation_id = str(uuid.uuid4())
        correlation_id = correlation_id or str(uuid.uuid4())
        
        # Add span attributes for storage operation
        add_span_attributes({
            "storage.system": "azure_datalake",
            "storage.operation": "path_exists",
            "storage.account": self.storage_account,
            "storage.container": self.container_name,
            "storage.path": path,
            "storage.operation_id": operation_id,
            "correlation_id": correlation_id
        })
        try:
            # Get the file system client
            service_client = await self._get_service_client()
            loop = asyncio.get_event_loop()
            file_system_client = await loop.run_in_executor(
                None,
                lambda: service_client.get_file_system_client(self.container_name)
            )
            
            # Check if path exists by trying to list it
            # This is more efficient than downloading the file
            paths = await loop.run_in_executor(
                None,
                lambda: list(file_system_client.get_paths(path, recursive=False, max_results=1))
            )
            
            return len(paths) > 0
            
        except Exception as e:
            logger.debug(f"Error checking if path {path} exists: {e}")
            return False
    
    @trace_method(name="LakehouseClient.list_files", kind="CLIENT")
    async def list_files(self, path: str, correlation_id: Optional[str] = None) -> List[str]:
        """List files in a directory in the data lake.
        
        Args:
            path: Directory path to list
            correlation_id: Optional correlation ID for distributed tracing
            
        Returns:
            List of file paths
        """
        # Generate operation ID for tracing
        operation_id = str(uuid.uuid4())
        correlation_id = correlation_id or str(uuid.uuid4())
        
        # Add span attributes for storage operation
        add_span_attributes({
            "storage.system": "azure_datalake",
            "storage.operation": "list_files",
            "storage.account": self.storage_account,
            "storage.container": self.container_name,
            "storage.path": path,
            "storage.operation_id": operation_id,
            "correlation_id": correlation_id
        })
        try:
            # Get the file system client
            service_client = await self._get_service_client()
            loop = asyncio.get_event_loop()
            file_system_client = await loop.run_in_executor(
                None,
                lambda: service_client.get_file_system_client(self.container_name)
            )
            
            # List paths
            paths = []
            async for path in self._list_directory_contents(file_system_client, path):
                paths.append(path)
                
            return paths
            
        except Exception as e:
            logger.error(f"Error listing files in {path}: {e}", exc_info=True)
            return []
    
    @trace_method(name="LakehouseClient._list_directory_contents", kind="INTERNAL")
    async def _list_directory_contents(self, file_system_client, directory_path):
        """Helper method to list directory contents asynchronously.
        
        Args:
            file_system_client: File system client
            directory_path: Directory path to list
            
        Yields:
            File paths in the directory
        """
        # Add span attributes for directory listing
        add_span_attributes({
            "storage.system": "azure_datalake",
            "storage.operation": "list_directory_contents",
            "storage.directory_path": directory_path
        })
        loop = asyncio.get_event_loop()
        paths = await loop.run_in_executor(
            None,
            lambda: list(file_system_client.get_paths(directory_path, recursive=False))
        )
        
        for path in paths:
            yield path.name

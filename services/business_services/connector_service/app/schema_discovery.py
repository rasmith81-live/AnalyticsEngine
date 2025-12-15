from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
import sqlalchemy
from sqlalchemy import inspect
import requests
from pydantic import BaseModel

class ColumnDefinition(BaseModel):
    name: str
    data_type: str
    is_nullable: bool = True
    is_primary_key: bool = False

class TableDefinition(BaseModel):
    name: str
    columns: List[ColumnDefinition]

class SourceAdapter(ABC):
    """Abstract base class for data source adapters."""
    
    @abstractmethod
    def discover_schema(self) -> List[TableDefinition]:
        pass

    @abstractmethod
    def preview_data(self, table_name: str, limit: int = 5) -> List[Dict[str, Any]]:
        pass

class SQLAdapter(SourceAdapter):
    """Adapter for SQL databases (Postgres, MSSQL, etc.) using SQLAlchemy."""
    
    def __init__(self, connection_string: str):
        self.engine = sqlalchemy.create_engine(connection_string)
        self.inspector = inspect(self.engine)

    def discover_schema(self) -> List[TableDefinition]:
        schema = []
        table_names = self.inspector.get_table_names()
        
        for table in table_names:
            columns_info = self.inspector.get_columns(table)
            pk_constraint = self.inspector.get_pk_constraint(table)
            pk_cols = set(pk_constraint.get('constrained_columns', []))
            
            cols = []
            for col in columns_info:
                cols.append(ColumnDefinition(
                    name=col['name'],
                    data_type=str(col['type']),
                    is_nullable=col.get('nullable', True),
                    is_primary_key=col['name'] in pk_cols
                ))
            
            schema.append(TableDefinition(name=table, columns=cols))
        
        return schema

    def preview_data(self, table_name: str, limit: int = 5) -> List[Dict[str, Any]]:
        with self.engine.connect() as conn:
            # Use text() for safety, though table_name should be validated
            query = sqlalchemy.text(f"SELECT * FROM {table_name} LIMIT {limit}")
            result = conn.execute(query)
            return [dict(row._mapping) for row in result]

class RESTAdapter(SourceAdapter):
    """
    Adapter for REST APIs. 
    Infers schema from a sample JSON response.
    """
    
    def __init__(self, base_url: str, endpoint: str, auth_headers: Dict[str, str] = None):
        self.url = f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        self.headers = auth_headers or {}

    def discover_schema(self) -> List[TableDefinition]:
        # Fetch sample data to infer schema
        data = self._fetch_sample()
        if not data:
            return []
        
        # Assume list of objects
        if isinstance(data, list) and len(data) > 0:
            sample_obj = data[0]
        elif isinstance(data, dict):
            sample_obj = data
        else:
            return []

        cols = []
        for key, value in sample_obj.items():
            cols.append(ColumnDefinition(
                name=key,
                data_type=type(value).__name__,
                is_nullable=True
            ))
            
        # Treat the endpoint as a single "Table"
        table_name = self.url.split('/')[-1] or "API_Response"
        return [TableDefinition(name=table_name, columns=cols)]

    def preview_data(self, table_name: str, limit: int = 5) -> List[Dict[str, Any]]:
        # In REST, we usually fetch the same endpoint
        data = self._fetch_sample()
        if isinstance(data, list):
            return data[:limit]
        return [data] if data else []

    def _fetch_sample(self) -> Any:
        try:
            resp = requests.get(self.url, headers=self.headers, timeout=10)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            print(f"API Error: {e}")
            return None

class SchemaDiscoveryEngine:
    """
    Facade for discovering schemas from various sources.
    """
    
    def get_adapter(self, connection_type: str, connection_params: Dict[str, Any]) -> SourceAdapter:
        if connection_type == "sql":
            return SQLAdapter(connection_params['connection_string'])
        elif connection_type == "rest":
            return RESTAdapter(
                connection_params['base_url'], 
                connection_params['endpoint'],
                connection_params.get('headers')
            )
        else:
            raise ValueError(f"Unsupported connection type: {connection_type}")

    def discover(self, connection_type: str, params: Dict[str, Any]) -> List[TableDefinition]:
        adapter = self.get_adapter(connection_type, params)
        return adapter.discover_schema()

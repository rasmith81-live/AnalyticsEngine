from pydantic import BaseModel, Field
from typing import Optional, Dict
from enum import Enum
import sqlalchemy
import requests

class ConnectionType(str, Enum):
    SQL_POSTGRES = "sql_postgres"
    SQL_MSSQL = "sql_mssql"
    REST_API = "rest_api"
    EXCEL_FILE = "excel_file"

class ConnectionProfile(BaseModel):
    id: str
    name: str
    type: ConnectionType
    host: Optional[str] = None
    port: Optional[int] = None
    database: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None # Should be encrypted in storage
    api_url: Optional[str] = None
    file_path: Optional[str] = None
    extra_params: Dict[str, str] = Field(default_factory=dict)

class ConnectionManager:
    """
    Manages secure connectivity to external data sources.
    """
    
    async def test_connection(self, profile: ConnectionProfile) -> bool:
        try:
            if profile.type in [ConnectionType.SQL_POSTGRES, ConnectionType.SQL_MSSQL]:
                return self._test_sql(profile)
            elif profile.type == ConnectionType.REST_API:
                return self._test_api(profile)
            elif profile.type == ConnectionType.EXCEL_FILE:
                return self._test_file(profile)
            return False
        except Exception as e:
            print(f"Connection failed: {str(e)}")
            return False

    def _test_sql(self, profile: ConnectionProfile) -> bool:
        # Construct connection string
        if profile.type == ConnectionType.SQL_POSTGRES:
            url = f"postgresql://{profile.username}:{profile.password}@{profile.host}:{profile.port}/{profile.database}"
        
        engine = sqlalchemy.create_engine(url)
        with engine.connect() as conn:
            return True

    def _test_api(self, profile: ConnectionProfile) -> bool:
        resp = requests.get(profile.api_url, timeout=5)
        return resp.status_code < 500

    def _test_file(self, profile: ConnectionProfile) -> bool:
        import os
        return os.path.exists(profile.file_path)

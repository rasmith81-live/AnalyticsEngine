"""
Demo/Config Service Data Models
"""

from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from enum import Enum


class IntegrationMethod(str, Enum):
    """Integration method types."""
    BATCH = "batch"
    REALTIME = "realtime"


class ProposalStatus(str, Enum):
    """Service proposal status."""
    DRAFT = "draft"
    SENT = "sent"
    SIGNED = "signed"
    REJECTED = "rejected"


class DataSourceType(str, Enum):
    """Data source types."""
    BATCH = "batch"
    API = "api"
    EVENT = "event"


# Request/Response Models

class ClientConfigCreate(BaseModel):
    """Client configuration creation request."""
    client_name: str = Field(..., description="Client name")
    selected_kpis: List[str] = Field(default_factory=list, description="Selected KPI codes")
    data_sources: Optional[List[Dict[str, Any]]] = Field(default=None, description="Data source configurations")
    deployment_config: Optional[Dict[str, Any]] = Field(default=None, description="Deployment configuration")


class ClientConfigUpdate(BaseModel):
    """Client configuration update request."""
    client_name: Optional[str] = Field(None, description="Client name")
    selected_kpis: Optional[List[str]] = Field(None, description="Selected KPI codes")
    data_sources: Optional[List[Dict[str, Any]]] = Field(None, description="Data source configurations")
    deployment_config: Optional[Dict[str, Any]] = Field(None, description="Deployment configuration")


class ClientConfigResponse(BaseModel):
    """Client configuration response."""
    id: str
    client_id: str
    client_name: str
    selected_kpis: List[str]
    custom_kpis: Optional[List[Dict[str, Any]]] = None
    data_sources: Optional[List[Dict[str, Any]]] = None
    deployment_config: Optional[Dict[str, Any]] = None
    license_key: Optional[str] = None
    license_expiration: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime


class CustomKPICreate(BaseModel):
    """Custom KPI creation request."""
    kpi_code: str = Field(..., description="Unique KPI code")
    source_kpi_code: str = Field(..., description="Original KPI code this is derived from")
    name: str = Field(..., description="KPI name")
    formula: str = Field(..., description="Calculation formula")
    unit: str = Field(..., description="Unit of measurement")
    description: Optional[str] = Field(None, description="Description")
    calculation_logic: Optional[str] = Field(None, description="Detailed calculation logic")
    required_objects: List[str] = Field(default_factory=list, description="Required object models")
    metadata_: Optional[Dict[str, Any]] = Field(default_factory=dict, description="Additional metadata")
    created_by: str = Field(..., description="User who created this KPI")


class CustomKPIResponse(BaseModel):
    """Custom KPI response."""
    id: str
    client_id: str
    kpi_code: str
    source_kpi_code: str
    name: str
    formula: str
    unit: str
    description: Optional[str] = None
    calculation_logic: Optional[str] = None
    required_objects: List[str]
    metadata_: Dict[str, Any]
    created_by: str
    created_at: datetime


class RequiredObjectsAnalysisRequest(BaseModel):
    """Required objects analysis request."""
    kpi_codes: List[str] = Field(..., description="List of KPI codes to analyze")


class RequiredObjectsAnalysisResponse(BaseModel):
    """Required objects analysis response."""
    kpi_codes: List[str]
    required_objects: List[str]
    object_details: Dict[str, Any]
    total_objects: int
    uml_diagram: Optional[str] = None  # PlantUML format


class ServiceProposalCreate(BaseModel):
    """Service proposal creation request."""
    client_id: str = Field(..., description="Client ID")
    kpi_codes: List[str] = Field(..., description="Selected KPI codes")
    integration_method: IntegrationMethod = Field(..., description="Integration method")
    custom_notes: Optional[str] = Field(None, description="Custom notes for proposal")


class ServiceProposalResponse(BaseModel):
    """Service proposal response."""
    id: str
    client_id: str
    required_objects: List[str]
    integration_method: IntegrationMethod
    estimated_hours: int
    estimated_cost: float
    timeline_weeks: int
    status: ProposalStatus
    breakdown: Dict[str, Any]
    created_at: datetime


class DataSourceCreate(BaseModel):
    """Data source creation request."""
    name: str = Field(..., description="Data source name")
    type: DataSourceType = Field(..., description="Data source type")
    connector_type: str = Field(..., description="Connector type (e.g., 'salesforce', 'sap')")
    config: Dict[str, Any] = Field(..., description="Connection configuration")


class DataSourceResponse(BaseModel):
    """Data source response."""
    id: str
    client_id: str
    name: str
    type: DataSourceType
    connector_type: str
    config: Dict[str, Any]
    status: str
    last_tested: Optional[datetime] = None
    created_at: datetime


class DemoDataRequest(BaseModel):
    """Demo data generation request."""
    kpi_codes: List[str] = Field(..., description="KPI codes to generate demo data for")
    time_period: str = Field(default="monthly", description="Time period for demo data")
    data_points: int = Field(default=12, description="Number of data points to generate")

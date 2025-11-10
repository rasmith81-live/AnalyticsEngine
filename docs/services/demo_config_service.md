# Demo Config Service

## Overview

Demo/Config Service

Handles client configuration, custom KPI creation, and service proposal generation.

## Data Models

### `ClientConfigCreate`

Client configuration creation request.

**Fields:**

- `client_name`: `str`
- `selected_kpis`: `List[str]`
- `data_sources`: `Optional[List[Dict[str, Any]]]`
- `deployment_config`: `Optional[Dict[str, Any]]`

### `ClientConfigUpdate`

Client configuration update request.

**Fields:**

- `client_name`: `Optional[str]`
- `selected_kpis`: `Optional[List[str]]`
- `data_sources`: `Optional[List[Dict[str, Any]]]`
- `deployment_config`: `Optional[Dict[str, Any]]`

### `ClientConfigResponse`

Client configuration response.

**Fields:**

- `id`: `str`
- `client_id`: `str`
- `client_name`: `str`
- `selected_kpis`: `List[str]`
- `custom_kpis`: `Optional[List[Dict[str, Any]]]`
- `data_sources`: `Optional[List[Dict[str, Any]]]`
- `deployment_config`: `Optional[Dict[str, Any]]`
- `license_key`: `Optional[str]`
- `license_expiration`: `Optional[datetime]`
- `created_at`: `datetime`
- `updated_at`: `datetime`

### `CustomKPICreate`

Custom KPI creation request.

**Fields:**

- `kpi_code`: `str`
- `source_kpi_code`: `str`
- `name`: `str`
- `formula`: `str`
- `unit`: `str`
- `description`: `Optional[str]`
- `calculation_logic`: `Optional[str]`
- `required_objects`: `List[str]`
- `metadata_`: `Optional[Dict[str, Any]]`
- `created_by`: `str`

### `CustomKPIResponse`

Custom KPI response.

**Fields:**

- `id`: `str`
- `client_id`: `str`
- `kpi_code`: `str`
- `source_kpi_code`: `str`
- `name`: `str`
- `formula`: `str`
- `unit`: `str`
- `description`: `Optional[str]`
- `calculation_logic`: `Optional[str]`
- `required_objects`: `List[str]`
- `metadata_`: `Dict[str, Any]`
- `created_by`: `str`
- `created_at`: `datetime`

### `RequiredObjectsAnalysisRequest`

Required objects analysis request.

**Fields:**

- `kpi_codes`: `List[str]`

### `RequiredObjectsAnalysisResponse`

Required objects analysis response.

**Fields:**

- `kpi_codes`: `List[str]`
- `required_objects`: `List[str]`
- `object_details`: `Dict[str, Any]`
- `total_objects`: `int`
- `uml_diagram`: `Optional[str]`

### `ServiceProposalCreate`

Service proposal creation request.

**Fields:**

- `client_id`: `str`
- `kpi_codes`: `List[str]`
- `integration_method`: `IntegrationMethod`
- `custom_notes`: `Optional[str]`

### `ServiceProposalResponse`

Service proposal response.

**Fields:**

- `id`: `str`
- `client_id`: `str`
- `required_objects`: `List[str]`
- `integration_method`: `IntegrationMethod`
- `estimated_hours`: `int`
- `estimated_cost`: `float`
- `timeline_weeks`: `int`
- `status`: `ProposalStatus`
- `breakdown`: `Dict[str, Any]`
- `created_at`: `datetime`

### `DataSourceCreate`

Data source creation request.

**Fields:**

- `name`: `str`
- `type`: `DataSourceType`
- `connector_type`: `str`
- `config`: `Dict[str, Any]`

### `DataSourceResponse`

Data source response.

**Fields:**

- `id`: `str`
- `client_id`: `str`
- `name`: `str`
- `type`: `DataSourceType`
- `connector_type`: `str`
- `config`: `Dict[str, Any]`
- `status`: `str`
- `last_tested`: `Optional[datetime]`
- `created_at`: `datetime`

### `DemoDataRequest`

Demo data generation request.

**Fields:**

- `kpi_codes`: `List[str]`
- `time_period`: `str`
- `data_points`: `int`


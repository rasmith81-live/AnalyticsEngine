"""FastAPI endpoints for metadata operations."""

from fastapi import APIRouter, Depends, HTTPException, Query, Path, Body
from typing import List, Optional, Dict, Any
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession

# Import ontology models
import sys
from pathlib import Path as FilePath
analytics_metadata_path = FilePath(__file__).parent.parent.parent / "analytics_metadata_service"
sys.path.insert(0, str(analytics_metadata_path))

from definitions.ontology_models import (
    ThingDefinition,
    EntityDefinition,
    MetricDefinition,
    ValueChainPatternDefinition,
    ActorDefinition,
    BeneficiaryDefinition,
    CompanyDefinition,
    BusinessProcessDefinition,
    StrategicObjectiveDefinition,
    BenchmarkDefinition,
)

from ..services import MetadataService, MetadataInstantiationService, ConsistencyService
from ..repositories import MetadataWriteRepository, MetadataQueryRepository
from ..dependencies import get_db_session, get_redis_client, get_event_publisher

router = APIRouter(prefix="/api/v1/metadata", tags=["metadata"])


# Dependency to create MetadataService
async def get_metadata_service(
    session: AsyncSession = Depends(get_db_session),
    redis_client = Depends(get_redis_client),
    event_publisher = Depends(get_event_publisher)
) -> MetadataService:
    """Create MetadataService with injected dependencies."""
    write_repo = MetadataWriteRepository(session, event_publisher)
    query_repo = MetadataQueryRepository(session, redis_client)
    instantiation_service = MetadataInstantiationService()
    
    return MetadataService(write_repo, query_repo, instantiation_service)


async def get_consistency_service(
    session: AsyncSession = Depends(get_db_session),
    redis_client = Depends(get_redis_client)
) -> ConsistencyService:
    """Create ConsistencyService with injected dependencies."""
    query_repo = MetadataQueryRepository(session, redis_client)
    return ConsistencyService(query_repo)


# -------------------------------------------------------------------------
# Generic endpoints (work for all definition types)
# -------------------------------------------------------------------------

@router.post("/definitions", response_model=Dict[str, str], status_code=201)
async def create_definition(
    definition: Dict[str, Any] = Body(...),
    created_by: str = Query(..., description="User creating the definition"),
    service: MetadataService = Depends(get_metadata_service)
):
    """Create a new metadata definition.
    
    Supports all definition types (entities, metrics, value chains, etc.)
    """
    try:
        # Instantiate from dict
        kind = definition.get('kind')
        if not kind:
            raise ValueError("Definition must have 'kind' field")
        
        pydantic_def = service.instantiation.instantiate(kind, definition)
        
        definition_id = await service.create_definition(pydantic_def, created_by)
        return {
            "id": str(definition_id),
            "code": service.instantiation.get_code_from_model(pydantic_def),
            "kind": kind
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to create definition: {str(e)}")


@router.get("/definitions/{kind}/{code}")
async def get_definition(
    kind: str = Path(..., description="Type of definition"),
    code: str = Path(..., description="Business identifier"),
    include_relationships: bool = Query(True, description="Include relationships"),
    version: Optional[int] = Query(None, description="Specific version (None = latest)"),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get definition by code."""
    definition = await service.get_definition(
        code=code,
        kind=kind,
        include_relationships=include_relationships,
        version=version
    )
    
    if not definition:
        raise HTTPException(status_code=404, detail=f"{kind}:{code} not found")
    
    return service.instantiation.serialize(definition)


@router.put("/definitions/{kind}/{code}", status_code=204)
async def update_definition(
    kind: str = Path(..., description="Type of definition"),
    code: str = Path(..., description="Business identifier"),
    definition: Dict[str, Any] = Body(...),
    changed_by: str = Query(..., description="User making the change"),
    change_description: Optional[str] = Query(None, description="Description of changes"),
    service: MetadataService = Depends(get_metadata_service)
):
    """Update definition (creates new version)."""
    try:
        pydantic_def = service.instantiation.instantiate(kind, definition)
        
        await service.update_definition(
            code=code,
            kind=kind,
            definition=pydantic_def,
            changed_by=changed_by,
            change_description=change_description
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update definition: {str(e)}")


@router.delete("/definitions/{kind}/{code}", status_code=204)
async def delete_definition(
    kind: str = Path(..., description="Type of definition"),
    code: str = Path(..., description="Business identifier"),
    deleted_by: str = Query(..., description="User deleting the definition"),
    service: MetadataService = Depends(get_metadata_service)
):
    """Soft delete definition."""
    try:
        await service.delete_definition(code=code, kind=kind, deleted_by=deleted_by)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete definition: {str(e)}")


@router.get("/definitions/{kind}")
async def list_definitions_by_kind(
    kind: str = Path(..., description="Type of definition"),
    limit: int = Query(100, ge=1, le=1000, description="Max results"),
    offset: int = Query(0, ge=0, description="Pagination offset"),
    service: MetadataService = Depends(get_metadata_service)
):
    """List all definitions of a specific kind."""
    definitions = await service.get_all_by_kind(kind=kind, limit=limit, offset=offset)
    return [service.instantiation.serialize(d) for d in definitions]


@router.post("/definitions/search")
async def search_definitions(
    kind: str = Query(..., description="Type of definition"),
    filters: Dict[str, Any] = Body(..., description="Search filters"),
    limit: int = Query(100, ge=1, le=1000),
    offset: int = Query(0, ge=0),
    service: MetadataService = Depends(get_metadata_service)
):
    """Search definitions with filters.
    
    Example filters:
    ```json
    {
        "code": "CUSTOMER*",
        "name": "customer",
        "data": {"category": "sales"}
    }
    ```
    """
    definitions = await service.search_definitions(
        kind=kind,
        filters=filters,
        limit=limit,
        offset=offset
    )
    return [service.instantiation.serialize(d) for d in definitions]


@router.get("/definitions/{kind}/count", response_model=Dict[str, int])
async def count_definitions(
    kind: str = Path(..., description="Type of definition"),
    service: MetadataService = Depends(get_metadata_service)
):
    """Count definitions of a specific kind."""
    count = await service.count_by_kind(kind)
    return {"kind": kind, "count": count}


# -------------------------------------------------------------------------
# Relationship endpoints
# -------------------------------------------------------------------------

@router.get("/definitions/{kind}/{code}/relationships")
async def get_relationships(
    kind: str = Path(..., description="Type of definition"),
    code: str = Path(..., description="Business identifier"),
    direction: str = Query("both", regex="^(outbound|inbound|both)$"),
    relationship_types: Optional[List[str]] = Query(None, description="Filter by types"),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get relationships for a definition."""
    return await service.query_repo.get_relationships(
        entity_code=code,
        direction=direction,
        relationship_types=relationship_types
    )


@router.get("/definitions/{kind}/{code}/graph")
async def get_knowledge_graph(
    kind: str = Path(..., description="Type of definition"),
    code: str = Path(..., description="Business identifier"),
    depth: int = Query(2, ge=1, le=5, description="Max traversal depth"),
    relationship_types: Optional[List[str]] = Query(None, description="Filter by types"),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get knowledge graph around a definition."""
    return await service.get_knowledge_graph(
        entity_code=code,
        depth=depth,
        relationship_types=relationship_types
    )


# -------------------------------------------------------------------------
# Version history endpoints
# -------------------------------------------------------------------------

@router.get("/definitions/{kind}/{code}/versions")
async def get_version_history(
    kind: str = Path(..., description="Type of definition"),
    code: str = Path(..., description="Business identifier"),
    limit: int = Query(50, ge=1, le=200),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get version history for a definition."""
    return await service.get_version_history(code=code, kind=kind, limit=limit)


# -------------------------------------------------------------------------
# Bulk operations
# -------------------------------------------------------------------------

@router.post("/definitions/bulk", response_model=Dict[str, Any], status_code=201)
async def bulk_create_definitions(
    definitions: List[Dict[str, Any]] = Body(...),
    created_by: str = Query(..., description="User creating the definitions"),
    service: MetadataService = Depends(get_metadata_service)
):
    """Bulk create definitions (for seeding)."""
    try:
        # Convert dicts to Pydantic models
        pydantic_defs = []
        for defn in definitions:
            kind = defn.get('kind')
            if not kind:
                raise ValueError("All definitions must have 'kind' field")
            pydantic_defs.append(service.instantiation.instantiate(kind, defn))
        
        ids = await service.bulk_create_definitions(pydantic_defs, created_by)
        return {
            "created_count": len(ids),
            "ids": [str(id) for id in ids]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Bulk create failed: {str(e)}")


# -------------------------------------------------------------------------
# Type-specific convenience endpoints
# -------------------------------------------------------------------------

@router.get("/entities/{code}")
async def get_entity(
    code: str = Path(...),
    include_relationships: bool = Query(True),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get entity by code."""
    entity = await service.get_definition(
        code=code,
        kind="entity_definition",
        include_relationships=include_relationships
    )
    
    if not entity:
        raise HTTPException(status_code=404, detail=f"Entity {code} not found")
    
    return service.instantiation.serialize(entity)


@router.get("/metrics/{code}")
async def get_metric(
    code: str = Path(...),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get metric by code."""
    metric = await service.get_definition(code=code, kind="metric_definition")
    
    if not metric:
        raise HTTPException(status_code=404, detail=f"Metric {code} not found")
    
    return service.instantiation.serialize(metric)


@router.get("/value-chains/{code}")
async def get_value_chain(
    code: str = Path(...),
    include_relationships: bool = Query(True),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get value chain pattern by code."""
    value_chain = await service.get_definition(
        code=code,
        kind="value_chain_pattern_definition",
        include_relationships=include_relationships
    )
    
    if not value_chain:
        raise HTTPException(status_code=404, detail=f"Value chain {code} not found")
    
    return service.instantiation.serialize(value_chain)


@router.get("/actors/{code}")
async def get_actor(
    code: str = Path(...),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get actor by code."""
    actor = await service.get_definition(code=code, kind="actor_definition")
    
    if not actor:
        raise HTTPException(status_code=404, detail=f"Actor {code} not found")
    
    return service.instantiation.serialize(actor)


@router.get("/beneficiaries/{code}")
async def get_beneficiary(
    code: str = Path(...),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get beneficiary by code."""
    beneficiary = await service.get_definition(code=code, kind="beneficiary_definition")
    
    if not beneficiary:
        raise HTTPException(status_code=404, detail=f"Beneficiary {code} not found")
    
    return service.instantiation.serialize(beneficiary)


@router.get("/companies/{code}")
async def get_company(
    code: str = Path(...),
    include_relationships: bool = Query(True),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get company by code."""
    company = await service.get_definition(
        code=code,
        kind="company_definition",
        include_relationships=include_relationships
    )
    
    if not company:
        raise HTTPException(status_code=404, detail=f"Company {code} not found")
    
    return service.instantiation.serialize(company)


@router.get("/business-processes/{code}")
async def get_business_process(
    code: str = Path(...),
    include_relationships: bool = Query(True),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get business process by code."""
    process = await service.get_definition(
        code=code,
        kind="business_process_definition",
        include_relationships=include_relationships
    )
    
    if not process:
        raise HTTPException(status_code=404, detail=f"Business process {code} not found")
    
    return service.instantiation.serialize(process)


@router.get("/strategic-objectives/{code}")
async def get_strategic_objective(
    code: str = Path(...),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get strategic objective by code."""
    objective = await service.get_definition(code=code, kind="strategic_objective_definition")
    
    if not objective:
        raise HTTPException(status_code=404, detail=f"Strategic objective {code} not found")
    
    return service.instantiation.serialize(objective)


@router.get("/benchmarks/{code}")
async def get_benchmark(
    code: str = Path(...),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get benchmark by code."""
    benchmark = await service.get_definition(code=code, kind="benchmark_definition")
    
    if not benchmark:
        raise HTTPException(status_code=404, detail=f"Benchmark {code} not found")
    
    return service.instantiation.serialize(benchmark)


@router.get("/metrics/{metric_code}/benchmarks")
async def get_benchmarks_for_metric(
    metric_code: str = Path(..., description="Metric code"),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get all benchmarks for a specific metric."""
    benchmarks = await service.search_definitions(
        kind="benchmark_definition",
        filters={"metric_code": metric_code}
    )
    return [service.instantiation.serialize(b) for b in benchmarks]


@router.get("/clients/{code}")
async def get_client(
    code: str = Path(...),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get client by code."""
    client = await service.get_definition(code=code, kind="client_definition")
    
    if not client:
        raise HTTPException(status_code=404, detail=f"Client {code} not found")
    
    return service.instantiation.serialize(client)


@router.get("/roles/{code}")
async def get_role(
    code: str = Path(...),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get role by code."""
    role = await service.get_definition(code=code, kind="role_definition")
    
    if not role:
        raise HTTPException(status_code=404, detail=f"Role {code} not found")
    
    return service.instantiation.serialize(role)


@router.get("/clients/{client_code}/roles")
async def get_roles_for_client(
    client_code: str = Path(..., description="Client code"),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get all roles for a specific client."""
    roles = await service.search_definitions(
        kind="role_definition",
        filters={"client_code": client_code}
    )
    return [service.instantiation.serialize(r) for r in roles]


@router.get("/permissions/{code}")
async def get_permission(
    code: str = Path(...),
    kind: str = Query("permission_definition", description="Permission type"),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get permission by code."""
    permission = await service.get_definition(code=code, kind=kind)
    
    if not permission:
        raise HTTPException(status_code=404, detail=f"Permission {code} not found")
    
    return service.instantiation.serialize(permission)


@router.get("/row-level-security/{code}")
async def get_row_level_security(
    code: str = Path(...),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get row-level security definition by code."""
    rls = await service.get_definition(code=code, kind="row_level_security_definition")
    
    if not rls:
        raise HTTPException(status_code=404, detail=f"Row-level security {code} not found")
    
    return service.instantiation.serialize(rls)


@router.get("/countries/{code}")
async def get_country(
    code: str = Path(...),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get country by code."""
    country = await service.get_definition(code=code, kind="country_definition")
    
    if not country:
        raise HTTPException(status_code=404, detail=f"Country {code} not found")
    
    return service.instantiation.serialize(country)


@router.get("/regions/{code}")
async def get_region(
    code: str = Path(...),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get region by code."""
    region = await service.get_definition(code=code, kind="region_definition")
    
    if not region:
        raise HTTPException(status_code=404, detail=f"Region {code} not found")
    
    return service.instantiation.serialize(region)


@router.get("/countries/{country_code}/regions")
async def get_regions_for_country(
    country_code: str = Path(..., description="Country code"),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get all regions for a specific country."""
    regions = await service.search_definitions(
        kind="region_definition",
        filters={"country_code": country_code}
    )
    return [service.instantiation.serialize(r) for r in regions]


@router.get("/metropolitan-areas/{code}")
async def get_metropolitan_area(
    code: str = Path(...),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get metropolitan area by code."""
    msa = await service.get_definition(code=code, kind="metropolitan_area_definition")
    
    if not msa:
        raise HTTPException(status_code=404, detail=f"Metropolitan area {code} not found")
    
    return service.instantiation.serialize(msa)


@router.get("/regions/{region_code}/metropolitan-areas")
async def get_msas_for_region(
    region_code: str = Path(..., description="Region code"),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get all metropolitan areas for a specific region."""
    msas = await service.search_definitions(
        kind="metropolitan_area_definition",
        filters={"region_code": region_code}
    )
    return [service.instantiation.serialize(m) for m in msas]


@router.get("/naics-industries/{code}")
async def get_naics_industry(
    code: str = Path(...),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get NAICS industry by code."""
    naics = await service.get_definition(code=code, kind="naics_industry_definition")
    
    if not naics:
        raise HTTPException(status_code=404, detail=f"NAICS industry {code} not found")
    
    return service.instantiation.serialize(naics)


@router.get("/analytics-strategies/{code}")
async def get_analytics_strategy(
    code: str = Path(...),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get analytics strategy by code."""
    strategy = await service.get_definition(code=code, kind="analytics_strategy_definition")
    
    if not strategy:
        raise HTTPException(status_code=404, detail=f"Analytics strategy {code} not found")
    
    return service.instantiation.serialize(strategy)


@router.get("/data-sources/{code}")
async def get_data_source(
    code: str = Path(...),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get data source by code."""
    source = await service.get_definition(code=code, kind="data_source_definition")
    
    if not source:
        raise HTTPException(status_code=404, detail=f"Data source {code} not found")
    
    return service.instantiation.serialize(source)


@router.get("/data-products/{code}")
async def get_data_product(
    code: str = Path(...),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get data product by code."""
    product = await service.get_definition(code=code, kind="data_product_definition")
    
    if not product:
        raise HTTPException(status_code=404, detail=f"Data product {code} not found")
    
    return service.instantiation.serialize(product)


@router.get("/analytics-use-cases/{code}")
async def get_analytics_use_case(
    code: str = Path(...),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get analytics use case by code."""
    use_case = await service.get_definition(code=code, kind="analytics_use_case_definition")
    
    if not use_case:
        raise HTTPException(status_code=404, detail=f"Analytics use case {code} not found")
    
    return service.instantiation.serialize(use_case)


@router.get("/dimensions/{code}")
async def get_dimension(
    code: str = Path(...),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get dimension by code."""
    dimension = await service.get_definition(code=code, kind="dimension_definition")
    
    if not dimension:
        raise HTTPException(status_code=404, detail=f"Dimension {code} not found")
    
    return service.instantiation.serialize(dimension)


@router.get("/metric-categories/{code}")
async def get_metric_category(
    code: str = Path(...),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get metric category by code."""
    category = await service.get_definition(code=code, kind="metric_category_definition")
    
    if not category:
        raise HTTPException(status_code=404, detail=f"Metric category {code} not found")
    
    return service.instantiation.serialize(category)


@router.get("/data-quality-rules/{code}")
async def get_data_quality_rule(
    code: str = Path(...),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get data quality rule by code."""
    rule = await service.get_definition(code=code, kind="data_quality_rule_definition")
    
    if not rule:
        raise HTTPException(status_code=404, detail=f"Data quality rule {code} not found")
    
    return service.instantiation.serialize(rule)


@router.get("/external-events/{code}")
async def get_external_event(
    code: str = Path(...),
    service: MetadataService = Depends(get_metadata_service)
):
    """Get external event by code."""
    event = await service.get_definition(code=code, kind="external_event_definition")
    
    if not event:
        raise HTTPException(status_code=404, detail=f"External event {code} not found")
    
    return service.instantiation.serialize(event)


# -------------------------------------------------------------------------
# Governance & Consistency Endpoints
# -------------------------------------------------------------------------

@router.get("/graph/uml", response_model=str)
async def get_ontology_uml(
    service: ConsistencyService = Depends(get_consistency_service)
):
    """Generate PlantUML diagram of the current ontology."""
    return await service.generate_plantuml()


@router.get("/consistency/check", response_model=Dict[str, List[str]])
async def check_consistency(
    service: ConsistencyService = Depends(get_consistency_service)
):
    """Run consistency checks on the metadata graph.
    
    Returns a list of errors found in relationships, metrics, and formulas.
    """
    return await service.check_integrity()


@router.post("/definitions/merge", status_code=204)
async def merge_definitions(
    target_code: str = Body(..., description="The definition to keep"),
    source_code: str = Body(..., description="The definition to merge and delete"),
    kind: str = Body(..., description="Type of definition"),
    merged_by: str = Query(..., description="User performing the merge"),
    service: MetadataService = Depends(get_metadata_service)
):
    """Merge two definitions (e.g. duplicates).
    
    Moves all relationships from source to target, then deletes source.
    """
    try:
        await service.merge_definitions(
            target_code=target_code,
            source_code=source_code,
            kind=kind,
            merged_by=merged_by
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Merge failed: {str(e)}")


# -------------------------------------------------------------------------
# Health check
# -------------------------------------------------------------------------

@router.get("/health", response_model=Dict[str, str])
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "service": "business_metadata"}

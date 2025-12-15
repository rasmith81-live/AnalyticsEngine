
import logging
from typing import List, Dict, Any, Optional
from fastapi import FastAPI, HTTPException, BackgroundTasks, Depends
from contextlib import asynccontextmanager
import uuid
from datetime import datetime

from .config import get_settings
from .models import (
    DataQualityRule, ValidationResult, 
    LineageNode, LineageEdge, LineageGraph,
    ServiceHealth, DependencyStatus
)
from .engine.rules_engine import RulesEngine
from .engine.lineage_engine import LineageEngine

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global engines
rules_engine = RulesEngine()
lineage_engine = LineageEngine()

# In-memory store for rules (replace with Database Service in production)
active_rules: Dict[str, DataQualityRule] = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan events."""
    settings = get_settings()
    logger.info(f"{settings.service_name} starting...")
    
    # Initialize/Load rules if needed
    # ...
    
    yield
    
    logger.info(f"{settings.service_name} shutting down...")

app = FastAPI(
    title="Data Governance Service",
    description="Service for Data Quality Validation and Lineage Tracking",
    version="1.0.0",
    lifespan=lifespan,
    openapi_url="/api/v1/openapi.json"
)

# --- Health Check ---

@app.get("/health", response_model=ServiceHealth)
async def health_check():
    """Check service health."""
    settings = get_settings()
    return ServiceHealth(
        status="healthy",
        timestamp=datetime.utcnow(),
        dependencies=[], # Add dependencies check (DB, Messaging) here
        uptime_seconds=0.0, # Implement uptime tracking
        version="1.0.0"
    )

# --- Data Quality Endpoints ---

@app.post("/api/v1/rules", response_model=DataQualityRule)
async def create_rule(rule: DataQualityRule):
    """Create a new data quality rule."""
    if rule.id in active_rules:
        raise HTTPException(status_code=409, detail="Rule ID already exists")
    
    active_rules[rule.id] = rule
    logger.info(f"Created rule: {rule.name} ({rule.id})")
    return rule

@app.get("/api/v1/rules", response_model=List[DataQualityRule])
async def list_rules():
    """List all active data quality rules."""
    return list(active_rules.values())

@app.post("/api/v1/validate/record", response_model=List[ValidationResult])
async def validate_record(record: Dict[str, Any], rule_ids: Optional[List[str]] = None):
    """
    Validate a single record against active rules.
    If rule_ids provided, only check those. Otherwise check all.
    """
    if rule_ids:
        rules_to_check = [active_rules[rid] for rid in rule_ids if rid in active_rules]
    else:
        rules_to_check = list(active_rules.values())
        
    return rules_engine.validate_record(record, rules_to_check)

@app.post("/api/v1/validate/dataset", response_model=List[ValidationResult])
async def validate_dataset(dataset: List[Dict[str, Any]], rule_ids: Optional[List[str]] = None):
    """
    Validate a dataset against active rules.
    """
    if rule_ids:
        rules_to_check = [active_rules[rid] for rid in rule_ids if rid in active_rules]
    else:
        rules_to_check = list(active_rules.values())
        
    return rules_engine.validate_dataset(dataset, rules_to_check)

# --- Lineage Endpoints ---

@app.post("/api/v1/lineage/nodes", response_model=LineageNode)
async def add_lineage_node(node: LineageNode):
    """Register a node in the lineage graph."""
    lineage_engine.add_node(node)
    return node

@app.post("/api/v1/lineage/edges", response_model=LineageEdge)
async def add_lineage_edge(edge: LineageEdge):
    """Register a flow (edge) between lineage nodes."""
    lineage_engine.add_edge(edge)
    return edge

@app.get("/api/v1/lineage/upstream/{node_id}", response_model=LineageGraph)
async def get_upstream_lineage(node_id: str, depth: int = 5):
    """Get upstream lineage (provenance) for a node."""
    return lineage_engine.get_upstream_lineage(node_id, depth)

@app.get("/api/v1/lineage/downstream/{node_id}", response_model=LineageGraph)
async def get_downstream_lineage(node_id: str, depth: int = 5):
    """Get downstream lineage (impact analysis) for a node."""
    return lineage_engine.get_downstream_lineage(node_id, depth)

if __name__ == "__main__":
    import uvicorn
    settings = get_settings()
    uvicorn.run(app, host=settings.service_host, port=settings.service_port)

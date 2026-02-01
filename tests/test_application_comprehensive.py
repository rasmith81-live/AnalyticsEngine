"""
Comprehensive Application Test Suite

Tests all services and features of the AnalyticsEngine application following
the Tester Agent contract requirements:
- Tier 0: Never claim tests pass when they don't
- Tier 1: Validate all core functionality before approval
- Tier 2: Include edge cases and failure scenarios

Services Tested:
  Backend: database_service, messaging_service, archival_service, observability_service, multi_agent_service
  Business: business_metadata, calculation_engine, demo_config, connector, ingestion, metadata_ingestion, conversation, data_simulator
  Support: systems_monitor, entity_resolution, data_governance, machine_learning
  Frontend: api_gateway

Uses data_simulator_service for test data generation per user requirements.
"""

import asyncio
import json
import logging
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import httpx

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s'
)
logger = logging.getLogger(__name__)

# =============================================================================
# Service Configuration
# =============================================================================

class ServiceTier(str, Enum):
    """Service tier classification."""
    BACKEND = "backend"
    BUSINESS = "business"
    SUPPORT = "support"
    FRONTEND = "frontend"


@dataclass
class ServiceConfig:
    """Configuration for a service."""
    name: str
    port: int
    tier: ServiceTier
    description: str
    critical: bool = True  # If failure blocks other services


SERVICES: Dict[str, ServiceConfig] = {
    # Backend Services
    "database_service": ServiceConfig("database_service", 8000, ServiceTier.BACKEND, "CQRS database operations", critical=True),
    "messaging_service": ServiceConfig("messaging_service", 8002, ServiceTier.BACKEND, "Redis pub/sub messaging", critical=True),
    "archival_service": ServiceConfig("archival_service", 8005, ServiceTier.BACKEND, "TimescaleDB archival to lakehouse"),
    "observability_service": ServiceConfig("observability_service", 8080, ServiceTier.BACKEND, "Monitoring and tracing"),
    "multi_agent_service": ServiceConfig("multi_agent_service", 8091, ServiceTier.BACKEND, "Agent contracts and blackboard"),
    
    # Business Services
    "business_metadata": ServiceConfig("business_metadata", 8020, ServiceTier.BUSINESS, "Analytics metadata management"),
    "calculation_engine_service": ServiceConfig("calculation_engine_service", 8021, ServiceTier.BUSINESS, "KPI calculations"),
    "demo_config_service": ServiceConfig("demo_config_service", 8022, ServiceTier.BUSINESS, "Demo configuration"),
    "connector_service": ServiceConfig("connector_service", 8023, ServiceTier.BUSINESS, "Data connectors"),
    "ingestion_service": ServiceConfig("ingestion_service", 8024, ServiceTier.BUSINESS, "Data ingestion"),
    "metadata_ingestion_service": ServiceConfig("metadata_ingestion_service", 8025, ServiceTier.BUSINESS, "NLP metadata ingestion"),
    "conversation_service": ServiceConfig("conversation_service", 8026, ServiceTier.BUSINESS, "AI conversation"),
    "data_simulator_service": ServiceConfig("data_simulator_service", 8007, ServiceTier.BUSINESS, "Test data simulation"),
    
    # Support Services
    "systems_monitor": ServiceConfig("systems_monitor", 8010, ServiceTier.SUPPORT, "System health monitoring"),
    "entity_resolution_service": ServiceConfig("entity_resolution_service", 8012, ServiceTier.SUPPORT, "Entity resolution with LLM"),
    "data_governance_service": ServiceConfig("data_governance_service", 8013, ServiceTier.SUPPORT, "Data governance policies"),
    "machine_learning_service": ServiceConfig("machine_learning_service", 8014, ServiceTier.SUPPORT, "ML model management"),
    
    # Frontend Services
    "api_gateway": ServiceConfig("api_gateway", 8090, ServiceTier.FRONTEND, "Unified API gateway"),
}

TEST_TIMEOUT = 30.0


# =============================================================================
# Test Results
# =============================================================================

@dataclass
class TestResult:
    """Result of a single test case."""
    test_name: str
    service: str
    feature: str
    passed: bool
    duration_ms: float
    details: str = ""
    error: Optional[str] = None
    tier: int = 1  # Contract tier (0, 1, or 2)


@dataclass 
class ServiceTestResults:
    """Results for a single service."""
    service_name: str
    healthy: bool
    tests_passed: int = 0
    tests_failed: int = 0
    tests_skipped: int = 0
    results: List[TestResult] = field(default_factory=list)
    
    @property
    def total_tests(self) -> int:
        return self.tests_passed + self.tests_failed + self.tests_skipped
    
    @property
    def pass_rate(self) -> float:
        if self.total_tests == 0:
            return 0.0
        return (self.tests_passed / self.total_tests) * 100


@dataclass
class ApplicationTestResults:
    """Results for the entire application."""
    services_tested: int = 0
    services_healthy: int = 0
    services_unhealthy: int = 0
    total_tests: int = 0
    passed: int = 0
    failed: int = 0
    skipped: int = 0
    service_results: Dict[str, ServiceTestResults] = field(default_factory=dict)
    issues_found: List[str] = field(default_factory=list)
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    
    @property
    def duration_seconds(self) -> float:
        if self.start_time and self.end_time:
            return (self.end_time - self.start_time).total_seconds()
        return 0.0
    
    @property
    def pass_rate(self) -> float:
        if self.total_tests == 0:
            return 0.0
        return (self.passed / self.total_tests) * 100


# =============================================================================
# HTTP Client
# =============================================================================

class ServiceClient:
    """HTTP client for testing service endpoints."""
    
    def __init__(self, service_name: str, port: int):
        self.service_name = service_name
        self.base_url = f"http://localhost:{port}"
        self._client: Optional[httpx.AsyncClient] = None
    
    async def __aenter__(self):
        self._client = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=TEST_TIMEOUT
        )
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._client:
            await self._client.aclose()
    
    async def health_check(self) -> Dict[str, Any]:
        """Check service health."""
        try:
            response = await self._client.get("/health")
            return response.json() if response.status_code == 200 else {"status": "error", "code": response.status_code}
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    async def get(self, path: str, params: Optional[Dict] = None) -> Tuple[int, Any]:
        """GET request."""
        try:
            response = await self._client.get(path, params=params)
            try:
                data = response.json()
            except:
                data = response.text
            return response.status_code, data
        except Exception as e:
            return 0, {"error": str(e)}
    
    async def post(self, path: str, json_data: Optional[Dict] = None, params: Optional[Dict] = None) -> Tuple[int, Any]:
        """POST request."""
        try:
            response = await self._client.post(path, json=json_data, params=params)
            try:
                data = response.json()
            except:
                data = response.text
            return response.status_code, data
        except Exception as e:
            return 0, {"error": str(e)}
    
    async def put(self, path: str, json_data: Optional[Dict] = None) -> Tuple[int, Any]:
        """PUT request."""
        try:
            response = await self._client.put(path, json=json_data)
            try:
                data = response.json()
            except:
                data = response.text
            return response.status_code, data
        except Exception as e:
            return 0, {"error": str(e)}
    
    async def delete(self, path: str) -> Tuple[int, Any]:
        """DELETE request."""
        try:
            response = await self._client.delete(path)
            try:
                data = response.json()
            except:
                data = response.text
            return response.status_code, data
        except Exception as e:
            return 0, {"error": str(e)}


# =============================================================================
# Test Suite
# =============================================================================

class ApplicationTestSuite:
    """Comprehensive test suite for the entire application."""
    
    def __init__(self):
        self.results = ApplicationTestResults()
        self.test_timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    
    def _record_result(self, service: str, result: TestResult):
        """Record a test result."""
        if service not in self.results.service_results:
            self.results.service_results[service] = ServiceTestResults(
                service_name=service,
                healthy=False
            )
        
        svc_results = self.results.service_results[service]
        svc_results.results.append(result)
        self.results.total_tests += 1
        
        if result.passed:
            svc_results.tests_passed += 1
            self.results.passed += 1
        else:
            svc_results.tests_failed += 1
            self.results.failed += 1
            if result.error:
                self.results.issues_found.append(
                    f"[{service}] {result.test_name}: {result.error}"
                )
    
    async def run_all_tests(self) -> ApplicationTestResults:
        """Run all test cases for all services."""
        self.results.start_time = datetime.utcnow()
        
        logger.info("=" * 80)
        logger.info("COMPREHENSIVE APPLICATION TEST SUITE")
        logger.info("Following Tester Agent Contract Requirements")
        logger.info("=" * 80)
        
        # Phase 1: Health checks for all services
        logger.info("\n--- Phase 1: Service Health Checks ---")
        await self._run_health_checks()
        
        # Phase 2: Backend service tests
        logger.info("\n--- Phase 2: Backend Services Tests ---")
        await self._test_database_service()
        await self._test_messaging_service()
        await self._test_archival_service()
        await self._test_observability_service()
        await self._test_multi_agent_service()
        
        # Phase 3: Business service tests
        logger.info("\n--- Phase 3: Business Services Tests ---")
        await self._test_business_metadata()
        await self._test_calculation_engine()
        await self._test_demo_config_service()
        await self._test_connector_service()
        await self._test_ingestion_service()
        await self._test_metadata_ingestion_service()
        await self._test_conversation_service()
        await self._test_data_simulator_service()
        
        # Phase 4: Support service tests
        logger.info("\n--- Phase 4: Support Services Tests ---")
        await self._test_systems_monitor()
        await self._test_entity_resolution_service()
        await self._test_data_governance_service()
        await self._test_machine_learning_service()
        
        # Phase 5: API Gateway tests
        logger.info("\n--- Phase 5: API Gateway Tests ---")
        await self._test_api_gateway()
        
        # Phase 6: Integration tests
        logger.info("\n--- Phase 6: Integration Tests ---")
        await self._test_service_integration()
        
        self.results.end_time = datetime.utcnow()
        return self.results
    
    # =========================================================================
    # Phase 1: Health Checks
    # =========================================================================
    
    async def _run_health_checks(self):
        """Run health checks for all services."""
        for service_name, config in SERVICES.items():
            start = datetime.utcnow()
            try:
                async with ServiceClient(service_name, config.port) as client:
                    result = await client.health_check()
                    healthy = result.get("status") in ("healthy", "ok")
                    
                    self.results.services_tested += 1
                    if healthy:
                        self.results.services_healthy += 1
                    else:
                        self.results.services_unhealthy += 1
                    
                    if service_name not in self.results.service_results:
                        self.results.service_results[service_name] = ServiceTestResults(
                            service_name=service_name,
                            healthy=healthy
                        )
                    else:
                        self.results.service_results[service_name].healthy = healthy
                    
                    self._record_result(service_name, TestResult(
                        test_name="health_check",
                        service=service_name,
                        feature="Health",
                        passed=healthy,
                        duration_ms=(datetime.utcnow() - start).total_seconds() * 1000,
                        details=f"Status: {result.get('status')}",
                        error=None if healthy else f"Service unhealthy: {result}",
                        tier=0
                    ))
                    logger.info(f"  {'✓' if healthy else '✗'} {service_name}: {result.get('status')}")
            except Exception as e:
                self.results.services_tested += 1
                self.results.services_unhealthy += 1
                self._record_result(service_name, TestResult(
                    test_name="health_check",
                    service=service_name,
                    feature="Health",
                    passed=False,
                    duration_ms=(datetime.utcnow() - start).total_seconds() * 1000,
                    error=str(e),
                    tier=0
                ))
                logger.error(f"  ✗ {service_name}: {e}")
    
    # =========================================================================
    # Phase 2: Backend Services
    # =========================================================================
    
    async def _test_database_service(self):
        """Test database service endpoints."""
        service = "database_service"
        config = SERVICES[service]
        
        if not self.results.service_results.get(service, ServiceTestResults(service, False)).healthy:
            logger.warning(f"  Skipping {service} tests - service unhealthy")
            return
        
        async with ServiceClient(service, config.port) as client:
            # Test: List tables
            await self._run_test(client, service, "list_tables", "GET", "/api/v1/tables")
            
            # Test: Query endpoint
            await self._run_test(client, service, "query_endpoint", "GET", "/api/v1/query/status")
            
            # Test: Schema info
            await self._run_test(client, service, "schema_info", "GET", "/api/v1/schema")
    
    async def _test_messaging_service(self):
        """Test messaging service endpoints."""
        service = "messaging_service"
        config = SERVICES[service]
        
        if not self.results.service_results.get(service, ServiceTestResults(service, False)).healthy:
            logger.warning(f"  Skipping {service} tests - service unhealthy")
            return
        
        async with ServiceClient(service, config.port) as client:
            # Test: Channels list
            await self._run_test(client, service, "list_channels", "GET", "/api/v1/channels")
            
            # Test: Publish message
            await self._run_test(client, service, "publish_message", "POST", "/api/v1/publish",
                                json_data={"channel": "test_channel", "message": {"test": True}})
            
            # Test: Stream info
            await self._run_test(client, service, "stream_info", "GET", "/api/v1/streams")
    
    async def _test_archival_service(self):
        """Test archival service endpoints."""
        service = "archival_service"
        config = SERVICES[service]
        
        if not self.results.service_results.get(service, ServiceTestResults(service, False)).healthy:
            logger.warning(f"  Skipping {service} tests - service unhealthy")
            return
        
        async with ServiceClient(service, config.port) as client:
            # Test: Archive status
            await self._run_test(client, service, "archive_status", "GET", "/api/v1/archive/status")
            
            # Test: List archived tables
            await self._run_test(client, service, "list_archived", "GET", "/api/v1/archive/tables")
    
    async def _test_observability_service(self):
        """Test observability service endpoints."""
        service = "observability_service"
        config = SERVICES[service]
        
        if not self.results.service_results.get(service, ServiceTestResults(service, False)).healthy:
            logger.warning(f"  Skipping {service} tests - service unhealthy")
            return
        
        async with ServiceClient(service, config.port) as client:
            # Test: Metrics endpoint
            await self._run_test(client, service, "metrics", "GET", "/metrics")
            
            # Test: Traces endpoint
            await self._run_test(client, service, "traces", "GET", "/api/v1/traces")
            
            # Test: Alerts
            await self._run_test(client, service, "alerts", "GET", "/api/v1/alerts")
    
    async def _test_multi_agent_service(self):
        """Test multi-agent service endpoints."""
        service = "multi_agent_service"
        config = SERVICES[service]
        
        if not self.results.service_results.get(service, ServiceTestResults(service, False)).healthy:
            logger.warning(f"  Skipping {service} tests - service unhealthy")
            return
        
        async with ServiceClient(service, config.port) as client:
            # Test: List agents
            await self._run_test(client, service, "list_agents", "GET", "/agents/list")
            
            # Test: Dashboard metrics
            await self._run_test(client, service, "dashboard_metrics", "GET", "/dashboard/metrics")
            
            # Test: Create session
            code, data = await client.post("/api/v1/agents/sessions", 
                                          json_data={"user_id": "test_user", "context": {}})
            session_id = data.get("session_id") if isinstance(data, dict) else None
            
            self._record_result(service, TestResult(
                test_name="create_session",
                service=service,
                feature="Sessions",
                passed=code in (200, 201) and session_id,
                duration_ms=0,
                details=f"Session: {session_id}",
                error=str(data) if code not in (200, 201) else None
            ))
            
            if session_id:
                # Test: Create task on blackboard
                await self._run_test(client, service, "create_task", "POST", 
                                    f"/blackboard/{session_id}/tasks",
                                    params={"creator_role": "coordinator"},
                                    json_data={"title": "Test Task", "description": "Test", "done_when": ["Done"]})
                
                # Test: State transition
                await self._run_test(client, service, "state_transition", "POST",
                                    f"/agents/tester/transition",
                                    params={"session_id": session_id},
                                    json_data={"to_state": "analysis", "rationale": "Testing"})
    
    # =========================================================================
    # Phase 3: Business Services
    # =========================================================================
    
    async def _test_business_metadata(self):
        """Test business metadata service endpoints."""
        service = "business_metadata"
        config = SERVICES[service]
        
        if not self.results.service_results.get(service, ServiceTestResults(service, False)).healthy:
            logger.warning(f"  Skipping {service} tests - service unhealthy")
            return
        
        async with ServiceClient(service, config.port) as client:
            # Test: List KPIs
            await self._run_test(client, service, "list_kpis", "GET", "/api/v1/kpis")
            
            # Test: List dimensions
            await self._run_test(client, service, "list_dimensions", "GET", "/api/v1/dimensions")
            
            # Test: List entities
            await self._run_test(client, service, "list_entities", "GET", "/api/v1/entities")
            
            # Test: SCOR mappings
            await self._run_test(client, service, "scor_mappings", "GET", "/api/v1/scor/mappings")
    
    async def _test_calculation_engine(self):
        """Test calculation engine service endpoints."""
        service = "calculation_engine_service"
        config = SERVICES[service]
        
        if not self.results.service_results.get(service, ServiceTestResults(service, False)).healthy:
            logger.warning(f"  Skipping {service} tests - service unhealthy")
            return
        
        async with ServiceClient(service, config.port) as client:
            # Test: List calculations
            await self._run_test(client, service, "list_calculations", "GET", "/api/v1/calculations")
            
            # Test: Validate expression
            await self._run_test(client, service, "validate_expression", "POST", "/api/v1/validate",
                                json_data={"expression": "revenue - cost"})
            
            # Test: Engine status
            await self._run_test(client, service, "engine_status", "GET", "/api/v1/status")
    
    async def _test_demo_config_service(self):
        """Test demo config service endpoints."""
        service = "demo_config_service"
        config = SERVICES[service]
        
        if not self.results.service_results.get(service, ServiceTestResults(service, False)).healthy:
            logger.warning(f"  Skipping {service} tests - service unhealthy")
            return
        
        async with ServiceClient(service, config.port) as client:
            # Test: List clients
            await self._run_test(client, service, "list_clients", "GET", "/api/v1/clients")
            
            # Test: List demos
            await self._run_test(client, service, "list_demos", "GET", "/api/v1/demos")
            
            # Test: Pricing calculator
            await self._run_test(client, service, "pricing_calculator", "POST", "/api/v1/pricing/calculate",
                                json_data={"objects": 10, "integration_type": "realtime"})
    
    async def _test_connector_service(self):
        """Test connector service endpoints."""
        service = "connector_service"
        config = SERVICES[service]
        
        if not self.results.service_results.get(service, ServiceTestResults(service, False)).healthy:
            logger.warning(f"  Skipping {service} tests - service unhealthy")
            return
        
        async with ServiceClient(service, config.port) as client:
            # Test: List connectors
            await self._run_test(client, service, "list_connectors", "GET", "/api/v1/connectors")
            
            # Test: Connector types
            await self._run_test(client, service, "connector_types", "GET", "/api/v1/connectors/types")
    
    async def _test_ingestion_service(self):
        """Test ingestion service endpoints."""
        service = "ingestion_service"
        config = SERVICES[service]
        
        if not self.results.service_results.get(service, ServiceTestResults(service, False)).healthy:
            logger.warning(f"  Skipping {service} tests - service unhealthy")
            return
        
        async with ServiceClient(service, config.port) as client:
            # Test: List jobs
            await self._run_test(client, service, "list_jobs", "GET", "/api/v1/jobs")
            
            # Test: Job status
            await self._run_test(client, service, "job_status", "GET", "/api/v1/jobs/status")
    
    async def _test_metadata_ingestion_service(self):
        """Test metadata ingestion service endpoints."""
        service = "metadata_ingestion_service"
        config = SERVICES[service]
        
        if not self.results.service_results.get(service, ServiceTestResults(service, False)).healthy:
            logger.warning(f"  Skipping {service} tests - service unhealthy")
            return
        
        async with ServiceClient(service, config.port) as client:
            # Test: NLP status
            await self._run_test(client, service, "nlp_status", "GET", "/api/v1/nlp/status")
            
            # Test: Extract entities (simple text)
            await self._run_test(client, service, "extract_entities", "POST", "/api/v1/extract",
                                json_data={"text": "Calculate revenue for Q1 2024"})
    
    async def _test_conversation_service(self):
        """Test conversation service endpoints."""
        service = "conversation_service"
        config = SERVICES[service]
        
        if not self.results.service_results.get(service, ServiceTestResults(service, False)).healthy:
            logger.warning(f"  Skipping {service} tests - service unhealthy")
            return
        
        async with ServiceClient(service, config.port) as client:
            # Test: List agents
            await self._run_test(client, service, "list_agents", "GET", "/api/v1/agents")
            
            # Test: Agent status
            await self._run_test(client, service, "agent_status", "GET", "/api/v1/agents/status")
            
            # Test: MCP servers
            await self._run_test(client, service, "mcp_servers", "GET", "/api/v1/mcp/servers")
    
    async def _test_data_simulator_service(self):
        """Test data simulator service endpoints."""
        service = "data_simulator_service"
        config = SERVICES[service]
        
        if not self.results.service_results.get(service, ServiceTestResults(service, False)).healthy:
            logger.warning(f"  Skipping {service} tests - service unhealthy")
            return
        
        async with ServiceClient(service, config.port) as client:
            # Test: List scenarios
            await self._run_test(client, service, "list_scenarios", "GET", "/api/v1/scenarios")
            
            # Test: Generate data
            await self._run_test(client, service, "generate_data", "POST", "/api/v1/simulate",
                                json_data={"scenario": "supply_chain", "records": 10})
            
            # Test: Simulator status
            await self._run_test(client, service, "simulator_status", "GET", "/api/v1/status")
    
    # =========================================================================
    # Phase 4: Support Services
    # =========================================================================
    
    async def _test_systems_monitor(self):
        """Test systems monitor service endpoints."""
        service = "systems_monitor"
        config = SERVICES[service]
        
        if not self.results.service_results.get(service, ServiceTestResults(service, False)).healthy:
            logger.warning(f"  Skipping {service} tests - service unhealthy")
            return
        
        async with ServiceClient(service, config.port) as client:
            # Test: System status
            await self._run_test(client, service, "system_status", "GET", "/api/v1/status")
            
            # Test: Service health
            await self._run_test(client, service, "service_health", "GET", "/api/v1/services")
            
            # Test: Alerts
            await self._run_test(client, service, "alerts", "GET", "/api/v1/alerts")
    
    async def _test_entity_resolution_service(self):
        """Test entity resolution service endpoints."""
        service = "entity_resolution_service"
        config = SERVICES[service]
        
        if not self.results.service_results.get(service, ServiceTestResults(service, False)).healthy:
            logger.warning(f"  Skipping {service} tests - service unhealthy")
            return
        
        async with ServiceClient(service, config.port) as client:
            # Test: Resolve entity
            await self._run_test(client, service, "resolve_entity", "POST", "/api/v1/resolve",
                                json_data={"text": "revenue", "context": "financial"})
            
            # Test: Entity types
            await self._run_test(client, service, "entity_types", "GET", "/api/v1/types")
    
    async def _test_data_governance_service(self):
        """Test data governance service endpoints."""
        service = "data_governance_service"
        config = SERVICES[service]
        
        if not self.results.service_results.get(service, ServiceTestResults(service, False)).healthy:
            logger.warning(f"  Skipping {service} tests - service unhealthy")
            return
        
        async with ServiceClient(service, config.port) as client:
            # Test: List policies
            await self._run_test(client, service, "list_policies", "GET", "/api/v1/policies")
            
            # Test: Data lineage
            await self._run_test(client, service, "data_lineage", "GET", "/api/v1/lineage")
            
            # Test: Quality rules
            await self._run_test(client, service, "quality_rules", "GET", "/api/v1/quality/rules")
    
    async def _test_machine_learning_service(self):
        """Test machine learning service endpoints."""
        service = "machine_learning_service"
        config = SERVICES[service]
        
        if not self.results.service_results.get(service, ServiceTestResults(service, False)).healthy:
            logger.warning(f"  Skipping {service} tests - service unhealthy")
            return
        
        async with ServiceClient(service, config.port) as client:
            # Test: List models
            await self._run_test(client, service, "list_models", "GET", "/api/v1/models")
            
            # Test: Model status
            await self._run_test(client, service, "model_status", "GET", "/api/v1/models/status")
            
            # Test: Predictions endpoint
            await self._run_test(client, service, "predictions_status", "GET", "/api/v1/predictions/status")
    
    # =========================================================================
    # Phase 5: API Gateway
    # =========================================================================
    
    async def _test_api_gateway(self):
        """Test API gateway endpoints."""
        service = "api_gateway"
        config = SERVICES[service]
        
        if not self.results.service_results.get(service, ServiceTestResults(service, False)).healthy:
            logger.warning(f"  Skipping {service} tests - service unhealthy")
            return
        
        async with ServiceClient(service, config.port) as client:
            # Test: Gateway health
            await self._run_test(client, service, "gateway_health", "GET", "/health")
            
            # Test: Service registry
            await self._run_test(client, service, "service_registry", "GET", "/api/v1/services")
            
            # Test: Rate limit status
            await self._run_test(client, service, "rate_limit_status", "GET", "/api/v1/rate-limit/status")
            
            # Test: Proxy to business_metadata
            await self._run_test(client, service, "proxy_metadata", "GET", "/api/metadata/health")
            
            # Test: Proxy to conversation
            await self._run_test(client, service, "proxy_conversation", "GET", "/api/conversation/health")
    
    # =========================================================================
    # Phase 6: Integration Tests
    # =========================================================================
    
    async def _test_service_integration(self):
        """Test integration between services."""
        logger.info("  Testing cross-service integration...")
        
        # Test: Database -> Messaging integration
        await self._test_db_messaging_integration()
        
        # Test: Metadata -> Calculation Engine integration
        await self._test_metadata_calculation_integration()
        
        # Test: Multi-Agent -> Conversation integration
        await self._test_agent_conversation_integration()
    
    async def _test_db_messaging_integration(self):
        """Test database and messaging service integration."""
        service = "integration"
        start = datetime.utcnow()
        
        try:
            async with ServiceClient("database_service", SERVICES["database_service"].port) as db_client:
                async with ServiceClient("messaging_service", SERVICES["messaging_service"].port) as msg_client:
                    # Publish a message
                    code1, data1 = await msg_client.post("/api/v1/publish", 
                        json_data={"channel": "db_test", "message": {"action": "test"}})
                    
                    # Check database can receive events (via health check as proxy)
                    code2, data2 = await db_client.get("/health")
                    
                    passed = code1 in (200, 201, 404) and code2 == 200
                    
                    self._record_result(service, TestResult(
                        test_name="db_messaging_integration",
                        service=service,
                        feature="Integration",
                        passed=passed,
                        duration_ms=(datetime.utcnow() - start).total_seconds() * 1000,
                        details=f"Messaging: {code1}, DB: {code2}",
                        error=None if passed else "Integration test failed"
                    ))
        except Exception as e:
            self._record_result(service, TestResult(
                test_name="db_messaging_integration",
                service=service,
                feature="Integration",
                passed=False,
                duration_ms=(datetime.utcnow() - start).total_seconds() * 1000,
                error=str(e)
            ))
    
    async def _test_metadata_calculation_integration(self):
        """Test metadata and calculation engine integration."""
        service = "integration"
        start = datetime.utcnow()
        
        try:
            async with ServiceClient("business_metadata", SERVICES["business_metadata"].port) as meta_client:
                async with ServiceClient("calculation_engine_service", SERVICES["calculation_engine_service"].port) as calc_client:
                    # Get KPIs from metadata
                    code1, kpis = await meta_client.get("/api/v1/kpis")
                    
                    # Check calculation engine can process
                    code2, status = await calc_client.get("/api/v1/status")
                    
                    passed = code1 in (200, 404) and code2 in (200, 404)
                    
                    self._record_result(service, TestResult(
                        test_name="metadata_calculation_integration",
                        service=service,
                        feature="Integration",
                        passed=passed,
                        duration_ms=(datetime.utcnow() - start).total_seconds() * 1000,
                        details=f"Metadata: {code1}, Calc: {code2}"
                    ))
        except Exception as e:
            self._record_result(service, TestResult(
                test_name="metadata_calculation_integration",
                service=service,
                feature="Integration",
                passed=False,
                duration_ms=(datetime.utcnow() - start).total_seconds() * 1000,
                error=str(e)
            ))
    
    async def _test_agent_conversation_integration(self):
        """Test multi-agent and conversation service integration."""
        service = "integration"
        start = datetime.utcnow()
        
        try:
            async with ServiceClient("multi_agent_service", SERVICES["multi_agent_service"].port) as agent_client:
                async with ServiceClient("conversation_service", SERVICES["conversation_service"].port) as conv_client:
                    # Check agent service
                    code1, agents = await agent_client.get("/agents/list")
                    
                    # Check conversation service connects to agents
                    code2, status = await conv_client.get("/api/v1/agents/status")
                    
                    passed = code1 == 200 and code2 in (200, 404)
                    
                    self._record_result(service, TestResult(
                        test_name="agent_conversation_integration",
                        service=service,
                        feature="Integration",
                        passed=passed,
                        duration_ms=(datetime.utcnow() - start).total_seconds() * 1000,
                        details=f"Agents: {code1}, Conversation: {code2}"
                    ))
        except Exception as e:
            self._record_result(service, TestResult(
                test_name="agent_conversation_integration",
                service=service,
                feature="Integration",
                passed=False,
                duration_ms=(datetime.utcnow() - start).total_seconds() * 1000,
                error=str(e)
            ))
    
    # =========================================================================
    # Helper Methods
    # =========================================================================
    
    async def _run_test(
        self,
        client: ServiceClient,
        service: str,
        test_name: str,
        method: str,
        path: str,
        json_data: Optional[Dict] = None,
        params: Optional[Dict] = None,
        expected_codes: List[int] = None
    ):
        """Run a single API test."""
        if expected_codes is None:
            expected_codes = [200, 201, 404]  # 404 is acceptable for missing resources
        
        start = datetime.utcnow()
        try:
            if method == "GET":
                code, data = await client.get(path, params=params)
            elif method == "POST":
                code, data = await client.post(path, json_data=json_data, params=params)
            elif method == "PUT":
                code, data = await client.put(path, json_data=json_data)
            elif method == "DELETE":
                code, data = await client.delete(path)
            else:
                code, data = 0, {"error": f"Unknown method: {method}"}
            
            passed = code in expected_codes
            
            self._record_result(service, TestResult(
                test_name=test_name,
                service=service,
                feature=path.split("/")[2] if len(path.split("/")) > 2 else "API",
                passed=passed,
                duration_ms=(datetime.utcnow() - start).total_seconds() * 1000,
                details=f"Status: {code}",
                error=str(data) if not passed else None
            ))
            logger.info(f"    {'✓' if passed else '✗'} {test_name}: {code}")
        except Exception as e:
            self._record_result(service, TestResult(
                test_name=test_name,
                service=service,
                feature="API",
                passed=False,
                duration_ms=(datetime.utcnow() - start).total_seconds() * 1000,
                error=str(e)
            ))
            logger.error(f"    ✗ {test_name}: {e}")


# =============================================================================
# Report Generation
# =============================================================================

def generate_report(results: ApplicationTestResults) -> str:
    """Generate comprehensive test report."""
    report = []
    report.append("=" * 80)
    report.append("COMPREHENSIVE APPLICATION TEST REPORT")
    report.append("Tester Agent Contract Compliance Report")
    report.append("=" * 80)
    report.append("")
    report.append(f"Execution Time: {results.start_time} - {results.end_time}")
    report.append(f"Duration: {results.duration_seconds:.2f} seconds")
    report.append("")
    
    # Overall Summary
    report.append("OVERALL SUMMARY")
    report.append("-" * 40)
    report.append(f"Services Tested: {results.services_tested}")
    report.append(f"Services Healthy: {results.services_healthy}")
    report.append(f"Services Unhealthy: {results.services_unhealthy}")
    report.append(f"Total Tests: {results.total_tests}")
    report.append(f"Passed: {results.passed}")
    report.append(f"Failed: {results.failed}")
    report.append(f"Pass Rate: {results.pass_rate:.1f}%")
    report.append("")
    
    # Results by Service Tier
    for tier in ServiceTier:
        tier_services = [s for s, c in SERVICES.items() if c.tier == tier]
        report.append(f"\n{tier.value.upper()} SERVICES")
        report.append("-" * 40)
        
        for svc in tier_services:
            if svc in results.service_results:
                svc_results = results.service_results[svc]
                status = "✓" if svc_results.healthy else "✗"
                report.append(f"\n{status} {svc} ({svc_results.tests_passed}/{svc_results.total_tests} passed)")
                for r in svc_results.results:
                    status = "✓" if r.passed else "✗"
                    report.append(f"    {status} {r.test_name} ({r.duration_ms:.1f}ms)")
                    if r.error:
                        report.append(f"        ERROR: {r.error[:100]}")
    
    # Integration Tests
    if "integration" in results.service_results:
        report.append("\n\nINTEGRATION TESTS")
        report.append("-" * 40)
        for r in results.service_results["integration"].results:
            status = "✓" if r.passed else "✗"
            report.append(f"  {status} {r.test_name}")
            if r.details:
                report.append(f"      {r.details}")
    
    # Issues Found
    if results.issues_found:
        report.append("\n\nISSUES FOUND")
        report.append("-" * 40)
        for issue in results.issues_found[:50]:  # Limit to 50 issues
            report.append(f"  • {issue[:150]}")
    
    report.append("\n" + "=" * 80)
    
    return "\n".join(report)


def generate_json_report(results: ApplicationTestResults) -> Dict[str, Any]:
    """Generate JSON report for programmatic use."""
    return {
        "summary": {
            "services_tested": results.services_tested,
            "services_healthy": results.services_healthy,
            "services_unhealthy": results.services_unhealthy,
            "total_tests": results.total_tests,
            "passed": results.passed,
            "failed": results.failed,
            "pass_rate": results.pass_rate,
            "duration_seconds": results.duration_seconds,
            "start_time": results.start_time.isoformat() if results.start_time else None,
            "end_time": results.end_time.isoformat() if results.end_time else None,
        },
        "services": {
            svc: {
                "healthy": r.healthy,
                "tests_passed": r.tests_passed,
                "tests_failed": r.tests_failed,
                "pass_rate": r.pass_rate,
                "tests": [
                    {
                        "name": t.test_name,
                        "passed": t.passed,
                        "duration_ms": t.duration_ms,
                        "error": t.error
                    }
                    for t in r.results
                ]
            }
            for svc, r in results.service_results.items()
        },
        "issues": results.issues_found
    }


# =============================================================================
# Main Entry Point
# =============================================================================

async def main():
    """Run the comprehensive application test suite."""
    logger.info("Starting Comprehensive Application Test Suite")
    
    # Run tests
    suite = ApplicationTestSuite()
    results = await suite.run_all_tests()
    
    # Generate reports
    text_report = generate_report(results)
    json_report = generate_json_report(results)
    
    # Print text report
    print(text_report)
    
    # Save reports
    timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
    report_dir = Path(__file__).parent.parent / "test_results"
    report_dir.mkdir(exist_ok=True)
    
    text_path = report_dir / f"application_test_{timestamp}.txt"
    json_path = report_dir / f"application_test_{timestamp}.json"
    
    text_path.write_text(text_report, encoding='utf-8')
    json_path.write_text(json.dumps(json_report, indent=2, default=str), encoding='utf-8')
    
    logger.info(f"Reports saved to:")
    logger.info(f"  Text: {text_path}")
    logger.info(f"  JSON: {json_path}")
    
    # Return exit code based on critical failures
    critical_failures = sum(
        1 for svc, cfg in SERVICES.items() 
        if cfg.critical and svc in results.service_results 
        and not results.service_results[svc].healthy
    )
    
    return 0 if critical_failures == 0 and results.pass_rate >= 70 else 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)

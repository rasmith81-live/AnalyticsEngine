"""
ML Handoff Workflow Test

Tests the complete ML model development workflow including:
1. Data Scientist correlation analysis and handoff to Architect
2. Architect model architecture design and handoff to Developer
3. Developer implementation and handoff to Tester/Documenter
4. Tester ML model testing workflow
5. Documenter ML documentation generation

Uses simulated data and direct agent tool invocations to verify
the handoff artifacts and collaboration patterns work correctly.
"""

import asyncio
import json
import logging
import sys
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field

# Add project root to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Test output directory
TEST_RESULTS_DIR = Path(__file__).parent.parent / "test_results"


@dataclass
class AgentContext:
    """Simulated agent context for testing."""
    session_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    value_chain_type: Optional[str] = None
    industry: Optional[str] = None
    identified_entities: List[str] = field(default_factory=list)
    artifacts: Dict[str, Any] = field(default_factory=dict)


@dataclass
class MLHandoffTestResult:
    """Result from an ML handoff test."""
    test_name: str
    agent_source: str
    agent_target: str
    handoff_type: str
    success: bool
    artifact_id: Optional[str] = None
    artifact_data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    duration_ms: float = 0.0


class MLHandoffWorkflowTester:
    """Tests ML handoff workflow between agents."""
    
    def __init__(self):
        self.context = AgentContext(
            value_chain_type="supply_chain",
            industry="B2B SaaS"
        )
        self.results: List[MLHandoffTestResult] = []
        self.summary: Dict[str, Any] = {}
    
    # =========================================================================
    # Simulated Tool Handlers (mimicking actual agent implementations)
    # =========================================================================
    
    async def simulate_data_scientist_correlation_analysis(
        self,
        kpi_ids: List[str],
        strategic_objectives: List[str]
    ) -> Dict[str, Any]:
        """Simulate Data Scientist correlation analysis."""
        correlation_result = {
            "id": f"CORR-{str(uuid.uuid4())[:8].upper()}",
            "kpi_ids": kpi_ids,
            "strategic_objectives": strategic_objectives,
            "correlation_matrix": {
                f"{kpi_ids[0]}_{kpi_ids[1]}": 0.85,
                f"{kpi_ids[0]}_{strategic_objectives[0]}": 0.72,
                f"{kpi_ids[1]}_{strategic_objectives[0]}": 0.68
            },
            "significant_correlations": [
                {
                    "pair": [kpi_ids[0], kpi_ids[1]],
                    "correlation": 0.85,
                    "p_value": 0.001,
                    "significance": "high"
                }
            ],
            "ml_opportunities": [
                {
                    "type": "predictive_model",
                    "target": kpi_ids[0],
                    "features": kpi_ids[1:],
                    "algorithm_recommendation": "gradient_boosting",
                    "confidence": 0.82
                }
            ],
            "created_at": datetime.utcnow().isoformat()
        }
        
        self.context.artifacts["correlation_analysis"] = [correlation_result]
        return correlation_result
    
    async def simulate_data_scientist_handoff_to_architect(
        self,
        correlation_analysis_id: str,
        model_type: str,
        target_variable: str,
        features: List[str]
    ) -> Dict[str, Any]:
        """Simulate Data Scientist handoff to Architect."""
        handoff = {
            "id": f"DS-ARCH-{str(uuid.uuid4())[:8].upper()}",
            "handoff_type": "data_scientist_to_architect",
            "correlation_analysis_id": correlation_analysis_id,
            "model_specification": {
                "model_type": model_type,
                "target_variable": target_variable,
                "features": features,
                "algorithm_recommendation": "gradient_boosting",
                "performance_requirements": {
                    "min_accuracy": 0.8,
                    "max_latency_ms": 100
                }
            },
            "status": "pending_architect",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "collaboration_requests" not in self.context.artifacts:
            self.context.artifacts["collaboration_requests"] = []
        self.context.artifacts["collaboration_requests"].append(handoff)
        
        return handoff
    
    async def simulate_architect_design_ml_architecture(
        self,
        model_specification_id: str,
        model_type: str,
        features: List[str]
    ) -> Dict[str, Any]:
        """Simulate Architect ML model architecture design."""
        architecture = {
            "id": f"ML-ARCH-{str(uuid.uuid4())[:8].upper()}",
            "model_specification_id": model_specification_id,
            "architecture": {
                "model_type": model_type,
                "framework": "scikit-learn",
                "layers": [
                    {"name": "feature_engineering", "type": "preprocessing"},
                    {"name": "model", "type": model_type},
                    {"name": "post_processing", "type": "calibration"}
                ],
                "feature_pipeline": {
                    "input_features": features,
                    "transformations": ["standard_scaler", "one_hot_encoder"]
                },
                "training_config": {
                    "cv_folds": 5,
                    "early_stopping": True,
                    "hyperparameter_tuning": "grid_search"
                }
            },
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "ml_architectures" not in self.context.artifacts:
            self.context.artifacts["ml_architectures"] = []
        self.context.artifacts["ml_architectures"].append(architecture)
        
        return architecture
    
    async def simulate_architect_handoff_to_developer(
        self,
        architecture_id: str,
        model_specification_id: str
    ) -> Dict[str, Any]:
        """Simulate Architect handoff to Developer."""
        handoff = {
            "id": f"ARCH-DEV-{str(uuid.uuid4())[:8].upper()}",
            "handoff_type": "architect_to_developer",
            "architecture_id": architecture_id,
            "model_specification_id": model_specification_id,
            "implementation_requirements": {
                "framework": "scikit-learn",
                "api_framework": "fastapi",
                "deployment_target": "kubernetes"
            },
            "status": "pending_developer",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "collaboration_requests" not in self.context.artifacts:
            self.context.artifacts["collaboration_requests"] = []
        self.context.artifacts["collaboration_requests"].append(handoff)
        
        return handoff
    
    async def simulate_developer_implement_model(
        self,
        model_specification_id: str,
        architecture_id: str
    ) -> Dict[str, Any]:
        """Simulate Developer ML model implementation."""
        implementation = {
            "id": f"ML-IMPL-{str(uuid.uuid4())[:8].upper()}",
            "model_specification_id": model_specification_id,
            "architecture_id": architecture_id,
            "implementation_artifacts": {
                "feature_engineering_module": "features/feature_pipeline.py",
                "training_pipeline": "training/train_model.py",
                "inference_api": "api/inference_endpoint.py",
                "test_suite": "tests/test_model.py"
            },
            "inference_endpoint": "/api/v1/models/predict",
            "status": "implementation_complete",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "ml_implementations" not in self.context.artifacts:
            self.context.artifacts["ml_implementations"] = []
        self.context.artifacts["ml_implementations"].append(implementation)
        
        return implementation
    
    async def simulate_developer_handoff_to_tester(
        self,
        model_specification_id: str,
        implementation_id: str,
        model_type: str,
        features: List[str]
    ) -> Dict[str, Any]:
        """Simulate Developer handoff to Tester."""
        handoff = {
            "id": f"DEV-TEST-{str(uuid.uuid4())[:8].upper()}",
            "handoff_type": "developer_to_tester",
            "model_specification_id": model_specification_id,
            "implementation_id": implementation_id,
            "model_type": model_type,
            "features": features,
            "inference_endpoint": "/api/v1/models/predict",
            "test_requirements": {
                "accuracy_threshold": 0.8,
                "latency_threshold_ms": 100,
                "expected_top_features": features[:3]
            },
            "status": "pending_tester",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "tester_handoffs" not in self.context.artifacts:
            self.context.artifacts["tester_handoffs"] = []
        self.context.artifacts["tester_handoffs"].append(handoff)
        
        return handoff
    
    async def simulate_developer_handoff_to_documenter(
        self,
        model_specification_id: str,
        model_name: str,
        model_purpose: str
    ) -> Dict[str, Any]:
        """Simulate Developer handoff to Documenter."""
        handoff = {
            "id": f"DEV-DOC-{str(uuid.uuid4())[:8].upper()}",
            "handoff_type": "developer_to_documenter",
            "model_specification_id": model_specification_id,
            "model_name": model_name,
            "model_purpose": model_purpose,
            "strategic_objectives": ["Reduce churn", "Increase retention"],
            "implementation_details": {
                "algorithm": "gradient_boosting",
                "framework": "scikit-learn",
                "inference_endpoint": "/api/v1/models/predict"
            },
            "status": "pending_documenter",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "documenter_handoffs" not in self.context.artifacts:
            self.context.artifacts["documenter_handoffs"] = []
        self.context.artifacts["documenter_handoffs"].append(handoff)
        
        return handoff
    
    async def simulate_tester_create_test_plan(
        self,
        model_specification_id: str,
        model_type: str,
        features: List[str]
    ) -> Dict[str, Any]:
        """Simulate Tester creating ML test plan."""
        test_plan = {
            "id": f"ML-TEST-PLAN-{str(uuid.uuid4())[:8].upper()}",
            "model_specification_id": model_specification_id,
            "model_type": model_type,
            "features": features,
            "test_cases": {
                "accuracy_tests": [
                    {"name": "Overall accuracy", "threshold": 0.8},
                    {"name": "Precision by class", "threshold": 0.75},
                    {"name": "Recall by class", "threshold": 0.75}
                ],
                "feature_importance_tests": [
                    {"name": "Top features alignment"}
                ],
                "api_tests": [
                    {"name": "Latency test", "max_ms": 100},
                    {"name": "Throughput test", "min_rps": 100}
                ]
            },
            "status": "test_plan_created",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "ml_test_plans" not in self.context.artifacts:
            self.context.artifacts["ml_test_plans"] = []
        self.context.artifacts["ml_test_plans"].append(test_plan)
        
        return test_plan
    
    async def simulate_tester_complete_testing(
        self,
        model_specification_id: str,
        test_plan_id: str
    ) -> Dict[str, Any]:
        """Simulate Tester completing ML testing."""
        completion = {
            "id": f"ML-TEST-COMPLETE-{str(uuid.uuid4())[:8].upper()}",
            "model_specification_id": model_specification_id,
            "test_plan_id": test_plan_id,
            "test_results": {
                "accuracy": 0.87,
                "precision": 0.85,
                "recall": 0.82,
                "latency_avg_ms": 45,
                "throughput_rps": 250
            },
            "issues_found": [],
            "approved_for_deployment": True,
            "status": "testing_complete",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "ml_test_completions" not in self.context.artifacts:
            self.context.artifacts["ml_test_completions"] = []
        self.context.artifacts["ml_test_completions"].append(completion)
        
        return completion
    
    async def simulate_documenter_create_documentation(
        self,
        model_specification_id: str,
        model_name: str,
        model_purpose: str
    ) -> Dict[str, Any]:
        """Simulate Documenter creating ML documentation."""
        documentation = {
            "id": f"ML-DOC-{str(uuid.uuid4())[:8].upper()}",
            "model_specification_id": model_specification_id,
            "model_name": model_name,
            "documentation": {
                "overview": f"# {model_name} Documentation\n\n## Purpose\n{model_purpose}",
                "api_docs": "## API Documentation\n\nEndpoint: POST /api/v1/models/predict",
                "feature_docs": "## Feature Documentation\n\n| Feature | Description |",
                "user_guide": f"## User Guide\n\nHow to use {model_name} predictions"
            },
            "status": "documentation_complete",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "ml_documentation" not in self.context.artifacts:
            self.context.artifacts["ml_documentation"] = []
        self.context.artifacts["ml_documentation"].append(documentation)
        
        return documentation
    
    # =========================================================================
    # Test Methods
    # =========================================================================
    
    async def test_data_scientist_to_architect_handoff(self) -> MLHandoffTestResult:
        """Test Data Scientist -> Architect handoff."""
        test_name = "DataScientist_to_Architect_Handoff"
        start_time = datetime.utcnow()
        
        try:
            # Step 1: Data Scientist performs correlation analysis
            correlation = await self.simulate_data_scientist_correlation_analysis(
                kpi_ids=["customer_churn_rate", "customer_satisfaction", "revenue_per_customer"],
                strategic_objectives=["reduce_churn", "increase_revenue"]
            )
            
            # Step 2: Data Scientist hands off to Architect
            handoff = await self.simulate_data_scientist_handoff_to_architect(
                correlation_analysis_id=correlation["id"],
                model_type="gradient_boosting",
                target_variable="customer_churn_rate",
                features=["customer_satisfaction", "revenue_per_customer"]
            )
            
            duration_ms = (datetime.utcnow() - start_time).total_seconds() * 1000
            
            # Verify handoff artifact
            assert handoff["handoff_type"] == "data_scientist_to_architect"
            assert "model_specification" in handoff
            assert handoff["status"] == "pending_architect"
            
            return MLHandoffTestResult(
                test_name=test_name,
                agent_source="DataScientist",
                agent_target="Architect",
                handoff_type="data_scientist_to_architect",
                success=True,
                artifact_id=handoff["id"],
                artifact_data=handoff,
                duration_ms=duration_ms
            )
            
        except Exception as e:
            return MLHandoffTestResult(
                test_name=test_name,
                agent_source="DataScientist",
                agent_target="Architect",
                handoff_type="data_scientist_to_architect",
                success=False,
                error=str(e)
            )
    
    async def test_architect_to_developer_handoff(self) -> MLHandoffTestResult:
        """Test Architect -> Developer handoff."""
        test_name = "Architect_to_Developer_Handoff"
        start_time = datetime.utcnow()
        
        try:
            # Step 1: Architect designs ML architecture
            architecture = await self.simulate_architect_design_ml_architecture(
                model_specification_id="MS-12345678",
                model_type="gradient_boosting",
                features=["customer_satisfaction", "revenue_per_customer"]
            )
            
            # Step 2: Architect hands off to Developer
            handoff = await self.simulate_architect_handoff_to_developer(
                architecture_id=architecture["id"],
                model_specification_id="MS-12345678"
            )
            
            duration_ms = (datetime.utcnow() - start_time).total_seconds() * 1000
            
            # Verify handoff artifact
            assert handoff["handoff_type"] == "architect_to_developer"
            assert "implementation_requirements" in handoff
            assert handoff["status"] == "pending_developer"
            
            return MLHandoffTestResult(
                test_name=test_name,
                agent_source="Architect",
                agent_target="Developer",
                handoff_type="architect_to_developer",
                success=True,
                artifact_id=handoff["id"],
                artifact_data=handoff,
                duration_ms=duration_ms
            )
            
        except Exception as e:
            return MLHandoffTestResult(
                test_name=test_name,
                agent_source="Architect",
                agent_target="Developer",
                handoff_type="architect_to_developer",
                success=False,
                error=str(e)
            )
    
    async def test_developer_to_tester_handoff(self) -> MLHandoffTestResult:
        """Test Developer -> Tester handoff."""
        test_name = "Developer_to_Tester_Handoff"
        start_time = datetime.utcnow()
        
        try:
            # Step 1: Developer implements model
            implementation = await self.simulate_developer_implement_model(
                model_specification_id="MS-12345678",
                architecture_id="ML-ARCH-12345678"
            )
            
            # Step 2: Developer hands off to Tester
            handoff = await self.simulate_developer_handoff_to_tester(
                model_specification_id="MS-12345678",
                implementation_id=implementation["id"],
                model_type="gradient_boosting",
                features=["customer_satisfaction", "revenue_per_customer"]
            )
            
            duration_ms = (datetime.utcnow() - start_time).total_seconds() * 1000
            
            # Verify handoff artifact
            assert handoff["handoff_type"] == "developer_to_tester"
            assert "test_requirements" in handoff
            assert handoff["status"] == "pending_tester"
            
            return MLHandoffTestResult(
                test_name=test_name,
                agent_source="Developer",
                agent_target="Tester",
                handoff_type="developer_to_tester",
                success=True,
                artifact_id=handoff["id"],
                artifact_data=handoff,
                duration_ms=duration_ms
            )
            
        except Exception as e:
            return MLHandoffTestResult(
                test_name=test_name,
                agent_source="Developer",
                agent_target="Tester",
                handoff_type="developer_to_tester",
                success=False,
                error=str(e)
            )
    
    async def test_developer_to_documenter_handoff(self) -> MLHandoffTestResult:
        """Test Developer -> Documenter handoff."""
        test_name = "Developer_to_Documenter_Handoff"
        start_time = datetime.utcnow()
        
        try:
            # Developer hands off to Documenter
            handoff = await self.simulate_developer_handoff_to_documenter(
                model_specification_id="MS-12345678",
                model_name="Customer Churn Predictor",
                model_purpose="Predict customer churn probability to enable proactive retention"
            )
            
            duration_ms = (datetime.utcnow() - start_time).total_seconds() * 1000
            
            # Verify handoff artifact
            assert handoff["handoff_type"] == "developer_to_documenter"
            assert "model_name" in handoff
            assert handoff["status"] == "pending_documenter"
            
            return MLHandoffTestResult(
                test_name=test_name,
                agent_source="Developer",
                agent_target="Documenter",
                handoff_type="developer_to_documenter",
                success=True,
                artifact_id=handoff["id"],
                artifact_data=handoff,
                duration_ms=duration_ms
            )
            
        except Exception as e:
            return MLHandoffTestResult(
                test_name=test_name,
                agent_source="Developer",
                agent_target="Documenter",
                handoff_type="developer_to_documenter",
                success=False,
                error=str(e)
            )
    
    async def test_tester_ml_workflow(self) -> MLHandoffTestResult:
        """Test Tester ML testing workflow."""
        test_name = "Tester_ML_Workflow"
        start_time = datetime.utcnow()
        
        try:
            # Step 1: Create test plan
            test_plan = await self.simulate_tester_create_test_plan(
                model_specification_id="MS-12345678",
                model_type="gradient_boosting",
                features=["customer_satisfaction", "revenue_per_customer"]
            )
            
            # Step 2: Complete testing
            completion = await self.simulate_tester_complete_testing(
                model_specification_id="MS-12345678",
                test_plan_id=test_plan["id"]
            )
            
            duration_ms = (datetime.utcnow() - start_time).total_seconds() * 1000
            
            # Verify test artifacts
            assert test_plan["status"] == "test_plan_created"
            assert completion["status"] == "testing_complete"
            assert completion["approved_for_deployment"] == True
            
            return MLHandoffTestResult(
                test_name=test_name,
                agent_source="Tester",
                agent_target="Stakeholders",
                handoff_type="tester_completion",
                success=True,
                artifact_id=completion["id"],
                artifact_data=completion,
                duration_ms=duration_ms
            )
            
        except Exception as e:
            return MLHandoffTestResult(
                test_name=test_name,
                agent_source="Tester",
                agent_target="Stakeholders",
                handoff_type="tester_completion",
                success=False,
                error=str(e)
            )
    
    async def test_documenter_ml_workflow(self) -> MLHandoffTestResult:
        """Test Documenter ML documentation workflow."""
        test_name = "Documenter_ML_Workflow"
        start_time = datetime.utcnow()
        
        try:
            # Create documentation
            documentation = await self.simulate_documenter_create_documentation(
                model_specification_id="MS-12345678",
                model_name="Customer Churn Predictor",
                model_purpose="Predict customer churn probability"
            )
            
            duration_ms = (datetime.utcnow() - start_time).total_seconds() * 1000
            
            # Verify documentation artifact
            assert documentation["status"] == "documentation_complete"
            assert "documentation" in documentation
            assert "overview" in documentation["documentation"]
            
            return MLHandoffTestResult(
                test_name=test_name,
                agent_source="Documenter",
                agent_target="Stakeholders",
                handoff_type="documenter_completion",
                success=True,
                artifact_id=documentation["id"],
                artifact_data=documentation,
                duration_ms=duration_ms
            )
            
        except Exception as e:
            return MLHandoffTestResult(
                test_name=test_name,
                agent_source="Documenter",
                agent_target="Stakeholders",
                handoff_type="documenter_completion",
                success=False,
                error=str(e)
            )
    
    async def test_full_ml_workflow(self) -> MLHandoffTestResult:
        """Test complete end-to-end ML handoff workflow."""
        test_name = "Full_ML_Handoff_Workflow"
        start_time = datetime.utcnow()
        
        try:
            # Reset context for clean test
            self.context = AgentContext(
                value_chain_type="supply_chain",
                industry="B2B SaaS"
            )
            
            # 1. Data Scientist correlation analysis
            correlation = await self.simulate_data_scientist_correlation_analysis(
                kpi_ids=["churn_rate", "satisfaction", "revenue"],
                strategic_objectives=["reduce_churn"]
            )
            
            # 2. Data Scientist -> Architect handoff
            ds_arch_handoff = await self.simulate_data_scientist_handoff_to_architect(
                correlation_analysis_id=correlation["id"],
                model_type="gradient_boosting",
                target_variable="churn_rate",
                features=["satisfaction", "revenue"]
            )
            
            # 3. Architect designs architecture
            architecture = await self.simulate_architect_design_ml_architecture(
                model_specification_id=ds_arch_handoff["id"],
                model_type="gradient_boosting",
                features=["satisfaction", "revenue"]
            )
            
            # 4. Architect -> Developer handoff
            arch_dev_handoff = await self.simulate_architect_handoff_to_developer(
                architecture_id=architecture["id"],
                model_specification_id=ds_arch_handoff["id"]
            )
            
            # 5. Developer implements
            implementation = await self.simulate_developer_implement_model(
                model_specification_id=ds_arch_handoff["id"],
                architecture_id=architecture["id"]
            )
            
            # 6. Developer -> Tester handoff
            dev_test_handoff = await self.simulate_developer_handoff_to_tester(
                model_specification_id=ds_arch_handoff["id"],
                implementation_id=implementation["id"],
                model_type="gradient_boosting",
                features=["satisfaction", "revenue"]
            )
            
            # 7. Developer -> Documenter handoff
            dev_doc_handoff = await self.simulate_developer_handoff_to_documenter(
                model_specification_id=ds_arch_handoff["id"],
                model_name="Churn Predictor",
                model_purpose="Predict customer churn"
            )
            
            # 8. Tester creates plan and completes testing
            test_plan = await self.simulate_tester_create_test_plan(
                model_specification_id=ds_arch_handoff["id"],
                model_type="gradient_boosting",
                features=["satisfaction", "revenue"]
            )
            test_completion = await self.simulate_tester_complete_testing(
                model_specification_id=ds_arch_handoff["id"],
                test_plan_id=test_plan["id"]
            )
            
            # 9. Documenter creates documentation
            documentation = await self.simulate_documenter_create_documentation(
                model_specification_id=ds_arch_handoff["id"],
                model_name="Churn Predictor",
                model_purpose="Predict customer churn"
            )
            
            duration_ms = (datetime.utcnow() - start_time).total_seconds() * 1000
            
            # Verify all artifacts were created
            errors = []
            if len(self.context.artifacts.get("correlation_analysis", [])) < 1:
                errors.append("Missing correlation_analysis artifact")
            if len(self.context.artifacts.get("collaboration_requests", [])) < 2:
                errors.append(f"Expected 2+ collaboration_requests, got {len(self.context.artifacts.get('collaboration_requests', []))}")
            if len(self.context.artifacts.get("ml_architectures", [])) < 1:
                errors.append("Missing ml_architectures artifact")
            if len(self.context.artifacts.get("ml_implementations", [])) < 1:
                errors.append("Missing ml_implementations artifact")
            if len(self.context.artifacts.get("tester_handoffs", [])) < 1:
                errors.append("Missing tester_handoffs artifact")
            if len(self.context.artifacts.get("documenter_handoffs", [])) < 1:
                errors.append("Missing documenter_handoffs artifact")
            if len(self.context.artifacts.get("ml_test_plans", [])) < 1:
                errors.append("Missing ml_test_plans artifact")
            if len(self.context.artifacts.get("ml_test_completions", [])) < 1:
                errors.append("Missing ml_test_completions artifact")
            if len(self.context.artifacts.get("ml_documentation", [])) < 1:
                errors.append("Missing ml_documentation artifact")
            
            if errors:
                raise AssertionError("; ".join(errors))
            
            return MLHandoffTestResult(
                test_name=test_name,
                agent_source="All Agents",
                agent_target="All Agents",
                handoff_type="full_workflow",
                success=True,
                artifact_id="FULL-WORKFLOW",
                artifact_data={
                    "total_artifacts": sum(len(v) if isinstance(v, list) else 1 for v in self.context.artifacts.values()),
                    "workflow_stages": [
                        "correlation_analysis",
                        "ds_to_architect",
                        "architecture_design",
                        "arch_to_developer",
                        "implementation",
                        "dev_to_tester",
                        "dev_to_documenter",
                        "testing",
                        "documentation"
                    ]
                },
                duration_ms=duration_ms
            )
            
        except Exception as e:
            return MLHandoffTestResult(
                test_name=test_name,
                agent_source="All Agents",
                agent_target="All Agents",
                handoff_type="full_workflow",
                success=False,
                error=str(e)
            )
    
    async def run_all_tests(self) -> None:
        """Run all ML handoff workflow tests."""
        logger.info("=" * 60)
        logger.info("ML Handoff Workflow Tests")
        logger.info("=" * 60)
        
        tests = [
            self.test_data_scientist_to_architect_handoff,
            self.test_architect_to_developer_handoff,
            self.test_developer_to_tester_handoff,
            self.test_developer_to_documenter_handoff,
            self.test_tester_ml_workflow,
            self.test_documenter_ml_workflow,
            self.test_full_ml_workflow
        ]
        
        for test in tests:
            result = await test()
            self.results.append(result)
            status = "✅ PASS" if result.success else "❌ FAIL"
            logger.info(f"{status} {result.test_name} ({result.duration_ms:.0f}ms)")
            if result.error:
                logger.error(f"   Error: {result.error}")
        
        self.generate_summary()
    
    def generate_summary(self) -> Dict[str, Any]:
        """Generate test summary."""
        total = len(self.results)
        passed = sum(1 for r in self.results if r.success)
        
        self.summary = {
            "test_run_id": f"ML-HANDOFF-TEST-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}",
            "total_tests": total,
            "passed": passed,
            "failed": total - passed,
            "success_rate": (passed / total * 100) if total > 0 else 0,
            "handoff_types_tested": list(set(r.handoff_type for r in self.results)),
            "avg_duration_ms": sum(r.duration_ms for r in self.results) / total if total > 0 else 0
        }
        
        return self.summary
    
    def save_results(self, output_dir: Path) -> str:
        """Save test results to files."""
        output_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        
        # Markdown report
        md_path = output_dir / f"ml_handoff_test_{timestamp}.md"
        
        md_content = f"""# ML Handoff Workflow Test Results

**Test Run ID:** {self.summary.get('test_run_id', 'N/A')}  
**Timestamp:** {datetime.utcnow().isoformat()}  

---

## Summary

| Metric | Value |
|--------|-------|
| Total Tests | {self.summary['total_tests']} |
| Passed | {self.summary['passed']} |
| Failed | {self.summary['failed']} |
| Success Rate | {self.summary['success_rate']:.1f}% |
| Avg Duration | {self.summary['avg_duration_ms']:.0f}ms |

## Handoff Types Tested

{chr(10).join([f"- {ht}" for ht in self.summary['handoff_types_tested']])}

---

## Test Results

"""
        for result in self.results:
            status = "✅ PASS" if result.success else "❌ FAIL"
            md_content += f"""
### {result.test_name} - {status}

- **Source Agent:** {result.agent_source}
- **Target Agent:** {result.agent_target}
- **Handoff Type:** {result.handoff_type}
- **Duration:** {result.duration_ms:.0f}ms
- **Artifact ID:** {result.artifact_id or 'N/A'}
"""
            if result.error:
                md_content += f"- **Error:** {result.error}\n"
        
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        
        # JSON report
        json_path = output_dir / f"ml_handoff_test_{timestamp}.json"
        json_data = {
            "summary": self.summary,
            "results": [
                {
                    "test_name": r.test_name,
                    "agent_source": r.agent_source,
                    "agent_target": r.agent_target,
                    "handoff_type": r.handoff_type,
                    "success": r.success,
                    "artifact_id": r.artifact_id,
                    "error": r.error,
                    "duration_ms": r.duration_ms
                }
                for r in self.results
            ]
        }
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2)
        
        logger.info(f"Results saved to: {md_path}")
        return str(md_path)


async def main():
    """Run ML handoff workflow tests."""
    tester = MLHandoffWorkflowTester()
    await tester.run_all_tests()
    
    # Print summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Total: {tester.summary['total_tests']}")
    print(f"Passed: {tester.summary['passed']}")
    print(f"Failed: {tester.summary['failed']}")
    print(f"Success Rate: {tester.summary['success_rate']:.1f}%")
    
    # Save results
    tester.save_results(TEST_RESULTS_DIR)
    
    # Return exit code
    return 0 if tester.summary['failed'] == 0 else 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)

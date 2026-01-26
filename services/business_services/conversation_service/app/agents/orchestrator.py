"""
Agent Orchestrator

Manages the lifecycle of multi-agent sessions and coordinates
the Strategy Coordinator with its sub-agents.
"""

from __future__ import annotations

import asyncio
import json
import logging
from datetime import datetime
from typing import Any, Dict, List, Optional, AsyncIterator
from uuid import uuid4

from pydantic import BaseModel, Field

from .base_agent import AgentContext, AgentMessage, AgentResponse, MessageRole
from .coordinator import StrategyCoordinator
from .sub_agents import (
    ArchitectAgent,
    BusinessAnalystAgent,
    DataAnalystAgent,
    DeveloperAgent,
    TesterAgent,
    DocumenterAgent,
    DeploymentSpecialistAgent,
    ProjectManagerAgent,
    LibrarianCuratorAgent
)
from .business_agents import (
    SalesManagerAgent,
    AccountantAgent,
    DataGovernanceSpecialistAgent,
    DataScientistAgent,
    MarketingManagerAgent,
    UIDesignerAgent,
    BusinessStrategistAgent,
    OperationsManagerAgent
)

# Import MCP client manager
from ..mcp.mcp_client_manager import MCPClientManager, MCPConfig

# Import secrets manager for secure API key retrieval
from ..secrets_manager import get_anthropic_api_key as get_anthropic_api_key_async

logger = logging.getLogger(__name__)


class OrchestratorConfig(BaseModel):
    """Configuration for the Agent Orchestrator."""
    api_key: Optional[str] = None
    parallel_execution: bool = True
    max_parallel_agents: int = 3
    session_timeout_seconds: float = 3600.0  # 1 hour
    enable_streaming: bool = True
    auto_finalize: bool = False
    enable_mcp: bool = True  # Enable MCP tool integration
    mcp_config: Optional[MCPConfig] = None  # Custom MCP configuration


class DesignSession(BaseModel):
    """A multi-agent design session."""
    id: str = Field(default_factory=lambda: str(uuid4()))
    user_id: str
    context: AgentContext
    status: str = "active"  # active, completed, failed, cancelled
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    message_count: int = 0
    artifacts_generated: List[str] = Field(default_factory=list)
    
    class Config:
        arbitrary_types_allowed = True


class AgentOrchestrator:
    """
    Orchestrates multi-agent design sessions.
    
    Manages the lifecycle of design sessions and coordinates
    the Strategy Coordinator with specialized sub-agents.
    """
    
    def __init__(self, config: Optional[OrchestratorConfig] = None):
        """
        Initialize the orchestrator.
        
        Args:
            config: Orchestrator configuration
        """
        self.config = config or OrchestratorConfig()
        self._sessions: Dict[str, DesignSession] = {}
        self._coordinator: Optional[StrategyCoordinator] = None
        self._sub_agents: Dict[str, Any] = {}
        self._mcp_manager: Optional[MCPClientManager] = None
        self._initialized = False
    
    async def initialize(self) -> None:
        """Initialize the orchestrator and all agents."""
        if self._initialized:
            return
        
        logger.info("Initializing Agent Orchestrator...")
        
        # Get API key from secure storage (with env fallback)
        api_key = self.config.api_key or await get_anthropic_api_key_async()
        
        if not api_key:
            logger.warning("ANTHROPIC_API_KEY not found in secure storage or environment")
        
        # Initialize MCP client manager if enabled
        if self.config.enable_mcp:
            try:
                mcp_config = self.config.mcp_config or MCPConfig.from_env()
                self._mcp_manager = MCPClientManager(mcp_config)
                await self._mcp_manager.initialize()
                logger.info(f"MCP Client Manager initialized with {len(self._mcp_manager.list_all_tools())} tools")
            except Exception as e:
                logger.warning(f"Failed to initialize MCP Client Manager: {e}. Agents will run without MCP tools.")
                self._mcp_manager = None
        
        # Initialize coordinator (with MCP manager)
        self._coordinator = StrategyCoordinator(api_key=api_key, mcp_manager=self._mcp_manager)
        await self._coordinator.initialize()
        
        # Initialize sub-agents (with MCP manager)
        self._sub_agents = {
            "architect": ArchitectAgent(api_key=api_key, mcp_manager=self._mcp_manager),
            "business_analyst": BusinessAnalystAgent(api_key=api_key, mcp_manager=self._mcp_manager),
            "data_analyst": DataAnalystAgent(api_key=api_key, mcp_manager=self._mcp_manager),
            "developer": DeveloperAgent(api_key=api_key, mcp_manager=self._mcp_manager),
            "tester": TesterAgent(api_key=api_key, mcp_manager=self._mcp_manager),
            "documenter": DocumenterAgent(api_key=api_key, mcp_manager=self._mcp_manager),
            "deployment_specialist": DeploymentSpecialistAgent(api_key=api_key, mcp_manager=self._mcp_manager),
            "project_manager": ProjectManagerAgent(api_key=api_key, mcp_manager=self._mcp_manager),
            "sales_manager": SalesManagerAgent(api_key=api_key, mcp_manager=self._mcp_manager),
            "accountant": AccountantAgent(api_key=api_key, mcp_manager=self._mcp_manager),
            "data_governance_specialist": DataGovernanceSpecialistAgent(api_key=api_key, mcp_manager=self._mcp_manager),
            "data_scientist": DataScientistAgent(api_key=api_key, mcp_manager=self._mcp_manager),
            "marketing_manager": MarketingManagerAgent(api_key=api_key, mcp_manager=self._mcp_manager),
            "ui_designer": UIDesignerAgent(api_key=api_key, mcp_manager=self._mcp_manager),
            "business_strategist": BusinessStrategistAgent(api_key=api_key, mcp_manager=self._mcp_manager),
            "operations_manager": OperationsManagerAgent(api_key=api_key, mcp_manager=self._mcp_manager),
            "librarian_curator": LibrarianCuratorAgent(api_key=api_key, mcp_manager=self._mcp_manager)
        }
        
        # Initialize each sub-agent
        for name, agent in self._sub_agents.items():
            await agent.initialize()
            self._coordinator.set_sub_agent(name, agent)
            logger.info(f"Initialized sub-agent: {name}")
        
        # Wire up peer-to-peer connections between sub-agents
        self._setup_peer_connections()
        
        # Configure messaging client for agents that need external service access
        self._setup_external_service_messaging()
        
        self._initialized = True
        logger.info("Agent Orchestrator initialized successfully")
    
    def _setup_peer_connections(self) -> None:
        """
        Set up peer-to-peer connections between sub-agents.
        
        This allows agents to consult each other directly without going
        through the coordinator, enabling more natural collaboration.
        """
        # Define peer connection groups - agents that should be able to talk to each other
        peer_groups = {
            # Strategic/Business group
            "business_strategist": ["business_analyst", "competitive_analyst", "operations_manager", "architect"],
            "business_analyst": ["business_strategist", "data_analyst", "architect", "operations_manager"],
            "operations_manager": ["business_strategist", "business_analyst", "data_analyst", "project_manager"],
            
            # Technical/Architecture group
            "architect": ["developer", "data_analyst", "deployment_specialist", "business_analyst"],
            "developer": ["architect", "tester", "deployment_specialist", "data_scientist"],
            "data_analyst": ["architect", "data_scientist", "business_analyst", "developer"],
            "data_scientist": ["data_analyst", "developer", "architect", "business_strategist"],
            
            # Operations/Support group
            "deployment_specialist": ["developer", "architect", "tester", "project_manager"],
            "tester": ["developer", "architect", "documenter", "deployment_specialist"],
            "documenter": ["architect", "developer", "tester", "project_manager"],
            "project_manager": ["operations_manager", "developer", "tester", "deployment_specialist"],
            
            # Domain specialists
            "ui_designer": ["developer", "architect", "business_analyst", "marketing_manager"],
            "sales_manager": ["marketing_manager", "accountant", "business_analyst", "operations_manager"],
            "marketing_manager": ["sales_manager", "data_analyst", "ui_designer", "business_strategist"],
            "accountant": ["sales_manager", "operations_manager", "data_analyst", "business_analyst"],
            "data_governance_specialist": ["architect", "data_analyst", "developer", "documenter"],
            "librarian_curator": ["architect", "business_analyst", "data_governance_specialist", "documenter"]
        }
        
        # Set up peer connections for each agent
        for agent_name, peer_names in peer_groups.items():
            if agent_name in self._sub_agents:
                agent = self._sub_agents[agent_name]
                peers = {}
                for peer_name in peer_names:
                    if peer_name in self._sub_agents:
                        peers[peer_name] = self._sub_agents[peer_name]
                
                if peers:
                    agent.set_peers(peers)
                    # Register peer communication tools
                    agent._register_peer_tools()
                    logger.debug(f"Agent {agent_name} connected to peers: {list(peers.keys())}")
    
    def _setup_external_service_messaging(self) -> None:
        """
        Configure messaging client for agents that need to call external services.
        
        Agents like data_scientist need to call the ML service, 
        architect may need to call the metadata service, etc.
        """
        # Get the messaging client from the main app context
        # This will be injected via set_messaging_client method
        from ..main import get_messaging_client
        
        try:
            messaging_client = get_messaging_client()
            if not messaging_client:
                logger.warning("Messaging client not available. External service calls will fail.")
                return
            
            # Agents that need external service access
            external_service_agents = [
                "data_scientist",      # Needs ML service
                "architect",           # Needs metadata service
                "data_analyst",        # Needs database service
                "data_governance_specialist",  # Needs metadata service
                "librarian_curator",   # Needs metadata service for ontology management
            ]
            
            for agent_name in external_service_agents:
                if agent_name in self._sub_agents:
                    self._sub_agents[agent_name].set_messaging_client(messaging_client)
                    logger.info(f"Agent {agent_name} configured for external service messaging")
                    
        except Exception as e:
            logger.warning(f"Failed to configure external service messaging: {e}")
    
    async def create_session(
        self, 
        user_id: str,
        business_description: Optional[str] = None,
        industry: Optional[str] = None
    ) -> DesignSession:
        """
        Create a new design session.
        
        Args:
            user_id: User identifier
            business_description: Initial business description
            industry: Target industry
            
        Returns:
            New DesignSession
        """
        if not self._initialized:
            await self.initialize()
        
        # Create context
        context = AgentContext(
            user_id=user_id,
            business_description=business_description or "",
            industry=industry
        )
        
        # Create session
        session = DesignSession(
            user_id=user_id,
            context=context
        )
        
        self._sessions[session.id] = session
        logger.info(f"Created design session {session.id} for user {user_id}")
        
        return session
    
    def get_session(self, session_id: str) -> Optional[DesignSession]:
        """Get a session by ID."""
        return self._sessions.get(session_id)
    
    async def process_message(
        self, 
        session_id: str, 
        message: str
    ) -> AgentResponse:
        """
        Process a user message in a design session.
        
        Args:
            session_id: Session identifier
            message: User message
            
        Returns:
            AgentResponse from the coordinator
        """
        if not self._initialized:
            await self.initialize()
        
        session = self._sessions.get(session_id)
        if not session:
            return AgentResponse(
                agent_role="coordinator",
                content="",
                success=False,
                error=f"Session {session_id} not found"
            )
        
        # Update session
        session.updated_at = datetime.utcnow()
        session.message_count += 1
        
        # Add message to context history
        session.context.conversation_history.append(
            AgentMessage(
                role=MessageRole.USER,
                content=message
            )
        )
        
        # Process with coordinator
        try:
            response = await self._coordinator.process(message, session.context)
            
            # Add response to context history
            if response.success and response.content:
                session.context.conversation_history.append(
                    AgentMessage(
                        role=MessageRole.ASSISTANT,
                        content=response.content
                    )
                )
            
            # Track generated artifacts
            for artifact_name in response.artifacts.keys():
                if artifact_name not in session.artifacts_generated:
                    session.artifacts_generated.append(artifact_name)
            
            return response
            
        except Exception as e:
            logger.error(f"Error processing message in session {session_id}: {e}")
            return AgentResponse(
                agent_role="coordinator",
                content="",
                success=False,
                error=str(e)
            )
    
    async def stream_message(
        self, 
        session_id: str, 
        message: str
    ) -> AsyncIterator[Any]:
        """
        Process a message with streaming response.
        
        Args:
            session_id: Session identifier
            message: User message
            
        Yields:
            StreamEvent objects (text chunks and activity events)
        """
        from .base_agent import StreamEvent, StreamEventType
        
        if not self._initialized:
            await self.initialize()
        
        session = self._sessions.get(session_id)
        if not session:
            yield StreamEvent(
                event_type=StreamEventType.TEXT,
                content=f"Error: Session {session_id} not found",
                source="orchestrator"
            )
            return
        
        # Update session
        session.updated_at = datetime.utcnow()
        session.message_count += 1
        
        # Add message to context history
        session.context.conversation_history.append(
            AgentMessage(
                role=MessageRole.USER,
                content=message
            )
        )
        
        # Stream from coordinator
        full_response = []
        try:
            async for event in self._coordinator.stream_process(message, session.context):
                # Pass through all events
                yield event
                # Collect text for history
                if event.event_type == StreamEventType.TEXT and event.content:
                    full_response.append(event.content)
            
            # Add complete response to history
            complete_response = "".join(full_response)
            if complete_response:
                session.context.conversation_history.append(
                    AgentMessage(
                        role=MessageRole.ASSISTANT,
                        content=complete_response
                    )
                )
            
        except Exception as e:
            logger.error(f"Error streaming message in session {session_id}: {e}")
            yield StreamEvent(
                event_type=StreamEventType.TEXT,
                content=f"\n\nError: {str(e)}",
                source="orchestrator"
            )
    
    async def run_parallel_analysis(
        self, 
        session_id: str,
        analysis_type: str = "comprehensive"
    ) -> Dict[str, AgentResponse]:
        """
        Run parallel analysis with multiple sub-agents.
        
        Args:
            session_id: Session identifier
            analysis_type: Type of analysis to run
            
        Returns:
            Dictionary of agent responses
        """
        if not self._initialized:
            await self.initialize()
        
        session = self._sessions.get(session_id)
        if not session:
            return {"error": AgentResponse(
                agent_role="orchestrator",
                content="",
                success=False,
                error=f"Session {session_id} not found"
            )}
        
        context = session.context
        
        # Define parallel tasks based on analysis type
        if analysis_type == "comprehensive":
            tasks = [
                {
                    "agent": "architect",
                    "task": f"Design a value chain structure for: {context.business_description}",
                    "additional_context": {"industry": context.industry}
                },
                {
                    "agent": "business_analyst",
                    "task": f"Identify relevant KPIs and best practices for: {context.business_description}",
                    "additional_context": {"industry": context.industry}
                },
                {
                    "agent": "developer",
                    "task": f"Prepare schema templates for: {context.business_description}",
                    "additional_context": {"entities": context.identified_entities}
                }
            ]
        elif analysis_type == "validation":
            tasks = [
                {
                    "agent": "tester",
                    "task": "Validate all generated artifacts",
                    "additional_context": {"artifacts": list(context.artifacts.keys())}
                },
                {
                    "agent": "documenter",
                    "task": "Generate documentation for the design",
                    "additional_context": {"artifacts": list(context.artifacts.keys())}
                }
            ]
        else:
            tasks = []
        
        # Run parallel delegation through coordinator
        results = await self._coordinator.run_parallel_delegation(tasks, context)
        
        # Convert to response dictionary
        responses = {}
        for i, result in enumerate(results):
            agent_name = tasks[i]["agent"] if i < len(tasks) else f"agent_{i}"
            responses[agent_name] = AgentResponse(
                agent_role=agent_name,
                content=result.get("content", ""),
                artifacts=result.get("artifacts", {}),
                success=result.get("success", False),
                error=result.get("error")
            )
        
        return responses
    
    async def finalize_session(
        self, 
        session_id: str,
        persist_artifacts: bool = True
    ) -> Dict[str, Any]:
        """
        Finalize a design session and generate all artifacts.
        
        Args:
            session_id: Session identifier
            persist_artifacts: Whether to persist artifacts to services
            
        Returns:
            Final session results with all artifacts
        """
        if not self._initialized:
            await self.initialize()
        
        session = self._sessions.get(session_id)
        if not session:
            return {
                "success": False,
                "error": f"Session {session_id} not found"
            }
        
        # Run validation
        validation_results = await self.run_parallel_analysis(session_id, "validation")
        
        # Collect all artifacts
        all_artifacts = dict(session.context.artifacts)
        
        for agent_name, response in validation_results.items():
            if response.success and response.artifacts:
                all_artifacts.update(response.artifacts)
        
        # Persist artifacts to services if requested
        persistence_results = {}
        if persist_artifacts:
            persistence_results = await self._persist_all_artifacts(session, all_artifacts)
        
        # Update session status
        session.status = "completed"
        session.updated_at = datetime.utcnow()
        
        # Build final result
        result = {
            "success": True,
            "session_id": session_id,
            "status": session.status,
            "message_count": session.message_count,
            "value_chain": {
                "name": session.context.value_chain_type or "Custom Value Chain",
                "industry": session.context.industry,
                "entities": session.context.identified_entities,
                "kpis": session.context.identified_kpis
            },
            "artifacts": all_artifacts,
            "validation": {
                agent: {
                    "success": resp.success,
                    "content": resp.content[:200] if resp.content else ""
                }
                for agent, resp in validation_results.items()
            },
            "persistence": persistence_results
        }
        
        logger.info(f"Finalized session {session_id} with {len(all_artifacts)} artifacts")
        
        return result
    
    async def _persist_all_artifacts(
        self,
        session: DesignSession,
        artifacts: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Persist all artifacts to appropriate services.
        
        Args:
            session: The design session
            artifacts: All artifacts to persist
            
        Returns:
            Persistence results by category
        """
        from .tools import get_tool
        
        results = {
            "entities": [],
            "kpis": [],
            "schemas": [],
            "relationships": [],
            "events_published": []
        }
        
        service_urls = {
            "metadata": "http://business_metadata:8000",
            "calculation": "http://calculation_engine:8000",
            "database": "http://database_service:8000",
            "messaging": "http://messaging_service:8000"
        }
        
        # Persist entities to Business Metadata Service
        persist_tool = get_tool("persist_to_metadata", service_urls)
        if persist_tool:
            for key, value in artifacts.items():
                if key.startswith("entity_") or (isinstance(value, dict) and value.get("type") == "entity"):
                    try:
                        result = await persist_tool.execute({
                            "artifact_type": "entity",
                            "artifact": value
                        })
                        results["entities"].append({
                            "key": key,
                            "success": result.success,
                            "error": result.error
                        })
                    except Exception as e:
                        logger.error(f"Failed to persist entity {key}: {e}")
                        results["entities"].append({"key": key, "success": False, "error": str(e)})
        
        # Register KPIs with Calculation Engine
        register_kpi_tool = get_tool("register_kpi_with_calculation_engine", service_urls)
        if register_kpi_tool:
            for key, value in artifacts.items():
                if key.startswith("kpi_") and isinstance(value, dict):
                    kpi_code = value.get("code", key.replace("kpi_", ""))
                    try:
                        result = await register_kpi_tool.execute({
                            "kpi_code": kpi_code,
                            "kpi_definition": value
                        })
                        results["kpis"].append({
                            "kpi_code": kpi_code,
                            "success": result.success,
                            "error": result.error
                        })
                    except Exception as e:
                        logger.error(f"Failed to register KPI {kpi_code}: {e}")
                        results["kpis"].append({"kpi_code": kpi_code, "success": False, "error": str(e)})
        
        # Execute schema migrations via Database Service
        schema_tool = get_tool("execute_schema_migration", service_urls)
        if schema_tool:
            for key, value in artifacts.items():
                if key.startswith("schema_") and isinstance(value, str):
                    schema_name = key.replace("schema_", "")
                    try:
                        result = await schema_tool.execute({
                            "schema_name": schema_name,
                            "ddl": value,
                            "is_hypertable": "create_hypertable" in value.lower()
                        })
                        results["schemas"].append({
                            "schema_name": schema_name,
                            "success": result.success,
                            "error": result.error
                        })
                    except Exception as e:
                        logger.error(f"Failed to execute schema {schema_name}: {e}")
                        results["schemas"].append({"schema_name": schema_name, "success": False, "error": str(e)})
        
        # Create relationships via metadata_relationships API
        relationship_tool = get_tool("create_relationship", service_urls)
        if relationship_tool:
            # Process bounded contexts -> value chain relationships
            if "bounded_contexts" in artifacts:
                for bc in artifacts["bounded_contexts"]:
                    if session.context.value_chain_type:
                        try:
                            result = await relationship_tool.execute({
                                "from_entity": bc.get("name", "").lower().replace(" ", "_"),
                                "to_entity": session.context.value_chain_type.lower().replace(" ", "_"),
                                "relationship_type": "belongs_to_value_chain"
                            })
                            results["relationships"].append({
                                "relationship": f"{bc.get('name')} -> {session.context.value_chain_type}",
                                "success": result.success,
                                "error": result.error
                            })
                        except Exception as e:
                            logger.error(f"Failed to create relationship: {e}")
            
            # Process KPI -> entity relationships
            for key, value in artifacts.items():
                if key.startswith("kpi_") and isinstance(value, dict):
                    kpi_code = value.get("code", key.replace("kpi_", ""))
                    for entity in value.get("required_entities", []):
                        try:
                            result = await relationship_tool.execute({
                                "from_entity": kpi_code,
                                "to_entity": entity,
                                "relationship_type": "uses"
                            })
                            results["relationships"].append({
                                "relationship": f"{kpi_code} uses {entity}",
                                "success": result.success,
                                "error": result.error
                            })
                        except Exception as e:
                            logger.error(f"Failed to create KPI-entity relationship: {e}")
        
        # Publish completion event
        event_tool = get_tool("publish_event", service_urls)
        if event_tool:
            try:
                result = await event_tool.execute({
                    "topic": "design.events",
                    "event_type": "design_session_completed",
                    "payload": {
                        "session_id": session.id,
                        "user_id": session.user_id,
                        "value_chain": session.context.value_chain_type,
                        "industry": session.context.industry,
                        "entity_count": len([k for k in artifacts if k.startswith("entity_")]),
                        "kpi_count": len([k for k in artifacts if k.startswith("kpi_")]),
                        "schema_count": len([k for k in artifacts if k.startswith("schema_")])
                    }
                })
                results["events_published"].append({
                    "event": "design_session_completed",
                    "success": result.success,
                    "error": result.error
                })
            except Exception as e:
                logger.error(f"Failed to publish completion event: {e}")
                results["events_published"].append({
                    "event": "design_session_completed",
                    "success": False,
                    "error": str(e)
                })
        
        return results
    
    async def get_session_artifacts(
        self, 
        session_id: str
    ) -> Dict[str, Any]:
        """
        Get all artifacts from a session.
        
        Args:
            session_id: Session identifier
            
        Returns:
            Dictionary of artifacts
        """
        session = self._sessions.get(session_id)
        if not session:
            return {"error": f"Session {session_id} not found"}
        
        return {
            "session_id": session_id,
            "artifacts": dict(session.context.artifacts),
            "entities": session.context.identified_entities,
            "kpis": session.context.identified_kpis
        }
    
    async def cancel_session(self, session_id: str) -> bool:
        """Cancel a design session."""
        session = self._sessions.get(session_id)
        if not session:
            return False
        
        session.status = "cancelled"
        session.updated_at = datetime.utcnow()
        logger.info(f"Cancelled session {session_id}")
        
        return True
    
    def list_sessions(self, user_id: Optional[str] = None) -> List[DesignSession]:
        """List all sessions, optionally filtered by user."""
        sessions = list(self._sessions.values())
        
        if user_id:
            sessions = [s for s in sessions if s.user_id == user_id]
        
        return sessions
    
    async def cleanup_expired_sessions(self) -> int:
        """Clean up expired sessions."""
        now = datetime.utcnow()
        expired = []
        
        for session_id, session in self._sessions.items():
            age = (now - session.updated_at).total_seconds()
            if age > self.config.session_timeout_seconds:
                expired.append(session_id)
        
        for session_id in expired:
            del self._sessions[session_id]
            logger.info(f"Cleaned up expired session {session_id}")
        
        return len(expired)


# Global orchestrator instance
_orchestrator: Optional[AgentOrchestrator] = None


async def get_orchestrator(config: Optional[OrchestratorConfig] = None) -> AgentOrchestrator:
    """Get or create the global orchestrator instance."""
    global _orchestrator
    
    if _orchestrator is None:
        _orchestrator = AgentOrchestrator(config)
        await _orchestrator.initialize()
    
    return _orchestrator

"""
Base Agent class for the Multi-Agent Framework.

Provides the foundation for all agents using the Anthropic Claude API.
Supports both Opus 4.5 (coordinator) and Sonnet 4 (sub-agents) models.
"""

from __future__ import annotations

import asyncio
import json
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional, Callable, AsyncIterator, TYPE_CHECKING
from uuid import uuid4

from pydantic import BaseModel, Field

if TYPE_CHECKING:
    from ..mcp.mcp_client_manager import MCPClientManager

logger = logging.getLogger(__name__)


class AgentRole(str, Enum):
    """Enumeration of agent roles in the multi-agent system."""
    COORDINATOR = "coordinator"
    ARCHITECT = "architect"
    BUSINESS_ANALYST = "business_analyst"
    DATA_ANALYST = "data_analyst"
    DEVELOPER = "developer"
    TESTER = "tester"
    DOCUMENTER = "documenter"
    DEPLOYMENT_SPECIALIST = "deployment_specialist"
    PROJECT_MANAGER = "project_manager"
    SALES_MANAGER = "sales_manager"
    ACCOUNTANT = "accountant"
    DATA_GOVERNANCE_SPECIALIST = "data_governance_specialist"
    DATA_SCIENTIST = "data_scientist"
    MARKETING_MANAGER = "marketing_manager"
    UI_DESIGNER = "ui_designer"
    BUSINESS_STRATEGIST = "business_strategist"
    OPERATIONS_MANAGER = "operations_manager"
    # New business-focused agents
    CUSTOMER_SUCCESS_MANAGER = "customer_success_manager"
    HR_TALENT_ANALYST = "hr_talent_analyst"
    RISK_COMPLIANCE_OFFICER = "risk_compliance_officer"
    SUPPLY_CHAIN_ANALYST = "supply_chain_analyst"
    # New technical agent
    ITIL_MANAGER = "itil_manager"
    # Analytics specialist
    MAPPING_SPECIALIST = "mapping_specialist"
    # Integration specialist
    CONNECTION_SPECIALIST = "connection_specialist"
    # Document analysis specialist
    DOCUMENT_ANALYZER = "document_analyzer"
    # Competitive intelligence specialist
    COMPETITIVE_ANALYST = "competitive_analyst"
    # Process simulation specialist
    PROCESS_SCENARIO_MODELER = "process_scenario_modeler"
    # Ontology management specialist
    LIBRARIAN_CURATOR = "librarian_curator"


class MessageRole(str, Enum):
    """Message roles for agent communication."""
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
    TOOL = "tool"


class AgentMessage(BaseModel):
    """A message in the agent conversation."""
    role: MessageRole
    content: str
    name: Optional[str] = None
    tool_call_id: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class ToolDefinition(BaseModel):
    """Definition of a tool available to an agent."""
    name: str
    description: str
    parameters: Dict[str, Any]
    handler: Optional[str] = None  # Reference to handler function


class StreamEventType(str, Enum):
    """Types of events that can be streamed."""
    TEXT = "text"
    DELEGATION = "delegation"
    TOOL_CALL = "tool_call"
    PEER_CONSULTATION = "peer_consultation"
    SYNTHESIS = "synthesis"


class StreamEvent(BaseModel):
    """Event yielded during streaming - can be text or activity."""
    event_type: StreamEventType
    content: Optional[str] = None  # For TEXT events
    source: Optional[str] = None   # For activity events
    target: Optional[str] = None   # For delegation/consultation events
    tool_name: Optional[str] = None  # For tool call events
    details: Optional[str] = None  # Additional context
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class AgentConfig(BaseModel):
    """Configuration for an agent."""
    role: AgentRole
    model: str = "claude-sonnet-4-20250514"
    max_tokens: int = 4096
    temperature: float = 0.5
    system_prompt: str = ""
    tools: List[ToolDefinition] = Field(default_factory=list)
    max_retries: int = 2
    timeout_seconds: float = 120.0
    # Cost optimization settings
    max_tool_calls: int = 5  # Maximum tool calls per task
    max_consultation_depth: int = 1  # Maximum peer consultation chain depth
    min_findings_for_ready: int = 2  # Minimum findings before signaling ready
    
    class Config:
        use_enum_values = True


class AgentResponse(BaseModel):
    """Response from an agent."""
    agent_role: AgentRole
    content: str
    tool_calls: List[Dict[str, Any]] = Field(default_factory=list)
    artifacts: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    success: bool = True
    error: Optional[str] = None
    execution_time_ms: float = 0.0


class AgentContext(BaseModel):
    """Shared context for agent sessions."""
    session_id: str = Field(default_factory=lambda: str(uuid4()))
    user_id: str = ""
    business_description: str = ""
    industry: Optional[str] = None
    value_chain_type: Optional[str] = None
    identified_entities: List[str] = Field(default_factory=list)
    identified_kpis: List[str] = Field(default_factory=list)
    conversation_history: List[AgentMessage] = Field(default_factory=list)
    artifacts: Dict[str, Any] = Field(default_factory=dict)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class BaseAgent(ABC):
    """
    Abstract base class for all agents in the multi-agent system.
    
    Provides common functionality for:
    - Claude API interaction
    - Tool execution
    - Context management
    - Error handling and retries
    """
    
    def __init__(
        self, 
        config: AgentConfig, 
        api_key: Optional[str] = None,
        mcp_manager: Optional["MCPClientManager"] = None
    ):
        """
        Initialize the agent.
        
        Args:
            config: Agent configuration
            api_key: Anthropic API key (uses env var if not provided)
            mcp_manager: Optional MCP client manager for external tools
        """
        self.config = config
        self.api_key = api_key
        self.mcp_manager = mcp_manager
        self._client = None
        self._tools: Dict[str, Callable] = {}
        self._mcp_tools: List[Dict[str, Any]] = []
        self._initialized = False
        # Peer-to-peer communication registry
        self._peers: Dict[str, "BaseAgent"] = {}
        self._collaboration_log: List[Dict[str, Any]] = []
        # External service messaging
        self._messaging_client = None
        self._pending_service_requests: Dict[str, asyncio.Future] = {}
        self._reply_channel: Optional[str] = None
        # Cost optimization tracking (reset per task)
        self._tool_call_count: int = 0
        self._consultation_depth: int = 0
        self._current_findings: List[str] = []
        self._has_signaled_ready: bool = False
        
    async def initialize(self) -> None:
        """Initialize the agent and its dependencies."""
        if self._initialized:
            return
            
        try:
            import anthropic
            self._client = anthropic.AsyncAnthropic(api_key=self.api_key)
            self._register_tools()
            
            # Register MCP tools if manager is available
            if self.mcp_manager:
                await self._register_mcp_tools()
            
            self._initialized = True
            logger.info(f"Agent {self.config.role} initialized with model {self.config.model}")
        except ImportError:
            logger.error("anthropic package not installed. Install with: pip install anthropic")
            raise
        except Exception as e:
            logger.error(f"Failed to initialize agent {self.config.role}: {e}")
            raise
    
    async def _register_mcp_tools(self) -> None:
        """Register MCP tools for this agent based on its role."""
        if not self.mcp_manager:
            return
        
        # Get role name for lookup
        role_name = self.config.role.value if hasattr(self.config.role, 'value') else str(self.config.role)
        
        # Get MCP tools for this agent's role
        mcp_tool_defs = self.mcp_manager.get_tools_for_agent(role_name)
        
        for tool_def in mcp_tool_defs:
            # Add to MCP tools list for schema building
            self._mcp_tools.append(tool_def.get_schema())
            
            # Create a handler that delegates to MCPClientManager
            tool_name = tool_def.name
            
            async def mcp_tool_handler(params: Dict[str, Any], context: AgentContext, _name=tool_name) -> Dict[str, Any]:
                """Execute MCP tool via the client manager."""
                result = await self.mcp_manager.execute_tool(_name, params)
                return result
            
            self._tools[tool_name] = mcp_tool_handler
            logger.debug(f"Registered MCP tool '{tool_name}' for agent {self.config.role}")
    
    def _register_tools(self) -> None:
        """Register tool handlers. Override in subclasses to add tools."""
        pass
    
    def register_tool(self, name: str, handler: Callable) -> None:
        """Register a tool handler."""
        self._tools[name] = handler
        logger.debug(f"Registered tool '{name}' for agent {self.config.role}")
    
    def register_peer(self, role: str, agent: "BaseAgent") -> None:
        """Register a peer agent for direct communication."""
        self._peers[role] = agent
        logger.debug(f"Agent {self.config.role} registered peer: {role}")
    
    def set_peers(self, peers: Dict[str, "BaseAgent"]) -> None:
        """Set multiple peer agents at once."""
        self._peers = peers
        logger.info(f"Agent {self.config.role} connected to {len(peers)} peers: {list(peers.keys())}")
    
    def set_messaging_client(self, messaging_client: Any) -> None:
        """Set the messaging client for external service calls."""
        self._messaging_client = messaging_client
        role_name = self.config.role.value if hasattr(self.config.role, 'value') else str(self.config.role)
        self._reply_channel = f"agent.reply.{role_name}.{uuid4().hex[:8]}"
        logger.info(f"Agent {self.config.role} configured for external service messaging")
    
    async def call_external_service(
        self,
        service_channel: str,
        request_type: str,
        payload: Dict[str, Any],
        timeout: float = 30.0
    ) -> Dict[str, Any]:
        """
        Call an external service via the messaging service.
        
        Uses request/reply pattern with correlation ID for async response tracking.
        
        Args:
            service_channel: The service's request channel (e.g., "ml.predict", "database.query")
            request_type: Type of request being made
            payload: Request payload data
            timeout: Timeout in seconds to wait for response
            
        Returns:
            Response payload from the external service
            
        Raises:
            RuntimeError: If messaging client not configured
            asyncio.TimeoutError: If no response within timeout
            Exception: If service returns an error
        """
        if not self._messaging_client:
            raise RuntimeError("Messaging client not configured. Call set_messaging_client() first.")
        
        correlation_id = str(uuid4())
        role_name = self.config.role.value if hasattr(self.config.role, 'value') else str(self.config.role)
        
        # Create future for response
        loop = asyncio.get_event_loop()
        future: asyncio.Future = loop.create_future()
        self._pending_service_requests[correlation_id] = future
        
        try:
            # Subscribe to reply channel if not already
            if self._reply_channel not in await self._messaging_client.get_active_subscriptions():
                await self._messaging_client.subscribe(
                    self._reply_channel,
                    self._handle_service_reply
                )
            
            # Build and publish request message
            request_message = {
                "correlation_id": correlation_id,
                "reply_to": self._reply_channel,
                "request_type": request_type,
                "source_agent": role_name,
                "source_service": "conversation_service",
                "timestamp": datetime.utcnow().isoformat(),
                "payload": payload
            }
            
            await self._messaging_client.publish_event(
                topic=service_channel,
                event_type=request_type,
                payload=request_message
            )
            
            logger.info(f"Agent {role_name} calling external service: {service_channel}/{request_type}")
            
            # Wait for response
            response = await asyncio.wait_for(future, timeout=timeout)
            
            # Check for error in response
            if response.get("error"):
                raise Exception(f"External service error: {response['error']}")
            
            logger.info(f"Agent {role_name} received response from {service_channel}")
            return response.get("payload", response)
            
        except asyncio.TimeoutError:
            logger.error(f"Agent {role_name} timeout calling {service_channel}/{request_type}")
            raise
        finally:
            self._pending_service_requests.pop(correlation_id, None)
    
    async def _handle_service_reply(self, message: Dict[str, Any]) -> None:
        """Handle reply messages from external services."""
        correlation_id = message.get("correlation_id")
        
        if correlation_id and correlation_id in self._pending_service_requests:
            future = self._pending_service_requests[correlation_id]
            if not future.done():
                future.set_result(message)
                logger.debug(f"Received reply for correlation_id: {correlation_id}")
    
    def _reset_task_tracking(self) -> None:
        """Reset per-task tracking variables for cost optimization."""
        self._tool_call_count = 0
        self._current_findings = []
        self._has_signaled_ready = False
        # Note: _consultation_depth is managed by the caller
    
    def _should_early_exit(self) -> bool:
        """Check if agent should exit early based on cost optimization rules."""
        # Exit if we've signaled ready
        if self._has_signaled_ready:
            return True
        # Exit if we've hit max tool calls
        if self._tool_call_count >= self.config.max_tool_calls:
            logger.info(f"Agent {self.config.role} reached max_tool_calls ({self.config.max_tool_calls})")
            return True
        return False
    
    async def _consult_peer(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Consult a peer agent directly for their expertise."""
        peer_role = tool_input.get("peer_role", "")
        question = tool_input.get("question", "")
        context_summary = tool_input.get("context_summary", "")
        
        # Check consultation depth limit
        if self._consultation_depth >= self.config.max_consultation_depth:
            logger.info(f"Agent {self.config.role} skipping peer consultation - max depth ({self.config.max_consultation_depth}) reached")
            return {
                "success": False,
                "skipped": True,
                "reason": f"Maximum consultation depth ({self.config.max_consultation_depth}) reached. Provide your best analysis based on available information.",
                "suggestion": "Proceed with your current findings without further peer consultation."
            }
        
        if peer_role not in self._peers:
            available = list(self._peers.keys())
            return {
                "success": False,
                "error": f"Peer '{peer_role}' not available. Available peers: {available}"
            }
        
        peer_agent = self._peers[peer_role]
        
        # Build consultation message with depth-aware instructions
        consultation_msg = f"""A peer agent ({self.config.role}) is consulting you for your expertise.

**Question**: {question}

**Context from consulting agent**: {context_summary}

**IMPORTANT**: Provide a concise, direct response. Do NOT consult additional peers - give your expert opinion based on your knowledge."""
        
        try:
            # Ensure peer is initialized
            if not peer_agent._initialized:
                await peer_agent.initialize()
            
            # Set peer's consultation depth to prevent recursive chains
            peer_agent._consultation_depth = self._consultation_depth + 1
            peer_agent._reset_task_tracking()
            
            # Process through peer agent
            response = await peer_agent.process(consultation_msg, context)
            
            # Log the collaboration
            collaboration_record = {
                "from_agent": str(self.config.role),
                "to_agent": peer_role,
                "question": question,
                "response_summary": response.content[:500] if response.content else "",
                "success": response.success,
                "timestamp": datetime.utcnow().isoformat()
            }
            self._collaboration_log.append(collaboration_record)
            
            # Store in context for coordinator visibility
            if "peer_collaborations" not in context.artifacts:
                context.artifacts["peer_collaborations"] = []
            context.artifacts["peer_collaborations"].append(collaboration_record)
            
            logger.info(f"Peer consultation: {self.config.role} → {peer_role} (success: {response.success})")
            
            return {
                "success": response.success,
                "peer_agent": peer_role,
                "response": response.content,
                "artifacts": response.artifacts,
                "collaboration_id": collaboration_record["timestamp"]
            }
        except Exception as e:
            logger.error(f"Peer consultation failed: {self.config.role} → {peer_role}: {e}")
            return {
                "success": False,
                "peer_agent": peer_role,
                "error": str(e)
            }
    
    async def _signal_ready_for_coordinator(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Signal that this agent has completed its work and peer consultations."""
        summary = tool_input.get("summary", "")
        key_findings = tool_input.get("key_findings", [])
        peers_consulted = tool_input.get("peers_consulted", [])
        recommendations = tool_input.get("recommendations", [])
        
        # Mark as signaled ready for early exit
        self._has_signaled_ready = True
        self._current_findings.extend(key_findings)
        
        ready_signal = {
            "agent": str(self.config.role),
            "status": "ready_for_synthesis",
            "summary": summary,
            "key_findings": key_findings,
            "peers_consulted": peers_consulted,
            "recommendations": recommendations,
            "collaboration_count": len(self._collaboration_log),
            "tool_calls_used": self._tool_call_count,
            "timestamp": datetime.utcnow().isoformat()
        }
        
        # Store in context for coordinator to pick up
        if "agent_ready_signals" not in context.artifacts:
            context.artifacts["agent_ready_signals"] = []
        context.artifacts["agent_ready_signals"].append(ready_signal)
        
        logger.info(f"Agent {self.config.role} signaled ready - consulted {len(peers_consulted)} peers, {len(key_findings)} findings, {self._tool_call_count} tool calls")
        
        return {
            "success": True,
            "signal": ready_signal,
            "message": "Your findings have been recorded. The coordinator will synthesize results from all agents."
        }
    
    def get_peer_tools(self) -> List[ToolDefinition]:
        """Get tool definitions for peer-to-peer communication."""
        peer_list = list(self._peers.keys()) if self._peers else ["No peers connected yet"]
        
        return [
            ToolDefinition(
                name="consult_peer",
                description=f"Consult a peer agent directly for their expertise. Available peers: {peer_list}. Use this to collaborate with other specialists before finalizing your response.",
                parameters={
                    "type": "object",
                    "properties": {
                        "peer_role": {
                            "type": "string",
                            "description": f"The role of the peer agent to consult. Available: {peer_list}"
                        },
                        "question": {
                            "type": "string",
                            "description": "The specific question or request for the peer agent"
                        },
                        "context_summary": {
                            "type": "string",
                            "description": "Brief summary of your current analysis to provide context"
                        }
                    },
                    "required": ["peer_role", "question"]
                }
            ),
            ToolDefinition(
                name="signal_ready_for_coordinator",
                description="Signal that you have completed your analysis and any peer consultations. Call this AFTER you have gathered all needed information from peers. The coordinator will then synthesize all agent results.",
                parameters={
                    "type": "object",
                    "properties": {
                        "summary": {
                            "type": "string",
                            "description": "Summary of your complete analysis"
                        },
                        "key_findings": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of key findings from your analysis"
                        },
                        "peers_consulted": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of peer agents you consulted"
                        },
                        "recommendations": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Your recommendations based on analysis"
                        }
                    },
                    "required": ["summary", "key_findings"]
                }
            )
        ]
    
    def _register_peer_tools(self) -> None:
        """Register the peer communication tool handlers."""
        self.register_tool("consult_peer", self._consult_peer)
        self.register_tool("signal_ready_for_coordinator", self._signal_ready_for_coordinator)
    
    @abstractmethod
    def get_system_prompt(self, context: AgentContext) -> str:
        """
        Get the system prompt for this agent.
        
        Args:
            context: Current agent context
            
        Returns:
            System prompt string
        """
        pass
    
    def _build_messages(
        self, 
        user_message: str, 
        context: AgentContext
    ) -> List[Dict[str, Any]]:
        """Build the message list for the API call."""
        messages = []
        
        # Add conversation history (last N messages)
        history_limit = 10
        for msg in context.conversation_history[-history_limit:]:
            # Skip messages with empty content (Claude API requires non-empty content)
            if not msg.content or not msg.content.strip():
                continue
            # Handle both enum and string roles
            role = msg.role.value if hasattr(msg.role, 'value') else msg.role
            messages.append({
                "role": role,
                "content": msg.content
            })
        
        # Add current user message
        messages.append({
            "role": "user",
            "content": user_message
        })
        
        return messages
    
    def _build_tools_schema(self) -> List[Dict[str, Any]]:
        """Build the tools schema for the API call."""
        tools = []
        
        # Add configured tools
        for tool_def in self.config.tools:
            tools.append({
                "name": tool_def.name,
                "description": tool_def.description,
                "input_schema": tool_def.parameters
            })
        
        # Add MCP tools
        for mcp_tool in self._mcp_tools:
            tools.append(mcp_tool)
        
        # Add peer communication tools if peers are connected
        if self._peers:
            for peer_tool in self.get_peer_tools():
                tools.append({
                    "name": peer_tool.name,
                    "description": peer_tool.description,
                    "input_schema": peer_tool.parameters
                })
        
        role_name = self.config.role.value if hasattr(self.config.role, 'value') else self.config.role
        logger.info(f"Agent {role_name} built {len(tools)} tools: {[t['name'] for t in tools[:5]]}...")
        return tools
    
    async def _execute_tool(
        self, 
        tool_name: str, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Any:
        """Execute a tool and return the result."""
        # Check both _tools and _tool_handlers for backwards compatibility
        handler = None
        if tool_name in self._tools:
            handler = self._tools[tool_name]
        elif hasattr(self, '_tool_handlers') and tool_name in self._tool_handlers:
            handler = self._tool_handlers[tool_name]
        
        if handler is None:
            raise ValueError(f"Unknown tool: {tool_name}")
        
        # Check if handler is async
        if asyncio.iscoroutinefunction(handler):
            return await handler(tool_input, context)
        else:
            return handler(tool_input, context)
    
    async def process(
        self, 
        message: str, 
        context: AgentContext
    ) -> AgentResponse:
        """
        Process a message and return a response.
        
        Args:
            message: User message to process
            context: Current agent context
            
        Returns:
            AgentResponse with results
        """
        if not self._initialized:
            await self.initialize()
        
        # Reset task tracking for new task (unless we're a consulted peer)
        if self._consultation_depth == 0:
            self._reset_task_tracking()
        
        start_time = datetime.utcnow()
        
        try:
            # Build request with cost optimization hints in system prompt
            system_prompt = self.get_system_prompt(context)
            
            # Add cost optimization instructions
            cost_hint = f"""

**EFFICIENCY GUIDELINES**:
- Be concise and direct in your analysis
- Limit to {self.config.max_tool_calls} tool calls maximum
- Signal ready after gathering {self.config.min_findings_for_ready}+ key findings
- If you've been consulted by a peer, provide direct expertise without consulting others"""
            
            system_prompt = system_prompt + cost_hint
            
            messages = self._build_messages(message, context)
            tools = self._build_tools_schema()
            
            # Make API call
            request_params = {
                "model": self.config.model,
                "max_tokens": self.config.max_tokens,
                "temperature": self.config.temperature,
                "system": system_prompt,
                "messages": messages
            }
            
            if tools:
                request_params["tools"] = tools
            
            response = await self._client.messages.create(**request_params)
            
            role_name = self.config.role.value if hasattr(self.config.role, 'value') else self.config.role
            logger.info(f"Agent {role_name} API response - stop_reason: {response.stop_reason}, content blocks: {len(response.content)}")
            
            # Process response with continuation loop for tool results
            content_parts = []
            tool_calls = []
            artifacts = {}
            all_messages = messages.copy()
            max_iterations = 8  # Allow more iterations for complex multi-tool responses
            iteration = 0
            
            while iteration < max_iterations:
                iteration += 1
                tool_results = []
                
                # Check for early exit before processing more tool calls
                if self._should_early_exit():
                    logger.info(f"Agent {role_name} early exit triggered after {self._tool_call_count} tool calls")
                    break
                
                for block in response.content:
                    if block.type == "text":
                        content_parts.append(block.text)
                    elif block.type == "tool_use":
                        # Track tool call count
                        self._tool_call_count += 1
                        
                        # Check if we've exceeded max tool calls
                        if self._tool_call_count > self.config.max_tool_calls:
                            logger.info(f"Agent {role_name} reached max_tool_calls limit ({self.config.max_tool_calls}), skipping: {block.name}")
                            tool_results.append({
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": json.dumps({
                                    "skipped": True,
                                    "reason": f"Tool call limit ({self.config.max_tool_calls}) reached. Please synthesize your findings and signal ready."
                                })
                            })
                            continue
                        
                        logger.info(f"Tool call {self._tool_call_count}/{self.config.max_tool_calls}: {block.name}")
                        tool_calls.append({
                            "id": block.id,
                            "name": block.name,
                            "input": block.input
                        })
                        
                        # Execute tool
                        try:
                            logger.info(f"Executing tool: {block.name}")
                            result = await self._execute_tool(
                                block.name, 
                                block.input, 
                                context
                            )
                            logger.info(f"Tool {block.name} executed successfully")
                            artifacts[block.name] = result
                            tool_results.append({
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": json.dumps(result) if isinstance(result, dict) else str(result)
                            })
                        except Exception as e:
                            logger.error(f"Tool execution failed for {block.name}: {e}")
                            artifacts[block.name] = {"error": str(e)}
                            tool_results.append({
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": json.dumps({"error": str(e)}),
                                "is_error": True
                            })
                
                # If no tools were called or stop_reason is end_turn, we're done
                if response.stop_reason != "tool_use" or not tool_results:
                    break
                
                # Check for early exit after tool execution
                if self._should_early_exit():
                    logger.info(f"Agent {role_name} early exit after signaling ready")
                    break
                
                # Continue conversation with tool results
                logger.info(f"Continuing conversation with {len(tool_results)} tool results")
                
                # Add assistant response and tool results to messages
                assistant_content = []
                for b in response.content:
                    if b.type == "tool_use":
                        assistant_content.append({
                            "type": "tool_use",
                            "id": b.id,
                            "name": b.name,
                            "input": b.input
                        })
                    elif b.type == "text":
                        assistant_content.append({
                            "type": "text",
                            "text": b.text
                        })
                all_messages.append({
                    "role": "assistant",
                    "content": assistant_content
                })
                all_messages.append({
                    "role": "user",
                    "content": tool_results
                })
                
                # Make continuation request
                request_params["messages"] = all_messages
                response = await self._client.messages.create(**request_params)
                logger.info(f"Agent {role_name} continuation response - stop_reason: {response.stop_reason}, content blocks: {len(response.content)}")
            
            # Check if we hit max iterations without getting a final response
            if iteration >= max_iterations and response.stop_reason == "tool_use":
                logger.warning(f"Agent {role_name} hit max iterations ({max_iterations}) - synthesizing response from artifacts")
                # Create a summary from collected artifacts
                if artifacts and not content_parts:
                    artifact_summary = f"Completed {len(tool_calls)} tool operations with results in artifacts."
                    content_parts.append(artifact_summary)
            
            # Calculate execution time
            execution_time = (datetime.utcnow() - start_time).total_seconds() * 1000
            
            # If no text content was generated, create summary from artifacts
            final_content = "\n".join(content_parts)
            if not final_content and artifacts:
                final_content = f"Analysis complete. Generated {len(artifacts)} artifact(s): {', '.join(artifacts.keys())}"
            
            return AgentResponse(
                agent_role=self.config.role,
                content=final_content,
                tool_calls=tool_calls,
                artifacts=artifacts,
                metadata={
                    "model": self.config.model,
                    "stop_reason": response.stop_reason,
                    "usage": {
                        "input_tokens": response.usage.input_tokens,
                        "output_tokens": response.usage.output_tokens
                    }
                },
                success=True,
                execution_time_ms=execution_time
            )
            
        except Exception as e:
            import traceback
            execution_time = (datetime.utcnow() - start_time).total_seconds() * 1000
            logger.error(f"Agent {self.config.role} processing failed: {e}\n{traceback.format_exc()}")
            
            return AgentResponse(
                agent_role=self.config.role,
                content="",
                success=False,
                error=str(e),
                execution_time_ms=execution_time
            )
    
    async def stream_process(
        self, 
        message: str, 
        context: AgentContext
    ) -> AsyncIterator[StreamEvent]:
        """
        Process a message with streaming response.
        
        Handles tool calls by executing them and continuing until a text response is ready.
        Yields StreamEvent objects for both text and activity tracking.
        
        Args:
            message: User message to process
            context: Current agent context
            
        Yields:
            StreamEvent objects (text chunks and activity events)
        """
        if not self._initialized:
            await self.initialize()
        
        try:
            system_prompt = self.get_system_prompt(context)
            messages = self._build_messages(message, context)
            tools = self._build_tools_schema()
            
            role_name = self.config.role.value if hasattr(self.config.role, 'value') else self.config.role
            
            # Reset task tracking for new message
            self._reset_task_tracking()
            
            request_params = {
                "model": self.config.model,
                "max_tokens": self.config.max_tokens,
                "temperature": self.config.temperature,
                "system": system_prompt,
                "messages": messages
            }
            
            if tools:
                request_params["tools"] = tools
            
            all_messages = messages.copy()
            max_iterations = 8
            iteration = 0
            
            # Process tool calls until we get a text response
            while iteration < max_iterations:
                iteration += 1
                
                # Make non-streaming call to check for tool use
                response = await self._client.messages.create(**request_params)
                
                logger.info(f"Agent {role_name} stream iteration {iteration} - stop_reason: {response.stop_reason}")
                
                # If no tool use, stream the final response
                if response.stop_reason != "tool_use":
                    # Extract and yield any text from this response
                    for block in response.content:
                        if block.type == "text":
                            yield StreamEvent(
                                event_type=StreamEventType.TEXT,
                                content=block.text,
                                source=role_name
                            )
                    break
                
                # Handle tool calls
                tool_results = []
                text_parts = []
                
                for block in response.content:
                    if block.type == "text":
                        text_parts.append(block.text)
                    elif block.type == "tool_use":
                        self._tool_call_count += 1
                        
                        if self._tool_call_count > self.config.max_tool_calls:
                            logger.info(f"Agent {role_name} reached max_tool_calls limit")
                            tool_results.append({
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": json.dumps({
                                    "skipped": True,
                                    "reason": f"Tool call limit reached. Please respond now."
                                })
                            })
                            continue
                        
                        # Emit activity event for delegation tools
                        if block.name.startswith("delegate_to_"):
                            target_agent = block.name.replace("delegate_to_", "")
                            yield StreamEvent(
                                event_type=StreamEventType.DELEGATION,
                                source=role_name,
                                target=target_agent,
                                details=block.input.get("task", "")[:100] if isinstance(block.input, dict) else ""
                            )
                        elif block.name == "consult_peer":
                            peer_name = block.input.get("peer_name", "unknown") if isinstance(block.input, dict) else "unknown"
                            yield StreamEvent(
                                event_type=StreamEventType.PEER_CONSULTATION,
                                source=role_name,
                                target=peer_name,
                                details=block.input.get("question", "")[:100] if isinstance(block.input, dict) else ""
                            )
                        else:
                            yield StreamEvent(
                                event_type=StreamEventType.TOOL_CALL,
                                source=role_name,
                                tool_name=block.name,
                                details=str(block.input)[:100] if block.input else ""
                            )
                        
                        logger.info(f"Stream executing tool: {block.name}")
                        try:
                            result = await self._execute_tool(block.name, block.input, context)
                            logger.info(f"Stream tool {block.name} executed successfully")
                            tool_results.append({
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": json.dumps(result) if isinstance(result, dict) else str(result)
                            })
                        except Exception as e:
                            logger.error(f"Stream tool execution failed for {block.name}: {e}")
                            tool_results.append({
                                "type": "tool_result",
                                "tool_use_id": block.id,
                                "content": json.dumps({"error": str(e)}),
                                "is_error": True
                            })
                
                # Yield any intermediate text
                if text_parts:
                    for text in text_parts:
                        yield StreamEvent(
                            event_type=StreamEventType.TEXT,
                            content=text,
                            source=role_name
                        )
                
                # Check for early exit
                if self._should_early_exit():
                    logger.info(f"Agent {role_name} early exit in stream")
                    break
                
                if not tool_results:
                    break
                
                # Build continuation messages
                assistant_content = []
                for b in response.content:
                    if b.type == "tool_use":
                        assistant_content.append({
                            "type": "tool_use",
                            "id": b.id,
                            "name": b.name,
                            "input": b.input
                        })
                    elif b.type == "text":
                        assistant_content.append({
                            "type": "text",
                            "text": b.text
                        })
                
                all_messages.append({"role": "assistant", "content": assistant_content})
                all_messages.append({"role": "user", "content": tool_results})
                
                # Update request for next iteration
                request_params["messages"] = all_messages
                    
        except Exception as e:
            logger.error(f"Agent {self.config.role} streaming failed: {e}")
            yield StreamEvent(
                event_type=StreamEventType.TEXT,
                content=f"Error: {str(e)}",
                source=role_name if 'role_name' in dir() else "unknown"
            )

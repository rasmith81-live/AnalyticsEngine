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
from typing import Any, Dict, List, Optional, Callable, AsyncIterator
from uuid import uuid4

from pydantic import BaseModel, Field

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
    
    def __init__(self, config: AgentConfig, api_key: Optional[str] = None):
        """
        Initialize the agent.
        
        Args:
            config: Agent configuration
            api_key: Anthropic API key (uses env var if not provided)
        """
        self.config = config
        self.api_key = api_key
        self._client = None
        self._tools: Dict[str, Callable] = {}
        self._initialized = False
        
    async def initialize(self) -> None:
        """Initialize the agent and its dependencies."""
        if self._initialized:
            return
            
        try:
            import anthropic
            self._client = anthropic.AsyncAnthropic(api_key=self.api_key)
            self._register_tools()
            self._initialized = True
            logger.info(f"Agent {self.config.role} initialized with model {self.config.model}")
        except ImportError:
            logger.error("anthropic package not installed. Install with: pip install anthropic")
            raise
        except Exception as e:
            logger.error(f"Failed to initialize agent {self.config.role}: {e}")
            raise
    
    def _register_tools(self) -> None:
        """Register tool handlers. Override in subclasses to add tools."""
        pass
    
    def register_tool(self, name: str, handler: Callable) -> None:
        """Register a tool handler."""
        self._tools[name] = handler
        logger.debug(f"Registered tool '{name}' for agent {self.config.role}")
    
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
            messages.append({
                "role": msg.role.value,
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
        for tool_def in self.config.tools:
            tools.append({
                "name": tool_def.name,
                "description": tool_def.description,
                "input_schema": tool_def.parameters
            })
        return tools
    
    async def _execute_tool(
        self, 
        tool_name: str, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Any:
        """Execute a tool and return the result."""
        if tool_name not in self._tools:
            raise ValueError(f"Unknown tool: {tool_name}")
        
        handler = self._tools[tool_name]
        
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
        
        start_time = datetime.utcnow()
        
        try:
            # Build request
            system_prompt = self.get_system_prompt(context)
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
            
            # Process response
            content_parts = []
            tool_calls = []
            artifacts = {}
            
            for block in response.content:
                if block.type == "text":
                    content_parts.append(block.text)
                elif block.type == "tool_use":
                    tool_calls.append({
                        "id": block.id,
                        "name": block.name,
                        "input": block.input
                    })
                    
                    # Execute tool
                    try:
                        result = await self._execute_tool(
                            block.name, 
                            block.input, 
                            context
                        )
                        artifacts[block.name] = result
                    except Exception as e:
                        logger.error(f"Tool execution failed: {e}")
                        artifacts[block.name] = {"error": str(e)}
            
            # Calculate execution time
            execution_time = (datetime.utcnow() - start_time).total_seconds() * 1000
            
            return AgentResponse(
                agent_role=self.config.role,
                content="\n".join(content_parts),
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
            execution_time = (datetime.utcnow() - start_time).total_seconds() * 1000
            logger.error(f"Agent {self.config.role} processing failed: {e}")
            
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
    ) -> AsyncIterator[str]:
        """
        Process a message with streaming response.
        
        Args:
            message: User message to process
            context: Current agent context
            
        Yields:
            Response text chunks
        """
        if not self._initialized:
            await self.initialize()
        
        try:
            system_prompt = self.get_system_prompt(context)
            messages = self._build_messages(message, context)
            tools = self._build_tools_schema()
            
            request_params = {
                "model": self.config.model,
                "max_tokens": self.config.max_tokens,
                "temperature": self.config.temperature,
                "system": system_prompt,
                "messages": messages
            }
            
            if tools:
                request_params["tools"] = tools
            
            async with self._client.messages.stream(**request_params) as stream:
                async for text in stream.text_stream:
                    yield text
                    
        except Exception as e:
            logger.error(f"Agent {self.config.role} streaming failed: {e}")
            yield f"Error: {str(e)}"

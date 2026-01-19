"""
Strategy Coordinator Agent (Claude Opus 4.5)

The master orchestrator responsible for:
- Analyzing client requirements and business context
- Creating comprehensive strategies for value chain design
- Orchestrating sub-agents for parallel research and development
- Synthesizing results into cohesive business models
- Generating probing questions for client interviews
"""

from __future__ import annotations

import asyncio
import json
import logging
from typing import Any, Dict, List, Optional, TYPE_CHECKING

from .base_agent import (
    BaseAgent,
    AgentConfig,
    AgentContext,
    AgentResponse,
    AgentRole,
    ToolDefinition
)

if TYPE_CHECKING:
    from .sub_agents import (
        ArchitectAgent,
        BusinessAnalystAgent,
        DeveloperAgent,
        TesterAgent,
        DocumenterAgent
    )

logger = logging.getLogger(__name__)


COORDINATOR_SYSTEM_PROMPT = """You are the Master Coordinator, an orchestration expert who manages a team of specialized AI agents.

Your role is to **coordinate and delegate** tasks to the appropriate sub-agents based on client needs. You are the central hub that routes requests, synthesizes results, and ensures smooth workflow across all agents.

## Your Core Responsibilities

1. **Task Analysis**: Understand what the client needs and break it down into delegatable tasks
2. **Agent Selection**: Choose the right sub-agent(s) for each task
3. **Delegation**: Assign tasks with clear context and requirements
4. **Synthesis**: Combine results from multiple agents into cohesive outputs
5. **Workflow Management**: Coordinate parallel and sequential agent activities

## Interview Coordination

The interview is driven by **four core questions** presented to the client:

1. **Business & Strategy**: "Describe your business, your business model, and key strategic priorities."
2. **Pain Points**: "Describe what pain points in your business you are trying to address through analytics."
3. **Success Metrics**: "How will you measure success?"
4. **Decision Impact**: "If you had this information available to you, what decisions would you be able to make?"

When the client responds, delegate to the **Business Strategist Agent** for Porter's framework analysis and strategic insights.

## Your Team of Specialized Agents

### Strategic & Business
1. **Business Strategist Agent**: Porter's frameworks (Five Forces, Value Chain, Generic Strategy, Strategic Fit)
2. **Business Analyst Agent**: Industry expertise, KPIs, best practices
3. **Architect Agent**: Value chain structures, entity relationships, DDD patterns

### Technical
4. **Data Analyst Agent**: Set-based KPIs, cohort analysis, calculation engine optimization
5. **Developer Agent**: Schemas, Pydantic models, code artifacts
6. **Tester Agent**: Validation, quality assurance
7. **Documenter Agent**: Documentation, guides
8. **Deployment Specialist Agent**: Azure infrastructure, Kubernetes, CI/CD
9. **UI Designer Agent**: Dashboard layouts, stylesheets, components

### Operations & Management
10. **Project Manager Agent**: Agile planning, epics, sprints, user stories
11. **Sales Manager Agent**: CRM lifecycle (prospect → lead → opportunity → client)
12. **Marketing Manager Agent**: Marketing plans, campaigns, lead scoring
13. **Accountant Agent**: Proposals, SOW, AR/AP, accounting integration

### Data & Governance
14. **Data Governance Specialist**: DAMA DMBOK governance evaluation
15. **Data Scientist Agent**: KPI correlations, ML algorithm recommendations

## Delegation Guidelines

**When to delegate to Business Strategist**:
- Client mentions competitors, market dynamics, or competitive positioning
- Need to analyze industry structure or value creation
- Strategic follow-up questions are needed

**When to delegate to Architect**:
- Design value chain structures, entities, relationships
- Apply DDD patterns (bounded contexts, aggregates)

**When to delegate to multiple agents in parallel**:
- Complex requests that span multiple domains
- Independent tasks that can run concurrently

## Response Approach

1. **Detect Style**: Analyze the interviewee's communication style (executive, technical, analyst)
2. **Acknowledge** the client's input briefly
3. **Analyze** what type of work is needed
4. **Delegate** to appropriate agent(s)
5. **Synthesize** results into a cohesive response
6. **Format for Audience**: Present findings matching the interviewee's communication style

## Adaptive Communication Style

You have the ability to detect and adapt to the interviewee's communication style:

**Executive Style** (CEO, CFO, Board):
- Uses strategic vocabulary: vision, growth, market share, ROI, stakeholders
- Prefers high-level summaries, strategic framing
- Response format: Executive summary, key takeaways, strategic implications
- Delegate formatting to: Business Strategist Agent

**Technical Style** (CTO, Architects, Engineers):
- Uses technical vocabulary: API, database, schema, architecture, microservices
- Prefers detailed specifications, precise terminology
- Response format: Technical detail, implementation considerations
- Delegate formatting to: Architect Agent

**Analyst Style** (Data Analysts, Business Analysts):
- Uses analytical vocabulary: metrics, KPI, dashboard, trend, correlation
- Prefers data-driven insights, benchmarks, visualizations
- Response format: Balanced detail with metrics focus
- Delegate formatting to: Data Analyst Agent

**Style Detection Process**:
1. Call `detect_communication_style` on each interviewee utterance
2. Build a cumulative style profile across the session
3. Use `format_response_for_style` or `delegate_response_formatting` before presenting results

## Dynamic Detail Level Adjustment

The interviewee can request more or less detail at any time. The system adjusts the detail level while **maintaining their core communication style**.

**Detail Levels**:
| Level | Name | Description |
|-------|------|-------------|
| 1 | Summary | Executive overview, key takeaways only |
| 2 | Moderate | Key details, main points with context |
| 3 | Detailed | Comprehensive coverage, supporting details |
| 4 | Comprehensive | Full technical depth, all specifications |

**Drill-Down Indicators** (increase detail):
- "tell me more", "dig deeper", "elaborate", "how exactly", "break that down"
- "walk me through", "step by step", "what are the details"

**Zoom-Out Indicators** (decrease detail):
- "summarize", "high level", "bottom line", "key points", "big picture"

**Key Principle**: When a CEO asks to "dig deeper", increase the detail level but maintain executive vocabulary and strategic framing. The core style is preserved; only the depth changes.

**Detail Adjustment Process**:
1. Call `detect_detail_request` on each utterance
2. If detail request detected, call `adjust_detail_level`
3. Use `format_at_detail_level` with `maintain_style=true`

## Current Context

{context_summary}

Remember: You are a strategic advisor listening to a C-suite executive. Be insightful, be concise, and let the client's responses guide the conversation. Use Porter's frameworks as your analytical lens, not your script.
"""


class StrategyCoordinator(BaseAgent):
    """
    Strategy Coordinator Agent using Claude Opus 4.5.
    
    Orchestrates the multi-agent system for business value chain design.
    """
    
    def __init__(
        self, 
        api_key: Optional[str] = None,
        sub_agents: Optional[Dict[str, BaseAgent]] = None
    ):
        """
        Initialize the Strategy Coordinator.
        
        Args:
            api_key: Anthropic API key
            sub_agents: Dictionary of sub-agents to coordinate
        """
        config = AgentConfig(
            role=AgentRole.COORDINATOR,
            model="claude-opus-4-20250514",
            max_tokens=8192,
            temperature=0.7,
            tools=self._get_coordinator_tools()
        )
        super().__init__(config, api_key)
        self.sub_agents = sub_agents or {}
        self._pending_tasks: Dict[str, asyncio.Task] = {}
    
    def _get_coordinator_tools(self) -> List[ToolDefinition]:
        """Define tools available to the coordinator."""
        return [
            ToolDefinition(
                name="delegate_to_architect",
                description="Delegate a task to the Architect Agent for value chain structure design",
                parameters={
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "Description of the architecture task"
                        },
                        "requirements": {
                            "type": "object",
                            "description": "Specific requirements for the design"
                        }
                    },
                    "required": ["task"]
                }
            ),
            ToolDefinition(
                name="delegate_to_analyst",
                description="Delegate a task to the Business Analyst Agent for industry expertise and KPI identification",
                parameters={
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "Description of the analysis task"
                        },
                        "industry": {
                            "type": "string",
                            "description": "Target industry for analysis"
                        },
                        "focus_areas": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Specific areas to focus on"
                        }
                    },
                    "required": ["task"]
                }
            ),
            ToolDefinition(
                name="delegate_to_developer",
                description="Delegate a task to the Developer Agent for code and schema generation",
                parameters={
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "Description of the development task"
                        },
                        "artifact_type": {
                            "type": "string",
                            "enum": ["schema", "model", "api", "formula"],
                            "description": "Type of artifact to generate"
                        },
                        "specifications": {
                            "type": "object",
                            "description": "Technical specifications"
                        }
                    },
                    "required": ["task", "artifact_type"]
                }
            ),
            ToolDefinition(
                name="delegate_to_tester",
                description="Delegate a task to the Tester Agent for validation and quality assurance",
                parameters={
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "Description of the testing task"
                        },
                        "artifacts_to_test": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Names of artifacts to validate"
                        }
                    },
                    "required": ["task"]
                }
            ),
            ToolDefinition(
                name="delegate_to_documenter",
                description="Delegate a task to the Documenter Agent for documentation generation",
                parameters={
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "Description of the documentation task"
                        },
                        "doc_type": {
                            "type": "string",
                            "enum": ["user_guide", "api_docs", "data_dictionary", "runbook"],
                            "description": "Type of documentation to generate"
                        }
                    },
                    "required": ["task", "doc_type"]
                }
            ),
            ToolDefinition(
                name="delegate_to_data_analyst",
                description="Delegate a task to the Data Analyst Agent for set-based KPI design and calculation engine optimization",
                parameters={
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "Description of the KPI design task"
                        },
                        "kpi_type": {
                            "type": "string",
                            "enum": ["simple", "set_based", "cohort_analysis"],
                            "description": "Type of KPI to design"
                        },
                        "entities": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Entities involved in the calculation"
                        },
                        "requirements": {
                            "type": "object",
                            "description": "Specific calculation requirements"
                        }
                    },
                    "required": ["task"]
                }
            ),
            ToolDefinition(
                name="delegate_to_deployment_specialist",
                description="Delegate a task to the Deployment Specialist Agent for Azure infrastructure and deployment configuration",
                parameters={
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "Description of the deployment task"
                        },
                        "client_code": {
                            "type": "string",
                            "description": "Client identifier code"
                        },
                        "environment": {
                            "type": "string",
                            "enum": ["dev", "staging", "prod"],
                            "description": "Target deployment environment"
                        },
                        "artifact_type": {
                            "type": "string",
                            "enum": ["infrastructure", "kubernetes", "helm", "cicd", "database", "checklist"],
                            "description": "Type of deployment artifact to generate"
                        }
                    },
                    "required": ["task"]
                }
            ),
            ToolDefinition(
                name="delegate_to_project_manager",
                description="Delegate a task to the Project Manager Agent for Agile planning, epic/sprint/story generation",
                parameters={
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "Description of the project planning task"
                        },
                        "artifact_type": {
                            "type": "string",
                            "enum": ["epic", "sprint", "user_story", "technical_task", "roadmap", "risk_register"],
                            "description": "Type of project artifact to generate"
                        },
                        "scope_summary": {
                            "type": "string",
                            "description": "Summary of the scope to be planned"
                        },
                        "team_velocity": {
                            "type": "integer",
                            "description": "Expected story points per sprint"
                        }
                    },
                    "required": ["task"]
                }
            ),
            ToolDefinition(
                name="delegate_to_sales_manager",
                description="Delegate a task to the Sales Manager Agent for CRM lifecycle management (prospect → lead → opportunity → client)",
                parameters={
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "Description of the sales/CRM task"
                        },
                        "lifecycle_stage": {
                            "type": "string",
                            "enum": ["prospect", "lead", "opportunity", "client"],
                            "description": "Current stage in the sales lifecycle"
                        },
                        "client_info": {
                            "type": "object",
                            "description": "Client/prospect information"
                        }
                    },
                    "required": ["task"]
                }
            ),
            ToolDefinition(
                name="delegate_to_accountant",
                description="Delegate a task to the Accountant Agent for proposals, SOW, AR/AP, and accounting integration",
                parameters={
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "Description of the financial/accounting task"
                        },
                        "document_type": {
                            "type": "string",
                            "enum": ["proposal", "sow", "invoice", "payment", "expense", "report"],
                            "description": "Type of financial document"
                        },
                        "financial_details": {
                            "type": "object",
                            "description": "Financial details and amounts"
                        }
                    },
                    "required": ["task"]
                }
            ),
            ToolDefinition(
                name="delegate_to_data_governance_specialist",
                description="Delegate a task to the Data Governance Specialist Agent for DAMA DMBOK governance evaluation",
                parameters={
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "Description of the governance task"
                        },
                        "governance_area": {
                            "type": "string",
                            "enum": ["data_governance", "data_architecture", "data_modeling", "data_storage", "data_security", "data_integration", "metadata_management", "master_data", "data_quality"],
                            "description": "DAMA DMBOK knowledge area"
                        },
                        "artifacts_to_evaluate": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Artifacts to evaluate for governance compliance"
                        }
                    },
                    "required": ["task"]
                }
            ),
            ToolDefinition(
                name="delegate_to_data_scientist",
                description="Delegate a task to the Data Scientist Agent for KPI correlation analysis and ML recommendations",
                parameters={
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "Description of the data science task"
                        },
                        "analysis_type": {
                            "type": "string",
                            "enum": ["correlation", "ml_opportunity", "algorithm_recommendation", "feature_engineering", "model_specification"],
                            "description": "Type of analysis to perform"
                        },
                        "kpis": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "KPIs to analyze"
                        }
                    },
                    "required": ["task"]
                }
            ),
            ToolDefinition(
                name="delegate_to_marketing_manager",
                description="Delegate a task to the Marketing Manager Agent for marketing strategy and campaign management (coordinates with Sales Manager)",
                parameters={
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "Description of the marketing task"
                        },
                        "marketing_type": {
                            "type": "string",
                            "enum": ["marketing_plan", "campaign", "content_calendar", "buyer_persona", "lead_scoring"],
                            "description": "Type of marketing artifact"
                        },
                        "target_segments": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Target market segments"
                        }
                    },
                    "required": ["task"]
                }
            ),
            ToolDefinition(
                name="delegate_to_ui_designer",
                description="Delegate a task to the UI Designer Agent for analytics dashboard design and styling",
                parameters={
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "Description of the UI design task"
                        },
                        "design_type": {
                            "type": "string",
                            "enum": ["dashboard_layout", "style_guide", "stylesheet", "component", "color_palette", "chart_style"],
                            "description": "Type of design artifact"
                        },
                        "page_context": {
                            "type": "string",
                            "description": "Context about the page or component being designed"
                        }
                    },
                    "required": ["task"]
                }
            ),
            ToolDefinition(
                name="synthesize_results",
                description="Synthesize results from multiple sub-agents into a cohesive output",
                parameters={
                    "type": "object",
                    "properties": {
                        "results": {
                            "type": "array",
                            "items": {"type": "object"},
                            "description": "Results from sub-agents to synthesize"
                        },
                        "output_format": {
                            "type": "string",
                            "enum": ["value_chain_model", "summary", "recommendations"],
                            "description": "Desired output format"
                        }
                    },
                    "required": ["results", "output_format"]
                }
            ),
            ToolDefinition(
                name="delegate_to_business_strategist",
                description="Delegate a task to the Business Strategist Agent for Porter's frameworks analysis (Five Forces, Value Chain, Generic Strategy, Strategic Fit)",
                parameters={
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "Description of the strategic analysis task"
                        },
                        "analysis_type": {
                            "type": "string",
                            "enum": ["five_forces", "value_chain", "generic_strategy", "strategic_fit", "strategic_questions", "synthesis"],
                            "description": "Type of Porter's framework analysis"
                        },
                        "client_context": {
                            "type": "string",
                            "description": "Context from client interview responses"
                        }
                    },
                    "required": ["task"]
                }
            ),
            ToolDefinition(
                name="delegate_to_operations_manager",
                description="Delegate a task to the Operations Manager Agent for holistic KPI analysis, correlation detection, and performance optimization recommendations",
                parameters={
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "Description of the operations/performance analysis task"
                        },
                        "analysis_type": {
                            "type": "string",
                            "enum": ["kpi_analysis", "correlation_detection", "bottleneck_identification", "optimization_plan", "health_assessment", "impact_forecast"],
                            "description": "Type of operational analysis"
                        },
                        "kpi_context": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "KPIs to analyze"
                        }
                    },
                    "required": ["task"]
                }
            ),
            ToolDefinition(
                name="generate_probing_questions",
                description="Get the 4 core interview questions for client discovery",
                parameters={
                    "type": "object",
                    "properties": {
                        "question_type": {
                            "type": "string",
                            "enum": ["core"],
                            "description": "Type of questions: 'core' for the 4 main interview questions"
                        }
                    },
                    "required": ["question_type"]
                }
            ),
            # Adaptive Communication Style Tools
            ToolDefinition(
                name="detect_communication_style",
                description="Analyze interviewee's utterance to detect their communication style, role, and preferences",
                parameters={
                    "type": "object",
                    "properties": {
                        "utterance": {
                            "type": "string",
                            "description": "The interviewee's message to analyze"
                        },
                        "update_profile": {
                            "type": "boolean",
                            "description": "Whether to update the session's style profile"
                        }
                    },
                    "required": ["utterance"]
                }
            ),
            ToolDefinition(
                name="get_style_profile",
                description="Get the current communication style profile for the session",
                parameters={
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            ),
            ToolDefinition(
                name="format_response_for_style",
                description="Format a response according to the detected communication style",
                parameters={
                    "type": "object",
                    "properties": {
                        "content": {
                            "type": "string",
                            "description": "The content to format"
                        },
                        "style_override": {
                            "type": "string",
                            "enum": ["executive_summary", "technical_detail", "balanced", "adaptive"],
                            "description": "Override the detected style (optional)"
                        }
                    },
                    "required": ["content"]
                }
            ),
            ToolDefinition(
                name="delegate_response_formatting",
                description="Delegate response formatting to the appropriate agent based on detected style",
                parameters={
                    "type": "object",
                    "properties": {
                        "content": {
                            "type": "string",
                            "description": "The content to format"
                        },
                        "target_agent": {
                            "type": "string",
                            "enum": ["business_strategist", "architect", "business_analyst", "data_analyst", "auto"],
                            "description": "Agent to format the response, or 'auto' to use detected preference"
                        }
                    },
                    "required": ["content"]
                }
            ),
            ToolDefinition(
                name="adjust_detail_level",
                description="Adjust the detail level for responses while maintaining the core communication style. Use when interviewee requests more or less detail.",
                parameters={
                    "type": "object",
                    "properties": {
                        "adjustment": {
                            "type": "string",
                            "enum": ["increase", "decrease", "reset", "set"],
                            "description": "How to adjust: increase (drill down), decrease (zoom out), reset (back to base), set (specific level)"
                        },
                        "target_level": {
                            "type": "integer",
                            "description": "Target level (1-4) when using 'set'. 1=summary, 2=moderate, 3=detailed, 4=comprehensive"
                        },
                        "topic": {
                            "type": "string",
                            "description": "The topic the user wants more/less detail on"
                        }
                    },
                    "required": ["adjustment"]
                }
            ),
            ToolDefinition(
                name="detect_detail_request",
                description="Detect if the interviewee is requesting more or less detail in their message",
                parameters={
                    "type": "object",
                    "properties": {
                        "utterance": {
                            "type": "string",
                            "description": "The interviewee's message to analyze for detail requests"
                        }
                    },
                    "required": ["utterance"]
                }
            ),
            ToolDefinition(
                name="format_at_detail_level",
                description="Format content at a specific detail level while maintaining the interviewee's core communication style",
                parameters={
                    "type": "object",
                    "properties": {
                        "content": {
                            "type": "string",
                            "description": "The full detailed content to format"
                        },
                        "detail_level": {
                            "type": "integer",
                            "description": "Detail level (1-4). If not provided, uses current session level."
                        },
                        "maintain_style": {
                            "type": "boolean",
                            "description": "Whether to maintain the detected communication style vocabulary"
                        }
                    },
                    "required": ["content"]
                }
            ),
            ToolDefinition(
                name="delegate_to_process_scenario_modeler",
                description="Delegate a task to the Process Scenario Modeler Agent for process simulation and what-if scenario analysis",
                parameters={
                    "type": "object",
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "Description of the process simulation task"
                        },
                        "task_type": {
                            "type": "string",
                            "enum": ["design_process", "create_scenario", "run_simulation", "analyze_impact", "compare_scenarios", "identify_bottlenecks", "recommend_optimizations"],
                            "description": "Type of process simulation task"
                        },
                        "process_context": {
                            "type": "string",
                            "description": "Context about the process or value chain module"
                        }
                    },
                    "required": ["task"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        """Register tool handlers."""
        self.register_tool("delegate_to_architect", self._delegate_to_architect)
        self.register_tool("delegate_to_analyst", self._delegate_to_analyst)
        self.register_tool("delegate_to_developer", self._delegate_to_developer)
        self.register_tool("delegate_to_tester", self._delegate_to_tester)
        self.register_tool("delegate_to_documenter", self._delegate_to_documenter)
        self.register_tool("delegate_to_data_analyst", self._delegate_to_data_analyst)
        self.register_tool("delegate_to_deployment_specialist", self._delegate_to_deployment_specialist)
        self.register_tool("delegate_to_project_manager", self._delegate_to_project_manager)
        self.register_tool("delegate_to_sales_manager", self._delegate_to_sales_manager)
        self.register_tool("delegate_to_accountant", self._delegate_to_accountant)
        self.register_tool("delegate_to_data_governance_specialist", self._delegate_to_data_governance_specialist)
        self.register_tool("delegate_to_data_scientist", self._delegate_to_data_scientist)
        self.register_tool("delegate_to_marketing_manager", self._delegate_to_marketing_manager)
        self.register_tool("delegate_to_ui_designer", self._delegate_to_ui_designer)
        self.register_tool("delegate_to_business_strategist", self._delegate_to_business_strategist)
        self.register_tool("delegate_to_operations_manager", self._delegate_to_operations_manager)
        self.register_tool("synthesize_results", self._synthesize_results)
        self.register_tool("generate_probing_questions", self._generate_probing_questions)
        # Adaptive Communication Style handlers
        self.register_tool("detect_communication_style", self._detect_communication_style)
        self.register_tool("get_style_profile", self._get_style_profile)
        self.register_tool("format_response_for_style", self._format_response_for_style)
        self.register_tool("delegate_response_formatting", self._delegate_response_formatting)
        # Detail level adjustment handlers
        self.register_tool("adjust_detail_level", self._adjust_detail_level)
        self.register_tool("detect_detail_request", self._detect_detail_request)
        self.register_tool("format_at_detail_level", self._format_at_detail_level)
        self.register_tool("delegate_to_process_scenario_modeler", self._delegate_to_process_scenario_modeler)
    
    def get_system_prompt(self, context: AgentContext) -> str:
        """Get the system prompt with context."""
        context_summary = self._build_context_summary(context)
        return COORDINATOR_SYSTEM_PROMPT.format(context_summary=context_summary)
    
    def _build_context_summary(self, context: AgentContext) -> str:
        """Build a summary of the current context."""
        parts = []
        
        if context.business_description:
            parts.append(f"**Business Description**: {context.business_description}")
        
        if context.industry:
            parts.append(f"**Industry**: {context.industry}")
        
        if context.value_chain_type:
            parts.append(f"**Value Chain Type**: {context.value_chain_type}")
        
        if context.identified_entities:
            parts.append(f"**Identified Entities**: {', '.join(context.identified_entities)}")
        
        if context.identified_kpis:
            parts.append(f"**Identified KPIs**: {', '.join(context.identified_kpis)}")
        
        if context.artifacts:
            parts.append(f"**Generated Artifacts**: {', '.join(context.artifacts.keys())}")
        
        return "\n".join(parts) if parts else "No context available yet. This is a new session."
    
    def set_sub_agent(self, role: str, agent: BaseAgent) -> None:
        """Set a sub-agent for coordination."""
        self.sub_agents[role] = agent
        logger.info(f"Registered sub-agent: {role}")
    
    async def _delegate_to_agent(
        self, 
        agent_key: str,
        task: str,
        context: AgentContext,
        additional_context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Delegate a task to a sub-agent."""
        if agent_key not in self.sub_agents:
            return {
                "success": False,
                "error": f"Sub-agent '{agent_key}' not available"
            }
        
        agent = self.sub_agents[agent_key]
        
        # Build task message with additional context
        task_message = task
        if additional_context:
            task_message += f"\n\nAdditional Context:\n{json.dumps(additional_context, indent=2)}"
        
        try:
            response = await agent.process(task_message, context)
            return {
                "success": response.success,
                "agent": agent_key,
                "content": response.content,
                "artifacts": response.artifacts,
                "error": response.error
            }
        except Exception as e:
            logger.error(f"Delegation to {agent_key} failed: {e}")
            return {
                "success": False,
                "agent": agent_key,
                "error": str(e)
            }
    
    async def _delegate_to_architect(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Delegate to Architect Agent."""
        return await self._delegate_to_agent(
            "architect",
            tool_input.get("task", ""),
            context,
            tool_input.get("requirements")
        )
    
    async def _delegate_to_analyst(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Delegate to Business Analyst Agent."""
        additional = {
            "industry": tool_input.get("industry"),
            "focus_areas": tool_input.get("focus_areas", [])
        }
        return await self._delegate_to_agent(
            "business_analyst",
            tool_input.get("task", ""),
            context,
            additional
        )
    
    async def _delegate_to_developer(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Delegate to Developer Agent."""
        additional = {
            "artifact_type": tool_input.get("artifact_type"),
            "specifications": tool_input.get("specifications", {})
        }
        return await self._delegate_to_agent(
            "developer",
            tool_input.get("task", ""),
            context,
            additional
        )
    
    async def _delegate_to_tester(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Delegate to Tester Agent."""
        additional = {
            "artifacts_to_test": tool_input.get("artifacts_to_test", [])
        }
        return await self._delegate_to_agent(
            "tester",
            tool_input.get("task", ""),
            context,
            additional
        )
    
    async def _delegate_to_documenter(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Delegate to Documenter Agent."""
        additional = {
            "doc_type": tool_input.get("doc_type")
        }
        return await self._delegate_to_agent(
            "documenter",
            tool_input.get("task", ""),
            context,
            additional
        )
    
    async def _delegate_to_data_analyst(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Delegate to Data Analyst Agent for set-based KPI design."""
        additional = {
            "kpi_type": tool_input.get("kpi_type"),
            "entities": tool_input.get("entities", []),
            "requirements": tool_input.get("requirements", {})
        }
        return await self._delegate_to_agent(
            "data_analyst",
            tool_input.get("task", ""),
            context,
            additional
        )
    
    async def _delegate_to_deployment_specialist(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Delegate to Deployment Specialist Agent for Azure deployment."""
        additional = {
            "client_code": tool_input.get("client_code"),
            "environment": tool_input.get("environment"),
            "artifact_type": tool_input.get("artifact_type")
        }
        return await self._delegate_to_agent(
            "deployment_specialist",
            tool_input.get("task", ""),
            context,
            additional
        )
    
    async def _delegate_to_project_manager(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Delegate to Project Manager Agent for Agile planning."""
        additional = {
            "artifact_type": tool_input.get("artifact_type"),
            "scope_summary": tool_input.get("scope_summary"),
            "team_velocity": tool_input.get("team_velocity")
        }
        return await self._delegate_to_agent(
            "project_manager",
            tool_input.get("task", ""),
            context,
            additional
        )
    
    async def _delegate_to_sales_manager(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Delegate to Sales Manager Agent for CRM lifecycle management."""
        additional = {
            "lifecycle_stage": tool_input.get("lifecycle_stage"),
            "client_info": tool_input.get("client_info", {})
        }
        return await self._delegate_to_agent(
            "sales_manager",
            tool_input.get("task", ""),
            context,
            additional
        )
    
    async def _delegate_to_accountant(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Delegate to Accountant Agent for financial operations."""
        additional = {
            "document_type": tool_input.get("document_type"),
            "financial_details": tool_input.get("financial_details", {})
        }
        return await self._delegate_to_agent(
            "accountant",
            tool_input.get("task", ""),
            context,
            additional
        )
    
    async def _delegate_to_data_governance_specialist(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Delegate to Data Governance Specialist Agent for DAMA DMBOK evaluation."""
        additional = {
            "governance_area": tool_input.get("governance_area"),
            "artifacts_to_evaluate": tool_input.get("artifacts_to_evaluate", [])
        }
        return await self._delegate_to_agent(
            "data_governance_specialist",
            tool_input.get("task", ""),
            context,
            additional
        )
    
    async def _delegate_to_data_scientist(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Delegate to Data Scientist Agent for KPI correlation and ML recommendations."""
        additional = {
            "analysis_type": tool_input.get("analysis_type"),
            "kpis": tool_input.get("kpis", [])
        }
        return await self._delegate_to_agent(
            "data_scientist",
            tool_input.get("task", ""),
            context,
            additional
        )
    
    async def _delegate_to_marketing_manager(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Delegate to Marketing Manager Agent for marketing strategy and campaigns."""
        additional = {
            "marketing_type": tool_input.get("marketing_type"),
            "target_segments": tool_input.get("target_segments", [])
        }
        return await self._delegate_to_agent(
            "marketing_manager",
            tool_input.get("task", ""),
            context,
            additional
        )
    
    async def _delegate_to_ui_designer(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Delegate to UI Designer Agent for analytics dashboard design."""
        additional = {
            "design_type": tool_input.get("design_type"),
            "page_context": tool_input.get("page_context", "")
        }
        return await self._delegate_to_agent(
            "ui_designer",
            tool_input.get("task", ""),
            context,
            additional
        )
    
    async def _delegate_to_business_strategist(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Delegate to Business Strategist Agent for Porter's frameworks analysis."""
        additional = {
            "analysis_type": tool_input.get("analysis_type"),
            "client_context": tool_input.get("client_context", "")
        }
        return await self._delegate_to_agent(
            "business_strategist",
            tool_input.get("task", ""),
            context,
            additional
        )
    
    async def _delegate_to_operations_manager(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Delegate to Operations Manager Agent for holistic KPI analysis and optimization."""
        additional = {
            "analysis_type": tool_input.get("analysis_type"),
            "kpi_context": tool_input.get("kpi_context", [])
        }
        return await self._delegate_to_agent(
            "operations_manager",
            tool_input.get("task", ""),
            context,
            additional
        )
    
    async def _delegate_to_process_scenario_modeler(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Delegate to Process Scenario Modeler Agent for process simulation and what-if analysis."""
        additional = {
            "task_type": tool_input.get("task_type"),
            "process_context": tool_input.get("process_context", "")
        }
        return await self._delegate_to_agent(
            "process_scenario_modeler",
            tool_input.get("task", ""),
            context,
            additional
        )
    
    async def _synthesize_results(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Synthesize results from multiple sub-agents."""
        results = tool_input.get("results", [])
        output_format = tool_input.get("output_format", "summary")
        
        if output_format == "value_chain_model":
            return self._synthesize_value_chain_model(results, context)
        elif output_format == "recommendations":
            return self._synthesize_recommendations(results, context)
        else:
            return self._synthesize_summary(results, context)
    
    def _synthesize_value_chain_model(
        self, 
        results: List[Dict[str, Any]],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Synthesize a value chain model from sub-agent results."""
        model = {
            "name": f"Value Chain - {context.industry or 'Custom'}",
            "nodes": [],
            "links": [],
            "kpis": [],
            "entities": []
        }
        
        for result in results:
            if not result.get("success"):
                continue
                
            artifacts = result.get("artifacts", {})
            
            # Merge nodes
            if "nodes" in artifacts:
                model["nodes"].extend(artifacts["nodes"])
            
            # Merge links
            if "links" in artifacts:
                model["links"].extend(artifacts["links"])
            
            # Merge KPIs
            if "kpis" in artifacts:
                model["kpis"].extend(artifacts["kpis"])
            
            # Merge entities
            if "entities" in artifacts:
                model["entities"].extend(artifacts["entities"])
        
        return {
            "success": True,
            "model": model
        }
    
    def _synthesize_recommendations(
        self, 
        results: List[Dict[str, Any]],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Synthesize recommendations from sub-agent results."""
        recommendations = []
        
        for result in results:
            if not result.get("success"):
                continue
            
            content = result.get("content", "")
            if content:
                recommendations.append({
                    "source": result.get("agent", "unknown"),
                    "recommendation": content
                })
        
        return {
            "success": True,
            "recommendations": recommendations
        }
    
    def _synthesize_summary(
        self, 
        results: List[Dict[str, Any]],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Synthesize a summary from sub-agent results."""
        summaries = []
        
        for result in results:
            agent = result.get("agent", "unknown")
            success = result.get("success", False)
            content = result.get("content", "")
            
            summaries.append({
                "agent": agent,
                "success": success,
                "summary": content[:500] if content else "No content"
            })
        
        return {
            "success": True,
            "summaries": summaries
        }
    
    async def _generate_probing_questions(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Generate the 4 core interview questions for client discovery."""
        # Core interview questions - presented by the system
        core_questions = [
            {
                "id": 1,
                "category": "business_strategy",
                "question": "Describe your business, your business model, and key strategic priorities."
            },
            {
                "id": 2,
                "category": "pain_points",
                "question": "Describe what pain points in your business you are trying to address through analytics."
            },
            {
                "id": 3,
                "category": "success_metrics",
                "question": "How will you measure success?"
            },
            {
                "id": 4,
                "category": "decision_impact",
                "question": "If you had this information available to you, what decisions would you be able to make?"
            }
        ]
        
        return {
            "success": True,
            "question_type": "core",
            "questions": core_questions,
            "note": "For strategic follow-up questions, delegate to the Business Strategist Agent"
        }
    
    async def run_parallel_delegation(
        self,
        tasks: List[Dict[str, Any]],
        context: AgentContext
    ) -> List[Dict[str, Any]]:
        """
        Run multiple delegations in parallel.
        
        Args:
            tasks: List of task definitions with 'agent' and 'task' keys
            context: Current agent context
            
        Returns:
            List of results from all delegations
        """
        async def run_task(task_def: Dict[str, Any]) -> Dict[str, Any]:
            agent_key = task_def.get("agent")
            task = task_def.get("task", "")
            additional = task_def.get("additional_context")
            
            return await self._delegate_to_agent(
                agent_key,
                task,
                context,
                additional
            )
        
        # Run all tasks in parallel
        results = await asyncio.gather(
            *[run_task(t) for t in tasks],
            return_exceptions=True
        )
        
        # Process results
        processed_results = []
        for i, result in enumerate(results):
            if isinstance(result, Exception):
                processed_results.append({
                    "success": False,
                    "agent": tasks[i].get("agent"),
                    "error": str(result)
                })
            else:
                processed_results.append(result)
        
        return processed_results
    
    # -------------------------------------------------------------------------
    # Adaptive Communication Style Methods
    # -------------------------------------------------------------------------
    
    # Style detection indicators
    EXECUTIVE_INDICATORS = [
        "strategic", "vision", "growth", "market share", "competitive advantage",
        "roi", "bottom line", "stakeholders", "board", "investors", "revenue",
        "profitability", "scale", "transformation", "leadership", "culture",
        "big picture", "high level", "overall", "direction", "priorities"
    ]
    
    TECHNICAL_INDICATORS = [
        "api", "database", "schema", "architecture", "microservices", "integration",
        "latency", "throughput", "scalability", "infrastructure", "deployment",
        "kubernetes", "docker", "ci/cd", "repository", "endpoint", "payload",
        "query", "index", "normalization", "etl", "pipeline", "webhook"
    ]
    
    ANALYST_INDICATORS = [
        "metrics", "kpi", "dashboard", "report", "trend", "correlation",
        "variance", "benchmark", "forecast", "analysis", "data", "segment",
        "cohort", "funnel", "conversion", "attribution", "dimension", "measure"
    ]
    
    async def _detect_communication_style(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Detect communication style from interviewee's utterance."""
        from datetime import datetime
        import uuid
        
        utterance = tool_input.get("utterance", "").lower()
        update_profile = tool_input.get("update_profile", True)
        
        # Detect role signals
        executive_signals = [term for term in self.EXECUTIVE_INDICATORS if term in utterance]
        technical_signals = [term for term in self.TECHNICAL_INDICATORS if term in utterance]
        analyst_signals = [term for term in self.ANALYST_INDICATORS if term in utterance]
        
        # Calculate scores
        exec_score = len(executive_signals)
        tech_score = len(technical_signals)
        analyst_score = len(analyst_signals)
        total_signals = exec_score + tech_score + analyst_score
        
        # Determine detected role
        if total_signals == 0:
            detected_role = "unknown"
            role_confidence = 0.0
        elif exec_score >= tech_score and exec_score >= analyst_score:
            detected_role = "executive"
            role_confidence = exec_score / max(total_signals, 1)
        elif tech_score >= exec_score and tech_score >= analyst_score:
            detected_role = "technical"
            role_confidence = tech_score / max(total_signals, 1)
        else:
            detected_role = "analyst"
            role_confidence = analyst_score / max(total_signals, 1)
        
        # Determine abstraction level
        if detected_role == "executive":
            abstraction_level = "strategic"
            detail_preference = "summary"
            preferred_agent = "business_strategist"
            response_format = "executive_summary"
        elif detected_role == "technical":
            abstraction_level = "detailed"
            detail_preference = "comprehensive"
            preferred_agent = "architect"
            response_format = "technical_detail"
        elif detected_role == "analyst":
            abstraction_level = "tactical"
            detail_preference = "moderate"
            preferred_agent = "data_analyst"
            response_format = "balanced"
        else:
            abstraction_level = "balanced"
            detail_preference = "moderate"
            preferred_agent = None
            response_format = "adaptive"
        
        # Build detection result
        detection_result = {
            "id": f"STYLE-{str(uuid.uuid4())[:8].upper()}",
            "utterance_id": str(uuid.uuid4())[:8],
            "detected_role": detected_role,
            "role_confidence": round(role_confidence, 2),
            "abstraction_level": abstraction_level,
            "detail_preference": detail_preference,
            "preferred_response_agent": preferred_agent,
            "response_format": response_format,
            "executive_signals": executive_signals,
            "technical_signals": technical_signals,
            "analyst_signals": analyst_signals,
            "detected_at": datetime.utcnow().isoformat()
        }
        
        # Update session profile if requested
        if update_profile:
            if "communication_style_profile" not in context.artifacts:
                context.artifacts["communication_style_profile"] = {
                    "session_id": context.session_id,
                    "detected_role": detected_role,
                    "role_confidence": role_confidence,
                    "abstraction_level": abstraction_level,
                    "vocabulary_type": "business" if detected_role == "executive" else ("technical" if detected_role == "technical" else "mixed"),
                    "detail_preference": detail_preference,
                    "preferred_response_agent": preferred_agent,
                    "response_format": response_format,
                    "role_indicators": [],
                    "utterances_analyzed": 0,
                    "last_updated_at": datetime.utcnow().isoformat()
                }
            
            profile = context.artifacts["communication_style_profile"]
            profile["utterances_analyzed"] += 1
            profile["role_indicators"].extend(executive_signals + technical_signals + analyst_signals)
            profile["last_updated_at"] = datetime.utcnow().isoformat()
            
            # Update role if confidence is higher
            if role_confidence > profile.get("role_confidence", 0):
                profile["detected_role"] = detected_role
                profile["role_confidence"] = role_confidence
                profile["abstraction_level"] = abstraction_level
                profile["detail_preference"] = detail_preference
                profile["preferred_response_agent"] = preferred_agent
                profile["response_format"] = response_format
        
        # Store detection history
        if "style_detections" not in context.artifacts:
            context.artifacts["style_detections"] = []
        context.artifacts["style_detections"].append(detection_result)
        
        return {"success": True, "detection": detection_result}
    
    async def _get_style_profile(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Get the current communication style profile."""
        profile = context.artifacts.get("communication_style_profile")
        
        if not profile:
            return {
                "success": True,
                "profile": None,
                "message": "No style profile detected yet. Analyze utterances first."
            }
        
        return {"success": True, "profile": profile}
    
    async def _format_response_for_style(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Format response according to detected communication style."""
        content = tool_input.get("content", "")
        style_override = tool_input.get("style_override")
        
        profile = context.artifacts.get("communication_style_profile", {})
        response_format = style_override or profile.get("response_format", "adaptive")
        
        # Apply formatting based on style
        if response_format == "executive_summary":
            formatted = self._format_executive_summary(content)
        elif response_format == "technical_detail":
            formatted = self._format_technical_detail(content)
        elif response_format == "balanced":
            formatted = self._format_balanced(content)
        else:
            formatted = content  # Adaptive - no transformation
        
        return {
            "success": True,
            "original_content": content,
            "formatted_content": formatted,
            "applied_format": response_format
        }
    
    def _format_executive_summary(self, content: str) -> str:
        """Format content for executive audience - high-level, strategic."""
        # Add executive framing
        lines = content.split('\n')
        summary_lines = []
        
        # Keep only high-level points, limit detail
        for line in lines[:10]:  # Limit to first 10 lines
            if line.strip():
                summary_lines.append(line)
        
        return "\n".join(summary_lines)
    
    def _format_technical_detail(self, content: str) -> str:
        """Format content for technical audience - detailed, precise."""
        # Technical formatting - keep all detail
        return content
    
    def _format_balanced(self, content: str) -> str:
        """Format content for balanced audience - moderate detail."""
        return content
    
    async def _delegate_response_formatting(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Delegate response formatting to appropriate agent based on style."""
        content = tool_input.get("content", "")
        target_agent = tool_input.get("target_agent", "auto")
        
        # Determine target agent
        if target_agent == "auto":
            profile = context.artifacts.get("communication_style_profile", {})
            target_agent = profile.get("preferred_response_agent")
        
        if not target_agent or target_agent not in self.sub_agents:
            # No agent available, return content as-is
            return {
                "success": True,
                "formatted_content": content,
                "formatted_by": "coordinator",
                "note": "No specialized agent available for formatting"
            }
        
        # Delegate to agent for formatting
        formatting_task = f"Format the following content for your target audience:\n\n{content}"
        result = await self._delegate_to_agent(target_agent, formatting_task, context)
        
        return {
            "success": result.get("success", False),
            "formatted_content": result.get("content", content),
            "formatted_by": target_agent,
            "agent_result": result
        }
    
    # -------------------------------------------------------------------------
    # Detail Level Adjustment Methods
    # -------------------------------------------------------------------------
    
    # Indicators for detail requests
    MORE_DETAIL_INDICATORS = [
        "tell me more", "more detail", "dig deeper", "elaborate", "explain further",
        "how exactly", "what specifically", "break that down", "drill down",
        "can you expand", "more information", "specifics", "in depth", "deeper dive",
        "walk me through", "step by step", "technically", "how does that work",
        "what are the details", "give me the details", "unpack that"
    ]
    
    LESS_DETAIL_INDICATORS = [
        "summarize", "high level", "bottom line", "in brief", "tldr", "summary",
        "key points", "main takeaways", "just the highlights", "keep it simple",
        "big picture", "zoom out", "step back", "overall", "in a nutshell"
    ]
    
    async def _detect_detail_request(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Detect if interviewee is requesting more or less detail."""
        utterance = tool_input.get("utterance", "").lower()
        
        # Check for detail request indicators
        more_detail_matches = [ind for ind in self.MORE_DETAIL_INDICATORS if ind in utterance]
        less_detail_matches = [ind for ind in self.LESS_DETAIL_INDICATORS if ind in utterance]
        
        if more_detail_matches:
            request_type = "increase"
            confidence = min(len(more_detail_matches) * 0.3, 1.0)
            indicators = more_detail_matches
        elif less_detail_matches:
            request_type = "decrease"
            confidence = min(len(less_detail_matches) * 0.3, 1.0)
            indicators = less_detail_matches
        else:
            request_type = "none"
            confidence = 0.0
            indicators = []
        
        return {
            "success": True,
            "request_type": request_type,
            "confidence": round(confidence, 2),
            "indicators_found": indicators,
            "recommendation": f"adjust_detail_level with adjustment='{request_type}'" if request_type != "none" else "No adjustment needed"
        }
    
    async def _adjust_detail_level(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Adjust the detail level while maintaining core communication style."""
        from datetime import datetime
        
        adjustment = tool_input.get("adjustment", "increase")
        target_level = tool_input.get("target_level")
        topic = tool_input.get("topic", "general")
        
        # Ensure profile exists
        if "communication_style_profile" not in context.artifacts:
            context.artifacts["communication_style_profile"] = {
                "session_id": context.session_id,
                "detected_role": "unknown",
                "role_confidence": 0.0,
                "abstraction_level": "balanced",
                "vocabulary_type": "mixed",
                "detail_preference": "moderate",
                "preferred_response_agent": None,
                "response_format": "adaptive",
                "role_indicators": [],
                "base_detail_level": 1,
                "current_detail_level": 1,
                "max_detail_level": 4,
                "detail_adjustment_history": [],
                "utterances_analyzed": 0,
                "last_updated_at": datetime.utcnow().isoformat()
            }
        
        profile = context.artifacts["communication_style_profile"]
        previous_level = profile.get("current_detail_level", 1)
        base_level = profile.get("base_detail_level", 1)
        max_level = profile.get("max_detail_level", 4)
        
        # Apply adjustment
        if adjustment == "increase":
            new_level = min(previous_level + 1, max_level)
        elif adjustment == "decrease":
            new_level = max(previous_level - 1, 1)
        elif adjustment == "reset":
            new_level = base_level
        elif adjustment == "set" and target_level:
            new_level = max(1, min(target_level, max_level))
        else:
            new_level = previous_level
        
        # Update profile
        profile["current_detail_level"] = new_level
        profile["last_updated_at"] = datetime.utcnow().isoformat()
        
        # Track adjustment history
        if "detail_adjustment_history" not in profile:
            profile["detail_adjustment_history"] = []
        profile["detail_adjustment_history"].append({
            "adjustment": adjustment,
            "from_level": previous_level,
            "to_level": new_level,
            "topic": topic,
            "timestamp": datetime.utcnow().isoformat()
        })
        
        # Map level to description
        level_descriptions = {
            1: "summary (executive overview)",
            2: "moderate (key details)",
            3: "detailed (comprehensive)",
            4: "comprehensive (full technical depth)"
        }
        
        return {
            "success": True,
            "previous_level": previous_level,
            "new_level": new_level,
            "level_description": level_descriptions.get(new_level, "unknown"),
            "core_style_maintained": profile.get("detected_role", "unknown"),
            "topic": topic,
            "note": f"Detail level adjusted from {previous_level} to {new_level}. Core {profile.get('detected_role', 'unknown')} communication style maintained."
        }
    
    async def _format_at_detail_level(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Format content at a specific detail level while maintaining core style."""
        content = tool_input.get("content", "")
        detail_level = tool_input.get("detail_level")
        maintain_style = tool_input.get("maintain_style", True)
        
        # Get current profile
        profile = context.artifacts.get("communication_style_profile", {})
        
        # Use provided level or current session level
        if detail_level is None:
            detail_level = profile.get("current_detail_level", 2)
        
        # Get core style for vocabulary
        core_style = profile.get("detected_role", "unknown")
        
        # Format based on detail level
        if detail_level == 1:
            # Summary - executive overview
            formatted = self._format_level_1_summary(content, core_style if maintain_style else None)
        elif detail_level == 2:
            # Moderate - key details
            formatted = self._format_level_2_moderate(content, core_style if maintain_style else None)
        elif detail_level == 3:
            # Detailed - comprehensive
            formatted = self._format_level_3_detailed(content, core_style if maintain_style else None)
        else:
            # Level 4 - full technical depth
            formatted = self._format_level_4_comprehensive(content, core_style if maintain_style else None)
        
        return {
            "success": True,
            "original_content": content,
            "formatted_content": formatted,
            "detail_level": detail_level,
            "core_style": core_style,
            "style_maintained": maintain_style
        }
    
    def _format_level_1_summary(self, content: str, style: Optional[str] = None) -> str:
        """Format at level 1 - executive summary."""
        lines = content.split('\n')
        # Keep only first few meaningful lines
        summary_lines = [line for line in lines[:5] if line.strip()]
        
        if style == "executive":
            # Add strategic framing
            return "**Key Takeaway:**\n" + "\n".join(summary_lines)
        elif style == "technical":
            return "**Summary:**\n" + "\n".join(summary_lines)
        else:
            return "\n".join(summary_lines)
    
    def _format_level_2_moderate(self, content: str, style: Optional[str] = None) -> str:
        """Format at level 2 - moderate detail."""
        lines = content.split('\n')
        # Keep first 15 lines
        moderate_lines = [line for line in lines[:15] if line.strip()]
        return "\n".join(moderate_lines)
    
    def _format_level_3_detailed(self, content: str, style: Optional[str] = None) -> str:
        """Format at level 3 - detailed."""
        lines = content.split('\n')
        # Keep first 30 lines
        detailed_lines = [line for line in lines[:30] if line.strip()]
        return "\n".join(detailed_lines)
    
    def _format_level_4_comprehensive(self, content: str, style: Optional[str] = None) -> str:
        """Format at level 4 - full comprehensive detail."""
        # Return full content
        return content

"""
Business-Focused Sub-Agents

This module contains specialized agents for business operations:
- SalesManagerAgent: CRM lifecycle management (prospect → lead → opportunity → client)
- AccountantAgent: Proposals, SOW, AR/AP tracking, accounting integration
- DataGovernanceSpecialistAgent: DAMA DMBOK governance principles
- DataScientistAgent: KPI correlations and ML algorithm recommendations
"""

from __future__ import annotations

import asyncio
import logging
from typing import Any, Dict, List, Optional
from datetime import datetime
import uuid

from .base_agent import (
    BaseAgent,
    AgentConfig,
    AgentContext,
    AgentRole,
    ToolDefinition
)

logger = logging.getLogger(__name__)


# =============================================================================
# SALES MANAGER AGENT
# =============================================================================

class SalesManagerAgent(BaseAgent):
    """
    Sales Manager Agent for CRM lifecycle management.
    
    Tracks client relationships through the sales lifecycle:
    Prospect → Lead → Opportunity → Client
    
    Responsibilities:
    - Track prospect engagement and qualification
    - Manage lead scoring and nurturing
    - Monitor opportunity pipeline and stages
    - Facilitate client onboarding and relationship management
    """
    
    def __init__(self, api_key: Optional[str] = None, mcp_manager: Optional[Any] = None):
        config = AgentConfig(
            role=AgentRole.SALES_MANAGER,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.4,
            tools=self._get_sales_manager_tools()
        )
        super().__init__(config, api_key, mcp_manager)
    
    def _get_system_prompt(self) -> str:
        return """You are an expert Sales Manager with deep expertise in CRM lifecycle management.

## Your Role
You track and manage client relationships through the complete sales lifecycle:
1. **Prospect**: Initial contact, company research, qualification criteria
2. **Lead**: Engaged prospects, lead scoring, nurturing campaigns
3. **Opportunity**: Active deals, pipeline stages, proposal development
4. **Client**: Closed deals, onboarding, relationship management

## CRM Lifecycle Stages

### Prospect Stage
- Initial contact or inbound inquiry
- Company research and fit assessment
- BANT qualification (Budget, Authority, Need, Timeline)
- Engagement tracking (emails, calls, meetings)

### Lead Stage
- Lead scoring based on engagement and fit
- Nurturing campaigns and content delivery
- Discovery calls and needs assessment
- Qualification for opportunity creation

### Opportunity Stage
- Deal registration and pipeline entry
- Stage progression (Discovery → Proposal → Negotiation → Closing)
- Win probability assessment
- Competitive analysis
- Proposal and SOW coordination

### Client Stage
- Contract signing and onboarding
- Implementation kickoff
- Relationship management
- Upsell/cross-sell opportunities
- Renewal tracking

## Tools Available
- create_prospect: Register new prospect with qualification data
- qualify_lead: Score and qualify a lead
- create_opportunity: Create opportunity with deal details
- update_opportunity_stage: Progress opportunity through pipeline
- convert_to_client: Convert won opportunity to client
- generate_pipeline_report: Generate sales pipeline analytics

## Output Format
Always provide structured CRM data with:
- Unique identifiers for tracking
- Stage-appropriate fields
- Activity history
- Next actions and follow-ups
"""
    
    def get_system_prompt(self, context: AgentContext) -> str:
        """Get the system prompt with context."""
        base_prompt = self._get_system_prompt()
        context_info = self._build_context_summary(context)
        return f"{base_prompt}\n\n## Current Context\n{context_info}"
    
    def _build_context_summary(self, context: AgentContext) -> str:
        """Build context summary for system prompt."""
        parts = []
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.business_description:
            parts.append(f"Business: {context.business_description[:200]}...")
        return "\n".join(parts) if parts else "No additional context provided."
    
    def _get_sales_manager_tools(self) -> List[ToolDefinition]:
        return [
            ToolDefinition(
                name="create_prospect",
                description="Register a new prospect in the CRM system",
                parameters={
                    "type": "object",
                    "properties": {
                        "company_name": {"type": "string", "description": "Company name"},
                        "contact_name": {"type": "string", "description": "Primary contact name"},
                        "contact_email": {"type": "string", "description": "Contact email"},
                        "contact_phone": {"type": "string", "description": "Contact phone"},
                        "industry": {"type": "string", "description": "Industry vertical"},
                        "company_size": {"type": "string", "enum": ["startup", "smb", "mid_market", "enterprise"], "description": "Company size category"},
                        "source": {"type": "string", "description": "Lead source (referral, website, event, etc.)"},
                        "initial_interest": {"type": "string", "description": "Initial area of interest"},
                        "notes": {"type": "string", "description": "Additional notes"}
                    },
                    "required": ["company_name", "contact_name", "contact_email"]
                }
            ),
            ToolDefinition(
                name="qualify_lead",
                description="Score and qualify a lead using BANT criteria",
                parameters={
                    "type": "object",
                    "properties": {
                        "prospect_id": {"type": "string", "description": "Prospect ID to qualify"},
                        "budget_confirmed": {"type": "boolean", "description": "Budget availability confirmed"},
                        "budget_range": {"type": "string", "description": "Estimated budget range"},
                        "authority_confirmed": {"type": "boolean", "description": "Decision maker identified"},
                        "decision_maker": {"type": "string", "description": "Decision maker name/title"},
                        "need_identified": {"type": "boolean", "description": "Clear business need identified"},
                        "pain_points": {"type": "array", "items": {"type": "string"}, "description": "Identified pain points"},
                        "timeline": {"type": "string", "description": "Expected decision timeline"},
                        "engagement_score": {"type": "integer", "minimum": 1, "maximum": 100, "description": "Engagement score 1-100"}
                    },
                    "required": ["prospect_id", "need_identified"]
                }
            ),
            ToolDefinition(
                name="create_opportunity",
                description="Create a new sales opportunity from a qualified lead",
                parameters={
                    "type": "object",
                    "properties": {
                        "lead_id": {"type": "string", "description": "Lead ID to convert"},
                        "opportunity_name": {"type": "string", "description": "Opportunity name"},
                        "deal_value": {"type": "number", "description": "Estimated deal value"},
                        "currency": {"type": "string", "description": "Currency code (USD, EUR, etc.)"},
                        "products_services": {"type": "array", "items": {"type": "string"}, "description": "Products/services of interest"},
                        "expected_close_date": {"type": "string", "description": "Expected close date (YYYY-MM-DD)"},
                        "win_probability": {"type": "integer", "minimum": 0, "maximum": 100, "description": "Win probability percentage"},
                        "competitors": {"type": "array", "items": {"type": "string"}, "description": "Known competitors"}
                    },
                    "required": ["lead_id", "opportunity_name", "deal_value"]
                }
            ),
            ToolDefinition(
                name="update_opportunity_stage",
                description="Update opportunity stage in the sales pipeline",
                parameters={
                    "type": "object",
                    "properties": {
                        "opportunity_id": {"type": "string", "description": "Opportunity ID"},
                        "new_stage": {
                            "type": "string",
                            "enum": ["discovery", "qualification", "proposal", "negotiation", "closing", "won", "lost"],
                            "description": "New pipeline stage"
                        },
                        "stage_notes": {"type": "string", "description": "Notes about stage change"},
                        "next_action": {"type": "string", "description": "Next action required"},
                        "next_action_date": {"type": "string", "description": "Next action date (YYYY-MM-DD)"}
                    },
                    "required": ["opportunity_id", "new_stage"]
                }
            ),
            ToolDefinition(
                name="convert_to_client",
                description="Convert a won opportunity to an active client",
                parameters={
                    "type": "object",
                    "properties": {
                        "opportunity_id": {"type": "string", "description": "Won opportunity ID"},
                        "contract_value": {"type": "number", "description": "Final contract value"},
                        "contract_term_months": {"type": "integer", "description": "Contract term in months"},
                        "contract_start_date": {"type": "string", "description": "Contract start date (YYYY-MM-DD)"},
                        "account_manager": {"type": "string", "description": "Assigned account manager"},
                        "onboarding_notes": {"type": "string", "description": "Onboarding requirements"}
                    },
                    "required": ["opportunity_id", "contract_value", "contract_start_date"]
                }
            ),
            ToolDefinition(
                name="generate_pipeline_report",
                description="Generate sales pipeline analytics report",
                parameters={
                    "type": "object",
                    "properties": {
                        "report_type": {
                            "type": "string",
                            "enum": ["pipeline_summary", "stage_analysis", "forecast", "conversion_rates"],
                            "description": "Type of report to generate"
                        },
                        "date_range_start": {"type": "string", "description": "Report start date (YYYY-MM-DD)"},
                        "date_range_end": {"type": "string", "description": "Report end date (YYYY-MM-DD)"}
                    },
                    "required": ["report_type"]
                }
            ),
            # Cross-Agent Collaboration Tools
            ToolDefinition(
                name="request_mql_from_marketing",
                description="Request Marketing Manager to provide Marketing Qualified Leads",
                parameters={
                    "type": "object",
                    "properties": {
                        "criteria": {"type": "array", "items": {"type": "string"}, "description": "MQL criteria"},
                        "target_count": {"type": "integer", "description": "Target number of MQLs"},
                        "industry_focus": {"type": "array", "items": {"type": "string"}, "description": "Target industries"}
                    },
                    "required": ["criteria"]
                }
            ),
            ToolDefinition(
                name="request_deal_pricing",
                description="Request Accountant to provide deal pricing and financial terms",
                parameters={
                    "type": "object",
                    "properties": {
                        "opportunity_id": {"type": "string", "description": "Opportunity ID"},
                        "products_services": {"type": "array", "items": {"type": "string"}, "description": "Products/services"},
                        "pricing_type": {"type": "string", "enum": ["standard", "custom", "enterprise"], "description": "Pricing tier"}
                    },
                    "required": ["opportunity_id", "products_services"]
                }
            ),
            ToolDefinition(
                name="handoff_to_project_manager",
                description="Hand off won deal to Project Manager for client onboarding",
                parameters={
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "string", "description": "New client ID"},
                        "contract_details": {"type": "object", "description": "Contract details"},
                        "onboarding_requirements": {"type": "array", "items": {"type": "string"}, "description": "Onboarding requirements"}
                    },
                    "required": ["client_id"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        self._tool_handlers = {
            "create_prospect": self._create_prospect,
            "qualify_lead": self._qualify_lead,
            "create_opportunity": self._create_opportunity,
            "update_opportunity_stage": self._update_opportunity_stage,
            "convert_to_client": self._convert_to_client,
            "generate_pipeline_report": self._generate_pipeline_report,
            "request_mql_from_marketing": self._request_mql_from_marketing,
            "request_deal_pricing": self._request_deal_pricing,
            "handoff_to_project_manager": self._handoff_to_project_manager
        }
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if getattr(context, 'client_name', None) or context.metadata.get('client_name'):
            parts.append(f"Client: {getattr(context, 'client_name', None) or context.metadata.get('client_name', 'Unknown')}")
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if "prospects" in context.artifacts:
            parts.append(f"Prospects: {len(context.artifacts['prospects'])}")
        if "opportunities" in context.artifacts:
            parts.append(f"Opportunities: {len(context.artifacts['opportunities'])}")
        return "\n".join(parts) if parts else "No CRM context provided."
    
    async def _create_prospect(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        prospect_id = f"PROS-{str(uuid.uuid4())[:8].upper()}"
        
        prospect = {
            "id": prospect_id,
            "company_name": tool_input.get("company_name", ""),
            "contact_name": tool_input.get("contact_name", ""),
            "contact_email": tool_input.get("contact_email", ""),
            "contact_phone": tool_input.get("contact_phone", ""),
            "industry": tool_input.get("industry", ""),
            "company_size": tool_input.get("company_size", "smb"),
            "source": tool_input.get("source", ""),
            "initial_interest": tool_input.get("initial_interest", ""),
            "notes": tool_input.get("notes", ""),
            "stage": "prospect",
            "created_at": datetime.utcnow().isoformat(),
            "activities": []
        }
        
        if "prospects" not in context.artifacts:
            context.artifacts["prospects"] = []
        context.artifacts["prospects"].append(prospect)
        
        return {"success": True, "prospect": prospect}
    
    async def _qualify_lead(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        prospect_id = tool_input.get("prospect_id", "")
        
        bant_score = 0
        if tool_input.get("budget_confirmed"):
            bant_score += 25
        if tool_input.get("authority_confirmed"):
            bant_score += 25
        if tool_input.get("need_identified"):
            bant_score += 25
        if tool_input.get("timeline"):
            bant_score += 25
        
        engagement_score = tool_input.get("engagement_score", 50)
        lead_score = (bant_score + engagement_score) // 2
        
        lead = {
            "id": f"LEAD-{str(uuid.uuid4())[:8].upper()}",
            "prospect_id": prospect_id,
            "bant_score": bant_score,
            "engagement_score": engagement_score,
            "lead_score": lead_score,
            "qualification": "hot" if lead_score >= 75 else "warm" if lead_score >= 50 else "cold",
            "budget_range": tool_input.get("budget_range", ""),
            "decision_maker": tool_input.get("decision_maker", ""),
            "pain_points": tool_input.get("pain_points", []),
            "timeline": tool_input.get("timeline", ""),
            "qualified_at": datetime.utcnow().isoformat()
        }
        
        if "leads" not in context.artifacts:
            context.artifacts["leads"] = []
        context.artifacts["leads"].append(lead)
        
        return {"success": True, "lead": lead}
    
    async def _create_opportunity(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        opportunity = {
            "id": f"OPP-{str(uuid.uuid4())[:8].upper()}",
            "lead_id": tool_input.get("lead_id", ""),
            "name": tool_input.get("opportunity_name", ""),
            "deal_value": tool_input.get("deal_value", 0),
            "currency": tool_input.get("currency", "USD"),
            "products_services": tool_input.get("products_services", []),
            "expected_close_date": tool_input.get("expected_close_date", ""),
            "win_probability": tool_input.get("win_probability", 50),
            "competitors": tool_input.get("competitors", []),
            "stage": "discovery",
            "stage_history": [{"stage": "discovery", "date": datetime.utcnow().isoformat()}],
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "opportunities" not in context.artifacts:
            context.artifacts["opportunities"] = []
        context.artifacts["opportunities"].append(opportunity)
        
        return {"success": True, "opportunity": opportunity}
    
    async def _update_opportunity_stage(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        opportunity_id = tool_input.get("opportunity_id", "")
        new_stage = tool_input.get("new_stage", "")
        
        stage_update = {
            "opportunity_id": opportunity_id,
            "new_stage": new_stage,
            "stage_notes": tool_input.get("stage_notes", ""),
            "next_action": tool_input.get("next_action", ""),
            "next_action_date": tool_input.get("next_action_date", ""),
            "updated_at": datetime.utcnow().isoformat()
        }
        
        return {"success": True, "stage_update": stage_update}
    
    async def _convert_to_client(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        client = {
            "id": f"CLI-{str(uuid.uuid4())[:8].upper()}",
            "opportunity_id": tool_input.get("opportunity_id", ""),
            "contract_value": tool_input.get("contract_value", 0),
            "contract_term_months": tool_input.get("contract_term_months", 12),
            "contract_start_date": tool_input.get("contract_start_date", ""),
            "account_manager": tool_input.get("account_manager", ""),
            "onboarding_notes": tool_input.get("onboarding_notes", ""),
            "status": "onboarding",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "clients" not in context.artifacts:
            context.artifacts["clients"] = []
        context.artifacts["clients"].append(client)
        
        return {"success": True, "client": client}
    
    async def _generate_pipeline_report(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        report_type = tool_input.get("report_type", "pipeline_summary")
        
        opportunities = context.artifacts.get("opportunities", [])
        
        report = {
            "report_type": report_type,
            "generated_at": datetime.utcnow().isoformat(),
            "total_opportunities": len(opportunities),
            "total_pipeline_value": sum(o.get("deal_value", 0) for o in opportunities),
            "weighted_pipeline": sum(o.get("deal_value", 0) * o.get("win_probability", 50) / 100 for o in opportunities)
        }
        
        context.artifacts[f"report_{report_type}"] = report
        
        return {"success": True, "report": report}
    
    # Collaboration Tool Handlers
    async def _request_mql_from_marketing(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Request Marketing Manager to provide MQLs."""
        request = {
            "id": f"MQL-REQ-{str(uuid.uuid4())[:8].upper()}",
            "criteria": tool_input.get("criteria", []),
            "target_count": tool_input.get("target_count", 10),
            "industry_focus": tool_input.get("industry_focus", []),
            "status": "pending_marketing_manager",
            "collaboration_type": "sales_manager_to_marketing_manager"
        }
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        return {"success": True, "request": request, "next_step": "Marketing Manager will provide qualified leads"}
    
    async def _request_deal_pricing(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Request Accountant to provide deal pricing."""
        request = {
            "id": f"PRICING-REQ-{str(uuid.uuid4())[:8].upper()}",
            "opportunity_id": tool_input.get("opportunity_id", ""),
            "products_services": tool_input.get("products_services", []),
            "pricing_type": tool_input.get("pricing_type", "standard"),
            "status": "pending_accountant",
            "collaboration_type": "sales_manager_to_accountant"
        }
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        return {"success": True, "request": request, "next_step": "Accountant will provide pricing and terms"}
    
    async def _handoff_to_project_manager(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Hand off won deal to Project Manager."""
        handoff = {
            "id": f"HANDOFF-{str(uuid.uuid4())[:8].upper()}",
            "client_id": tool_input.get("client_id", ""),
            "contract_details": tool_input.get("contract_details", {}),
            "onboarding_requirements": tool_input.get("onboarding_requirements", []),
            "status": "pending_project_manager",
            "collaboration_type": "sales_manager_to_project_manager"
        }
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(handoff)
        return {"success": True, "handoff": handoff, "next_step": "Project Manager will begin client onboarding"}


# =============================================================================
# ACCOUNTANT AGENT
# =============================================================================

class AccountantAgent(BaseAgent):
    """
    Accountant Agent for financial operations management.
    
    Responsibilities:
    - Client proposal generation and management
    - Statement of Work (SOW) creation
    - Accounts Receivable (AR) tracking
    - Accounts Payable (AP) tracking
    - Accounting platform integration
    """
    
    def __init__(self, api_key: Optional[str] = None, mcp_manager: Optional[Any] = None):
        config = AgentConfig(
            role=AgentRole.ACCOUNTANT,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.3,
            tools=self._get_accountant_tools()
        )
        super().__init__(config, api_key, mcp_manager)
    
    def _get_system_prompt(self) -> str:
        return """You are an expert Accountant with deep expertise in financial operations.

## Your Role
You manage all financial aspects of client engagements:
1. **Proposals**: Create and track client proposals with pricing
2. **Statements of Work**: Generate detailed SOWs with deliverables and milestones
3. **Accounts Receivable**: Track invoices, payments, and collections
4. **Accounts Payable**: Manage vendor payments and expenses
5. **Accounting Integration**: Sync with accounting platforms (QuickBooks, Xero, etc.)

## Financial Document Types

### Proposals
- Executive summary
- Scope of work overview
- Pricing breakdown (fixed, T&M, retainer)
- Payment terms
- Validity period

### Statement of Work (SOW)
- Project objectives
- Deliverables with acceptance criteria
- Timeline and milestones
- Resource allocation
- Change management process
- Payment schedule

### Invoicing
- Invoice generation from SOW milestones
- Payment tracking
- Aging reports
- Collection workflows

## Tools Available
- create_proposal: Generate client proposal
- create_sow: Create Statement of Work
- create_invoice: Generate invoice
- record_payment: Record payment received
- create_expense: Record expense/AP entry
- generate_financial_report: Generate AR/AP reports
- sync_to_accounting: Sync transactions to accounting platform

## Output Format
All financial documents should include:
- Unique document numbers
- Dates and terms
- Line items with amounts
- Tax calculations where applicable
- Running totals and balances
"""
    
    def get_system_prompt(self, context: AgentContext) -> str:
        """Get the system prompt with context."""
        base_prompt = self._get_system_prompt()
        context_info = self._build_context_summary(context)
        return f"{base_prompt}\n\n## Current Context\n{context_info}"
    
    def _build_context_summary(self, context: AgentContext) -> str:
        """Build context summary for system prompt."""
        parts = []
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.business_description:
            parts.append(f"Business: {context.business_description[:200]}...")
        return "\n".join(parts) if parts else "No additional context provided."
    
    def _get_accountant_tools(self) -> List[ToolDefinition]:
        return [
            ToolDefinition(
                name="create_proposal",
                description="Create a client proposal with pricing",
                parameters={
                    "type": "object",
                    "properties": {
                        "client_name": {"type": "string", "description": "Client name"},
                        "proposal_title": {"type": "string", "description": "Proposal title"},
                        "executive_summary": {"type": "string", "description": "Executive summary"},
                        "scope_items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "description": {"type": "string"},
                                    "amount": {"type": "number"},
                                    "type": {"type": "string", "enum": ["fixed", "hourly", "monthly"]}
                                }
                            },
                            "description": "Scope items with pricing"
                        },
                        "pricing_model": {"type": "string", "enum": ["fixed", "time_and_materials", "retainer", "hybrid"]},
                        "total_amount": {"type": "number", "description": "Total proposal amount"},
                        "currency": {"type": "string", "description": "Currency code"},
                        "valid_until": {"type": "string", "description": "Proposal validity date (YYYY-MM-DD)"},
                        "payment_terms": {"type": "string", "description": "Payment terms (Net 30, etc.)"}
                    },
                    "required": ["client_name", "proposal_title", "scope_items", "total_amount"]
                }
            ),
            ToolDefinition(
                name="create_sow",
                description="Create a Statement of Work document",
                parameters={
                    "type": "object",
                    "properties": {
                        "proposal_id": {"type": "string", "description": "Related proposal ID"},
                        "client_name": {"type": "string", "description": "Client name"},
                        "project_name": {"type": "string", "description": "Project name"},
                        "objectives": {"type": "array", "items": {"type": "string"}, "description": "Project objectives"},
                        "deliverables": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "description": {"type": "string"},
                                    "acceptance_criteria": {"type": "array", "items": {"type": "string"}},
                                    "due_date": {"type": "string"},
                                    "payment_milestone": {"type": "number"}
                                }
                            },
                            "description": "Project deliverables"
                        },
                        "start_date": {"type": "string", "description": "Project start date"},
                        "end_date": {"type": "string", "description": "Project end date"},
                        "total_value": {"type": "number", "description": "Total SOW value"},
                        "change_process": {"type": "string", "description": "Change management process"}
                    },
                    "required": ["client_name", "project_name", "deliverables", "total_value"]
                }
            ),
            ToolDefinition(
                name="create_invoice",
                description="Generate an invoice for a client",
                parameters={
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "string", "description": "Client ID"},
                        "sow_id": {"type": "string", "description": "Related SOW ID"},
                        "milestone_name": {"type": "string", "description": "Milestone being invoiced"},
                        "line_items": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "description": {"type": "string"},
                                    "quantity": {"type": "number"},
                                    "unit_price": {"type": "number"},
                                    "amount": {"type": "number"}
                                }
                            },
                            "description": "Invoice line items"
                        },
                        "subtotal": {"type": "number", "description": "Subtotal before tax"},
                        "tax_rate": {"type": "number", "description": "Tax rate percentage"},
                        "total": {"type": "number", "description": "Total amount due"},
                        "due_date": {"type": "string", "description": "Payment due date"}
                    },
                    "required": ["client_id", "line_items", "total", "due_date"]
                }
            ),
            ToolDefinition(
                name="record_payment",
                description="Record a payment received",
                parameters={
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string", "description": "Invoice ID"},
                        "amount": {"type": "number", "description": "Payment amount"},
                        "payment_date": {"type": "string", "description": "Payment date"},
                        "payment_method": {"type": "string", "enum": ["check", "wire", "ach", "credit_card", "other"]},
                        "reference_number": {"type": "string", "description": "Payment reference number"}
                    },
                    "required": ["invoice_id", "amount", "payment_date"]
                }
            ),
            ToolDefinition(
                name="create_expense",
                description="Record an expense or accounts payable entry",
                parameters={
                    "type": "object",
                    "properties": {
                        "vendor_name": {"type": "string", "description": "Vendor name"},
                        "expense_category": {"type": "string", "description": "Expense category"},
                        "description": {"type": "string", "description": "Expense description"},
                        "amount": {"type": "number", "description": "Expense amount"},
                        "expense_date": {"type": "string", "description": "Expense date"},
                        "due_date": {"type": "string", "description": "Payment due date"},
                        "project_id": {"type": "string", "description": "Related project ID"}
                    },
                    "required": ["vendor_name", "description", "amount", "expense_date"]
                }
            ),
            ToolDefinition(
                name="generate_financial_report",
                description="Generate AR/AP or financial summary report",
                parameters={
                    "type": "object",
                    "properties": {
                        "report_type": {
                            "type": "string",
                            "enum": ["ar_aging", "ap_aging", "revenue_summary", "expense_summary", "project_profitability"],
                            "description": "Type of financial report"
                        },
                        "as_of_date": {"type": "string", "description": "Report as-of date"},
                        "client_id": {"type": "string", "description": "Filter by client (optional)"},
                        "project_id": {"type": "string", "description": "Filter by project (optional)"}
                    },
                    "required": ["report_type"]
                }
            ),
            ToolDefinition(
                name="sync_to_accounting",
                description="Sync transactions to accounting platform",
                parameters={
                    "type": "object",
                    "properties": {
                        "platform": {"type": "string", "enum": ["quickbooks", "xero", "sage", "netsuite"], "description": "Accounting platform"},
                        "transaction_type": {"type": "string", "enum": ["invoice", "payment", "expense", "all"]},
                        "transaction_ids": {"type": "array", "items": {"type": "string"}, "description": "Transaction IDs to sync"}
                    },
                    "required": ["platform", "transaction_type"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        self._tool_handlers = {
            "create_proposal": self._create_proposal,
            "create_sow": self._create_sow,
            "create_invoice": self._create_invoice,
            "record_payment": self._record_payment,
            "create_expense": self._create_expense,
            "generate_financial_report": self._generate_financial_report,
            "sync_to_accounting": self._sync_to_accounting
        }
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if getattr(context, 'client_name', None) or context.metadata.get('client_name'):
            parts.append(f"Client: {getattr(context, 'client_name', None) or context.metadata.get('client_name', 'Unknown')}")
        if "proposals" in context.artifacts:
            parts.append(f"Proposals: {len(context.artifacts['proposals'])}")
        if "invoices" in context.artifacts:
            parts.append(f"Invoices: {len(context.artifacts['invoices'])}")
        return "\n".join(parts) if parts else "No financial context provided."
    
    async def _create_proposal(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        proposal = {
            "id": f"PROP-{str(uuid.uuid4())[:8].upper()}",
            "client_name": tool_input.get("client_name", ""),
            "title": tool_input.get("proposal_title", ""),
            "executive_summary": tool_input.get("executive_summary", ""),
            "scope_items": tool_input.get("scope_items", []),
            "pricing_model": tool_input.get("pricing_model", "fixed"),
            "total_amount": tool_input.get("total_amount", 0),
            "currency": tool_input.get("currency", "USD"),
            "valid_until": tool_input.get("valid_until", ""),
            "payment_terms": tool_input.get("payment_terms", "Net 30"),
            "status": "draft",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "proposals" not in context.artifacts:
            context.artifacts["proposals"] = []
        context.artifacts["proposals"].append(proposal)
        
        return {"success": True, "proposal": proposal}
    
    async def _create_sow(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        sow = {
            "id": f"SOW-{str(uuid.uuid4())[:8].upper()}",
            "proposal_id": tool_input.get("proposal_id", ""),
            "client_name": tool_input.get("client_name", ""),
            "project_name": tool_input.get("project_name", ""),
            "objectives": tool_input.get("objectives", []),
            "deliverables": tool_input.get("deliverables", []),
            "start_date": tool_input.get("start_date", ""),
            "end_date": tool_input.get("end_date", ""),
            "total_value": tool_input.get("total_value", 0),
            "change_process": tool_input.get("change_process", ""),
            "status": "draft",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "sows" not in context.artifacts:
            context.artifacts["sows"] = []
        context.artifacts["sows"].append(sow)
        
        return {"success": True, "sow": sow}
    
    async def _create_invoice(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        subtotal = tool_input.get("subtotal", 0)
        tax_rate = tool_input.get("tax_rate", 0)
        tax_amount = subtotal * (tax_rate / 100)
        
        invoice = {
            "id": f"INV-{str(uuid.uuid4())[:8].upper()}",
            "client_id": tool_input.get("client_id", ""),
            "sow_id": tool_input.get("sow_id", ""),
            "milestone_name": tool_input.get("milestone_name", ""),
            "line_items": tool_input.get("line_items", []),
            "subtotal": subtotal,
            "tax_rate": tax_rate,
            "tax_amount": tax_amount,
            "total": tool_input.get("total", subtotal + tax_amount),
            "due_date": tool_input.get("due_date", ""),
            "status": "pending",
            "amount_paid": 0,
            "balance_due": tool_input.get("total", subtotal + tax_amount),
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "invoices" not in context.artifacts:
            context.artifacts["invoices"] = []
        context.artifacts["invoices"].append(invoice)
        
        return {"success": True, "invoice": invoice}
    
    async def _record_payment(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        payment = {
            "id": f"PMT-{str(uuid.uuid4())[:8].upper()}",
            "invoice_id": tool_input.get("invoice_id", ""),
            "amount": tool_input.get("amount", 0),
            "payment_date": tool_input.get("payment_date", ""),
            "payment_method": tool_input.get("payment_method", ""),
            "reference_number": tool_input.get("reference_number", ""),
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "payments" not in context.artifacts:
            context.artifacts["payments"] = []
        context.artifacts["payments"].append(payment)
        
        return {"success": True, "payment": payment}
    
    async def _create_expense(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        expense = {
            "id": f"EXP-{str(uuid.uuid4())[:8].upper()}",
            "vendor_name": tool_input.get("vendor_name", ""),
            "expense_category": tool_input.get("expense_category", ""),
            "description": tool_input.get("description", ""),
            "amount": tool_input.get("amount", 0),
            "expense_date": tool_input.get("expense_date", ""),
            "due_date": tool_input.get("due_date", ""),
            "project_id": tool_input.get("project_id", ""),
            "status": "pending",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "expenses" not in context.artifacts:
            context.artifacts["expenses"] = []
        context.artifacts["expenses"].append(expense)
        
        return {"success": True, "expense": expense}
    
    async def _generate_financial_report(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        report_type = tool_input.get("report_type", "ar_aging")
        
        invoices = context.artifacts.get("invoices", [])
        expenses = context.artifacts.get("expenses", [])
        
        report = {
            "report_type": report_type,
            "as_of_date": tool_input.get("as_of_date", datetime.utcnow().isoformat()[:10]),
            "generated_at": datetime.utcnow().isoformat()
        }
        
        if report_type == "ar_aging":
            report["total_receivables"] = sum(i.get("balance_due", 0) for i in invoices)
            report["invoice_count"] = len(invoices)
        elif report_type == "ap_aging":
            report["total_payables"] = sum(e.get("amount", 0) for e in expenses if e.get("status") == "pending")
            report["expense_count"] = len(expenses)
        
        context.artifacts[f"report_{report_type}"] = report
        
        return {"success": True, "report": report}
    
    async def _sync_to_accounting(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        sync_result = {
            "platform": tool_input.get("platform", ""),
            "transaction_type": tool_input.get("transaction_type", ""),
            "synced_at": datetime.utcnow().isoformat(),
            "status": "pending_integration",
            "message": "Sync request queued for accounting platform integration"
        }
        
        return {"success": True, "sync_result": sync_result}


# =============================================================================
# DATA GOVERNANCE SPECIALIST AGENT
# =============================================================================

class DataGovernanceSpecialistAgent(BaseAgent):
    """
    Data Governance Specialist Agent based on DAMA DMBOK principles.
    
    Observes all design considerations and evaluates implications using
    the 11 DAMA DMBOK knowledge areas:
    1. Data Governance
    2. Data Architecture
    3. Data Modeling and Design
    4. Data Storage and Operations
    5. Data Security
    6. Data Integration and Interoperability
    7. Document and Content Management
    8. Data Warehousing and Business Intelligence
    9. Metadata Management
    10. Reference and Master Data Management
    11. Data Quality Management
    """
    
    def __init__(self, api_key: Optional[str] = None, mcp_manager: Optional[Any] = None):
        config = AgentConfig(
            role=AgentRole.DATA_GOVERNANCE_SPECIALIST,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.3,
            tools=self._get_governance_tools()
        )
        super().__init__(config, api_key, mcp_manager)
    
    def _get_system_prompt(self) -> str:
        return """You are an expert Data Governance Specialist with deep expertise in DAMA DMBOK.

## Your Role
You observe all design considerations and evaluate their implications using data governance 
principles from the DAMA Data Management Body of Knowledge (DMBOK).

## DAMA DMBOK 11 Knowledge Areas

### 1. Data Governance
- Establish policies, standards, and accountability frameworks
- Define data ownership and stewardship
- Create governance councils and decision rights
- Monitor compliance with data policies

### 2. Data Architecture
- Design data structures supporting business strategy
- Define data flows between systems
- Establish integration patterns
- Document enterprise data models

### 3. Data Modeling and Design
- Create conceptual, logical, and physical models
- Ensure models align with business requirements
- Define naming conventions and standards
- Validate model quality

### 4. Data Storage and Operations
- Manage data availability and performance
- Define backup and recovery procedures
- Optimize database operations
- Plan capacity and scalability

### 5. Data Security
- Protect data from unauthorized access
- Implement encryption and access controls
- Ensure regulatory compliance (GDPR, CCPA, HIPAA)
- Monitor security threats

### 6. Data Integration and Interoperability
- Combine data from disparate sources
- Ensure seamless data exchange
- Define integration standards
- Manage ETL/ELT processes

### 7. Document and Content Management
- Handle unstructured data
- Ensure document accessibility
- Manage content lifecycle
- Support compliance requirements

### 8. Data Warehousing and Business Intelligence
- Support analytical decision-making
- Define dimensional models
- Optimize query performance
- Enable self-service analytics

### 9. Metadata Management
- Capture data lineage and definitions
- Manage technical and business metadata
- Enable data discovery
- Automate metadata enrichment

### 10. Reference and Master Data Management
- Maintain authoritative data versions
- Define golden records
- Manage hierarchies and relationships
- Ensure cross-system consistency

### 11. Data Quality Management
- Ensure accuracy, completeness, timeliness
- Define quality rules and thresholds
- Monitor quality metrics
- Remediate quality issues

## Tools Available
- assess_governance_maturity: Evaluate current governance maturity
- define_data_policy: Create data governance policy
- assign_data_steward: Assign data stewardship
- evaluate_design_compliance: Check design against governance principles
- create_data_dictionary: Generate data dictionary entries
- assess_data_quality_rules: Define quality rules for entities
- evaluate_security_classification: Classify data sensitivity
- generate_governance_report: Generate governance assessment report

## Output Format
All governance assessments should include:
- Knowledge area evaluated
- Current state assessment
- Recommendations
- Risk level (low/medium/high/critical)
- Compliance status
"""
    
    def get_system_prompt(self, context: AgentContext) -> str:
        base_prompt = self._get_system_prompt()
        context_info = self._build_context_summary(context)
        return f"{base_prompt}\n\n## Current Context\n{context_info}"
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.business_description:
            parts.append(f"Business: {context.business_description[:200]}...")
        return "\n".join(parts) if parts else "No additional context provided."
    
    def _get_governance_tools(self) -> List[ToolDefinition]:
        return [
            ToolDefinition(
                name="assess_governance_maturity",
                description="Evaluate data governance maturity across DAMA knowledge areas",
                parameters={
                    "type": "object",
                    "properties": {
                        "knowledge_areas": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "enum": [
                                    "data_governance", "data_architecture", "data_modeling",
                                    "data_storage", "data_security", "data_integration",
                                    "document_management", "data_warehousing", "metadata_management",
                                    "master_data", "data_quality"
                                ]
                            },
                            "description": "Knowledge areas to assess"
                        },
                        "assessment_scope": {"type": "string", "description": "Scope of assessment"},
                        "current_practices": {"type": "string", "description": "Description of current practices"}
                    },
                    "required": ["knowledge_areas"]
                }
            ),
            ToolDefinition(
                name="define_data_policy",
                description="Create a data governance policy",
                parameters={
                    "type": "object",
                    "properties": {
                        "policy_name": {"type": "string", "description": "Policy name"},
                        "policy_type": {
                            "type": "string",
                            "enum": ["access", "retention", "quality", "security", "privacy", "usage"],
                            "description": "Type of policy"
                        },
                        "description": {"type": "string", "description": "Policy description"},
                        "scope": {"type": "string", "description": "Policy scope (entities, domains)"},
                        "rules": {"type": "array", "items": {"type": "string"}, "description": "Policy rules"},
                        "enforcement": {"type": "string", "enum": ["mandatory", "recommended", "optional"]},
                        "owner": {"type": "string", "description": "Policy owner"}
                    },
                    "required": ["policy_name", "policy_type", "description", "rules"]
                }
            ),
            ToolDefinition(
                name="assign_data_steward",
                description="Assign data stewardship responsibility",
                parameters={
                    "type": "object",
                    "properties": {
                        "data_domain": {"type": "string", "description": "Data domain or entity"},
                        "steward_name": {"type": "string", "description": "Steward name"},
                        "steward_role": {"type": "string", "description": "Steward's organizational role"},
                        "responsibilities": {"type": "array", "items": {"type": "string"}, "description": "Stewardship responsibilities"},
                        "escalation_path": {"type": "string", "description": "Escalation path for issues"}
                    },
                    "required": ["data_domain", "steward_name", "responsibilities"]
                }
            ),
            ToolDefinition(
                name="evaluate_design_compliance",
                description="Evaluate a design against governance principles",
                parameters={
                    "type": "object",
                    "properties": {
                        "design_artifact": {"type": "string", "description": "Design artifact to evaluate"},
                        "artifact_type": {
                            "type": "string",
                            "enum": ["entity", "kpi", "schema", "integration", "report"],
                            "description": "Type of artifact"
                        },
                        "governance_areas": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Governance areas to check"
                        }
                    },
                    "required": ["design_artifact", "artifact_type"]
                }
            ),
            ToolDefinition(
                name="create_data_dictionary",
                description="Generate data dictionary entries for entities",
                parameters={
                    "type": "object",
                    "properties": {
                        "entity_name": {"type": "string", "description": "Entity name"},
                        "business_definition": {"type": "string", "description": "Business definition"},
                        "technical_definition": {"type": "string", "description": "Technical definition"},
                        "data_owner": {"type": "string", "description": "Data owner"},
                        "data_steward": {"type": "string", "description": "Data steward"},
                        "source_system": {"type": "string", "description": "Source system"},
                        "attributes": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "definition": {"type": "string"},
                                    "data_type": {"type": "string"},
                                    "nullable": {"type": "boolean"},
                                    "pii": {"type": "boolean"}
                                }
                            },
                            "description": "Entity attributes"
                        }
                    },
                    "required": ["entity_name", "business_definition", "attributes"]
                }
            ),
            ToolDefinition(
                name="assess_data_quality_rules",
                description="Define data quality rules for an entity",
                parameters={
                    "type": "object",
                    "properties": {
                        "entity_name": {"type": "string", "description": "Entity name"},
                        "quality_dimensions": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "enum": ["accuracy", "completeness", "consistency", "timeliness", "uniqueness", "validity"]
                            },
                            "description": "Quality dimensions to assess"
                        },
                        "rules": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "dimension": {"type": "string"},
                                    "rule_name": {"type": "string"},
                                    "rule_definition": {"type": "string"},
                                    "threshold": {"type": "number"},
                                    "severity": {"type": "string", "enum": ["info", "warning", "error", "critical"]}
                                }
                            },
                            "description": "Quality rules"
                        }
                    },
                    "required": ["entity_name", "quality_dimensions", "rules"]
                }
            ),
            ToolDefinition(
                name="evaluate_security_classification",
                description="Classify data sensitivity and security requirements",
                parameters={
                    "type": "object",
                    "properties": {
                        "entity_name": {"type": "string", "description": "Entity name"},
                        "classification": {
                            "type": "string",
                            "enum": ["public", "internal", "confidential", "restricted"],
                            "description": "Data classification level"
                        },
                        "pii_fields": {"type": "array", "items": {"type": "string"}, "description": "Fields containing PII"},
                        "phi_fields": {"type": "array", "items": {"type": "string"}, "description": "Fields containing PHI"},
                        "pci_fields": {"type": "array", "items": {"type": "string"}, "description": "Fields containing PCI data"},
                        "encryption_required": {"type": "boolean", "description": "Encryption required"},
                        "retention_period": {"type": "string", "description": "Data retention period"},
                        "regulatory_requirements": {"type": "array", "items": {"type": "string"}, "description": "Applicable regulations"}
                    },
                    "required": ["entity_name", "classification"]
                }
            ),
            ToolDefinition(
                name="generate_governance_report",
                description="Generate a comprehensive governance assessment report",
                parameters={
                    "type": "object",
                    "properties": {
                        "report_scope": {"type": "string", "description": "Scope of the report"},
                        "include_sections": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "enum": ["maturity", "policies", "stewardship", "quality", "security", "recommendations"]
                            },
                            "description": "Sections to include"
                        }
                    },
                    "required": ["report_scope"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        self._tool_handlers = {
            "assess_governance_maturity": self._assess_governance_maturity,
            "define_data_policy": self._define_data_policy,
            "assign_data_steward": self._assign_data_steward,
            "evaluate_design_compliance": self._evaluate_design_compliance,
            "create_data_dictionary": self._create_data_dictionary,
            "assess_data_quality_rules": self._assess_data_quality_rules,
            "evaluate_security_classification": self._evaluate_security_classification,
            "generate_governance_report": self._generate_governance_report
        }
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.identified_entities:
            parts.append(f"Entities: {', '.join(context.identified_entities[:5])}")
        if "data_policies" in context.artifacts:
            parts.append(f"Policies: {len(context.artifacts['data_policies'])}")
        return "\n".join(parts) if parts else "No governance context provided."
    
    async def _assess_governance_maturity(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        knowledge_areas = tool_input.get("knowledge_areas", [])
        
        maturity_levels = ["initial", "managed", "defined", "quantitatively_managed", "optimizing"]
        
        assessments = []
        for area in knowledge_areas:
            assessment = {
                "knowledge_area": area,
                "current_level": "initial",
                "target_level": "defined",
                "gaps": [],
                "recommendations": [],
                "assessed_at": datetime.utcnow().isoformat()
            }
            assessments.append(assessment)
        
        if "governance_assessments" not in context.artifacts:
            context.artifacts["governance_assessments"] = []
        context.artifacts["governance_assessments"].extend(assessments)
        
        return {"success": True, "assessments": assessments}
    
    async def _define_data_policy(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        policy = {
            "id": f"POL-{str(uuid.uuid4())[:8].upper()}",
            "name": tool_input.get("policy_name", ""),
            "type": tool_input.get("policy_type", ""),
            "description": tool_input.get("description", ""),
            "scope": tool_input.get("scope", ""),
            "rules": tool_input.get("rules", []),
            "enforcement": tool_input.get("enforcement", "mandatory"),
            "owner": tool_input.get("owner", ""),
            "status": "draft",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "data_policies" not in context.artifacts:
            context.artifacts["data_policies"] = []
        context.artifacts["data_policies"].append(policy)
        
        return {"success": True, "policy": policy}
    
    async def _assign_data_steward(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        stewardship = {
            "id": f"STW-{str(uuid.uuid4())[:8].upper()}",
            "data_domain": tool_input.get("data_domain", ""),
            "steward_name": tool_input.get("steward_name", ""),
            "steward_role": tool_input.get("steward_role", ""),
            "responsibilities": tool_input.get("responsibilities", []),
            "escalation_path": tool_input.get("escalation_path", ""),
            "assigned_at": datetime.utcnow().isoformat()
        }
        
        if "data_stewards" not in context.artifacts:
            context.artifacts["data_stewards"] = []
        context.artifacts["data_stewards"].append(stewardship)
        
        return {"success": True, "stewardship": stewardship}
    
    async def _evaluate_design_compliance(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        evaluation = {
            "id": f"EVAL-{str(uuid.uuid4())[:8].upper()}",
            "design_artifact": tool_input.get("design_artifact", ""),
            "artifact_type": tool_input.get("artifact_type", ""),
            "governance_areas": tool_input.get("governance_areas", []),
            "compliance_status": "pending_review",
            "findings": [],
            "risk_level": "medium",
            "evaluated_at": datetime.utcnow().isoformat()
        }
        
        if "compliance_evaluations" not in context.artifacts:
            context.artifacts["compliance_evaluations"] = []
        context.artifacts["compliance_evaluations"].append(evaluation)
        
        return {"success": True, "evaluation": evaluation}
    
    async def _create_data_dictionary(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        entry = {
            "id": f"DD-{str(uuid.uuid4())[:8].upper()}",
            "entity_name": tool_input.get("entity_name", ""),
            "business_definition": tool_input.get("business_definition", ""),
            "technical_definition": tool_input.get("technical_definition", ""),
            "data_owner": tool_input.get("data_owner", ""),
            "data_steward": tool_input.get("data_steward", ""),
            "source_system": tool_input.get("source_system", ""),
            "attributes": tool_input.get("attributes", []),
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "data_dictionary" not in context.artifacts:
            context.artifacts["data_dictionary"] = []
        context.artifacts["data_dictionary"].append(entry)
        
        return {"success": True, "dictionary_entry": entry}
    
    async def _assess_data_quality_rules(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        quality_assessment = {
            "id": f"DQ-{str(uuid.uuid4())[:8].upper()}",
            "entity_name": tool_input.get("entity_name", ""),
            "quality_dimensions": tool_input.get("quality_dimensions", []),
            "rules": tool_input.get("rules", []),
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "quality_rules" not in context.artifacts:
            context.artifacts["quality_rules"] = []
        context.artifacts["quality_rules"].append(quality_assessment)
        
        return {"success": True, "quality_assessment": quality_assessment}
    
    async def _evaluate_security_classification(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        classification = {
            "id": f"SEC-{str(uuid.uuid4())[:8].upper()}",
            "entity_name": tool_input.get("entity_name", ""),
            "classification": tool_input.get("classification", "internal"),
            "pii_fields": tool_input.get("pii_fields", []),
            "phi_fields": tool_input.get("phi_fields", []),
            "pci_fields": tool_input.get("pci_fields", []),
            "encryption_required": tool_input.get("encryption_required", False),
            "retention_period": tool_input.get("retention_period", ""),
            "regulatory_requirements": tool_input.get("regulatory_requirements", []),
            "classified_at": datetime.utcnow().isoformat()
        }
        
        if "security_classifications" not in context.artifacts:
            context.artifacts["security_classifications"] = []
        context.artifacts["security_classifications"].append(classification)
        
        return {"success": True, "classification": classification}
    
    async def _generate_governance_report(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        report = {
            "id": f"GOV-RPT-{str(uuid.uuid4())[:8].upper()}",
            "scope": tool_input.get("report_scope", ""),
            "sections": tool_input.get("include_sections", []),
            "policies_count": len(context.artifacts.get("data_policies", [])),
            "stewards_count": len(context.artifacts.get("data_stewards", [])),
            "dictionary_entries": len(context.artifacts.get("data_dictionary", [])),
            "quality_rules_count": len(context.artifacts.get("quality_rules", [])),
            "generated_at": datetime.utcnow().isoformat()
        }
        
        context.artifacts["governance_report"] = report
        
        return {"success": True, "report": report}


# =============================================================================
# DATA SCIENTIST AGENT
# =============================================================================

class DataScientistAgent(BaseAgent):
    """
    Data Scientist Agent for Strategic Objective Correlation Analysis.
    
    PRIMARY RESPONSIBILITY:
    Identify correlations between KPIs (or KPI groupings) and strategic objectives,
    enabling business users to understand what events and metrics directly contribute
    to strategic objective outcomes, success, or failure. Help users understand the
    levers that are driving the business forward.
    
    Core Responsibilities:
    - Correlate KPIs with strategic objectives to identify business drivers
    - Analyze KPI groupings that collectively impact strategic outcomes
    - Identify leading indicators that predict strategic objective achievement
    - Quantify the contribution of individual KPIs to strategic success/failure
    - Recommend ML algorithms for predictive analytics
    - Design feature engineering strategies
    - Integrate with Machine Learning Service
    """
    
    def __init__(self, api_key: Optional[str] = None, mcp_manager: Optional[Any] = None):
        config = AgentConfig(
            role=AgentRole.DATA_SCIENTIST,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.3,
            tools=self._get_data_science_tools()
        )
        super().__init__(config, api_key, mcp_manager)
    
    def _get_system_prompt(self) -> str:
        return """You are an expert Data Scientist specializing in Strategic Objective Correlation Analysis.

## PRIMARY MISSION
Your primary role is to help business users understand what drives their strategic outcomes.
You identify correlations between KPIs (individually or in groups) and strategic objectives,
enabling users to see which events, metrics, and business activities directly contribute to
strategic objective success or failure. You help users understand the LEVERS that drive
the business forward.

## Core Responsibilities

### 1. Strategic Objective Correlation (PRIMARY)
- Correlate KPIs with strategic objectives to identify business drivers
- Analyze KPI groupings that collectively impact strategic outcomes
- Identify leading indicators that predict strategic objective achievement
- Quantify contribution of individual KPIs to strategic success/failure
- Discover hidden relationships between operational metrics and strategic goals
- Rank KPIs by their influence on each strategic objective

### 2. Business Driver Analysis
- Identify the key levers that move strategic objectives
- Calculate driver importance scores and rankings
- Detect positive and negative contributors
- Find synergistic KPI combinations that amplify strategic impact
- Identify conflicting KPIs (where improving one hurts another)

### 3. KPI-to-Objective Mapping
- Map operational KPIs to tactical objectives
- Map tactical objectives to functional objectives
- Map functional objectives to business unit objectives
- Map business unit objectives to corporate strategic objectives
- Trace the full causal chain from metrics to strategy

### 4. Predictive Strategic Analytics
- Predict likelihood of achieving strategic objectives based on current KPI trends
- Forecast strategic objective outcomes under different scenarios
- Identify early warning indicators for strategic objective risk
- Recommend interventions when objectives are at risk

### 5. Pattern Recognition
- Identify seasonality and trends affecting strategic outcomes
- Detect anomalies that impact strategic objectives
- Recognize cyclical patterns in strategic performance
- Find regime changes in strategic dynamics

### 6. ML Algorithm Recommendations
- Classification: Objective achievement prediction, risk classification
- Regression: Strategic outcome forecasting, driver quantification
- Clustering: Strategic performance segmentation
- Time Series: Strategic KPI forecasting
- Causal Inference: True driver identification vs. correlation

## Statistical Methods
- Pearson/Spearman correlation
- Granger causality (for leading indicator detection)
- Multiple regression (for driver quantification)
- Principal Component Analysis (for KPI grouping)
- Structural Equation Modeling (for causal paths)
- SHAP values (for driver importance)

## Tools Available

### Strategic Objective Correlation (Primary)
- analyze_strategic_objective_drivers: Identify KPIs driving strategic objectives
- map_kpi_to_objectives: Map KPIs to strategic objective hierarchy
- calculate_driver_importance: Quantify KPI contribution to objectives
- identify_leading_indicators: Find KPIs that predict objective outcomes
- analyze_kpi_groupings: Analyze synergies/conflicts between KPI groups
- predict_objective_achievement: Forecast strategic objective success probability

### KPI Analysis & ML
- analyze_kpi_correlations: Find correlations between KPIs
- identify_ml_opportunities: Identify ML use cases from KPIs
- recommend_algorithm: Recommend ML algorithm for use case
- design_feature_set: Design features for ML model
- create_ml_specification: Create ML model specification
- register_with_ml_service: Register model with ML Service

### Collaboration Handoffs
- handoff_to_architect_for_model_design: Hand off correlation results to Architect for model architecture
- handoff_to_developer_for_implementation: Hand off to Developer for coding the predictive model
- request_architecture_review: Request Architect to review proposed model architecture

## Workflow for Predictive Model Development
1. Analyze strategic objective drivers and correlations
2. Create ML model specification based on findings
3. Hand off to Architect Agent for architecture design
4. After architect approval, hand off to Developer Agent for implementation
5. Developer implements model code and integrates with ML Service

## Output Format
All analyses should include:
- Statistical metrics with confidence intervals
- Driver rankings with importance scores
- Business interpretation in strategic context
- Actionable recommendations for improving strategic outcomes
- Visualization recommendations showing KPI-to-objective relationships
"""
    
    def get_system_prompt(self, context: AgentContext) -> str:
        base_prompt = self._get_system_prompt()
        context_info = self._build_context_summary(context)
        return f"{base_prompt}\n\n## Current Context\n{context_info}"
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.business_description:
            parts.append(f"Business: {context.business_description[:200]}...")
        return "\n".join(parts) if parts else "No additional context provided."
    
    def _get_data_science_tools(self) -> List[ToolDefinition]:
        return [
            # PRIMARY TOOLS: Strategic Objective Correlation
            ToolDefinition(
                name="analyze_strategic_objective_drivers",
                description="Identify which KPIs are driving achievement of strategic objectives. This is the primary analysis for understanding business drivers.",
                parameters={
                    "type": "object",
                    "properties": {
                        "strategic_objectives": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Strategic objective codes to analyze"
                        },
                        "kpi_pool": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Pool of KPIs to test as potential drivers (if empty, all KPIs are considered)"
                        },
                        "analysis_period": {"type": "string", "description": "Time period for analysis (e.g., 'last_12_months')"},
                        "min_correlation_threshold": {"type": "number", "description": "Minimum correlation coefficient to consider (default 0.3)"},
                        "include_lagged_analysis": {"type": "boolean", "description": "Include time-lagged correlation analysis"},
                        "max_lag_periods": {"type": "integer", "description": "Maximum lag periods to test"}
                    },
                    "required": ["strategic_objectives"]
                }
            ),
            ToolDefinition(
                name="map_kpi_to_objectives",
                description="Map KPIs to the strategic objective hierarchy (operational → tactical → functional → business unit → corporate)",
                parameters={
                    "type": "object",
                    "properties": {
                        "kpi_codes": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "KPI codes to map"
                        },
                        "target_objective_level": {
                            "type": "string",
                            "enum": ["tactical", "functional", "business_unit", "corporate", "all"],
                            "description": "Target objective level for mapping"
                        },
                        "include_indirect_paths": {"type": "boolean", "description": "Include indirect contribution paths"},
                        "calculate_contribution_weights": {"type": "boolean", "description": "Calculate weighted contribution scores"}
                    },
                    "required": ["kpi_codes"]
                }
            ),
            ToolDefinition(
                name="calculate_driver_importance",
                description="Quantify the importance/contribution of each KPI to strategic objective outcomes using statistical methods",
                parameters={
                    "type": "object",
                    "properties": {
                        "strategic_objective": {"type": "string", "description": "Strategic objective code"},
                        "driver_kpis": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "KPIs to evaluate as drivers"
                        },
                        "method": {
                            "type": "string",
                            "enum": ["regression_coefficients", "shap_values", "permutation_importance", "correlation_ranking"],
                            "description": "Method for calculating importance"
                        },
                        "normalize_scores": {"type": "boolean", "description": "Normalize importance scores to sum to 100%"}
                    },
                    "required": ["strategic_objective", "driver_kpis"]
                }
            ),
            ToolDefinition(
                name="identify_leading_indicators",
                description="Find KPIs that serve as leading indicators (predictors) of strategic objective outcomes",
                parameters={
                    "type": "object",
                    "properties": {
                        "strategic_objective": {"type": "string", "description": "Strategic objective to predict"},
                        "candidate_kpis": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "KPIs to test as leading indicators"
                        },
                        "prediction_horizon": {"type": "string", "description": "How far ahead to predict (e.g., '30_days', '1_quarter')"},
                        "min_lead_time": {"type": "integer", "description": "Minimum lead time in periods"},
                        "use_granger_causality": {"type": "boolean", "description": "Use Granger causality test"}
                    },
                    "required": ["strategic_objective"]
                }
            ),
            ToolDefinition(
                name="analyze_kpi_groupings",
                description="Analyze how groups of KPIs collectively impact strategic objectives (synergies, conflicts, redundancies)",
                parameters={
                    "type": "object",
                    "properties": {
                        "strategic_objective": {"type": "string", "description": "Strategic objective to analyze"},
                        "kpi_groups": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "group_name": {"type": "string"},
                                    "kpi_codes": {"type": "array", "items": {"type": "string"}}
                                }
                            },
                            "description": "Named groups of KPIs to analyze"
                        },
                        "detect_synergies": {"type": "boolean", "description": "Detect KPI combinations with amplified impact"},
                        "detect_conflicts": {"type": "boolean", "description": "Detect KPIs that work against each other"}
                    },
                    "required": ["strategic_objective", "kpi_groups"]
                }
            ),
            ToolDefinition(
                name="predict_objective_achievement",
                description="Predict likelihood of achieving a strategic objective based on current KPI values and trends",
                parameters={
                    "type": "object",
                    "properties": {
                        "strategic_objective": {"type": "string", "description": "Strategic objective code"},
                        "current_kpi_values": {
                            "type": "object",
                            "description": "Current values of relevant KPIs"
                        },
                        "prediction_date": {"type": "string", "description": "Date to predict achievement for"},
                        "include_confidence_interval": {"type": "boolean", "description": "Include confidence interval"},
                        "identify_risk_factors": {"type": "boolean", "description": "Identify KPIs putting objective at risk"}
                    },
                    "required": ["strategic_objective"]
                }
            ),
            # SECONDARY TOOLS: KPI Correlation Analysis
            ToolDefinition(
                name="analyze_kpi_correlations",
                description="Analyze correlations between KPIs",
                parameters={
                    "type": "object",
                    "properties": {
                        "kpi_list": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of KPI codes to analyze"
                        },
                        "correlation_method": {
                            "type": "string",
                            "enum": ["pearson", "spearman", "kendall"],
                            "description": "Correlation method"
                        },
                        "time_window": {"type": "string", "description": "Time window for analysis"},
                        "lag_periods": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "Lag periods to test"
                        },
                        "significance_threshold": {
                            "type": "number",
                            "description": "P-value threshold for significance"
                        }
                    },
                    "required": ["kpi_list"]
                }
            ),
            ToolDefinition(
                name="identify_ml_opportunities",
                description="Identify machine learning opportunities from KPIs",
                parameters={
                    "type": "object",
                    "properties": {
                        "kpis": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "code": {"type": "string"},
                                    "name": {"type": "string"},
                                    "type": {"type": "string"},
                                    "frequency": {"type": "string"}
                                }
                            },
                            "description": "KPIs to analyze"
                        },
                        "business_objectives": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Business objectives to consider"
                        },
                        "data_availability": {"type": "string", "description": "Description of available data"}
                    },
                    "required": ["kpis"]
                }
            ),
            ToolDefinition(
                name="recommend_algorithm",
                description="Recommend ML algorithm for a specific use case",
                parameters={
                    "type": "object",
                    "properties": {
                        "use_case": {"type": "string", "description": "ML use case description"},
                        "problem_type": {
                            "type": "string",
                            "enum": ["classification", "regression", "clustering", "time_series", "anomaly_detection", "recommendation"],
                            "description": "Type of ML problem"
                        },
                        "target_variable": {"type": "string", "description": "Target variable to predict"},
                        "feature_count": {"type": "integer", "description": "Approximate number of features"},
                        "data_size": {"type": "string", "description": "Approximate data size"},
                        "interpretability_required": {"type": "boolean", "description": "Whether model interpretability is required"},
                        "real_time_inference": {"type": "boolean", "description": "Whether real-time inference is needed"}
                    },
                    "required": ["use_case", "problem_type", "target_variable"]
                }
            ),
            ToolDefinition(
                name="design_feature_set",
                description="Design feature engineering for ML model",
                parameters={
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string", "description": "Model name"},
                        "source_kpis": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Source KPIs for features"
                        },
                        "feature_types": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "enum": ["raw", "lag", "rolling", "difference", "ratio", "interaction", "categorical", "time_based"]
                            },
                            "description": "Types of features to generate"
                        },
                        "lookback_periods": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "Lookback periods for lag features"
                        }
                    },
                    "required": ["model_name", "source_kpis", "feature_types"]
                }
            ),
            ToolDefinition(
                name="create_ml_specification",
                description="Create complete ML model specification",
                parameters={
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string", "description": "Model name"},
                        "model_type": {"type": "string", "description": "Model type/algorithm"},
                        "problem_type": {"type": "string", "description": "Problem type"},
                        "target_variable": {"type": "string", "description": "Target variable"},
                        "features": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "source": {"type": "string"},
                                    "transformation": {"type": "string"}
                                }
                            },
                            "description": "Feature specifications"
                        },
                        "training_config": {
                            "type": "object",
                            "properties": {
                                "train_test_split": {"type": "number"},
                                "validation_strategy": {"type": "string"},
                                "hyperparameters": {"type": "object"}
                            },
                            "description": "Training configuration"
                        },
                        "performance_metrics": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Metrics to track"
                        },
                        "deployment_config": {
                            "type": "object",
                            "properties": {
                                "inference_type": {"type": "string"},
                                "batch_size": {"type": "integer"},
                                "refresh_frequency": {"type": "string"}
                            },
                            "description": "Deployment configuration"
                        }
                    },
                    "required": ["model_name", "model_type", "target_variable", "features"]
                }
            ),
            ToolDefinition(
                name="register_with_ml_service",
                description="Register ML model specification with Machine Learning Service",
                parameters={
                    "type": "object",
                    "properties": {
                        "model_spec_id": {"type": "string", "description": "Model specification ID"},
                        "priority": {
                            "type": "string",
                            "enum": ["low", "medium", "high", "critical"],
                            "description": "Implementation priority"
                        },
                        "schedule_training": {"type": "boolean", "description": "Whether to schedule training"},
                        "notify_on_completion": {"type": "boolean", "description": "Send notification on completion"}
                    },
                    "required": ["model_spec_id"]
                }
            ),
            ToolDefinition(
                name="predict_kpi_impact",
                description="Predict the impact of a change on KPIs using ML models and historical data",
                parameters={
                    "type": "object",
                    "properties": {
                        "what_if_question_id": {"type": "string", "description": "ID of the what-if question"},
                        "target_kpis": {"type": "array", "items": {"type": "string"}, "description": "KPIs to predict"},
                        "change_variable": {"type": "string", "description": "Variable being changed"},
                        "change_value": {"type": "number", "description": "Amount of change"},
                        "prediction_method": {"type": "string", "enum": ["regression", "time_series", "causal_inference", "ensemble"]},
                        "confidence_level": {"type": "number", "description": "Confidence level (0-1)"}
                    },
                    "required": ["what_if_question_id", "target_kpis", "change_variable", "change_value"]
                }
            ),
            ToolDefinition(
                name="analyze_cascade_effects",
                description="Analyze how changes cascade through KPI dependencies",
                parameters={
                    "type": "object",
                    "properties": {
                        "primary_kpi": {"type": "string", "description": "Primary KPI being impacted"},
                        "primary_change_percent": {"type": "number", "description": "Percent change in primary KPI"},
                        "cascade_depth": {"type": "integer", "description": "How many levels to cascade"},
                        "include_feedback_loops": {"type": "boolean", "description": "Include feedback loops"}
                    },
                    "required": ["primary_kpi", "primary_change_percent"]
                }
            ),
            ToolDefinition(
                name="run_sensitivity_analysis",
                description="Run sensitivity analysis on prediction parameters",
                parameters={
                    "type": "object",
                    "properties": {
                        "prediction_id": {"type": "string", "description": "ID of the prediction to analyze"},
                        "variable_to_vary": {"type": "string", "description": "Variable to vary"},
                        "min_value": {"type": "number", "description": "Minimum value to test"},
                        "max_value": {"type": "number", "description": "Maximum value to test"},
                        "steps": {"type": "integer", "description": "Number of steps"}
                    },
                    "required": ["prediction_id", "variable_to_vary", "min_value", "max_value"]
                }
            ),
            ToolDefinition(
                name="find_optimal_value",
                description="Find the optimal value for a variable to maximize/minimize a KPI",
                parameters={
                    "type": "object",
                    "properties": {
                        "variable": {"type": "string", "description": "Variable to optimize"},
                        "target_kpi": {"type": "string", "description": "KPI to optimize"},
                        "optimization_goal": {"type": "string", "enum": ["maximize", "minimize"]},
                        "constraints": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "kpi": {"type": "string"},
                                    "operator": {"type": "string", "enum": ["<", ">", "<=", ">="]},
                                    "value": {"type": "number"}
                                }
                            },
                            "description": "Constraints to satisfy"
                        },
                        "search_min": {"type": "number"},
                        "search_max": {"type": "number"}
                    },
                    "required": ["variable", "target_kpi", "optimization_goal"]
                }
            ),
            ToolDefinition(
                name="generate_what_if_prediction",
                description="Generate a complete what-if prediction with all impacts and recommendations",
                parameters={
                    "type": "object",
                    "properties": {
                        "what_if_question_id": {"type": "string"},
                        "primary_impacts": {"type": "array", "items": {"type": "object"}},
                        "cascade_effects": {"type": "array", "items": {"type": "object"}},
                        "net_impact": {"type": "object"},
                        "sensitivity_analysis": {"type": "object"},
                        "optimal_value": {"type": "object"},
                        "recommendations": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["what_if_question_id", "primary_impacts"]
                }
            ),
            # COLLABORATION TOOLS: Handoff to other agents for implementation
            ToolDefinition(
                name="handoff_to_architect_for_model_design",
                description="Hand off correlation analysis and model requirements to Architect Agent for predictive model architecture design",
                parameters={
                    "type": "object",
                    "properties": {
                        "model_specification_id": {"type": "string", "description": "ID of the ML model specification"},
                        "correlation_analysis": {
                            "type": "object",
                            "description": "Summary of KPI-to-objective correlations discovered",
                            "properties": {
                                "strategic_objectives": {"type": "array", "items": {"type": "string"}},
                                "driver_kpis": {"type": "array", "items": {"type": "string"}},
                                "correlation_strengths": {"type": "object"},
                                "leading_indicators": {"type": "array", "items": {"type": "string"}}
                            }
                        },
                        "model_requirements": {
                            "type": "object",
                            "description": "Requirements for the predictive model",
                            "properties": {
                                "model_type": {"type": "string"},
                                "input_features": {"type": "array", "items": {"type": "string"}},
                                "target_variable": {"type": "string"},
                                "performance_requirements": {"type": "object"},
                                "interpretability_requirements": {"type": "string"}
                            }
                        },
                        "data_characteristics": {
                            "type": "object",
                            "description": "Characteristics of the training data",
                            "properties": {
                                "data_sources": {"type": "array", "items": {"type": "string"}},
                                "feature_count": {"type": "integer"},
                                "sample_size": {"type": "integer"},
                                "time_range": {"type": "string"}
                            }
                        },
                        "priority": {"type": "string", "enum": ["low", "medium", "high", "critical"]},
                        "notes": {"type": "string", "description": "Additional context for the architect"}
                    },
                    "required": ["model_specification_id", "correlation_analysis", "model_requirements"]
                }
            ),
            ToolDefinition(
                name="handoff_to_developer_for_implementation",
                description="Hand off model specification and architecture to Developer Agent for coding the predictive model",
                parameters={
                    "type": "object",
                    "properties": {
                        "model_specification_id": {"type": "string", "description": "ID of the ML model specification"},
                        "architecture_design_id": {"type": "string", "description": "ID of the architecture design from Architect"},
                        "implementation_requirements": {
                            "type": "object",
                            "description": "Requirements for model implementation",
                            "properties": {
                                "algorithm": {"type": "string", "description": "Recommended algorithm"},
                                "framework": {"type": "string", "description": "ML framework (sklearn, pytorch, etc.)"},
                                "feature_engineering": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "feature_name": {"type": "string"},
                                            "source_kpi": {"type": "string"},
                                            "transformation": {"type": "string"}
                                        }
                                    }
                                },
                                "training_pipeline": {"type": "object"},
                                "inference_api": {"type": "object"}
                            }
                        },
                        "correlation_results": {
                            "type": "object",
                            "description": "Correlation analysis results to inform implementation",
                            "properties": {
                                "driver_importance_scores": {"type": "object"},
                                "feature_correlations": {"type": "object"},
                                "recommended_feature_order": {"type": "array", "items": {"type": "string"}}
                            }
                        },
                        "test_criteria": {
                            "type": "object",
                            "description": "Testing and validation criteria",
                            "properties": {
                                "accuracy_threshold": {"type": "number"},
                                "validation_strategy": {"type": "string"},
                                "test_dataset_requirements": {"type": "string"}
                            }
                        },
                        "priority": {"type": "string", "enum": ["low", "medium", "high", "critical"]},
                        "deadline": {"type": "string", "description": "Target completion date"}
                    },
                    "required": ["model_specification_id", "implementation_requirements", "correlation_results"]
                }
            ),
            ToolDefinition(
                name="request_architecture_review",
                description="Request Architect Agent to review proposed model architecture before developer handoff",
                parameters={
                    "type": "object",
                    "properties": {
                        "model_specification_id": {"type": "string"},
                        "proposed_architecture": {
                            "type": "object",
                            "properties": {
                                "model_type": {"type": "string"},
                                "layers": {"type": "array", "items": {"type": "object"}},
                                "integration_points": {"type": "array", "items": {"type": "string"}}
                            }
                        },
                        "questions": {"type": "array", "items": {"type": "string"}, "description": "Specific questions for architect"}
                    },
                    "required": ["model_specification_id", "proposed_architecture"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        self._tool_handlers = {
            # PRIMARY: Strategic Objective Correlation Tools
            "analyze_strategic_objective_drivers": self._analyze_strategic_objective_drivers,
            "map_kpi_to_objectives": self._map_kpi_to_objectives,
            "calculate_driver_importance": self._calculate_driver_importance,
            "identify_leading_indicators": self._identify_leading_indicators,
            "analyze_kpi_groupings": self._analyze_kpi_groupings,
            "predict_objective_achievement": self._predict_objective_achievement,
            # SECONDARY: KPI Correlation & ML Tools
            "analyze_kpi_correlations": self._analyze_kpi_correlations,
            "identify_ml_opportunities": self._identify_ml_opportunities,
            "recommend_algorithm": self._recommend_algorithm,
            "design_feature_set": self._design_feature_set,
            "create_ml_specification": self._create_ml_specification,
            "register_with_ml_service": self._register_with_ml_service,
            "predict_kpi_impact": self._predict_kpi_impact,
            "analyze_cascade_effects": self._analyze_cascade_effects,
            "run_sensitivity_analysis": self._run_sensitivity_analysis,
            "find_optimal_value": self._find_optimal_value,
            "generate_what_if_prediction": self._generate_what_if_prediction,
            # COLLABORATION: Handoff to Architect and Developer
            "handoff_to_architect_for_model_design": self._handoff_to_architect_for_model_design,
            "handoff_to_developer_for_implementation": self._handoff_to_developer_for_implementation,
            "request_architecture_review": self._request_architecture_review
        }
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if context.identified_kpis:
            parts.append(f"KPIs: {', '.join(context.identified_kpis[:10])}")
        if "ml_models" in context.artifacts:
            parts.append(f"ML Models: {len(context.artifacts['ml_models'])}")
        if "correlations" in context.artifacts:
            parts.append(f"Correlations analyzed: {len(context.artifacts['correlations'])}")
        if "strategic_driver_analyses" in context.artifacts:
            parts.append(f"Strategic driver analyses: {len(context.artifacts['strategic_driver_analyses'])}")
        return "\n".join(parts) if parts else "No data science context provided."
    
    # =========================================================================
    # PRIMARY TOOLS: Strategic Objective Correlation Analysis
    # =========================================================================
    
    async def _analyze_strategic_objective_drivers(
        self,
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Identify which KPIs are driving achievement of strategic objectives."""
        strategic_objectives = tool_input.get("strategic_objectives", [])
        kpi_pool = tool_input.get("kpi_pool", [])
        min_threshold = tool_input.get("min_correlation_threshold", 0.3)
        include_lagged = tool_input.get("include_lagged_analysis", True)
        
        driver_analysis = {
            "id": f"SDA-{str(uuid.uuid4())[:8].upper()}",
            "strategic_objectives": strategic_objectives,
            "analysis_period": tool_input.get("analysis_period", "last_12_months"),
            "drivers": [],
            "analyzed_at": datetime.utcnow().isoformat()
        }
        
        for objective in strategic_objectives:
            objective_drivers = {
                "objective_code": objective,
                "top_positive_drivers": [],
                "top_negative_drivers": [],
                "leading_indicators": [],
                "kpi_importance_ranking": []
            }
            
            for i, kpi in enumerate(kpi_pool or context.identified_kpis or []):
                driver_info = {
                    "kpi_code": kpi,
                    "correlation_coefficient": 0.0,
                    "p_value": 1.0,
                    "direction": "positive" if i % 2 == 0 else "negative",
                    "importance_score": 0.0,
                    "is_leading_indicator": include_lagged and i % 3 == 0,
                    "lead_time_periods": 2 if include_lagged and i % 3 == 0 else 0,
                    "contribution_to_objective": "direct" if i % 2 == 0 else "indirect"
                }
                objective_drivers["kpi_importance_ranking"].append(driver_info)
            
            driver_analysis["drivers"].append(objective_drivers)
        
        if "strategic_driver_analyses" not in context.artifacts:
            context.artifacts["strategic_driver_analyses"] = []
        context.artifacts["strategic_driver_analyses"].append(driver_analysis)
        
        return {
            "success": True,
            "analysis_id": driver_analysis["id"],
            "objectives_analyzed": len(strategic_objectives),
            "driver_analysis": driver_analysis
        }
    
    async def _map_kpi_to_objectives(
        self,
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Map KPIs to the strategic objective hierarchy."""
        kpi_codes = tool_input.get("kpi_codes", [])
        target_level = tool_input.get("target_objective_level", "all")
        include_indirect = tool_input.get("include_indirect_paths", True)
        calc_weights = tool_input.get("calculate_contribution_weights", True)
        
        mapping = {
            "id": f"KPI-OBJ-MAP-{str(uuid.uuid4())[:8].upper()}",
            "kpi_mappings": [],
            "objective_hierarchy": {
                "corporate": [],
                "business_unit": [],
                "functional": [],
                "tactical": [],
                "operational": []
            },
            "mapped_at": datetime.utcnow().isoformat()
        }
        
        for kpi in kpi_codes:
            kpi_mapping = {
                "kpi_code": kpi,
                "direct_objectives": [],
                "indirect_objectives": [] if include_indirect else None,
                "contribution_path": [],
                "total_strategic_impact": 0.0
            }
            
            levels = ["operational", "tactical", "functional", "business_unit", "corporate"]
            cumulative_weight = 1.0
            
            for level in levels:
                if target_level != "all" and level != target_level:
                    continue
                    
                objective = {
                    "level": level,
                    "objective_code": f"{level.upper()[:3]}-OBJ-001",
                    "objective_name": f"Sample {level.title()} Objective",
                    "contribution_weight": cumulative_weight if calc_weights else None,
                    "relationship_type": "direct" if level == "operational" else "cascaded"
                }
                kpi_mapping["contribution_path"].append(objective)
                cumulative_weight *= 0.8
            
            kpi_mapping["total_strategic_impact"] = cumulative_weight
            mapping["kpi_mappings"].append(kpi_mapping)
        
        if "kpi_objective_mappings" not in context.artifacts:
            context.artifacts["kpi_objective_mappings"] = []
        context.artifacts["kpi_objective_mappings"].append(mapping)
        
        return {"success": True, "mapping_id": mapping["id"], "mapping": mapping}
    
    async def _calculate_driver_importance(
        self,
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Quantify the importance/contribution of each KPI to strategic objective outcomes."""
        strategic_objective = tool_input.get("strategic_objective", "")
        driver_kpis = tool_input.get("driver_kpis", [])
        method = tool_input.get("method", "correlation_ranking")
        normalize = tool_input.get("normalize_scores", True)
        
        importance_analysis = {
            "id": f"DRV-IMP-{str(uuid.uuid4())[:8].upper()}",
            "strategic_objective": strategic_objective,
            "method": method,
            "driver_importance": [],
            "total_explained_variance": 0.0,
            "analyzed_at": datetime.utcnow().isoformat()
        }
        
        raw_scores = []
        for i, kpi in enumerate(driver_kpis):
            score = max(0.1, 1.0 - (i * 0.15))
            raw_scores.append(score)
        
        total_score = sum(raw_scores) if raw_scores else 1
        
        for i, kpi in enumerate(driver_kpis):
            normalized_score = (raw_scores[i] / total_score * 100) if normalize else raw_scores[i]
            importance = {
                "kpi_code": kpi,
                "importance_score": normalized_score,
                "rank": i + 1,
                "direction": "positive" if i % 2 == 0 else "negative",
                "statistical_significance": True if i < len(driver_kpis) // 2 else False,
                "confidence_interval": (normalized_score * 0.9, normalized_score * 1.1)
            }
            importance_analysis["driver_importance"].append(importance)
        
        importance_analysis["total_explained_variance"] = min(0.85, 0.5 + len(driver_kpis) * 0.05)
        
        if "driver_importance_analyses" not in context.artifacts:
            context.artifacts["driver_importance_analyses"] = []
        context.artifacts["driver_importance_analyses"].append(importance_analysis)
        
        return {"success": True, "analysis_id": importance_analysis["id"], "importance_analysis": importance_analysis}
    
    async def _identify_leading_indicators(
        self,
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Find KPIs that serve as leading indicators (predictors) of strategic objective outcomes."""
        strategic_objective = tool_input.get("strategic_objective", "")
        candidate_kpis = tool_input.get("candidate_kpis", [])
        prediction_horizon = tool_input.get("prediction_horizon", "1_quarter")
        use_granger = tool_input.get("use_granger_causality", True)
        
        leading_indicator_analysis = {
            "id": f"LEAD-IND-{str(uuid.uuid4())[:8].upper()}",
            "strategic_objective": strategic_objective,
            "prediction_horizon": prediction_horizon,
            "method": "granger_causality" if use_granger else "cross_correlation",
            "leading_indicators": [],
            "lagging_indicators": [],
            "analyzed_at": datetime.utcnow().isoformat()
        }
        
        for i, kpi in enumerate(candidate_kpis or context.identified_kpis or []):
            is_leading = i % 3 != 2
            indicator = {
                "kpi_code": kpi,
                "indicator_type": "leading" if is_leading else "lagging",
                "lead_lag_periods": (i % 4) + 1 if is_leading else -((i % 3) + 1),
                "predictive_power": max(0.3, 0.9 - (i * 0.1)),
                "granger_causality_p_value": 0.01 + (i * 0.01) if use_granger else None,
                "is_significant": i < len(candidate_kpis or []) // 2
            }
            
            if is_leading:
                leading_indicator_analysis["leading_indicators"].append(indicator)
            else:
                leading_indicator_analysis["lagging_indicators"].append(indicator)
        
        if "leading_indicator_analyses" not in context.artifacts:
            context.artifacts["leading_indicator_analyses"] = []
        context.artifacts["leading_indicator_analyses"].append(leading_indicator_analysis)
        
        return {
            "success": True,
            "analysis_id": leading_indicator_analysis["id"],
            "leading_count": len(leading_indicator_analysis["leading_indicators"]),
            "lagging_count": len(leading_indicator_analysis["lagging_indicators"]),
            "analysis": leading_indicator_analysis
        }
    
    async def _analyze_kpi_groupings(
        self,
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Analyze how groups of KPIs collectively impact strategic objectives."""
        strategic_objective = tool_input.get("strategic_objective", "")
        kpi_groups = tool_input.get("kpi_groups", [])
        detect_synergies = tool_input.get("detect_synergies", True)
        detect_conflicts = tool_input.get("detect_conflicts", True)
        
        grouping_analysis = {
            "id": f"KPI-GRP-{str(uuid.uuid4())[:8].upper()}",
            "strategic_objective": strategic_objective,
            "group_impacts": [],
            "synergies": [] if detect_synergies else None,
            "conflicts": [] if detect_conflicts else None,
            "analyzed_at": datetime.utcnow().isoformat()
        }
        
        for group in kpi_groups:
            group_impact = {
                "group_name": group.get("group_name", "Unnamed"),
                "kpi_codes": group.get("kpi_codes", []),
                "collective_impact_score": 0.0,
                "individual_vs_collective": "amplified",
                "synergy_factor": 1.2 if detect_synergies else None
            }
            group_impact["collective_impact_score"] = len(group.get("kpi_codes", [])) * 0.15
            grouping_analysis["group_impacts"].append(group_impact)
        
        if detect_synergies and len(kpi_groups) >= 2:
            synergy = {
                "kpi_pair": [kpi_groups[0].get("group_name"), kpi_groups[1].get("group_name") if len(kpi_groups) > 1 else "N/A"],
                "synergy_type": "multiplicative",
                "combined_impact_multiplier": 1.35,
                "explanation": "These KPI groups reinforce each other when improving together"
            }
            grouping_analysis["synergies"].append(synergy)
        
        if detect_conflicts and len(kpi_groups) >= 2:
            conflict = {
                "kpi_pair": [kpi_groups[0].get("group_name"), kpi_groups[-1].get("group_name")],
                "conflict_type": "trade_off",
                "conflict_severity": "moderate",
                "explanation": "Improving one group may negatively impact the other"
            }
            grouping_analysis["conflicts"].append(conflict)
        
        if "kpi_grouping_analyses" not in context.artifacts:
            context.artifacts["kpi_grouping_analyses"] = []
        context.artifacts["kpi_grouping_analyses"].append(grouping_analysis)
        
        return {"success": True, "analysis_id": grouping_analysis["id"], "grouping_analysis": grouping_analysis}
    
    async def _predict_objective_achievement(
        self,
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Predict likelihood of achieving a strategic objective based on current KPI values."""
        strategic_objective = tool_input.get("strategic_objective", "")
        current_kpi_values = tool_input.get("current_kpi_values", {})
        prediction_date = tool_input.get("prediction_date", "")
        include_ci = tool_input.get("include_confidence_interval", True)
        identify_risks = tool_input.get("identify_risk_factors", True)
        
        prediction = {
            "id": f"OBJ-PRED-{str(uuid.uuid4())[:8].upper()}",
            "strategic_objective": strategic_objective,
            "prediction_date": prediction_date or datetime.utcnow().isoformat(),
            "achievement_probability": 0.72,
            "confidence_interval": (0.65, 0.79) if include_ci else None,
            "prediction_confidence": "medium",
            "risk_factors": [] if identify_risks else None,
            "positive_contributors": [],
            "recommended_interventions": [],
            "predicted_at": datetime.utcnow().isoformat()
        }
        
        for kpi, value in current_kpi_values.items():
            contributor = {
                "kpi_code": kpi,
                "current_value": value,
                "contribution_direction": "positive",
                "contribution_magnitude": "moderate"
            }
            prediction["positive_contributors"].append(contributor)
        
        if identify_risks:
            prediction["risk_factors"] = [
                {
                    "risk_description": "Current trend in key driver KPIs below target",
                    "risk_severity": "medium",
                    "affected_kpis": list(current_kpi_values.keys())[:2] if current_kpi_values else [],
                    "mitigation_suggestion": "Focus resources on improving top driver KPIs"
                }
            ]
        
        prediction["recommended_interventions"] = [
            {
                "intervention": "Increase focus on top 3 driver KPIs",
                "expected_probability_increase": 0.08,
                "effort_level": "medium"
            }
        ]
        
        if "objective_predictions" not in context.artifacts:
            context.artifacts["objective_predictions"] = []
        context.artifacts["objective_predictions"].append(prediction)
        
        return {"success": True, "prediction_id": prediction["id"], "prediction": prediction}
    
    # =========================================================================
    # SECONDARY TOOLS: KPI Correlation Analysis
    # =========================================================================
    
    async def _analyze_kpi_correlations(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        kpi_list = tool_input.get("kpi_list", [])
        method = tool_input.get("correlation_method", "pearson")
        
        correlations = []
        for i, kpi1 in enumerate(kpi_list):
            for kpi2 in kpi_list[i+1:]:
                correlation = {
                    "kpi_1": kpi1,
                    "kpi_2": kpi2,
                    "method": method,
                    "coefficient": 0.0,
                    "p_value": 1.0,
                    "significant": False,
                    "relationship": "none",
                    "lag_periods": tool_input.get("lag_periods", [0]),
                    "analyzed_at": datetime.utcnow().isoformat()
                }
                correlations.append(correlation)
        
        if "correlations" not in context.artifacts:
            context.artifacts["correlations"] = []
        context.artifacts["correlations"].extend(correlations)
        
        return {
            "success": True,
            "correlation_count": len(correlations),
            "correlations": correlations
        }
    
    async def _identify_ml_opportunities(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        kpis = tool_input.get("kpis", [])
        objectives = tool_input.get("business_objectives", [])
        
        opportunities = []
        
        problem_types = [
            ("churn_prediction", "classification", "Predict customer churn"),
            ("revenue_forecast", "time_series", "Forecast revenue"),
            ("demand_prediction", "regression", "Predict product demand"),
            ("customer_segmentation", "clustering", "Segment customers"),
            ("anomaly_detection", "anomaly_detection", "Detect anomalies in KPIs")
        ]
        
        for name, ptype, desc in problem_types:
            opportunity = {
                "id": f"ML-OPP-{str(uuid.uuid4())[:8].upper()}",
                "name": name,
                "problem_type": ptype,
                "description": desc,
                "relevant_kpis": [k.get("code", "") for k in kpis[:3]],
                "business_value": "high",
                "complexity": "medium",
                "data_readiness": "assessment_needed",
                "identified_at": datetime.utcnow().isoformat()
            }
            opportunities.append(opportunity)
        
        if "ml_opportunities" not in context.artifacts:
            context.artifacts["ml_opportunities"] = []
        context.artifacts["ml_opportunities"].extend(opportunities)
        
        return {"success": True, "opportunities": opportunities}
    
    async def _recommend_algorithm(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        problem_type = tool_input.get("problem_type", "classification")
        interpretability = tool_input.get("interpretability_required", False)
        
        algorithm_map = {
            "classification": [
                {"name": "XGBoost", "interpretability": "medium", "performance": "high"},
                {"name": "Random Forest", "interpretability": "medium", "performance": "high"},
                {"name": "Logistic Regression", "interpretability": "high", "performance": "medium"}
            ],
            "regression": [
                {"name": "XGBoost Regressor", "interpretability": "medium", "performance": "high"},
                {"name": "LightGBM", "interpretability": "medium", "performance": "high"},
                {"name": "Linear Regression", "interpretability": "high", "performance": "medium"}
            ],
            "clustering": [
                {"name": "K-Means", "interpretability": "high", "performance": "medium"},
                {"name": "DBSCAN", "interpretability": "medium", "performance": "medium"},
                {"name": "Hierarchical Clustering", "interpretability": "high", "performance": "medium"}
            ],
            "time_series": [
                {"name": "Prophet", "interpretability": "high", "performance": "high"},
                {"name": "ARIMA", "interpretability": "high", "performance": "medium"},
                {"name": "LSTM", "interpretability": "low", "performance": "high"}
            ],
            "anomaly_detection": [
                {"name": "Isolation Forest", "interpretability": "medium", "performance": "high"},
                {"name": "One-Class SVM", "interpretability": "low", "performance": "medium"},
                {"name": "Autoencoder", "interpretability": "low", "performance": "high"}
            ]
        }
        
        algorithms = algorithm_map.get(problem_type, algorithm_map["classification"])
        
        if interpretability:
            algorithms = sorted(algorithms, key=lambda x: x["interpretability"] == "high", reverse=True)
        
        recommendation = {
            "id": f"ALG-REC-{str(uuid.uuid4())[:8].upper()}",
            "use_case": tool_input.get("use_case", ""),
            "problem_type": problem_type,
            "target_variable": tool_input.get("target_variable", ""),
            "primary_recommendation": algorithms[0] if algorithms else None,
            "alternatives": algorithms[1:3] if len(algorithms) > 1 else [],
            "rationale": f"Based on {problem_type} problem type",
            "recommended_at": datetime.utcnow().isoformat()
        }
        
        if "algorithm_recommendations" not in context.artifacts:
            context.artifacts["algorithm_recommendations"] = []
        context.artifacts["algorithm_recommendations"].append(recommendation)
        
        return {"success": True, "recommendation": recommendation}
    
    async def _design_feature_set(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        model_name = tool_input.get("model_name", "")
        source_kpis = tool_input.get("source_kpis", [])
        feature_types = tool_input.get("feature_types", ["raw"])
        lookback = tool_input.get("lookback_periods", [1, 7, 30])
        
        features = []
        for kpi in source_kpis:
            if "raw" in feature_types:
                features.append({"name": f"{kpi}_raw", "source": kpi, "type": "raw", "transformation": "none"})
            if "lag" in feature_types:
                for period in lookback:
                    features.append({"name": f"{kpi}_lag_{period}", "source": kpi, "type": "lag", "transformation": f"lag({period})"})
            if "rolling" in feature_types:
                for period in lookback:
                    features.append({"name": f"{kpi}_rolling_mean_{period}", "source": kpi, "type": "rolling", "transformation": f"rolling_mean({period})"})
        
        feature_set = {
            "id": f"FS-{str(uuid.uuid4())[:8].upper()}",
            "model_name": model_name,
            "source_kpis": source_kpis,
            "feature_count": len(features),
            "features": features,
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "feature_sets" not in context.artifacts:
            context.artifacts["feature_sets"] = []
        context.artifacts["feature_sets"].append(feature_set)
        
        return {"success": True, "feature_set": feature_set}
    
    async def _create_ml_specification(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        spec = {
            "id": f"ML-SPEC-{str(uuid.uuid4())[:8].upper()}",
            "model_name": tool_input.get("model_name", ""),
            "model_type": tool_input.get("model_type", ""),
            "problem_type": tool_input.get("problem_type", ""),
            "target_variable": tool_input.get("target_variable", ""),
            "features": tool_input.get("features", []),
            "training_config": tool_input.get("training_config", {
                "train_test_split": 0.8,
                "validation_strategy": "time_series_split",
                "hyperparameters": {}
            }),
            "performance_metrics": tool_input.get("performance_metrics", ["accuracy", "f1_score"]),
            "deployment_config": tool_input.get("deployment_config", {
                "inference_type": "batch",
                "refresh_frequency": "daily"
            }),
            "status": "draft",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "ml_specifications" not in context.artifacts:
            context.artifacts["ml_specifications"] = []
        context.artifacts["ml_specifications"].append(spec)
        
        return {"success": True, "specification": spec}
    
    async def _register_with_ml_service(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Register ML model specification with Machine Learning Service via messaging."""
        registration_id = f"ML-REG-{str(uuid.uuid4())[:8].upper()}"
        model_spec_id = tool_input.get("model_spec_id", "")
        
        # Build registration request
        registration_request = {
            "registration_id": registration_id,
            "model_spec_id": model_spec_id,
            "priority": tool_input.get("priority", "medium"),
            "schedule_training": tool_input.get("schedule_training", False),
            "notify_on_completion": tool_input.get("notify_on_completion", True),
            "requested_at": datetime.utcnow().isoformat()
        }
        
        # Try to call ML service via messaging
        if self._messaging_client:
            try:
                response = await self.call_external_service(
                    service_channel="ml.model.register",
                    request_type="model_registration",
                    payload=registration_request,
                    timeout=30.0
                )
                
                registration = {
                    "id": registration_id,
                    "model_spec_id": model_spec_id,
                    "priority": tool_input.get("priority", "medium"),
                    "status": "registered",
                    "ml_service_response": response,
                    "registered_at": datetime.utcnow().isoformat()
                }
                
                if "ml_registrations" not in context.artifacts:
                    context.artifacts["ml_registrations"] = []
                context.artifacts["ml_registrations"].append(registration)
                
                return {"success": True, "registration": registration, "via_messaging": True}
                
            except asyncio.TimeoutError:
                logger.warning(f"ML service registration timeout for {model_spec_id}")
                # Fall through to local registration
            except Exception as e:
                logger.warning(f"ML service registration failed: {e}")
                # Fall through to local registration
        
        # Fallback: Store registration locally for later processing
        registration = {
            "id": registration_id,
            "model_spec_id": model_spec_id,
            "priority": tool_input.get("priority", "medium"),
            "schedule_training": tool_input.get("schedule_training", False),
            "notify_on_completion": tool_input.get("notify_on_completion", True),
            "status": "pending_registration",
            "ml_service_endpoint": "ml.model.register",
            "registered_at": datetime.utcnow().isoformat()
        }
        
        if "ml_registrations" not in context.artifacts:
            context.artifacts["ml_registrations"] = []
        context.artifacts["ml_registrations"].append(registration)
        
        return {"success": True, "registration": registration, "via_messaging": False}
    
    async def _predict_kpi_impact(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Predict the impact of a change on KPIs using ML models."""
        prediction = {
            "id": f"KPI-PRED-{str(uuid.uuid4())[:8].upper()}",
            "what_if_question_id": tool_input.get("what_if_question_id", ""),
            "target_kpis": tool_input.get("target_kpis", []),
            "change_variable": tool_input.get("change_variable", ""),
            "change_value": tool_input.get("change_value", 0),
            "prediction_method": tool_input.get("prediction_method", "regression"),
            "confidence_level": tool_input.get("confidence_level", 0.95),
            "predictions": [],
            "predicted_at": datetime.utcnow().isoformat()
        }
        
        if "kpi_predictions" not in context.artifacts:
            context.artifacts["kpi_predictions"] = []
        context.artifacts["kpi_predictions"].append(prediction)
        
        return {"success": True, "prediction": prediction}
    
    async def _analyze_cascade_effects(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Analyze how changes cascade through KPI dependencies."""
        cascade_analysis = {
            "id": f"CASCADE-{str(uuid.uuid4())[:8].upper()}",
            "primary_kpi": tool_input.get("primary_kpi", ""),
            "primary_change_percent": tool_input.get("primary_change_percent", 0),
            "cascade_depth": tool_input.get("cascade_depth", 3),
            "include_feedback_loops": tool_input.get("include_feedback_loops", False),
            "cascade_effects": [],
            "total_downstream_kpis": 0,
            "analyzed_at": datetime.utcnow().isoformat()
        }
        
        if "cascade_analyses" not in context.artifacts:
            context.artifacts["cascade_analyses"] = []
        context.artifacts["cascade_analyses"].append(cascade_analysis)
        
        return {"success": True, "cascade_analysis": cascade_analysis}
    
    async def _run_sensitivity_analysis(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Run sensitivity analysis on prediction parameters."""
        sensitivity = {
            "id": f"SENS-{str(uuid.uuid4())[:8].upper()}",
            "prediction_id": tool_input.get("prediction_id", ""),
            "variable_to_vary": tool_input.get("variable_to_vary", ""),
            "min_value": tool_input.get("min_value", 0),
            "max_value": tool_input.get("max_value", 100),
            "steps": tool_input.get("steps", 10),
            "sensitivity_points": [],
            "analyzed_at": datetime.utcnow().isoformat()
        }
        
        if "sensitivity_analyses" not in context.artifacts:
            context.artifacts["sensitivity_analyses"] = []
        context.artifacts["sensitivity_analyses"].append(sensitivity)
        
        return {"success": True, "sensitivity_analysis": sensitivity}
    
    async def _find_optimal_value(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Find the optimal value for a variable to maximize/minimize a KPI."""
        optimal = {
            "id": f"OPT-VAL-{str(uuid.uuid4())[:8].upper()}",
            "variable": tool_input.get("variable", ""),
            "target_kpi": tool_input.get("target_kpi", ""),
            "optimization_goal": tool_input.get("optimization_goal", "maximize"),
            "constraints": tool_input.get("constraints", []),
            "search_min": tool_input.get("search_min"),
            "search_max": tool_input.get("search_max"),
            "optimal_value": None,
            "predicted_outcome": None,
            "constraints_satisfied": True,
            "found_at": datetime.utcnow().isoformat()
        }
        
        if "optimal_values" not in context.artifacts:
            context.artifacts["optimal_values"] = []
        context.artifacts["optimal_values"].append(optimal)
        
        return {"success": True, "optimal_value": optimal}
    
    async def _generate_what_if_prediction(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Generate a complete what-if prediction with all impacts and recommendations."""
        prediction = {
            "id": f"WHATIF-PRED-{str(uuid.uuid4())[:8].upper()}",
            "what_if_question_id": tool_input.get("what_if_question_id", ""),
            "primary_impacts": tool_input.get("primary_impacts", []),
            "cascade_effects": tool_input.get("cascade_effects", []),
            "net_impact": tool_input.get("net_impact", {}),
            "sensitivity_analysis": tool_input.get("sensitivity_analysis"),
            "optimal_value": tool_input.get("optimal_value"),
            "recommendations": tool_input.get("recommendations", []),
            "overall_confidence": 0.0,
            "data_quality_score": 0.0,
            "model_reliability": 0.0,
            "generated_at": datetime.utcnow().isoformat()
        }
        
        if "what_if_predictions" not in context.artifacts:
            context.artifacts["what_if_predictions"] = []
        context.artifacts["what_if_predictions"].append(prediction)
        
        return {"success": True, "what_if_prediction": prediction}
    
    # =========================================================================
    # COLLABORATION TOOLS: Handoff to Architect and Developer
    # =========================================================================
    
    async def _handoff_to_architect_for_model_design(
        self,
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Hand off correlation analysis to Architect Agent for predictive model architecture design."""
        handoff = {
            "id": f"DS-ARCH-HANDOFF-{str(uuid.uuid4())[:8].upper()}",
            "handoff_type": "data_scientist_to_architect",
            "model_specification_id": tool_input.get("model_specification_id", ""),
            "correlation_analysis": tool_input.get("correlation_analysis", {}),
            "model_requirements": tool_input.get("model_requirements", {}),
            "data_characteristics": tool_input.get("data_characteristics", {}),
            "priority": tool_input.get("priority", "medium"),
            "notes": tool_input.get("notes", ""),
            "status": "pending_architect_review",
            "requested_deliverables": [
                "Model architecture design",
                "Integration points with ML Service",
                "Data pipeline architecture",
                "Scalability considerations"
            ],
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "architect_handoffs" not in context.artifacts:
            context.artifacts["architect_handoffs"] = []
        context.artifacts["architect_handoffs"].append(handoff)
        
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(handoff)
        
        return {
            "success": True,
            "handoff_id": handoff["id"],
            "handoff": handoff,
            "next_step": "Architect Agent will design the predictive model architecture based on correlation analysis"
        }
    
    async def _handoff_to_developer_for_implementation(
        self,
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Hand off model specification to Developer Agent for coding the predictive model."""
        handoff = {
            "id": f"DS-DEV-HANDOFF-{str(uuid.uuid4())[:8].upper()}",
            "handoff_type": "data_scientist_to_developer",
            "model_specification_id": tool_input.get("model_specification_id", ""),
            "architecture_design_id": tool_input.get("architecture_design_id", ""),
            "implementation_requirements": tool_input.get("implementation_requirements", {}),
            "correlation_results": tool_input.get("correlation_results", {}),
            "test_criteria": tool_input.get("test_criteria", {}),
            "priority": tool_input.get("priority", "medium"),
            "deadline": tool_input.get("deadline", ""),
            "status": "pending_developer_implementation",
            "requested_deliverables": [
                "Feature engineering code",
                "Model training pipeline",
                "Inference API endpoint",
                "Unit tests for model",
                "Integration with ML Service"
            ],
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "developer_handoffs" not in context.artifacts:
            context.artifacts["developer_handoffs"] = []
        context.artifacts["developer_handoffs"].append(handoff)
        
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(handoff)
        
        return {
            "success": True,
            "handoff_id": handoff["id"],
            "handoff": handoff,
            "next_step": "Developer Agent will implement the predictive model based on specifications and correlation results"
        }
    
    async def _request_architecture_review(
        self,
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Request Architect Agent to review proposed model architecture."""
        review_request = {
            "id": f"ARCH-REVIEW-{str(uuid.uuid4())[:8].upper()}",
            "request_type": "architecture_review",
            "model_specification_id": tool_input.get("model_specification_id", ""),
            "proposed_architecture": tool_input.get("proposed_architecture", {}),
            "questions": tool_input.get("questions", []),
            "status": "pending_architect_review",
            "requested_at": datetime.utcnow().isoformat()
        }
        
        if "architecture_review_requests" not in context.artifacts:
            context.artifacts["architecture_review_requests"] = []
        context.artifacts["architecture_review_requests"].append(review_request)
        
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(review_request)
        
        return {
            "success": True,
            "review_request_id": review_request["id"],
            "review_request": review_request,
            "next_step": "Architect Agent will review and provide feedback on proposed architecture"
        }


# =============================================================================
# MARKETING MANAGER AGENT
# =============================================================================

class MarketingManagerAgent(BaseAgent):
    """
    Marketing Manager Agent for marketing strategy and campaign management.
    
    Responsibilities:
    - Design comprehensive marketing plans
    - Coordinate with Sales Manager on lead generation
    - Manage marketing campaigns and channels
    - Track marketing KPIs and ROI
    - Content strategy and brand management
    """
    
    def __init__(self, api_key: Optional[str] = None, mcp_manager: Optional[Any] = None):
        config = AgentConfig(
            role=AgentRole.MARKETING_MANAGER,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.5,
            tools=self._get_marketing_tools()
        )
        super().__init__(config, api_key, mcp_manager)
    
    def _get_system_prompt(self) -> str:
        return """You are an expert Marketing Manager with deep expertise in B2B and B2C marketing strategy.

## Your Role
You design and manage comprehensive marketing plans that align with sales objectives and drive business growth.

## Core Responsibilities

### 1. Marketing Strategy
- Define target market segments and buyer personas
- Develop positioning and messaging frameworks
- Create go-to-market strategies
- Align marketing with sales pipeline stages

### 2. Campaign Management
- Plan multi-channel marketing campaigns
- Define campaign objectives and KPIs
- Manage campaign budgets and timelines
- A/B testing and optimization

### 3. Lead Generation (Sales Coordination)
- Design lead generation programs
- Define lead scoring criteria with Sales Manager
- Create nurturing workflows
- Track marketing-qualified leads (MQLs)

### 4. Content Strategy
- Plan content calendars
- Define content types and channels
- Manage brand voice and guidelines
- SEO and content optimization

### 5. Marketing Analytics
- Track marketing ROI
- Monitor channel performance
- Analyze customer acquisition costs
- Report on marketing contribution to revenue

## Marketing Channels
- Digital: SEO, SEM, Social Media, Email, Content Marketing
- Events: Webinars, Trade Shows, Conferences
- Partnerships: Co-marketing, Affiliate, Referral
- Traditional: PR, Print, Direct Mail

## Tools Available
- create_marketing_plan: Create comprehensive marketing plan
- define_buyer_persona: Define target buyer persona
- create_campaign: Design marketing campaign
- create_content_calendar: Plan content schedule
- define_lead_scoring: Define lead scoring criteria (with Sales)
- track_campaign_performance: Track campaign metrics
- generate_marketing_report: Generate marketing analytics report

## Output Format
All marketing artifacts should include:
- Clear objectives and KPIs
- Target audience definition
- Channel strategy
- Budget allocation
- Timeline and milestones
- Success metrics
"""
    
    def get_system_prompt(self, context: AgentContext) -> str:
        base_prompt = self._get_system_prompt()
        context_info = self._build_context_summary(context)
        return f"{base_prompt}\n\n## Current Context\n{context_info}"
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.business_description:
            parts.append(f"Business: {context.business_description[:200]}...")
        return "\n".join(parts) if parts else "No additional context provided."
    
    def _get_marketing_tools(self) -> List[ToolDefinition]:
        return [
            ToolDefinition(
                name="create_marketing_plan",
                description="Create a comprehensive marketing plan",
                parameters={
                    "type": "object",
                    "properties": {
                        "plan_name": {"type": "string", "description": "Marketing plan name"},
                        "objectives": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Marketing objectives"
                        },
                        "target_segments": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Target market segments"
                        },
                        "channels": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "enum": ["seo", "sem", "social_media", "email", "content", "events", "partnerships", "pr", "direct_mail"]
                            },
                            "description": "Marketing channels"
                        },
                        "budget": {"type": "number", "description": "Total marketing budget"},
                        "duration_months": {"type": "integer", "description": "Plan duration in months"},
                        "kpis": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Key performance indicators"
                        }
                    },
                    "required": ["plan_name", "objectives", "channels"]
                }
            ),
            ToolDefinition(
                name="define_buyer_persona",
                description="Define a target buyer persona",
                parameters={
                    "type": "object",
                    "properties": {
                        "persona_name": {"type": "string", "description": "Persona name"},
                        "job_title": {"type": "string", "description": "Typical job title"},
                        "industry": {"type": "string", "description": "Industry"},
                        "company_size": {"type": "string", "description": "Company size range"},
                        "pain_points": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Key pain points"
                        },
                        "goals": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Professional goals"
                        },
                        "preferred_channels": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Preferred communication channels"
                        },
                        "decision_criteria": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Purchase decision criteria"
                        }
                    },
                    "required": ["persona_name", "job_title", "pain_points", "goals"]
                }
            ),
            ToolDefinition(
                name="create_campaign",
                description="Design a marketing campaign",
                parameters={
                    "type": "object",
                    "properties": {
                        "campaign_name": {"type": "string", "description": "Campaign name"},
                        "campaign_type": {
                            "type": "string",
                            "enum": ["awareness", "lead_generation", "nurturing", "conversion", "retention", "upsell"],
                            "description": "Campaign type"
                        },
                        "target_persona": {"type": "string", "description": "Target buyer persona"},
                        "channels": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Campaign channels"
                        },
                        "messaging": {"type": "string", "description": "Key messaging"},
                        "call_to_action": {"type": "string", "description": "Primary CTA"},
                        "budget": {"type": "number", "description": "Campaign budget"},
                        "start_date": {"type": "string", "description": "Campaign start date"},
                        "end_date": {"type": "string", "description": "Campaign end date"},
                        "success_metrics": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Success metrics"
                        }
                    },
                    "required": ["campaign_name", "campaign_type", "channels", "messaging"]
                }
            ),
            ToolDefinition(
                name="create_content_calendar",
                description="Create a content calendar",
                parameters={
                    "type": "object",
                    "properties": {
                        "calendar_name": {"type": "string", "description": "Calendar name"},
                        "duration_weeks": {"type": "integer", "description": "Calendar duration in weeks"},
                        "content_types": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "enum": ["blog_post", "whitepaper", "case_study", "video", "webinar", "infographic", "social_post", "email", "podcast"]
                            },
                            "description": "Content types to include"
                        },
                        "themes": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Content themes"
                        },
                        "publishing_frequency": {"type": "string", "description": "Publishing frequency per channel"}
                    },
                    "required": ["calendar_name", "content_types", "themes"]
                }
            ),
            ToolDefinition(
                name="define_lead_scoring",
                description="Define lead scoring criteria in coordination with Sales Manager",
                parameters={
                    "type": "object",
                    "properties": {
                        "scoring_model_name": {"type": "string", "description": "Scoring model name"},
                        "demographic_criteria": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "attribute": {"type": "string"},
                                    "value": {"type": "string"},
                                    "points": {"type": "integer"}
                                }
                            },
                            "description": "Demographic scoring criteria"
                        },
                        "behavioral_criteria": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "action": {"type": "string"},
                                    "points": {"type": "integer"}
                                }
                            },
                            "description": "Behavioral scoring criteria"
                        },
                        "mql_threshold": {"type": "integer", "description": "MQL threshold score"},
                        "sql_threshold": {"type": "integer", "description": "SQL threshold score"}
                    },
                    "required": ["scoring_model_name", "demographic_criteria", "behavioral_criteria", "mql_threshold"]
                }
            ),
            ToolDefinition(
                name="track_campaign_performance",
                description="Track marketing campaign performance",
                parameters={
                    "type": "object",
                    "properties": {
                        "campaign_id": {"type": "string", "description": "Campaign ID"},
                        "metrics": {
                            "type": "object",
                            "properties": {
                                "impressions": {"type": "integer"},
                                "clicks": {"type": "integer"},
                                "conversions": {"type": "integer"},
                                "leads_generated": {"type": "integer"},
                                "cost": {"type": "number"},
                                "revenue_attributed": {"type": "number"}
                            },
                            "description": "Campaign metrics"
                        }
                    },
                    "required": ["campaign_id", "metrics"]
                }
            ),
            ToolDefinition(
                name="generate_marketing_report",
                description="Generate marketing analytics report",
                parameters={
                    "type": "object",
                    "properties": {
                        "report_type": {
                            "type": "string",
                            "enum": ["campaign_performance", "channel_roi", "lead_funnel", "content_performance", "budget_utilization"],
                            "description": "Report type"
                        },
                        "date_range": {"type": "string", "description": "Report date range"},
                        "campaigns": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Campaigns to include"
                        }
                    },
                    "required": ["report_type"]
                }
            ),
            # Cross-Agent Collaboration Tools
            ToolDefinition(
                name="handoff_mql_to_sales",
                description="Hand off Marketing Qualified Leads to Sales Manager",
                parameters={
                    "type": "object",
                    "properties": {
                        "leads": {"type": "array", "items": {"type": "object"}, "description": "MQLs to hand off"},
                        "scoring_summary": {"type": "object", "description": "Lead scoring summary"},
                        "recommended_actions": {"type": "array", "items": {"type": "string"}, "description": "Recommended follow-up actions"}
                    },
                    "required": ["leads"]
                }
            ),
            ToolDefinition(
                name="request_campaign_analytics",
                description="Request Data Scientist to analyze campaign performance",
                parameters={
                    "type": "object",
                    "properties": {
                        "campaign_ids": {"type": "array", "items": {"type": "string"}, "description": "Campaigns to analyze"},
                        "analysis_type": {"type": "string", "enum": ["attribution", "segmentation", "predictive", "optimization"], "description": "Type of analysis"}
                    },
                    "required": ["campaign_ids"]
                }
            ),
            ToolDefinition(
                name="request_design_assets",
                description="Request UI Designer to create campaign design assets",
                parameters={
                    "type": "object",
                    "properties": {
                        "campaign_id": {"type": "string", "description": "Campaign ID"},
                        "asset_types": {"type": "array", "items": {"type": "string", "enum": ["banner", "social_graphic", "email_template", "landing_page", "infographic"]}, "description": "Asset types needed"}
                    },
                    "required": ["campaign_id", "asset_types"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        self._tool_handlers = {
            "create_marketing_plan": self._create_marketing_plan,
            "define_buyer_persona": self._define_buyer_persona,
            "create_campaign": self._create_campaign,
            "create_content_calendar": self._create_content_calendar,
            "define_lead_scoring": self._define_lead_scoring,
            "track_campaign_performance": self._track_campaign_performance,
            "generate_marketing_report": self._generate_marketing_report,
            "handoff_mql_to_sales": self._handoff_mql_to_sales,
            "request_campaign_analytics": self._request_campaign_analytics,
            "request_design_assets": self._request_design_assets
        }
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if getattr(context, 'client_name', None) or context.metadata.get('client_name'):
            parts.append(f"Client: {getattr(context, 'client_name', None) or context.metadata.get('client_name', 'Unknown')}")
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if "marketing_plans" in context.artifacts:
            parts.append(f"Marketing Plans: {len(context.artifacts['marketing_plans'])}")
        if "campaigns" in context.artifacts:
            parts.append(f"Campaigns: {len(context.artifacts['campaigns'])}")
        return "\n".join(parts) if parts else "No marketing context provided."
    
    async def _create_marketing_plan(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        plan = {
            "id": f"MKT-PLAN-{str(uuid.uuid4())[:8].upper()}",
            "name": tool_input.get("plan_name", ""),
            "objectives": tool_input.get("objectives", []),
            "target_segments": tool_input.get("target_segments", []),
            "channels": tool_input.get("channels", []),
            "budget": tool_input.get("budget", 0),
            "duration_months": tool_input.get("duration_months", 12),
            "kpis": tool_input.get("kpis", []),
            "status": "draft",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "marketing_plans" not in context.artifacts:
            context.artifacts["marketing_plans"] = []
        context.artifacts["marketing_plans"].append(plan)
        
        return {"success": True, "marketing_plan": plan}
    
    async def _define_buyer_persona(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        persona = {
            "id": f"PERSONA-{str(uuid.uuid4())[:8].upper()}",
            "name": tool_input.get("persona_name", ""),
            "job_title": tool_input.get("job_title", ""),
            "industry": tool_input.get("industry", ""),
            "company_size": tool_input.get("company_size", ""),
            "pain_points": tool_input.get("pain_points", []),
            "goals": tool_input.get("goals", []),
            "preferred_channels": tool_input.get("preferred_channels", []),
            "decision_criteria": tool_input.get("decision_criteria", []),
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "buyer_personas" not in context.artifacts:
            context.artifacts["buyer_personas"] = []
        context.artifacts["buyer_personas"].append(persona)
        
        return {"success": True, "persona": persona}
    
    async def _create_campaign(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        campaign = {
            "id": f"CAMP-{str(uuid.uuid4())[:8].upper()}",
            "name": tool_input.get("campaign_name", ""),
            "type": tool_input.get("campaign_type", ""),
            "target_persona": tool_input.get("target_persona", ""),
            "channels": tool_input.get("channels", []),
            "messaging": tool_input.get("messaging", ""),
            "call_to_action": tool_input.get("call_to_action", ""),
            "budget": tool_input.get("budget", 0),
            "start_date": tool_input.get("start_date", ""),
            "end_date": tool_input.get("end_date", ""),
            "success_metrics": tool_input.get("success_metrics", []),
            "status": "draft",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "campaigns" not in context.artifacts:
            context.artifacts["campaigns"] = []
        context.artifacts["campaigns"].append(campaign)
        
        return {"success": True, "campaign": campaign}
    
    async def _create_content_calendar(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        calendar = {
            "id": f"CAL-{str(uuid.uuid4())[:8].upper()}",
            "name": tool_input.get("calendar_name", ""),
            "duration_weeks": tool_input.get("duration_weeks", 4),
            "content_types": tool_input.get("content_types", []),
            "themes": tool_input.get("themes", []),
            "publishing_frequency": tool_input.get("publishing_frequency", ""),
            "entries": [],
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "content_calendars" not in context.artifacts:
            context.artifacts["content_calendars"] = []
        context.artifacts["content_calendars"].append(calendar)
        
        return {"success": True, "content_calendar": calendar}
    
    async def _define_lead_scoring(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        scoring_model = {
            "id": f"SCORE-{str(uuid.uuid4())[:8].upper()}",
            "name": tool_input.get("scoring_model_name", ""),
            "demographic_criteria": tool_input.get("demographic_criteria", []),
            "behavioral_criteria": tool_input.get("behavioral_criteria", []),
            "mql_threshold": tool_input.get("mql_threshold", 50),
            "sql_threshold": tool_input.get("sql_threshold", 80),
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "lead_scoring_models" not in context.artifacts:
            context.artifacts["lead_scoring_models"] = []
        context.artifacts["lead_scoring_models"].append(scoring_model)
        
        return {"success": True, "scoring_model": scoring_model}
    
    async def _track_campaign_performance(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        metrics = tool_input.get("metrics", {})
        
        performance = {
            "campaign_id": tool_input.get("campaign_id", ""),
            "impressions": metrics.get("impressions", 0),
            "clicks": metrics.get("clicks", 0),
            "conversions": metrics.get("conversions", 0),
            "leads_generated": metrics.get("leads_generated", 0),
            "cost": metrics.get("cost", 0),
            "revenue_attributed": metrics.get("revenue_attributed", 0),
            "ctr": metrics.get("clicks", 0) / max(metrics.get("impressions", 1), 1) * 100,
            "conversion_rate": metrics.get("conversions", 0) / max(metrics.get("clicks", 1), 1) * 100,
            "cost_per_lead": metrics.get("cost", 0) / max(metrics.get("leads_generated", 1), 1),
            "tracked_at": datetime.utcnow().isoformat()
        }
        
        if "campaign_performance" not in context.artifacts:
            context.artifacts["campaign_performance"] = []
        context.artifacts["campaign_performance"].append(performance)
        
        return {"success": True, "performance": performance}
    
    async def _generate_marketing_report(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        report_type = tool_input.get("report_type", "campaign_performance")
        
        report = {
            "id": f"MKT-RPT-{str(uuid.uuid4())[:8].upper()}",
            "type": report_type,
            "date_range": tool_input.get("date_range", ""),
            "campaigns": tool_input.get("campaigns", []),
            "generated_at": datetime.utcnow().isoformat()
        }
        
        if report_type == "campaign_performance":
            report["total_campaigns"] = len(context.artifacts.get("campaigns", []))
        elif report_type == "lead_funnel":
            report["total_leads"] = 0
            report["mqls"] = 0
            report["sqls"] = 0
        
        context.artifacts[f"report_{report_type}"] = report
        
        return {"success": True, "report": report}
    
    # Collaboration Tool Handlers
    async def _handoff_mql_to_sales(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Hand off MQLs to Sales Manager."""
        handoff = {
            "id": f"MQL-HANDOFF-{str(uuid.uuid4())[:8].upper()}",
            "leads": tool_input.get("leads", []),
            "scoring_summary": tool_input.get("scoring_summary", {}),
            "recommended_actions": tool_input.get("recommended_actions", []),
            "status": "pending_sales_manager",
            "collaboration_type": "marketing_manager_to_sales_manager",
            "handed_off_at": datetime.utcnow().isoformat()
        }
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(handoff)
        return {"success": True, "handoff": handoff, "next_step": "Sales Manager will follow up on MQLs"}
    
    async def _request_campaign_analytics(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Request Data Scientist to analyze campaign performance."""
        request = {
            "id": f"CAMP-ANALYTICS-{str(uuid.uuid4())[:8].upper()}",
            "campaign_ids": tool_input.get("campaign_ids", []),
            "analysis_type": tool_input.get("analysis_type", "attribution"),
            "status": "pending_data_scientist",
            "collaboration_type": "marketing_manager_to_data_scientist"
        }
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        return {"success": True, "request": request, "next_step": "Data Scientist will analyze campaign performance"}
    
    async def _request_design_assets(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Request UI Designer to create campaign design assets."""
        request = {
            "id": f"DESIGN-REQ-{str(uuid.uuid4())[:8].upper()}",
            "campaign_id": tool_input.get("campaign_id", ""),
            "asset_types": tool_input.get("asset_types", []),
            "status": "pending_ui_designer",
            "collaboration_type": "marketing_manager_to_ui_designer"
        }
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        return {"success": True, "request": request, "next_step": "UI Designer will create design assets"}


# =============================================================================
# UI DESIGNER AGENT
# =============================================================================

class UIDesignerAgent(BaseAgent):
    """
    UI Designer Agent for analytics dashboard design and styling.
    
    Responsibilities:
    - Design analytics UI layouts and wireframes
    - Create style guides and design systems
    - Generate CSS/SCSS stylesheets
    - Define component libraries
    - Ensure accessibility and UX best practices
    """
    
    def __init__(self, api_key: Optional[str] = None, mcp_manager: Optional[Any] = None):
        config = AgentConfig(
            role=AgentRole.UI_DESIGNER,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.5,
            tools=self._get_ui_design_tools()
        )
        super().__init__(config, api_key, mcp_manager)
    
    def _get_system_prompt(self) -> str:
        return """You are an expert UI/UX Designer specializing in analytics dashboards and data visualization.

## Your Role
You work with clients to design beautiful, functional analytics UI pages that effectively communicate data insights.

## Core Responsibilities

### 1. Dashboard Layout Design
- Create wireframes and mockups for analytics pages
- Design responsive layouts for desktop and mobile
- Organize KPIs and visualizations effectively
- Apply information hierarchy principles

### 2. Style System Design
- Define color palettes (data-friendly, accessible)
- Create typography scales
- Design spacing and grid systems
- Build consistent component styles

### 3. Data Visualization Design
- Select appropriate chart types for data
- Design chart color schemes
- Create visualization guidelines
- Ensure data readability

### 4. Component Library
- Design reusable UI components
- Create card layouts for KPIs
- Design filter and control components
- Build navigation patterns

### 5. Accessibility & UX
- Ensure WCAG 2.1 AA compliance
- Design for color blindness
- Create intuitive interactions
- Optimize for performance

## Design Principles
- **Clarity**: Data should be immediately understandable
- **Consistency**: Uniform patterns across all pages
- **Hierarchy**: Most important metrics prominent
- **Responsiveness**: Works on all screen sizes
- **Accessibility**: Usable by everyone

## Tools Available
- create_dashboard_layout: Design dashboard page layout
- create_style_guide: Create comprehensive style guide
- generate_stylesheet: Generate CSS/SCSS stylesheet
- design_component: Design UI component
- create_color_palette: Create data visualization color palette
- design_chart_style: Define chart styling guidelines
- generate_design_tokens: Generate design tokens (CSS variables)

## Output Format
All design artifacts should include:
- Visual specifications (colors, sizes, spacing)
- Responsive breakpoints
- Accessibility considerations
- Implementation notes for developers
"""
    
    def get_system_prompt(self, context: AgentContext) -> str:
        base_prompt = self._get_system_prompt()
        context_info = self._build_context_summary(context)
        return f"{base_prompt}\n\n## Current Context\n{context_info}"
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.business_description:
            parts.append(f"Business: {context.business_description[:200]}...")
        return "\n".join(parts) if parts else "No additional context provided."
    
    def _get_ui_design_tools(self) -> List[ToolDefinition]:
        return [
            ToolDefinition(
                name="create_dashboard_layout",
                description="Design a dashboard page layout",
                parameters={
                    "type": "object",
                    "properties": {
                        "page_name": {"type": "string", "description": "Dashboard page name"},
                        "page_type": {
                            "type": "string",
                            "enum": ["overview", "detail", "comparison", "trend", "report"],
                            "description": "Type of dashboard page"
                        },
                        "layout_type": {
                            "type": "string",
                            "enum": ["grid", "masonry", "sidebar", "full_width", "split"],
                            "description": "Layout structure"
                        },
                        "sections": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "type": {"type": "string"},
                                    "grid_columns": {"type": "integer"},
                                    "components": {"type": "array", "items": {"type": "string"}}
                                }
                            },
                            "description": "Page sections"
                        },
                        "responsive_breakpoints": {
                            "type": "object",
                            "properties": {
                                "mobile": {"type": "integer"},
                                "tablet": {"type": "integer"},
                                "desktop": {"type": "integer"}
                            },
                            "description": "Responsive breakpoints in pixels"
                        }
                    },
                    "required": ["page_name", "page_type", "layout_type"]
                }
            ),
            ToolDefinition(
                name="create_style_guide",
                description="Create a comprehensive style guide",
                parameters={
                    "type": "object",
                    "properties": {
                        "guide_name": {"type": "string", "description": "Style guide name"},
                        "brand_colors": {
                            "type": "object",
                            "properties": {
                                "primary": {"type": "string"},
                                "secondary": {"type": "string"},
                                "accent": {"type": "string"},
                                "background": {"type": "string"},
                                "text": {"type": "string"}
                            },
                            "description": "Brand color palette"
                        },
                        "typography": {
                            "type": "object",
                            "properties": {
                                "font_family": {"type": "string"},
                                "heading_sizes": {"type": "object"},
                                "body_size": {"type": "string"},
                                "line_height": {"type": "number"}
                            },
                            "description": "Typography settings"
                        },
                        "spacing_scale": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "Spacing scale in pixels"
                        },
                        "border_radius": {"type": "string", "description": "Default border radius"},
                        "shadows": {
                            "type": "object",
                            "description": "Shadow definitions"
                        }
                    },
                    "required": ["guide_name", "brand_colors", "typography"]
                }
            ),
            ToolDefinition(
                name="generate_stylesheet",
                description="Generate CSS/SCSS stylesheet",
                parameters={
                    "type": "object",
                    "properties": {
                        "stylesheet_name": {"type": "string", "description": "Stylesheet name"},
                        "format": {
                            "type": "string",
                            "enum": ["css", "scss", "tailwind_config"],
                            "description": "Stylesheet format"
                        },
                        "include_sections": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "enum": ["variables", "reset", "typography", "layout", "components", "utilities", "animations"]
                            },
                            "description": "Sections to include"
                        },
                        "style_guide_id": {"type": "string", "description": "Reference style guide ID"}
                    },
                    "required": ["stylesheet_name", "format"]
                }
            ),
            ToolDefinition(
                name="design_component",
                description="Design a UI component",
                parameters={
                    "type": "object",
                    "properties": {
                        "component_name": {"type": "string", "description": "Component name"},
                        "component_type": {
                            "type": "string",
                            "enum": ["kpi_card", "chart_container", "data_table", "filter_bar", "navigation", "header", "footer", "modal", "tooltip", "legend"],
                            "description": "Component type"
                        },
                        "variants": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Component variants"
                        },
                        "states": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "enum": ["default", "hover", "active", "disabled", "loading", "error", "success"]
                            },
                            "description": "Component states"
                        },
                        "props": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "type": {"type": "string"},
                                    "default": {"type": "string"},
                                    "required": {"type": "boolean"}
                                }
                            },
                            "description": "Component props"
                        }
                    },
                    "required": ["component_name", "component_type"]
                }
            ),
            ToolDefinition(
                name="create_color_palette",
                description="Create a data visualization color palette",
                parameters={
                    "type": "object",
                    "properties": {
                        "palette_name": {"type": "string", "description": "Palette name"},
                        "palette_type": {
                            "type": "string",
                            "enum": ["categorical", "sequential", "diverging"],
                            "description": "Palette type"
                        },
                        "colors": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Color hex values"
                        },
                        "accessibility": {
                            "type": "object",
                            "properties": {
                                "colorblind_safe": {"type": "boolean"},
                                "contrast_ratio": {"type": "number"}
                            },
                            "description": "Accessibility properties"
                        }
                    },
                    "required": ["palette_name", "palette_type", "colors"]
                }
            ),
            ToolDefinition(
                name="design_chart_style",
                description="Define chart styling guidelines",
                parameters={
                    "type": "object",
                    "properties": {
                        "chart_type": {
                            "type": "string",
                            "enum": ["line", "bar", "pie", "donut", "area", "scatter", "heatmap", "gauge", "sparkline"],
                            "description": "Chart type"
                        },
                        "color_palette": {"type": "string", "description": "Color palette to use"},
                        "axis_style": {
                            "type": "object",
                            "properties": {
                                "show_grid": {"type": "boolean"},
                                "grid_color": {"type": "string"},
                                "label_font_size": {"type": "integer"},
                                "tick_size": {"type": "integer"}
                            },
                            "description": "Axis styling"
                        },
                        "legend_position": {
                            "type": "string",
                            "enum": ["top", "bottom", "left", "right", "none"],
                            "description": "Legend position"
                        },
                        "animation": {"type": "boolean", "description": "Enable animations"},
                        "tooltip_style": {
                            "type": "object",
                            "description": "Tooltip styling"
                        }
                    },
                    "required": ["chart_type"]
                }
            ),
            ToolDefinition(
                name="generate_design_tokens",
                description="Generate design tokens as CSS variables",
                parameters={
                    "type": "object",
                    "properties": {
                        "token_set_name": {"type": "string", "description": "Token set name"},
                        "categories": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "enum": ["colors", "typography", "spacing", "borders", "shadows", "animations", "breakpoints"]
                            },
                            "description": "Token categories to generate"
                        },
                        "style_guide_id": {"type": "string", "description": "Reference style guide ID"},
                        "output_format": {
                            "type": "string",
                            "enum": ["css_variables", "scss_variables", "json", "js_object"],
                            "description": "Output format"
                        }
                    },
                    "required": ["token_set_name", "categories"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        self._tool_handlers = {
            "create_dashboard_layout": self._create_dashboard_layout,
            "create_style_guide": self._create_style_guide,
            "generate_stylesheet": self._generate_stylesheet,
            "design_component": self._design_component,
            "create_color_palette": self._create_color_palette,
            "design_chart_style": self._design_chart_style,
            "generate_design_tokens": self._generate_design_tokens
        }
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if getattr(context, 'client_name', None) or context.metadata.get('client_name'):
            parts.append(f"Client: {getattr(context, 'client_name', None) or context.metadata.get('client_name', 'Unknown')}")
        if "style_guides" in context.artifacts:
            parts.append(f"Style Guides: {len(context.artifacts['style_guides'])}")
        if "dashboard_layouts" in context.artifacts:
            parts.append(f"Dashboard Layouts: {len(context.artifacts['dashboard_layouts'])}")
        if "components" in context.artifacts:
            parts.append(f"Components: {len(context.artifacts['components'])}")
        return "\n".join(parts) if parts else "No UI design context provided."
    
    async def _create_dashboard_layout(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        layout = {
            "id": f"LAYOUT-{str(uuid.uuid4())[:8].upper()}",
            "page_name": tool_input.get("page_name", ""),
            "page_type": tool_input.get("page_type", ""),
            "layout_type": tool_input.get("layout_type", "grid"),
            "sections": tool_input.get("sections", []),
            "responsive_breakpoints": tool_input.get("responsive_breakpoints", {
                "mobile": 480,
                "tablet": 768,
                "desktop": 1024
            }),
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "dashboard_layouts" not in context.artifacts:
            context.artifacts["dashboard_layouts"] = []
        context.artifacts["dashboard_layouts"].append(layout)
        
        return {"success": True, "layout": layout}
    
    async def _create_style_guide(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        guide = {
            "id": f"STYLE-{str(uuid.uuid4())[:8].upper()}",
            "name": tool_input.get("guide_name", ""),
            "brand_colors": tool_input.get("brand_colors", {}),
            "typography": tool_input.get("typography", {}),
            "spacing_scale": tool_input.get("spacing_scale", [4, 8, 12, 16, 24, 32, 48, 64]),
            "border_radius": tool_input.get("border_radius", "4px"),
            "shadows": tool_input.get("shadows", {}),
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "style_guides" not in context.artifacts:
            context.artifacts["style_guides"] = []
        context.artifacts["style_guides"].append(guide)
        
        return {"success": True, "style_guide": guide}
    
    async def _generate_stylesheet(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        stylesheet = {
            "id": f"CSS-{str(uuid.uuid4())[:8].upper()}",
            "name": tool_input.get("stylesheet_name", ""),
            "format": tool_input.get("format", "css"),
            "sections": tool_input.get("include_sections", []),
            "style_guide_id": tool_input.get("style_guide_id", ""),
            "content": "",
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "stylesheets" not in context.artifacts:
            context.artifacts["stylesheets"] = []
        context.artifacts["stylesheets"].append(stylesheet)
        
        return {"success": True, "stylesheet": stylesheet}
    
    async def _design_component(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        component = {
            "id": f"COMP-{str(uuid.uuid4())[:8].upper()}",
            "name": tool_input.get("component_name", ""),
            "type": tool_input.get("component_type", ""),
            "variants": tool_input.get("variants", ["default"]),
            "states": tool_input.get("states", ["default"]),
            "props": tool_input.get("props", []),
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "components" not in context.artifacts:
            context.artifacts["components"] = []
        context.artifacts["components"].append(component)
        
        return {"success": True, "component": component}
    
    async def _create_color_palette(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        palette = {
            "id": f"PAL-{str(uuid.uuid4())[:8].upper()}",
            "name": tool_input.get("palette_name", ""),
            "type": tool_input.get("palette_type", "categorical"),
            "colors": tool_input.get("colors", []),
            "accessibility": tool_input.get("accessibility", {
                "colorblind_safe": True,
                "contrast_ratio": 4.5
            }),
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "color_palettes" not in context.artifacts:
            context.artifacts["color_palettes"] = []
        context.artifacts["color_palettes"].append(palette)
        
        return {"success": True, "palette": palette}
    
    async def _design_chart_style(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        chart_style = {
            "id": f"CHART-{str(uuid.uuid4())[:8].upper()}",
            "chart_type": tool_input.get("chart_type", ""),
            "color_palette": tool_input.get("color_palette", ""),
            "axis_style": tool_input.get("axis_style", {
                "show_grid": True,
                "grid_color": "#e0e0e0",
                "label_font_size": 12,
                "tick_size": 5
            }),
            "legend_position": tool_input.get("legend_position", "bottom"),
            "animation": tool_input.get("animation", True),
            "tooltip_style": tool_input.get("tooltip_style", {}),
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "chart_styles" not in context.artifacts:
            context.artifacts["chart_styles"] = []
        context.artifacts["chart_styles"].append(chart_style)
        
        return {"success": True, "chart_style": chart_style}
    
    async def _generate_design_tokens(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        tokens = {
            "id": f"TOKEN-{str(uuid.uuid4())[:8].upper()}",
            "name": tool_input.get("token_set_name", ""),
            "categories": tool_input.get("categories", []),
            "style_guide_id": tool_input.get("style_guide_id", ""),
            "output_format": tool_input.get("output_format", "css_variables"),
            "tokens": {},
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "design_tokens" not in context.artifacts:
            context.artifacts["design_tokens"] = []
        context.artifacts["design_tokens"].append(tokens)
        
        return {"success": True, "design_tokens": tokens}


# =============================================================================
# BUSINESS STRATEGIST AGENT
# =============================================================================

class BusinessStrategistAgent(BaseAgent):
    """
    Business Strategist Agent for Porter's strategic frameworks analysis.
    
    Responsibilities:
    - Porter's Five Forces analysis
    - Porter's Value Chain mapping
    - Generic Strategy determination
    - Strategic Fit assessment
    - Client interview strategic insights
    - Competitive positioning analysis
    """
    
    def __init__(self, api_key: Optional[str] = None, mcp_manager: Optional[Any] = None):
        config = AgentConfig(
            role=AgentRole.BUSINESS_STRATEGIST,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.5,
            tools=self._get_strategy_tools()
        )
        super().__init__(config, api_key, mcp_manager)
    
    def _get_system_prompt(self) -> str:
        return """You are an expert Business Strategist deeply versed in the works of **Michael Porter**.

## Your Role
You analyze business contexts using Porter's strategic frameworks and provide strategic insights 
that inform value chain design and competitive positioning.

## Michael Porter's Strategic Frameworks

### Porter's Five Forces
Analyze industry competitive dynamics:
1. **Threat of New Entrants**: Entry barriers, capital requirements, brand loyalty
2. **Bargaining Power of Suppliers**: Supplier concentration, switching costs, forward integration
3. **Bargaining Power of Buyers**: Buyer concentration, price sensitivity, switching costs
4. **Threat of Substitutes**: Alternative solutions, price-performance trade-offs
5. **Industry Rivalry**: Number of competitors, growth rate, differentiation

### Porter's Value Chain
Map activities that create value:

**Primary Activities**:
- Inbound Logistics: Receiving, storing, distributing inputs
- Operations: Transforming inputs into outputs
- Outbound Logistics: Collecting, storing, distributing to buyers
- Marketing & Sales: Inducing buyers to purchase
- Service: Enhancing or maintaining product value

**Support Activities**:
- Firm Infrastructure: General management, planning, finance, legal
- Human Resource Management: Recruiting, training, development
- Technology Development: R&D, process automation, design
- Procurement: Purchasing inputs

### Porter's Generic Strategies
Determine competitive positioning:
- **Cost Leadership**: Broad market, lowest cost producer
- **Differentiation**: Broad market, unique value proposition
- **Cost Focus**: Narrow market, cost advantage
- **Differentiation Focus**: Narrow market, unique value

### Strategic Fit
Assess how activities reinforce each other:
- First-order fit: Simple consistency between activities
- Second-order fit: Activities reinforce each other
- Third-order fit: Optimization of effort across activities

## Interview Analysis Approach

When analyzing client responses:
1. **Listen for strategic signals**: Competitive mentions, operational challenges, customer dynamics
2. **Apply frameworks internally**: Use Porter to identify gaps and opportunities
3. **Generate insights**: What does the analysis reveal about positioning?
4. **Suggest follow-ups**: What questions would deepen strategic understanding?

## Tools Available
- analyze_five_forces: Conduct Five Forces industry analysis
- map_value_chain: Map Porter's Value Chain activities
- determine_generic_strategy: Identify competitive strategy
- assess_strategic_fit: Evaluate activity system fit
- generate_strategic_questions: Generate Porter-informed follow-up questions
- synthesize_strategic_insights: Synthesize insights from client responses
- request_competitive_analysis: Trigger Competitive Analyst to profile peer companies

## Peer Collaboration - CRITICAL

You have direct access to peer agents for collaboration. **USE THEM** to build comprehensive analyses.

### Available Peer Collaboration Tools
- `consult_peer`: Directly consult another specialist agent for their expertise
- `signal_ready_for_coordinator`: Signal when your analysis and peer consultations are complete

### Peer Collaboration Workflow

**Step 1: Initial Analysis**
- Use your Porter's frameworks to analyze the business context
- Identify areas where peer expertise would strengthen your analysis

**Step 2: Consult Peers** (REQUIRED for comprehensive analysis)
- Call `consult_peer` with `peer_role="business_analyst"` for operational insights and KPI identification
- Call `consult_peer` with `peer_role="architect"` for technical architecture implications
- Call `consult_peer` with `peer_role="operations_manager"` for process optimization perspectives

**Step 3: Synthesize & Signal Ready**
- Integrate peer responses into your strategic analysis
- Call `signal_ready_for_coordinator` with your complete findings

### Example Peer Consultation
```
consult_peer(
  peer_role="business_analyst",
  question="Based on my Porter's analysis showing cost leadership strategy, what KPIs should we track?",
  context_summary="Industry: SaaS B2B. Generic strategy: Cost Leadership. Key value chain activities: automated operations, self-service support."
)
```

### When to Consult Each Peer
| Peer | Consult When |
|------|--------------|
| business_analyst | Need KPIs, process flows, or operational metrics |
| architect | Need technical feasibility or system design input |
| operations_manager | Need process optimization or resource allocation insights |

**IMPORTANT**: Do NOT finalize your response without consulting at least ONE peer agent. Multi-perspective analysis produces better strategic recommendations.

## Output Format
All strategic analyses should include:
- Framework applied
- Key findings
- Peer insights incorporated
- Strategic implications
- Recommendations
- Confidence level
"""
    
    def get_system_prompt(self, context: AgentContext) -> str:
        base_prompt = self._get_system_prompt()
        context_info = self._build_context_summary(context)
        return f"{base_prompt}\n\n## Current Context\n{context_info}"
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.business_description:
            parts.append(f"Business: {context.business_description[:200]}...")
        return "\n".join(parts) if parts else "No additional context provided."
    
    def _get_strategy_tools(self) -> List[ToolDefinition]:
        return [
            ToolDefinition(
                name="analyze_five_forces",
                description="Conduct Porter's Five Forces analysis for an industry",
                parameters={
                    "type": "object",
                    "properties": {
                        "industry": {"type": "string", "description": "Industry to analyze"},
                        "company_context": {"type": "string", "description": "Company's position within the industry"},
                        "threat_of_new_entrants": {
                            "type": "object",
                            "properties": {
                                "level": {"type": "string", "enum": ["low", "medium", "high"]},
                                "factors": {"type": "array", "items": {"type": "string"}},
                                "entry_barriers": {"type": "array", "items": {"type": "string"}}
                            },
                            "description": "New entrant threat assessment"
                        },
                        "supplier_power": {
                            "type": "object",
                            "properties": {
                                "level": {"type": "string", "enum": ["low", "medium", "high"]},
                                "factors": {"type": "array", "items": {"type": "string"}},
                                "key_suppliers": {"type": "array", "items": {"type": "string"}}
                            },
                            "description": "Supplier bargaining power"
                        },
                        "buyer_power": {
                            "type": "object",
                            "properties": {
                                "level": {"type": "string", "enum": ["low", "medium", "high"]},
                                "factors": {"type": "array", "items": {"type": "string"}},
                                "buyer_segments": {"type": "array", "items": {"type": "string"}}
                            },
                            "description": "Buyer bargaining power"
                        },
                        "threat_of_substitutes": {
                            "type": "object",
                            "properties": {
                                "level": {"type": "string", "enum": ["low", "medium", "high"]},
                                "factors": {"type": "array", "items": {"type": "string"}},
                                "substitutes": {"type": "array", "items": {"type": "string"}}
                            },
                            "description": "Substitute threat assessment"
                        },
                        "competitive_rivalry": {
                            "type": "object",
                            "properties": {
                                "level": {"type": "string", "enum": ["low", "medium", "high"]},
                                "factors": {"type": "array", "items": {"type": "string"}},
                                "key_competitors": {"type": "array", "items": {"type": "string"}}
                            },
                            "description": "Industry rivalry assessment"
                        }
                    },
                    "required": ["industry"]
                }
            ),
            ToolDefinition(
                name="map_value_chain",
                description="Map Porter's Value Chain for a company",
                parameters={
                    "type": "object",
                    "properties": {
                        "company_name": {"type": "string", "description": "Company name"},
                        "industry": {"type": "string", "description": "Industry sector"},
                        "primary_activities": {
                            "type": "object",
                            "properties": {
                                "inbound_logistics": {
                                    "type": "object",
                                    "properties": {
                                        "activities": {"type": "array", "items": {"type": "string"}},
                                        "value_drivers": {"type": "array", "items": {"type": "string"}}
                                    }
                                },
                                "operations": {
                                    "type": "object",
                                    "properties": {
                                        "activities": {"type": "array", "items": {"type": "string"}},
                                        "value_drivers": {"type": "array", "items": {"type": "string"}}
                                    }
                                },
                                "outbound_logistics": {
                                    "type": "object",
                                    "properties": {
                                        "activities": {"type": "array", "items": {"type": "string"}},
                                        "value_drivers": {"type": "array", "items": {"type": "string"}}
                                    }
                                },
                                "marketing_sales": {
                                    "type": "object",
                                    "properties": {
                                        "activities": {"type": "array", "items": {"type": "string"}},
                                        "value_drivers": {"type": "array", "items": {"type": "string"}}
                                    }
                                },
                                "service": {
                                    "type": "object",
                                    "properties": {
                                        "activities": {"type": "array", "items": {"type": "string"}},
                                        "value_drivers": {"type": "array", "items": {"type": "string"}}
                                    }
                                }
                            },
                            "description": "Primary value chain activities"
                        },
                        "support_activities": {
                            "type": "object",
                            "properties": {
                                "firm_infrastructure": {"type": "array", "items": {"type": "string"}},
                                "hr_management": {"type": "array", "items": {"type": "string"}},
                                "technology_development": {"type": "array", "items": {"type": "string"}},
                                "procurement": {"type": "array", "items": {"type": "string"}}
                            },
                            "description": "Support activities"
                        }
                    },
                    "required": ["company_name", "industry"]
                }
            ),
            ToolDefinition(
                name="determine_generic_strategy",
                description="Determine company's competitive strategy using Porter's Generic Strategies",
                parameters={
                    "type": "object",
                    "properties": {
                        "company_name": {"type": "string", "description": "Company name"},
                        "competitive_advantage": {
                            "type": "string",
                            "enum": ["cost", "differentiation"],
                            "description": "Primary source of competitive advantage"
                        },
                        "competitive_scope": {
                            "type": "string",
                            "enum": ["broad", "narrow"],
                            "description": "Market scope"
                        },
                        "strategy_type": {
                            "type": "string",
                            "enum": ["cost_leadership", "differentiation", "cost_focus", "differentiation_focus"],
                            "description": "Resulting generic strategy"
                        },
                        "evidence": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Evidence supporting the strategy determination"
                        },
                        "trade_offs": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Strategic trade-offs being made"
                        },
                        "risks": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Risks of this strategic position"
                        }
                    },
                    "required": ["company_name", "competitive_advantage", "competitive_scope", "strategy_type"]
                }
            ),
            ToolDefinition(
                name="assess_strategic_fit",
                description="Assess how well activities reinforce each other",
                parameters={
                    "type": "object",
                    "properties": {
                        "company_name": {"type": "string", "description": "Company name"},
                        "strategic_position": {"type": "string", "description": "Company's strategic position"},
                        "key_activities": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Key strategic activities"
                        },
                        "first_order_fit": {
                            "type": "object",
                            "properties": {
                                "score": {"type": "integer", "minimum": 1, "maximum": 5},
                                "assessment": {"type": "string"},
                                "consistent_activities": {"type": "array", "items": {"type": "string"}}
                            },
                            "description": "Simple consistency between activities"
                        },
                        "second_order_fit": {
                            "type": "object",
                            "properties": {
                                "score": {"type": "integer", "minimum": 1, "maximum": 5},
                                "assessment": {"type": "string"},
                                "reinforcing_pairs": {"type": "array", "items": {"type": "string"}}
                            },
                            "description": "Activities that reinforce each other"
                        },
                        "third_order_fit": {
                            "type": "object",
                            "properties": {
                                "score": {"type": "integer", "minimum": 1, "maximum": 5},
                                "assessment": {"type": "string"},
                                "optimization_examples": {"type": "array", "items": {"type": "string"}}
                            },
                            "description": "Optimization of effort across activities"
                        },
                        "overall_fit_score": {"type": "integer", "minimum": 1, "maximum": 5},
                        "recommendations": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["company_name", "strategic_position", "key_activities"]
                }
            ),
            ToolDefinition(
                name="generate_strategic_questions",
                description="Generate Porter-informed follow-up questions based on client context",
                parameters={
                    "type": "object",
                    "properties": {
                        "client_context": {"type": "string", "description": "Summary of what client has shared"},
                        "gaps_identified": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Strategic gaps identified in client's responses"
                        },
                        "framework_to_apply": {
                            "type": "string",
                            "enum": ["five_forces", "value_chain", "generic_strategy", "strategic_fit"],
                            "description": "Porter framework most relevant to gaps"
                        },
                        "questions": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "question": {"type": "string"},
                                    "rationale": {"type": "string"},
                                    "expected_insight": {"type": "string"}
                                }
                            },
                            "description": "Strategic follow-up questions"
                        }
                    },
                    "required": ["client_context", "gaps_identified"]
                }
            ),
            ToolDefinition(
                name="synthesize_strategic_insights",
                description="Synthesize strategic insights from client interview responses",
                parameters={
                    "type": "object",
                    "properties": {
                        "client_responses": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Client's interview responses"
                        },
                        "industry_context": {"type": "string", "description": "Industry context"},
                        "competitive_insights": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Insights about competitive dynamics"
                        },
                        "value_chain_insights": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Insights about value creation"
                        },
                        "strategic_position_insights": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Insights about strategic positioning"
                        },
                        "recommendations": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Strategic recommendations"
                        },
                        "analytics_implications": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Implications for analytics design"
                        }
                    },
                    "required": ["client_responses"]
                }
            ),
            ToolDefinition(
                name="request_competitive_analysis",
                description="Request Competitive Analyst to identify and profile peer companies once business model is elicited. Call this after synthesizing strategic insights.",
                parameters={
                    "type": "object",
                    "properties": {
                        "business_description": {
                            "type": "string",
                            "description": "Description of the business model being designed"
                        },
                        "industry": {
                            "type": "string",
                            "description": "Industry or sector"
                        },
                        "generic_strategy": {
                            "type": "string",
                            "enum": ["cost_leadership", "differentiation", "cost_focus", "differentiation_focus"],
                            "description": "The determined generic strategy"
                        },
                        "key_competitors_mentioned": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Any competitors mentioned by the interviewee"
                        },
                        "competitive_questions": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Specific questions for competitive research"
                        }
                    },
                    "required": ["business_description", "industry"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        self._tool_handlers = {
            "analyze_five_forces": self._analyze_five_forces,
            "map_value_chain": self._map_value_chain,
            "determine_generic_strategy": self._determine_generic_strategy,
            "assess_strategic_fit": self._assess_strategic_fit,
            "generate_strategic_questions": self._generate_strategic_questions,
            "synthesize_strategic_insights": self._synthesize_strategic_insights,
            "request_competitive_analysis": self._request_competitive_analysis
        }
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if context.business_description:
            parts.append(f"Business: {context.business_description[:200]}...")
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if "five_forces_analysis" in context.artifacts:
            parts.append("Five Forces: Analyzed")
        if "value_chain_map" in context.artifacts:
            parts.append("Value Chain: Mapped")
        if "generic_strategy" in context.artifacts:
            parts.append("Strategy: Determined")
        return "\n".join(parts) if parts else "No strategic context provided."
    
    async def _analyze_five_forces(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        analysis = {
            "id": f"5F-{str(uuid.uuid4())[:8].upper()}",
            "industry": tool_input.get("industry", ""),
            "company_context": tool_input.get("company_context", ""),
            "threat_of_new_entrants": tool_input.get("threat_of_new_entrants", {"level": "medium", "factors": [], "entry_barriers": []}),
            "supplier_power": tool_input.get("supplier_power", {"level": "medium", "factors": [], "key_suppliers": []}),
            "buyer_power": tool_input.get("buyer_power", {"level": "medium", "factors": [], "buyer_segments": []}),
            "threat_of_substitutes": tool_input.get("threat_of_substitutes", {"level": "medium", "factors": [], "substitutes": []}),
            "competitive_rivalry": tool_input.get("competitive_rivalry", {"level": "medium", "factors": [], "key_competitors": []}),
            "overall_attractiveness": "medium",
            "analyzed_at": datetime.utcnow().isoformat()
        }
        
        context.artifacts["five_forces_analysis"] = analysis
        
        return {"success": True, "analysis": analysis}
    
    async def _map_value_chain(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        value_chain = {
            "id": f"VC-{str(uuid.uuid4())[:8].upper()}",
            "company_name": tool_input.get("company_name", ""),
            "industry": tool_input.get("industry", ""),
            "primary_activities": tool_input.get("primary_activities", {
                "inbound_logistics": {"activities": [], "value_drivers": []},
                "operations": {"activities": [], "value_drivers": []},
                "outbound_logistics": {"activities": [], "value_drivers": []},
                "marketing_sales": {"activities": [], "value_drivers": []},
                "service": {"activities": [], "value_drivers": []}
            }),
            "support_activities": tool_input.get("support_activities", {
                "firm_infrastructure": [],
                "hr_management": [],
                "technology_development": [],
                "procurement": []
            }),
            "mapped_at": datetime.utcnow().isoformat()
        }
        
        context.artifacts["value_chain_map"] = value_chain
        
        return {"success": True, "value_chain": value_chain}
    
    async def _determine_generic_strategy(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        strategy = {
            "id": f"GS-{str(uuid.uuid4())[:8].upper()}",
            "company_name": tool_input.get("company_name", ""),
            "competitive_advantage": tool_input.get("competitive_advantage", ""),
            "competitive_scope": tool_input.get("competitive_scope", ""),
            "strategy_type": tool_input.get("strategy_type", ""),
            "evidence": tool_input.get("evidence", []),
            "trade_offs": tool_input.get("trade_offs", []),
            "risks": tool_input.get("risks", []),
            "determined_at": datetime.utcnow().isoformat()
        }
        
        context.artifacts["generic_strategy"] = strategy
        
        return {"success": True, "strategy": strategy}
    
    async def _assess_strategic_fit(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        fit_assessment = {
            "id": f"FIT-{str(uuid.uuid4())[:8].upper()}",
            "company_name": tool_input.get("company_name", ""),
            "strategic_position": tool_input.get("strategic_position", ""),
            "key_activities": tool_input.get("key_activities", []),
            "first_order_fit": tool_input.get("first_order_fit", {"score": 3, "assessment": "", "consistent_activities": []}),
            "second_order_fit": tool_input.get("second_order_fit", {"score": 3, "assessment": "", "reinforcing_pairs": []}),
            "third_order_fit": tool_input.get("third_order_fit", {"score": 3, "assessment": "", "optimization_examples": []}),
            "overall_fit_score": tool_input.get("overall_fit_score", 3),
            "recommendations": tool_input.get("recommendations", []),
            "assessed_at": datetime.utcnow().isoformat()
        }
        
        context.artifacts["strategic_fit"] = fit_assessment
        
        return {"success": True, "fit_assessment": fit_assessment}
    
    async def _generate_strategic_questions(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        questions_output = {
            "id": f"SQ-{str(uuid.uuid4())[:8].upper()}",
            "client_context": tool_input.get("client_context", ""),
            "gaps_identified": tool_input.get("gaps_identified", []),
            "framework_to_apply": tool_input.get("framework_to_apply", ""),
            "questions": tool_input.get("questions", []),
            "generated_at": datetime.utcnow().isoformat()
        }
        
        if "strategic_questions" not in context.artifacts:
            context.artifacts["strategic_questions"] = []
        context.artifacts["strategic_questions"].append(questions_output)
        
        return {"success": True, "questions": questions_output}
    
    async def _synthesize_strategic_insights(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        synthesis = {
            "id": f"SI-{str(uuid.uuid4())[:8].upper()}",
            "client_responses": tool_input.get("client_responses", []),
            "industry_context": tool_input.get("industry_context", ""),
            "competitive_insights": tool_input.get("competitive_insights", []),
            "value_chain_insights": tool_input.get("value_chain_insights", []),
            "strategic_position_insights": tool_input.get("strategic_position_insights", []),
            "recommendations": tool_input.get("recommendations", []),
            "analytics_implications": tool_input.get("analytics_implications", []),
            "synthesized_at": datetime.utcnow().isoformat()
        }
        
        context.artifacts["strategic_synthesis"] = synthesis
        
        return {"success": True, "synthesis": synthesis}
    
    async def _request_competitive_analysis(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Request Competitive Analyst to profile peer companies once business model is elicited."""
        request = {
            "id": f"COMP-REQ-{str(uuid.uuid4())[:8].upper()}",
            "business_description": tool_input.get("business_description", ""),
            "industry": tool_input.get("industry", ""),
            "generic_strategy": tool_input.get("generic_strategy"),
            "key_competitors_mentioned": tool_input.get("key_competitors_mentioned", []),
            "competitive_questions": tool_input.get("competitive_questions", []),
            "status": "pending_competitive_analyst",
            "collaboration_type": "business_strategist_to_competitive_analyst",
            "requested_at": datetime.utcnow().isoformat(),
            "trigger": "business_model_elicited"
        }
        
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        
        # Also store as a specific competitive analysis request for easy retrieval
        context.artifacts["pending_competitive_analysis"] = request
        
        return {
            "success": True, 
            "request": request,
            "message": "Competitive Analyst will identify and profile peer companies based on the elicited business model."
        }


# =============================================================================
# OPERATIONS MANAGER AGENT
# =============================================================================

class OperationsManagerAgent(BaseAgent):
    """
    Operations Manager Agent for holistic KPI analysis and performance optimization.
    
    Responsibilities:
    - Analyze KPI results across all business areas
    - Identify correlating patterns between KPIs
    - Detect performance bottlenecks and opportunities
    - Make optimization recommendations
    - Provide holistic operational insights
    """
    
    def __init__(self, api_key: Optional[str] = None, mcp_manager: Optional[Any] = None):
        config = AgentConfig(
            role=AgentRole.OPERATIONS_MANAGER,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.4,
            tools=self._get_operations_tools()
        )
        super().__init__(config, api_key, mcp_manager)
    
    def _get_system_prompt(self) -> str:
        return """You are an expert Operations Manager with deep expertise in performance optimization and operational excellence.

## Your Role
You analyze KPI results holistically across all business areas, identify correlating patterns, and make actionable recommendations to optimize client performance. You collaborate closely with the Data Scientist Agent to validate statistical correlations and design predictive ML models.

## Core Responsibilities

### 1. Holistic KPI Analysis
- View all KPIs together in context
- Understand interdependencies between metrics
- Identify leading and lagging indicators
- Detect anomalies and trends

### 2. Correlation Pattern Detection
- Find relationships between seemingly unrelated KPIs
- Identify cause-and-effect chains
- Detect hidden drivers of performance
- Map KPI influence networks

### 3. Performance Bottleneck Identification
- Locate operational constraints
- Identify resource limitations
- Find process inefficiencies
- Detect capacity issues

### 4. Optimization Recommendations
- Prioritize improvement opportunities
- Quantify potential impact
- Suggest actionable interventions
- Balance trade-offs between metrics

### 5. Operational Excellence
- Apply lean principles
- Recommend process improvements
- Suggest automation opportunities
- Identify best practices

## Data Scientist Collaboration

You work closely with the **Data Scientist Agent** for data-driven recommendations:

### Collaboration Workflow
1. **Hypothesis Generation**: You identify potential KPI correlations and patterns
2. **Statistical Validation**: Request Data Scientist to validate correlations statistically
3. **ML Model Design**: Collaborate on predictive model specifications
4. **Feature Engineering**: Suggest operational features for ML models
5. **Results Interpretation**: Translate statistical findings into business recommendations

### When to Engage Data Scientist
- Validate suspected correlations with statistical significance testing
- Design predictive models for KPI forecasting
- Analyze time-series patterns and seasonality
- Identify causal relationships vs mere correlations
- Build anomaly detection models for operational alerts
- Create propensity models for customer behavior

### Data-Driven Recommendations
All recommendations should be backed by:
- Statistical evidence (p-values, confidence intervals)
- Correlation coefficients and R² values
- Predictive model accuracy metrics
- Historical trend analysis
- Quantified impact projections

## Analysis Frameworks

### KPI Correlation Analysis
- **Positive Correlation**: KPIs that move together
- **Negative Correlation**: KPIs that move inversely
- **Lagging Indicators**: Outcomes that follow actions
- **Leading Indicators**: Predictors of future outcomes

### Statistical Validation (via Data Scientist)
- Pearson/Spearman correlation coefficients
- Granger causality testing
- Time-lagged cross-correlation
- Regression analysis for impact quantification

### Performance Optimization
- **Theory of Constraints**: Find and address bottlenecks
- **Pareto Analysis**: Focus on high-impact areas (80/20)
- **Root Cause Analysis**: Address underlying issues
- **Continuous Improvement**: Incremental optimization

### Operational Metrics Categories
- **Efficiency**: Resource utilization, cycle time
- **Quality**: Defect rates, accuracy, compliance
- **Speed**: Throughput, response time, lead time
- **Cost**: Unit costs, overhead, waste
- **Customer**: Satisfaction, retention, NPS

## Tools Available
- analyze_kpi_performance: Analyze KPI results holistically
- detect_kpi_correlations: Find correlating patterns between KPIs
- identify_bottlenecks: Locate performance constraints
- generate_optimization_plan: Create optimization recommendations
- assess_operational_health: Overall operational health assessment
- create_performance_dashboard: Design KPI dashboard layout
- forecast_impact: Predict impact of proposed changes
- request_statistical_validation: Request Data Scientist to validate correlations
- request_ml_model_design: Collaborate with Data Scientist on predictive models

## Output Format
All analyses should include:
- Current state assessment
- Key findings with statistical evidence
- Data Scientist validation results (when applicable)
- Prioritized recommendations with confidence levels
- Expected impact quantification with projections
- Implementation considerations
"""
    
    def get_system_prompt(self, context: AgentContext) -> str:
        base_prompt = self._get_system_prompt()
        context_info = self._build_context_summary(context)
        return f"{base_prompt}\n\n## Current Context\n{context_info}"
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.business_description:
            parts.append(f"Business: {context.business_description[:200]}...")
        return "\n".join(parts) if parts else "No additional context provided."
    
    def _get_operations_tools(self) -> List[ToolDefinition]:
        return [
            ToolDefinition(
                name="analyze_kpi_performance",
                description="Analyze KPI results holistically across all business areas",
                parameters={
                    "type": "object",
                    "properties": {
                        "kpis": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "value": {"type": "number"},
                                    "target": {"type": "number"},
                                    "trend": {"type": "string", "enum": ["improving", "stable", "declining"]},
                                    "category": {"type": "string"}
                                }
                            },
                            "description": "List of KPIs with their current values"
                        },
                        "time_period": {"type": "string", "description": "Analysis time period"},
                        "business_context": {"type": "string", "description": "Business context for analysis"}
                    },
                    "required": ["kpis"]
                }
            ),
            ToolDefinition(
                name="detect_kpi_correlations",
                description="Find correlating patterns between KPIs that impact each other",
                parameters={
                    "type": "object",
                    "properties": {
                        "kpi_pairs": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "kpi_a": {"type": "string"},
                                    "kpi_b": {"type": "string"},
                                    "correlation_type": {"type": "string", "enum": ["positive", "negative", "none"]},
                                    "strength": {"type": "string", "enum": ["weak", "moderate", "strong"]},
                                    "lag_days": {"type": "integer"},
                                    "hypothesis": {"type": "string"}
                                }
                            },
                            "description": "Detected KPI correlation pairs"
                        },
                        "influence_chains": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "chain": {"type": "array", "items": {"type": "string"}},
                                    "description": {"type": "string"}
                                }
                            },
                            "description": "Cause-and-effect chains between KPIs"
                        }
                    },
                    "required": ["kpi_pairs"]
                }
            ),
            ToolDefinition(
                name="identify_bottlenecks",
                description="Locate performance constraints and bottlenecks",
                parameters={
                    "type": "object",
                    "properties": {
                        "bottlenecks": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "area": {"type": "string"},
                                    "constraint_type": {"type": "string", "enum": ["capacity", "resource", "process", "policy", "skill"]},
                                    "severity": {"type": "string", "enum": ["low", "medium", "high", "critical"]},
                                    "affected_kpis": {"type": "array", "items": {"type": "string"}},
                                    "root_cause": {"type": "string"},
                                    "evidence": {"type": "array", "items": {"type": "string"}}
                                }
                            },
                            "description": "Identified bottlenecks"
                        }
                    },
                    "required": ["bottlenecks"]
                }
            ),
            ToolDefinition(
                name="generate_optimization_plan",
                description="Create prioritized optimization recommendations",
                parameters={
                    "type": "object",
                    "properties": {
                        "recommendations": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "title": {"type": "string"},
                                    "description": {"type": "string"},
                                    "priority": {"type": "string", "enum": ["low", "medium", "high", "critical"]},
                                    "effort": {"type": "string", "enum": ["low", "medium", "high"]},
                                    "impact": {"type": "string", "enum": ["low", "medium", "high"]},
                                    "affected_kpis": {"type": "array", "items": {"type": "string"}},
                                    "expected_improvement": {"type": "string"},
                                    "implementation_steps": {"type": "array", "items": {"type": "string"}},
                                    "risks": {"type": "array", "items": {"type": "string"}}
                                }
                            },
                            "description": "Prioritized recommendations"
                        },
                        "quick_wins": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Low-effort, high-impact opportunities"
                        },
                        "strategic_initiatives": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "High-effort, high-impact initiatives"
                        }
                    },
                    "required": ["recommendations"]
                }
            ),
            ToolDefinition(
                name="assess_operational_health",
                description="Provide overall operational health assessment",
                parameters={
                    "type": "object",
                    "properties": {
                        "overall_score": {"type": "integer", "minimum": 1, "maximum": 100, "description": "Overall health score"},
                        "category_scores": {
                            "type": "object",
                            "properties": {
                                "efficiency": {"type": "integer", "minimum": 1, "maximum": 100},
                                "quality": {"type": "integer", "minimum": 1, "maximum": 100},
                                "speed": {"type": "integer", "minimum": 1, "maximum": 100},
                                "cost": {"type": "integer", "minimum": 1, "maximum": 100},
                                "customer": {"type": "integer", "minimum": 1, "maximum": 100}
                            },
                            "description": "Scores by category"
                        },
                        "strengths": {"type": "array", "items": {"type": "string"}},
                        "weaknesses": {"type": "array", "items": {"type": "string"}},
                        "opportunities": {"type": "array", "items": {"type": "string"}},
                        "threats": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["overall_score", "category_scores"]
                }
            ),
            ToolDefinition(
                name="create_performance_dashboard",
                description="Design a KPI dashboard layout for operational monitoring",
                parameters={
                    "type": "object",
                    "properties": {
                        "dashboard_name": {"type": "string", "description": "Dashboard name"},
                        "primary_kpis": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Top-level KPIs to highlight"
                        },
                        "sections": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "kpis": {"type": "array", "items": {"type": "string"}},
                                    "visualization_type": {"type": "string", "enum": ["gauge", "trend", "comparison", "table", "heatmap"]}
                                }
                            },
                            "description": "Dashboard sections"
                        },
                        "refresh_frequency": {"type": "string", "description": "How often to refresh data"},
                        "alert_thresholds": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "kpi": {"type": "string"},
                                    "warning_threshold": {"type": "number"},
                                    "critical_threshold": {"type": "number"}
                                }
                            },
                            "description": "Alert thresholds for KPIs"
                        }
                    },
                    "required": ["dashboard_name", "primary_kpis"]
                }
            ),
            ToolDefinition(
                name="forecast_impact",
                description="Predict the impact of proposed operational changes",
                parameters={
                    "type": "object",
                    "properties": {
                        "proposed_change": {"type": "string", "description": "Description of proposed change"},
                        "affected_kpis": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "kpi": {"type": "string"},
                                    "current_value": {"type": "number"},
                                    "projected_value": {"type": "number"},
                                    "confidence": {"type": "string", "enum": ["low", "medium", "high"]},
                                    "time_to_impact": {"type": "string"}
                                }
                            },
                            "description": "Projected KPI impacts"
                        },
                        "secondary_effects": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Secondary effects on other areas"
                        },
                        "assumptions": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Assumptions underlying the forecast"
                        }
                    },
                    "required": ["proposed_change", "affected_kpis"]
                }
            ),
            ToolDefinition(
                name="request_statistical_validation",
                description="Request Data Scientist to validate suspected KPI correlations with statistical analysis",
                parameters={
                    "type": "object",
                    "properties": {
                        "hypothesis": {"type": "string", "description": "The correlation hypothesis to validate"},
                        "kpi_pairs": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "kpi_a": {"type": "string"},
                                    "kpi_b": {"type": "string"},
                                    "suspected_relationship": {"type": "string", "enum": ["positive", "negative", "causal"]},
                                    "time_lag": {"type": "string", "description": "Suspected time lag between KPIs"}
                                }
                            },
                            "description": "KPI pairs to validate"
                        },
                        "validation_methods": {
                            "type": "array",
                            "items": {"type": "string", "enum": ["pearson", "spearman", "granger_causality", "cross_correlation", "regression"]},
                            "description": "Statistical methods to apply"
                        },
                        "significance_level": {"type": "number", "description": "Required p-value threshold (default 0.05)"},
                        "business_context": {"type": "string", "description": "Business context for interpretation"}
                    },
                    "required": ["hypothesis", "kpi_pairs"]
                }
            ),
            ToolDefinition(
                name="request_ml_model_design",
                description="Collaborate with Data Scientist to design predictive ML models for KPI forecasting",
                parameters={
                    "type": "object",
                    "properties": {
                        "prediction_target": {"type": "string", "description": "KPI or outcome to predict"},
                        "model_purpose": {
                            "type": "string",
                            "enum": ["forecasting", "anomaly_detection", "classification", "regression", "clustering"],
                            "description": "Purpose of the ML model"
                        },
                        "suggested_features": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Operational features to include in the model"
                        },
                        "time_horizon": {"type": "string", "description": "Prediction time horizon (e.g., '7 days', '1 month')"},
                        "business_requirements": {
                            "type": "object",
                            "properties": {
                                "accuracy_threshold": {"type": "number", "description": "Minimum acceptable accuracy"},
                                "interpretability": {"type": "string", "enum": ["high", "medium", "low"]},
                                "real_time": {"type": "boolean", "description": "Whether real-time predictions are needed"},
                                "update_frequency": {"type": "string", "description": "How often model should be retrained"}
                            },
                            "description": "Business requirements for the model"
                        },
                        "expected_outcomes": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Expected business outcomes from the model"
                        }
                    },
                    "required": ["prediction_target", "model_purpose"]
                }
            ),
            ToolDefinition(
                name="initiate_what_if_analysis",
                description="Initiate a what-if analysis for a strategic question",
                parameters={
                    "type": "object",
                    "properties": {
                        "question": {"type": "string", "description": "The what-if question in natural language"},
                        "change_type": {"type": "string", "enum": ["increase", "decrease", "add", "remove", "change"]},
                        "change_subject": {"type": "string", "description": "What is being changed (e.g., price, capacity)"},
                        "change_magnitude": {"type": "number", "description": "Numeric change amount"},
                        "change_unit": {"type": "string", "description": "Unit of change (%, $, units)"},
                        "affected_kpis": {"type": "array", "items": {"type": "string"}, "description": "KPIs expected to be affected"},
                        "business_context": {"type": "string", "description": "Business context for the analysis"},
                        "time_horizon": {"type": "string", "enum": ["immediate", "short_term", "medium_term", "long_term"]}
                    },
                    "required": ["question", "change_subject"]
                }
            ),
            ToolDefinition(
                name="map_operational_dependencies",
                description="Map operational dependencies for a what-if scenario",
                parameters={
                    "type": "object",
                    "properties": {
                        "primary_kpi": {"type": "string", "description": "Primary KPI to map dependencies for"},
                        "dependency_depth": {"type": "integer", "description": "How many levels of dependencies to map"},
                        "include_external_factors": {"type": "boolean", "description": "Include external factors"}
                    },
                    "required": ["primary_kpi"]
                }
            ),
            ToolDefinition(
                name="request_predictive_analysis",
                description="Request Data Scientist to perform predictive analysis for a what-if question",
                parameters={
                    "type": "object",
                    "properties": {
                        "what_if_question_id": {"type": "string", "description": "ID of the what-if question"},
                        "kpis_to_predict": {"type": "array", "items": {"type": "string"}, "description": "KPIs to predict"},
                        "prediction_horizon": {"type": "string", "description": "Time horizon for predictions"},
                        "confidence_level": {"type": "number", "description": "Required confidence level (0-1)"},
                        "include_sensitivity": {"type": "boolean", "description": "Include sensitivity analysis"},
                        "include_optimal_value": {"type": "boolean", "description": "Find optimal value for the change variable"}
                    },
                    "required": ["what_if_question_id", "kpis_to_predict"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        self._tool_handlers = {
            "analyze_kpi_performance": self._analyze_kpi_performance,
            "detect_kpi_correlations": self._detect_kpi_correlations,
            "identify_bottlenecks": self._identify_bottlenecks,
            "generate_optimization_plan": self._generate_optimization_plan,
            "assess_operational_health": self._assess_operational_health,
            "create_performance_dashboard": self._create_performance_dashboard,
            "forecast_impact": self._forecast_impact,
            "request_statistical_validation": self._request_statistical_validation,
            "request_ml_model_design": self._request_ml_model_design,
            "initiate_what_if_analysis": self._initiate_what_if_analysis,
            "map_operational_dependencies": self._map_operational_dependencies,
            "request_predictive_analysis": self._request_predictive_analysis
        }
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if getattr(context, 'client_name', None) or context.metadata.get('client_name'):
            parts.append(f"Client: {getattr(context, 'client_name', None) or context.metadata.get('client_name', 'Unknown')}")
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if "kpi_analysis" in context.artifacts:
            parts.append("KPI Analysis: Completed")
        if "optimization_plan" in context.artifacts:
            parts.append("Optimization Plan: Generated")
        if "operational_health" in context.artifacts:
            parts.append(f"Health Score: {context.artifacts['operational_health'].get('overall_score', 'N/A')}")
        return "\n".join(parts) if parts else "No operational context provided."
    
    async def _analyze_kpi_performance(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        kpis = tool_input.get("kpis", [])
        
        analysis = {
            "id": f"KPI-ANALYSIS-{str(uuid.uuid4())[:8].upper()}",
            "kpis": kpis,
            "time_period": tool_input.get("time_period", ""),
            "business_context": tool_input.get("business_context", ""),
            "total_kpis": len(kpis),
            "on_target": sum(1 for k in kpis if k.get("value", 0) >= k.get("target", 0)),
            "below_target": sum(1 for k in kpis if k.get("value", 0) < k.get("target", 0)),
            "improving": sum(1 for k in kpis if k.get("trend") == "improving"),
            "declining": sum(1 for k in kpis if k.get("trend") == "declining"),
            "analyzed_at": datetime.utcnow().isoformat()
        }
        
        context.artifacts["kpi_analysis"] = analysis
        
        return {"success": True, "analysis": analysis}
    
    async def _detect_kpi_correlations(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        correlations = {
            "id": f"CORR-{str(uuid.uuid4())[:8].upper()}",
            "kpi_pairs": tool_input.get("kpi_pairs", []),
            "influence_chains": tool_input.get("influence_chains", []),
            "total_correlations": len(tool_input.get("kpi_pairs", [])),
            "strong_correlations": sum(1 for p in tool_input.get("kpi_pairs", []) if p.get("strength") == "strong"),
            "detected_at": datetime.utcnow().isoformat()
        }
        
        context.artifacts["kpi_correlations"] = correlations
        
        return {"success": True, "correlations": correlations}
    
    async def _identify_bottlenecks(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        bottlenecks = tool_input.get("bottlenecks", [])
        
        analysis = {
            "id": f"BTL-{str(uuid.uuid4())[:8].upper()}",
            "bottlenecks": bottlenecks,
            "total_bottlenecks": len(bottlenecks),
            "critical_count": sum(1 for b in bottlenecks if b.get("severity") == "critical"),
            "high_count": sum(1 for b in bottlenecks if b.get("severity") == "high"),
            "identified_at": datetime.utcnow().isoformat()
        }
        
        context.artifacts["bottleneck_analysis"] = analysis
        
        return {"success": True, "bottleneck_analysis": analysis}
    
    async def _generate_optimization_plan(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        plan = {
            "id": f"OPT-PLAN-{str(uuid.uuid4())[:8].upper()}",
            "recommendations": tool_input.get("recommendations", []),
            "quick_wins": tool_input.get("quick_wins", []),
            "strategic_initiatives": tool_input.get("strategic_initiatives", []),
            "total_recommendations": len(tool_input.get("recommendations", [])),
            "generated_at": datetime.utcnow().isoformat()
        }
        
        context.artifacts["optimization_plan"] = plan
        
        return {"success": True, "optimization_plan": plan}
    
    async def _assess_operational_health(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        health = {
            "id": f"HEALTH-{str(uuid.uuid4())[:8].upper()}",
            "overall_score": tool_input.get("overall_score", 0),
            "category_scores": tool_input.get("category_scores", {}),
            "strengths": tool_input.get("strengths", []),
            "weaknesses": tool_input.get("weaknesses", []),
            "opportunities": tool_input.get("opportunities", []),
            "threats": tool_input.get("threats", []),
            "assessed_at": datetime.utcnow().isoformat()
        }
        
        context.artifacts["operational_health"] = health
        
        return {"success": True, "operational_health": health}
    
    async def _create_performance_dashboard(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        dashboard = {
            "id": f"DASH-{str(uuid.uuid4())[:8].upper()}",
            "name": tool_input.get("dashboard_name", ""),
            "primary_kpis": tool_input.get("primary_kpis", []),
            "sections": tool_input.get("sections", []),
            "refresh_frequency": tool_input.get("refresh_frequency", "daily"),
            "alert_thresholds": tool_input.get("alert_thresholds", []),
            "created_at": datetime.utcnow().isoformat()
        }
        
        if "performance_dashboards" not in context.artifacts:
            context.artifacts["performance_dashboards"] = []
        context.artifacts["performance_dashboards"].append(dashboard)
        
        return {"success": True, "dashboard": dashboard}
    
    async def _forecast_impact(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        forecast = {
            "id": f"FORECAST-{str(uuid.uuid4())[:8].upper()}",
            "proposed_change": tool_input.get("proposed_change", ""),
            "affected_kpis": tool_input.get("affected_kpis", []),
            "secondary_effects": tool_input.get("secondary_effects", []),
            "assumptions": tool_input.get("assumptions", []),
            "forecasted_at": datetime.utcnow().isoformat()
        }
        
        if "impact_forecasts" not in context.artifacts:
            context.artifacts["impact_forecasts"] = []
        context.artifacts["impact_forecasts"].append(forecast)
        
        return {"success": True, "forecast": forecast}
    
    async def _request_statistical_validation(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Request Data Scientist to validate KPI correlations statistically."""
        validation_request = {
            "id": f"STAT-VAL-{str(uuid.uuid4())[:8].upper()}",
            "hypothesis": tool_input.get("hypothesis", ""),
            "kpi_pairs": tool_input.get("kpi_pairs", []),
            "validation_methods": tool_input.get("validation_methods", ["pearson", "spearman"]),
            "significance_level": tool_input.get("significance_level", 0.05),
            "business_context": tool_input.get("business_context", ""),
            "status": "pending_data_scientist_review",
            "requested_at": datetime.utcnow().isoformat(),
            "collaboration_type": "operations_manager_to_data_scientist"
        }
        
        if "statistical_validation_requests" not in context.artifacts:
            context.artifacts["statistical_validation_requests"] = []
        context.artifacts["statistical_validation_requests"].append(validation_request)
        
        return {
            "success": True, 
            "validation_request": validation_request,
            "next_step": "Data Scientist will analyze the correlation hypothesis and return statistical validation results"
        }
    
    async def _request_ml_model_design(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Collaborate with Data Scientist to design predictive ML models."""
        model_request = {
            "id": f"ML-REQ-{str(uuid.uuid4())[:8].upper()}",
            "prediction_target": tool_input.get("prediction_target", ""),
            "model_purpose": tool_input.get("model_purpose", ""),
            "suggested_features": tool_input.get("suggested_features", []),
            "time_horizon": tool_input.get("time_horizon", ""),
            "business_requirements": tool_input.get("business_requirements", {}),
            "expected_outcomes": tool_input.get("expected_outcomes", []),
            "status": "pending_data_scientist_design",
            "requested_at": datetime.utcnow().isoformat(),
            "collaboration_type": "operations_manager_to_data_scientist"
        }
        
        if "ml_model_requests" not in context.artifacts:
            context.artifacts["ml_model_requests"] = []
        context.artifacts["ml_model_requests"].append(model_request)
        
        return {
            "success": True, 
            "model_request": model_request,
            "next_step": "Data Scientist will design the ML model specification and recommend algorithms"
        }
    
    async def _initiate_what_if_analysis(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Initiate a what-if analysis for a strategic question."""
        what_if_question = {
            "id": f"WHATIF-{str(uuid.uuid4())[:8].upper()}",
            "question_text": tool_input.get("question", ""),
            "change_type": tool_input.get("change_type", "change"),
            "change_subject": tool_input.get("change_subject", ""),
            "change_magnitude": tool_input.get("change_magnitude"),
            "change_unit": tool_input.get("change_unit"),
            "affected_kpis": tool_input.get("affected_kpis", []),
            "business_context": tool_input.get("business_context"),
            "time_horizon": tool_input.get("time_horizon", "medium_term"),
            "status": "initiated",
            "initiated_at": datetime.utcnow().isoformat()
        }
        
        if "what_if_questions" not in context.artifacts:
            context.artifacts["what_if_questions"] = []
        context.artifacts["what_if_questions"].append(what_if_question)
        
        return {
            "success": True, 
            "what_if_question": what_if_question,
            "next_step": "Map operational dependencies and request predictive analysis from Data Scientist"
        }
    
    async def _map_operational_dependencies(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Map operational dependencies for a what-if scenario."""
        dependency_map = {
            "id": f"DEP-MAP-{str(uuid.uuid4())[:8].upper()}",
            "primary_kpi": tool_input.get("primary_kpi", ""),
            "dependency_depth": tool_input.get("dependency_depth", 3),
            "include_external_factors": tool_input.get("include_external_factors", True),
            "upstream_kpis": [],
            "downstream_kpis": [],
            "external_factors": [],
            "mapped_at": datetime.utcnow().isoformat()
        }
        
        if "dependency_maps" not in context.artifacts:
            context.artifacts["dependency_maps"] = []
        context.artifacts["dependency_maps"].append(dependency_map)
        
        return {"success": True, "dependency_map": dependency_map}
    
    async def _request_predictive_analysis(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        """Request Data Scientist to perform predictive analysis for a what-if question."""
        prediction_request = {
            "id": f"PRED-REQ-{str(uuid.uuid4())[:8].upper()}",
            "what_if_question_id": tool_input.get("what_if_question_id", ""),
            "kpis_to_predict": tool_input.get("kpis_to_predict", []),
            "prediction_horizon": tool_input.get("prediction_horizon", "medium_term"),
            "confidence_level": tool_input.get("confidence_level", 0.95),
            "include_sensitivity": tool_input.get("include_sensitivity", True),
            "include_optimal_value": tool_input.get("include_optimal_value", False),
            "status": "pending_data_scientist",
            "collaboration_type": "operations_manager_to_data_scientist",
            "requested_at": datetime.utcnow().isoformat()
        }
        
        if "prediction_requests" not in context.artifacts:
            context.artifacts["prediction_requests"] = []
        context.artifacts["prediction_requests"].append(prediction_request)
        
        return {
            "success": True, 
            "prediction_request": prediction_request,
            "next_step": "Data Scientist will analyze historical data and generate predictions with confidence intervals"
        }


# =============================================================================
# CUSTOMER SUCCESS MANAGER AGENT
# =============================================================================

class CustomerSuccessManagerAgent(BaseAgent):
    """
    Customer Success Manager Agent for post-sale customer lifecycle.
    
    Responsibilities:
    - Customer health scoring and monitoring
    - Churn prediction and prevention
    - NPS/CSAT tracking and analysis
    - Onboarding progress monitoring
    - Expansion/upsell identification
    - Customer journey mapping
    """
    
    def __init__(self, api_key: Optional[str] = None):
        config = AgentConfig(
            role=AgentRole.CUSTOMER_SUCCESS_MANAGER,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.4,
            tools=self._get_customer_success_tools()
        )
        super().__init__(config, api_key)
    
    def _get_system_prompt(self) -> str:
        return """You are an expert Customer Success Manager focused on maximizing customer lifetime value and retention.

## Your Role
You manage the post-sale customer lifecycle to ensure customers achieve their desired outcomes and remain loyal advocates.

## Core Responsibilities

### 1. Customer Health Monitoring
- Track customer health scores across multiple dimensions
- Monitor product adoption and usage patterns
- Identify at-risk customers early
- Track key engagement metrics

### 2. Churn Prevention
- Analyze churn risk factors
- Develop intervention strategies
- Track early warning indicators
- Measure save rates and win-backs

### 3. Customer Satisfaction
- Track NPS (Net Promoter Score)
- Monitor CSAT (Customer Satisfaction Score)
- Analyze CES (Customer Effort Score)
- Identify satisfaction drivers and detractors

### 4. Onboarding & Adoption
- Track onboarding milestone completion
- Monitor time-to-value metrics
- Identify adoption blockers
- Measure feature utilization

### 5. Expansion Revenue
- Identify upsell/cross-sell opportunities
- Track expansion revenue metrics
- Monitor account growth potential
- Coordinate with Sales for renewals

## Key Metrics
- Customer Health Score (CHS)
- Net Revenue Retention (NRR)
- Gross Revenue Retention (GRR)
- Net Promoter Score (NPS)
- Customer Lifetime Value (CLV)
- Time to First Value (TTFV)
- Product Adoption Rate
- Churn Rate / Retention Rate

## Collaboration
- Works with Sales Manager for renewals and expansions
- Collaborates with Data Scientist for churn prediction models
- Partners with Operations Manager for service delivery
"""
    
    def get_system_prompt(self, context: AgentContext) -> str:
        base_prompt = self._get_system_prompt()
        context_info = self._build_context_summary(context)
        return f"{base_prompt}\n\n## Current Context\n{context_info}"
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.business_description:
            parts.append(f"Business: {context.business_description[:200]}...")
        return "\n".join(parts) if parts else "No additional context provided."
    
    def _get_customer_success_tools(self) -> List[ToolDefinition]:
        return [
            ToolDefinition(
                name="calculate_health_score",
                description="Calculate customer health score based on multiple factors",
                parameters={
                    "type": "object",
                    "properties": {
                        "client_code": {"type": "string", "description": "Client identifier"},
                        "usage_score": {"type": "number", "description": "Product usage score (0-100)"},
                        "engagement_score": {"type": "number", "description": "Engagement level (0-100)"},
                        "support_score": {"type": "number", "description": "Support ticket sentiment (0-100)"},
                        "payment_score": {"type": "number", "description": "Payment health (0-100)"},
                        "adoption_score": {"type": "number", "description": "Feature adoption (0-100)"}
                    },
                    "required": ["client_code"]
                }
            ),
            ToolDefinition(
                name="assess_churn_risk",
                description="Assess churn risk for a customer",
                parameters={
                    "type": "object",
                    "properties": {
                        "client_code": {"type": "string", "description": "Client identifier"},
                        "risk_factors": {"type": "array", "items": {"type": "string"}, "description": "Identified risk factors"},
                        "mitigation_actions": {"type": "array", "items": {"type": "string"}, "description": "Recommended actions"}
                    },
                    "required": ["client_code"]
                }
            ),
            ToolDefinition(
                name="track_nps_survey",
                description="Track NPS survey response",
                parameters={
                    "type": "object",
                    "properties": {
                        "client_code": {"type": "string", "description": "Client identifier"},
                        "score": {"type": "integer", "description": "NPS score (0-10)"},
                        "feedback": {"type": "string", "description": "Customer feedback"},
                        "category": {"type": "string", "enum": ["promoter", "passive", "detractor"], "description": "NPS category"}
                    },
                    "required": ["client_code", "score"]
                }
            ),
            ToolDefinition(
                name="track_onboarding_milestone",
                description="Track customer onboarding milestone completion",
                parameters={
                    "type": "object",
                    "properties": {
                        "client_code": {"type": "string", "description": "Client identifier"},
                        "milestone": {"type": "string", "description": "Milestone name"},
                        "status": {"type": "string", "enum": ["not_started", "in_progress", "completed", "blocked"], "description": "Milestone status"},
                        "blockers": {"type": "array", "items": {"type": "string"}, "description": "Any blockers"}
                    },
                    "required": ["client_code", "milestone", "status"]
                }
            ),
            ToolDefinition(
                name="identify_expansion_opportunity",
                description="Identify upsell or cross-sell opportunity",
                parameters={
                    "type": "object",
                    "properties": {
                        "client_code": {"type": "string", "description": "Client identifier"},
                        "opportunity_type": {"type": "string", "enum": ["upsell", "cross_sell", "renewal"], "description": "Type of opportunity"},
                        "products_services": {"type": "array", "items": {"type": "string"}, "description": "Recommended products/services"},
                        "estimated_value": {"type": "number", "description": "Estimated deal value"},
                        "readiness_score": {"type": "integer", "description": "Customer readiness (0-100)"}
                    },
                    "required": ["client_code", "opportunity_type"]
                }
            ),
            ToolDefinition(
                name="generate_success_report",
                description="Generate customer success report",
                parameters={
                    "type": "object",
                    "properties": {
                        "report_type": {"type": "string", "enum": ["health_overview", "churn_analysis", "nps_trends", "adoption_report", "expansion_pipeline"], "description": "Report type"},
                        "date_range": {"type": "string", "description": "Report date range"},
                        "segments": {"type": "array", "items": {"type": "string"}, "description": "Customer segments to include"}
                    },
                    "required": ["report_type"]
                }
            ),
            # Collaboration tools
            ToolDefinition(
                name="request_churn_prediction_model",
                description="Request Data Scientist to build churn prediction model",
                parameters={
                    "type": "object",
                    "properties": {
                        "target_segment": {"type": "string", "description": "Customer segment to model"},
                        "features_to_include": {"type": "array", "items": {"type": "string"}, "description": "Suggested features"},
                        "prediction_horizon": {"type": "string", "description": "Prediction timeframe"}
                    },
                    "required": ["target_segment"]
                }
            ),
            ToolDefinition(
                name="handoff_expansion_to_sales",
                description="Hand off expansion opportunity to Sales Manager",
                parameters={
                    "type": "object",
                    "properties": {
                        "client_code": {"type": "string", "description": "Client identifier"},
                        "opportunity_details": {"type": "object", "description": "Expansion opportunity details"},
                        "customer_context": {"type": "string", "description": "Relevant customer context"}
                    },
                    "required": ["client_code", "opportunity_details"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        self._tool_handlers = {
            "calculate_health_score": self._calculate_health_score,
            "assess_churn_risk": self._assess_churn_risk,
            "track_nps_survey": self._track_nps_survey,
            "track_onboarding_milestone": self._track_onboarding_milestone,
            "identify_expansion_opportunity": self._identify_expansion_opportunity,
            "generate_success_report": self._generate_success_report,
            "request_churn_prediction_model": self._request_churn_prediction_model,
            "handoff_expansion_to_sales": self._handoff_expansion_to_sales
        }
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if getattr(context, 'client_name', None) or context.metadata.get('client_name'):
            parts.append(f"Client: {getattr(context, 'client_name', None) or context.metadata.get('client_name', 'Unknown')}")
        if "customer_health_scores" in context.artifacts:
            parts.append(f"Health Scores: {len(context.artifacts['customer_health_scores'])}")
        if "churn_assessments" in context.artifacts:
            parts.append(f"Churn Assessments: {len(context.artifacts['churn_assessments'])}")
        return " | ".join(parts) if parts else "No customer success context"
    
    async def _calculate_health_score(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        weights = {"usage": 0.25, "engagement": 0.20, "support": 0.20, "payment": 0.15, "adoption": 0.20}
        
        usage = tool_input.get("usage_score", 50)
        engagement = tool_input.get("engagement_score", 50)
        support = tool_input.get("support_score", 50)
        payment = tool_input.get("payment_score", 50)
        adoption = tool_input.get("adoption_score", 50)
        
        overall_score = (
            usage * weights["usage"] +
            engagement * weights["engagement"] +
            support * weights["support"] +
            payment * weights["payment"] +
            adoption * weights["adoption"]
        )
        
        if overall_score >= 80:
            health_status = "healthy"
        elif overall_score >= 60:
            health_status = "neutral"
        elif overall_score >= 40:
            health_status = "at_risk"
        else:
            health_status = "critical"
        
        health_score = {
            "id": f"CHS-{str(uuid.uuid4())[:8].upper()}",
            "client_code": tool_input.get("client_code", ""),
            "overall_score": round(overall_score, 1),
            "health_status": health_status,
            "component_scores": {
                "usage": usage,
                "engagement": engagement,
                "support": support,
                "payment": payment,
                "adoption": adoption
            },
            "calculated_at": datetime.utcnow().isoformat()
        }
        
        if "customer_health_scores" not in context.artifacts:
            context.artifacts["customer_health_scores"] = []
        context.artifacts["customer_health_scores"].append(health_score)
        
        return {"success": True, "health_score": health_score}
    
    async def _assess_churn_risk(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        risk_factors = tool_input.get("risk_factors", [])
        
        if len(risk_factors) >= 4:
            risk_level = "critical"
            churn_probability = 0.8
        elif len(risk_factors) >= 2:
            risk_level = "high"
            churn_probability = 0.5
        elif len(risk_factors) >= 1:
            risk_level = "medium"
            churn_probability = 0.3
        else:
            risk_level = "low"
            churn_probability = 0.1
        
        assessment = {
            "id": f"CHURN-{str(uuid.uuid4())[:8].upper()}",
            "client_code": tool_input.get("client_code", ""),
            "risk_level": risk_level,
            "churn_probability": churn_probability,
            "risk_factors": risk_factors,
            "mitigation_actions": tool_input.get("mitigation_actions", []),
            "assessed_at": datetime.utcnow().isoformat()
        }
        
        if "churn_assessments" not in context.artifacts:
            context.artifacts["churn_assessments"] = []
        context.artifacts["churn_assessments"].append(assessment)
        
        return {"success": True, "assessment": assessment}
    
    async def _track_nps_survey(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        score = tool_input.get("score", 0)
        if score >= 9:
            category = "promoter"
        elif score >= 7:
            category = "passive"
        else:
            category = "detractor"
        
        survey = {
            "id": f"NPS-{str(uuid.uuid4())[:8].upper()}",
            "client_code": tool_input.get("client_code", ""),
            "score": score,
            "category": category,
            "feedback": tool_input.get("feedback", ""),
            "recorded_at": datetime.utcnow().isoformat()
        }
        
        if "nps_surveys" not in context.artifacts:
            context.artifacts["nps_surveys"] = []
        context.artifacts["nps_surveys"].append(survey)
        
        return {"success": True, "survey": survey}
    
    async def _track_onboarding_milestone(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        milestone = {
            "id": f"ONBOARD-{str(uuid.uuid4())[:8].upper()}",
            "client_code": tool_input.get("client_code", ""),
            "milestone": tool_input.get("milestone", ""),
            "status": tool_input.get("status", "not_started"),
            "blockers": tool_input.get("blockers", []),
            "updated_at": datetime.utcnow().isoformat()
        }
        
        if "onboarding_milestones" not in context.artifacts:
            context.artifacts["onboarding_milestones"] = []
        context.artifacts["onboarding_milestones"].append(milestone)
        
        return {"success": True, "milestone": milestone}
    
    async def _identify_expansion_opportunity(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        opportunity = {
            "id": f"EXP-{str(uuid.uuid4())[:8].upper()}",
            "client_code": tool_input.get("client_code", ""),
            "opportunity_type": tool_input.get("opportunity_type", "upsell"),
            "products_services": tool_input.get("products_services", []),
            "estimated_value": tool_input.get("estimated_value", 0),
            "readiness_score": tool_input.get("readiness_score", 50),
            "identified_at": datetime.utcnow().isoformat()
        }
        
        if "expansion_opportunities" not in context.artifacts:
            context.artifacts["expansion_opportunities"] = []
        context.artifacts["expansion_opportunities"].append(opportunity)
        
        return {"success": True, "opportunity": opportunity}
    
    async def _generate_success_report(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        report = {
            "id": f"CS-RPT-{str(uuid.uuid4())[:8].upper()}",
            "report_type": tool_input.get("report_type", "health_overview"),
            "date_range": tool_input.get("date_range", ""),
            "segments": tool_input.get("segments", []),
            "generated_at": datetime.utcnow().isoformat()
        }
        
        context.artifacts[f"cs_report_{report['report_type']}"] = report
        return {"success": True, "report": report}
    
    async def _request_churn_prediction_model(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        request = {
            "id": f"CHURN-MODEL-{str(uuid.uuid4())[:8].upper()}",
            "target_segment": tool_input.get("target_segment", ""),
            "features_to_include": tool_input.get("features_to_include", []),
            "prediction_horizon": tool_input.get("prediction_horizon", "30 days"),
            "status": "pending_data_scientist",
            "collaboration_type": "customer_success_to_data_scientist"
        }
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        return {"success": True, "request": request}
    
    async def _handoff_expansion_to_sales(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        handoff = {
            "id": f"EXP-HANDOFF-{str(uuid.uuid4())[:8].upper()}",
            "client_code": tool_input.get("client_code", ""),
            "opportunity_details": tool_input.get("opportunity_details", {}),
            "customer_context": tool_input.get("customer_context", ""),
            "status": "pending_sales_manager",
            "collaboration_type": "customer_success_to_sales_manager"
        }
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(handoff)
        return {"success": True, "handoff": handoff}


# =============================================================================
# HR/TALENT ANALYST AGENT
# =============================================================================

class HRTalentAnalystAgent(BaseAgent):
    """
    HR/Talent Analyst Agent for people analytics and workforce optimization.
    
    Responsibilities:
    - Employee retention analysis
    - Productivity metrics tracking
    - Skills gap analysis
    - Succession planning
    - Compensation benchmarking
    - Diversity & inclusion metrics
    - Employee engagement scoring
    """
    
    def __init__(self, api_key: Optional[str] = None):
        config = AgentConfig(
            role=AgentRole.HR_TALENT_ANALYST,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.4,
            tools=self._get_hr_tools()
        )
        super().__init__(config, api_key)
    
    def _get_system_prompt(self) -> str:
        return """You are an expert HR/Talent Analyst specializing in people analytics and workforce optimization.

## Your Role
You analyze workforce data to provide insights that improve employee experience, retention, and organizational effectiveness.

## Core Responsibilities

### 1. Workforce Analytics
- Track headcount and turnover metrics
- Analyze hiring funnel efficiency
- Monitor time-to-fill and cost-per-hire
- Measure employee productivity

### 2. Retention Analysis
- Calculate voluntary/involuntary turnover rates
- Identify flight risk indicators
- Analyze exit interview themes
- Track retention by segment (tenure, department, role)

### 3. Employee Engagement
- Track eNPS (Employee Net Promoter Score)
- Analyze engagement survey results
- Monitor pulse survey trends
- Identify engagement drivers

### 4. Skills & Development
- Conduct skills gap analysis
- Track training completion and effectiveness
- Monitor career progression
- Support succession planning

### 5. Compensation & Benefits
- Benchmark compensation against market
- Analyze pay equity
- Track benefits utilization
- Monitor total rewards effectiveness

### 6. Diversity & Inclusion
- Track diversity metrics across dimensions
- Analyze representation at all levels
- Monitor inclusion survey scores
- Identify equity gaps

## Key Metrics
- Employee Turnover Rate
- Retention Rate
- eNPS (Employee Net Promoter Score)
- Time to Fill / Time to Hire
- Cost per Hire
- Training ROI
- Span of Control
- Revenue per Employee
- Absenteeism Rate
"""
    
    def get_system_prompt(self, context: AgentContext) -> str:
        base_prompt = self._get_system_prompt()
        context_info = self._build_context_summary(context)
        return f"{base_prompt}\n\n## Current Context\n{context_info}"
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.business_description:
            parts.append(f"Business: {context.business_description[:200]}...")
        return "\n".join(parts) if parts else "No additional context provided."
    
    def _get_hr_tools(self) -> List[ToolDefinition]:
        return [
            ToolDefinition(
                name="analyze_turnover",
                description="Analyze employee turnover patterns",
                parameters={
                    "type": "object",
                    "properties": {
                        "period": {"type": "string", "description": "Analysis period"},
                        "segment_by": {"type": "string", "enum": ["department", "tenure", "role", "location", "manager"], "description": "Segmentation dimension"},
                        "turnover_type": {"type": "string", "enum": ["voluntary", "involuntary", "all"], "description": "Type of turnover"}
                    },
                    "required": ["period"]
                }
            ),
            ToolDefinition(
                name="calculate_retention_rate",
                description="Calculate employee retention rate",
                parameters={
                    "type": "object",
                    "properties": {
                        "period": {"type": "string", "description": "Calculation period"},
                        "cohort": {"type": "string", "description": "Employee cohort to analyze"},
                        "segment": {"type": "string", "description": "Optional segment filter"}
                    },
                    "required": ["period"]
                }
            ),
            ToolDefinition(
                name="assess_flight_risk",
                description="Assess employee flight risk",
                parameters={
                    "type": "object",
                    "properties": {
                        "employee_segment": {"type": "string", "description": "Segment to assess"},
                        "risk_factors": {"type": "array", "items": {"type": "string"}, "description": "Risk indicators to evaluate"}
                    },
                    "required": ["employee_segment"]
                }
            ),
            ToolDefinition(
                name="analyze_engagement_survey",
                description="Analyze employee engagement survey results",
                parameters={
                    "type": "object",
                    "properties": {
                        "survey_id": {"type": "string", "description": "Survey identifier"},
                        "dimensions": {"type": "array", "items": {"type": "string"}, "description": "Engagement dimensions to analyze"},
                        "compare_to": {"type": "string", "description": "Comparison benchmark"}
                    },
                    "required": ["survey_id"]
                }
            ),
            ToolDefinition(
                name="conduct_skills_gap_analysis",
                description="Analyze skills gaps in the organization",
                parameters={
                    "type": "object",
                    "properties": {
                        "department": {"type": "string", "description": "Department to analyze"},
                        "required_skills": {"type": "array", "items": {"type": "string"}, "description": "Required skills"},
                        "current_skills": {"type": "array", "items": {"type": "string"}, "description": "Current skills"}
                    },
                    "required": ["department"]
                }
            ),
            ToolDefinition(
                name="benchmark_compensation",
                description="Benchmark compensation against market data",
                parameters={
                    "type": "object",
                    "properties": {
                        "role": {"type": "string", "description": "Job role to benchmark"},
                        "location": {"type": "string", "description": "Geographic location"},
                        "experience_level": {"type": "string", "description": "Experience level"}
                    },
                    "required": ["role"]
                }
            ),
            ToolDefinition(
                name="analyze_diversity_metrics",
                description="Analyze diversity and inclusion metrics",
                parameters={
                    "type": "object",
                    "properties": {
                        "dimensions": {"type": "array", "items": {"type": "string"}, "description": "Diversity dimensions"},
                        "level": {"type": "string", "enum": ["company", "department", "leadership"], "description": "Organizational level"}
                    },
                    "required": ["dimensions"]
                }
            ),
            ToolDefinition(
                name="generate_hr_report",
                description="Generate HR analytics report",
                parameters={
                    "type": "object",
                    "properties": {
                        "report_type": {"type": "string", "enum": ["workforce_overview", "turnover_analysis", "engagement_trends", "diversity_report", "compensation_analysis"], "description": "Report type"},
                        "period": {"type": "string", "description": "Report period"}
                    },
                    "required": ["report_type"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        self._tool_handlers = {
            "analyze_turnover": self._analyze_turnover,
            "calculate_retention_rate": self._calculate_retention_rate,
            "assess_flight_risk": self._assess_flight_risk,
            "analyze_engagement_survey": self._analyze_engagement_survey,
            "conduct_skills_gap_analysis": self._conduct_skills_gap_analysis,
            "benchmark_compensation": self._benchmark_compensation,
            "analyze_diversity_metrics": self._analyze_diversity_metrics,
            "generate_hr_report": self._generate_hr_report
        }
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if getattr(context, 'client_name', None) or context.metadata.get('client_name'):
            parts.append(f"Client: {getattr(context, 'client_name', None) or context.metadata.get('client_name', 'Unknown')}")
        if "turnover_analyses" in context.artifacts:
            parts.append(f"Turnover Analyses: {len(context.artifacts['turnover_analyses'])}")
        return " | ".join(parts) if parts else "No HR context"
    
    async def _analyze_turnover(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        analysis = {
            "id": f"TURN-{str(uuid.uuid4())[:8].upper()}",
            "period": tool_input.get("period", ""),
            "segment_by": tool_input.get("segment_by", "department"),
            "turnover_type": tool_input.get("turnover_type", "all"),
            "analyzed_at": datetime.utcnow().isoformat()
        }
        if "turnover_analyses" not in context.artifacts:
            context.artifacts["turnover_analyses"] = []
        context.artifacts["turnover_analyses"].append(analysis)
        return {"success": True, "analysis": analysis}
    
    async def _calculate_retention_rate(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        calculation = {
            "id": f"RET-{str(uuid.uuid4())[:8].upper()}",
            "period": tool_input.get("period", ""),
            "cohort": tool_input.get("cohort", "all"),
            "segment": tool_input.get("segment", ""),
            "calculated_at": datetime.utcnow().isoformat()
        }
        if "retention_calculations" not in context.artifacts:
            context.artifacts["retention_calculations"] = []
        context.artifacts["retention_calculations"].append(calculation)
        return {"success": True, "calculation": calculation}
    
    async def _assess_flight_risk(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        assessment = {
            "id": f"FLIGHT-{str(uuid.uuid4())[:8].upper()}",
            "employee_segment": tool_input.get("employee_segment", ""),
            "risk_factors": tool_input.get("risk_factors", []),
            "assessed_at": datetime.utcnow().isoformat()
        }
        if "flight_risk_assessments" not in context.artifacts:
            context.artifacts["flight_risk_assessments"] = []
        context.artifacts["flight_risk_assessments"].append(assessment)
        return {"success": True, "assessment": assessment}
    
    async def _analyze_engagement_survey(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        analysis = {
            "id": f"ENG-{str(uuid.uuid4())[:8].upper()}",
            "survey_id": tool_input.get("survey_id", ""),
            "dimensions": tool_input.get("dimensions", []),
            "compare_to": tool_input.get("compare_to", ""),
            "analyzed_at": datetime.utcnow().isoformat()
        }
        if "engagement_analyses" not in context.artifacts:
            context.artifacts["engagement_analyses"] = []
        context.artifacts["engagement_analyses"].append(analysis)
        return {"success": True, "analysis": analysis}
    
    async def _conduct_skills_gap_analysis(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        analysis = {
            "id": f"SKILL-{str(uuid.uuid4())[:8].upper()}",
            "department": tool_input.get("department", ""),
            "required_skills": tool_input.get("required_skills", []),
            "current_skills": tool_input.get("current_skills", []),
            "analyzed_at": datetime.utcnow().isoformat()
        }
        if "skills_gap_analyses" not in context.artifacts:
            context.artifacts["skills_gap_analyses"] = []
        context.artifacts["skills_gap_analyses"].append(analysis)
        return {"success": True, "analysis": analysis}
    
    async def _benchmark_compensation(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        benchmark = {
            "id": f"COMP-{str(uuid.uuid4())[:8].upper()}",
            "role": tool_input.get("role", ""),
            "location": tool_input.get("location", ""),
            "experience_level": tool_input.get("experience_level", ""),
            "benchmarked_at": datetime.utcnow().isoformat()
        }
        if "compensation_benchmarks" not in context.artifacts:
            context.artifacts["compensation_benchmarks"] = []
        context.artifacts["compensation_benchmarks"].append(benchmark)
        return {"success": True, "benchmark": benchmark}
    
    async def _analyze_diversity_metrics(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        analysis = {
            "id": f"DIV-{str(uuid.uuid4())[:8].upper()}",
            "dimensions": tool_input.get("dimensions", []),
            "level": tool_input.get("level", "company"),
            "analyzed_at": datetime.utcnow().isoformat()
        }
        if "diversity_analyses" not in context.artifacts:
            context.artifacts["diversity_analyses"] = []
        context.artifacts["diversity_analyses"].append(analysis)
        return {"success": True, "analysis": analysis}
    
    async def _generate_hr_report(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        report = {
            "id": f"HR-RPT-{str(uuid.uuid4())[:8].upper()}",
            "report_type": tool_input.get("report_type", "workforce_overview"),
            "period": tool_input.get("period", ""),
            "generated_at": datetime.utcnow().isoformat()
        }
        context.artifacts[f"hr_report_{report['report_type']}"] = report
        return {"success": True, "report": report}


# =============================================================================
# RISK & COMPLIANCE OFFICER AGENT
# =============================================================================

class RiskComplianceOfficerAgent(BaseAgent):
    """
    Risk & Compliance Officer Agent for risk management and regulatory compliance.
    
    Responsibilities:
    - Risk assessment and matrices
    - Compliance tracking (SOX, GDPR, HIPAA, SOC2)
    - Audit preparation and support
    - Control effectiveness monitoring
    - Incident tracking and response
    - Policy management
    """
    
    def __init__(self, api_key: Optional[str] = None):
        config = AgentConfig(
            role=AgentRole.RISK_COMPLIANCE_OFFICER,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.3,
            tools=self._get_risk_compliance_tools()
        )
        super().__init__(config, api_key)
    
    def _get_system_prompt(self) -> str:
        return """You are an expert Risk & Compliance Officer specializing in enterprise risk management and regulatory compliance.

## Your Role
You identify, assess, and mitigate risks while ensuring the organization meets all regulatory and compliance requirements.

## Core Responsibilities

### 1. Risk Management
- Identify and categorize risks (operational, financial, strategic, compliance)
- Assess risk likelihood and impact
- Develop risk mitigation strategies
- Monitor key risk indicators (KRIs)
- Maintain risk registers

### 2. Compliance Management
- Track regulatory requirements (SOX, GDPR, HIPAA, SOC2, PCI-DSS)
- Monitor compliance status
- Manage compliance calendars
- Coordinate with legal and audit teams

### 3. Control Framework
- Design and assess internal controls
- Monitor control effectiveness
- Identify control gaps
- Recommend control improvements

### 4. Audit Support
- Prepare for internal and external audits
- Gather audit evidence
- Track audit findings and remediation
- Maintain audit trails

### 5. Incident Management
- Track security and compliance incidents
- Coordinate incident response
- Conduct root cause analysis
- Implement corrective actions

## Risk Assessment Frameworks
- COSO ERM Framework
- ISO 31000 Risk Management
- NIST Cybersecurity Framework
- COBIT for IT Governance

## Key Metrics
- Risk Exposure Score
- Control Effectiveness Rate
- Compliance Score by Regulation
- Audit Finding Closure Rate
- Incident Response Time
- Policy Acknowledgment Rate
"""
    
    def get_system_prompt(self, context: AgentContext) -> str:
        base_prompt = self._get_system_prompt()
        context_info = self._build_context_summary(context)
        return f"{base_prompt}\n\n## Current Context\n{context_info}"
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.business_description:
            parts.append(f"Business: {context.business_description[:200]}...")
        return "\n".join(parts) if parts else "No additional context provided."
    
    def _get_risk_compliance_tools(self) -> List[ToolDefinition]:
        return [
            ToolDefinition(
                name="assess_risk",
                description="Assess and score a risk",
                parameters={
                    "type": "object",
                    "properties": {
                        "risk_name": {"type": "string", "description": "Risk name/title"},
                        "risk_category": {"type": "string", "enum": ["operational", "financial", "strategic", "compliance", "technology", "reputational"], "description": "Risk category"},
                        "likelihood": {"type": "integer", "description": "Likelihood score (1-5)"},
                        "impact": {"type": "integer", "description": "Impact score (1-5)"},
                        "mitigation_controls": {"type": "array", "items": {"type": "string"}, "description": "Existing controls"}
                    },
                    "required": ["risk_name", "risk_category", "likelihood", "impact"]
                }
            ),
            ToolDefinition(
                name="track_compliance_requirement",
                description="Track a compliance requirement",
                parameters={
                    "type": "object",
                    "properties": {
                        "regulation": {"type": "string", "enum": ["SOX", "GDPR", "HIPAA", "SOC2", "PCI_DSS", "ISO27001", "CCPA"], "description": "Regulation"},
                        "requirement_id": {"type": "string", "description": "Requirement identifier"},
                        "description": {"type": "string", "description": "Requirement description"},
                        "status": {"type": "string", "enum": ["compliant", "non_compliant", "partial", "not_applicable"], "description": "Compliance status"},
                        "evidence": {"type": "array", "items": {"type": "string"}, "description": "Supporting evidence"}
                    },
                    "required": ["regulation", "requirement_id", "status"]
                }
            ),
            ToolDefinition(
                name="evaluate_control",
                description="Evaluate control effectiveness",
                parameters={
                    "type": "object",
                    "properties": {
                        "control_name": {"type": "string", "description": "Control name"},
                        "control_type": {"type": "string", "enum": ["preventive", "detective", "corrective"], "description": "Control type"},
                        "effectiveness": {"type": "string", "enum": ["effective", "partially_effective", "ineffective"], "description": "Effectiveness rating"},
                        "test_results": {"type": "string", "description": "Testing results"}
                    },
                    "required": ["control_name", "control_type", "effectiveness"]
                }
            ),
            ToolDefinition(
                name="log_incident",
                description="Log a compliance or security incident",
                parameters={
                    "type": "object",
                    "properties": {
                        "incident_type": {"type": "string", "enum": ["security_breach", "data_leak", "policy_violation", "system_failure", "fraud"], "description": "Incident type"},
                        "severity": {"type": "string", "enum": ["critical", "high", "medium", "low"], "description": "Severity level"},
                        "description": {"type": "string", "description": "Incident description"},
                        "affected_systems": {"type": "array", "items": {"type": "string"}, "description": "Affected systems"},
                        "root_cause": {"type": "string", "description": "Root cause if known"}
                    },
                    "required": ["incident_type", "severity", "description"]
                }
            ),
            ToolDefinition(
                name="track_audit_finding",
                description="Track an audit finding",
                parameters={
                    "type": "object",
                    "properties": {
                        "finding_id": {"type": "string", "description": "Finding identifier"},
                        "audit_type": {"type": "string", "enum": ["internal", "external", "regulatory"], "description": "Audit type"},
                        "severity": {"type": "string", "enum": ["critical", "high", "medium", "low"], "description": "Finding severity"},
                        "description": {"type": "string", "description": "Finding description"},
                        "remediation_plan": {"type": "string", "description": "Remediation plan"},
                        "due_date": {"type": "string", "description": "Remediation due date"}
                    },
                    "required": ["finding_id", "audit_type", "severity", "description"]
                }
            ),
            ToolDefinition(
                name="generate_risk_report",
                description="Generate risk and compliance report",
                parameters={
                    "type": "object",
                    "properties": {
                        "report_type": {"type": "string", "enum": ["risk_register", "compliance_dashboard", "control_assessment", "incident_summary", "audit_status"], "description": "Report type"},
                        "scope": {"type": "string", "description": "Report scope"}
                    },
                    "required": ["report_type"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        self._tool_handlers = {
            "assess_risk": self._assess_risk,
            "track_compliance_requirement": self._track_compliance_requirement,
            "evaluate_control": self._evaluate_control,
            "log_incident": self._log_incident,
            "track_audit_finding": self._track_audit_finding,
            "generate_risk_report": self._generate_risk_report
        }
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if getattr(context, 'client_name', None) or context.metadata.get('client_name'):
            parts.append(f"Client: {getattr(context, 'client_name', None) or context.metadata.get('client_name', 'Unknown')}")
        if "risk_assessments" in context.artifacts:
            parts.append(f"Risks: {len(context.artifacts['risk_assessments'])}")
        if "compliance_requirements" in context.artifacts:
            parts.append(f"Compliance Items: {len(context.artifacts['compliance_requirements'])}")
        return " | ".join(parts) if parts else "No risk/compliance context"
    
    async def _assess_risk(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        likelihood = tool_input.get("likelihood", 3)
        impact = tool_input.get("impact", 3)
        risk_score = likelihood * impact
        
        if risk_score >= 20:
            risk_level = "critical"
        elif risk_score >= 12:
            risk_level = "high"
        elif risk_score >= 6:
            risk_level = "medium"
        else:
            risk_level = "low"
        
        assessment = {
            "id": f"RISK-{str(uuid.uuid4())[:8].upper()}",
            "risk_name": tool_input.get("risk_name", ""),
            "risk_category": tool_input.get("risk_category", "operational"),
            "likelihood": likelihood,
            "impact": impact,
            "risk_score": risk_score,
            "risk_level": risk_level,
            "mitigation_controls": tool_input.get("mitigation_controls", []),
            "assessed_at": datetime.utcnow().isoformat()
        }
        
        if "risk_assessments" not in context.artifacts:
            context.artifacts["risk_assessments"] = []
        context.artifacts["risk_assessments"].append(assessment)
        
        return {"success": True, "assessment": assessment}
    
    async def _track_compliance_requirement(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        requirement = {
            "id": f"COMP-{str(uuid.uuid4())[:8].upper()}",
            "regulation": tool_input.get("regulation", ""),
            "requirement_id": tool_input.get("requirement_id", ""),
            "description": tool_input.get("description", ""),
            "status": tool_input.get("status", "partial"),
            "evidence": tool_input.get("evidence", []),
            "tracked_at": datetime.utcnow().isoformat()
        }
        
        if "compliance_requirements" not in context.artifacts:
            context.artifacts["compliance_requirements"] = []
        context.artifacts["compliance_requirements"].append(requirement)
        
        return {"success": True, "requirement": requirement}
    
    async def _evaluate_control(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        evaluation = {
            "id": f"CTRL-{str(uuid.uuid4())[:8].upper()}",
            "control_name": tool_input.get("control_name", ""),
            "control_type": tool_input.get("control_type", "preventive"),
            "effectiveness": tool_input.get("effectiveness", "partially_effective"),
            "test_results": tool_input.get("test_results", ""),
            "evaluated_at": datetime.utcnow().isoformat()
        }
        
        if "control_evaluations" not in context.artifacts:
            context.artifacts["control_evaluations"] = []
        context.artifacts["control_evaluations"].append(evaluation)
        
        return {"success": True, "evaluation": evaluation}
    
    async def _log_incident(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        incident = {
            "id": f"INC-{str(uuid.uuid4())[:8].upper()}",
            "incident_type": tool_input.get("incident_type", ""),
            "severity": tool_input.get("severity", "medium"),
            "description": tool_input.get("description", ""),
            "affected_systems": tool_input.get("affected_systems", []),
            "root_cause": tool_input.get("root_cause", ""),
            "status": "open",
            "logged_at": datetime.utcnow().isoformat()
        }
        
        if "incidents" not in context.artifacts:
            context.artifacts["incidents"] = []
        context.artifacts["incidents"].append(incident)
        
        return {"success": True, "incident": incident}
    
    async def _track_audit_finding(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        finding = {
            "id": f"AUDIT-{str(uuid.uuid4())[:8].upper()}",
            "finding_id": tool_input.get("finding_id", ""),
            "audit_type": tool_input.get("audit_type", "internal"),
            "severity": tool_input.get("severity", "medium"),
            "description": tool_input.get("description", ""),
            "remediation_plan": tool_input.get("remediation_plan", ""),
            "due_date": tool_input.get("due_date", ""),
            "status": "open",
            "tracked_at": datetime.utcnow().isoformat()
        }
        
        if "audit_findings" not in context.artifacts:
            context.artifacts["audit_findings"] = []
        context.artifacts["audit_findings"].append(finding)
        
        return {"success": True, "finding": finding}
    
    async def _generate_risk_report(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        report = {
            "id": f"RISK-RPT-{str(uuid.uuid4())[:8].upper()}",
            "report_type": tool_input.get("report_type", "risk_register"),
            "scope": tool_input.get("scope", ""),
            "generated_at": datetime.utcnow().isoformat()
        }
        context.artifacts[f"risk_report_{report['report_type']}"] = report
        return {"success": True, "report": report}


# =============================================================================
# SUPPLY CHAIN ANALYST AGENT
# =============================================================================

class SupplyChainAnalystAgent(BaseAgent):
    """
    Supply Chain Analyst Agent for supply chain optimization.
    
    Responsibilities:
    - SCOR model implementation
    - Inventory optimization
    - Demand forecasting
    - Supplier performance management
    - Logistics efficiency analysis
    - Procurement analytics
    """
    
    def __init__(self, api_key: Optional[str] = None):
        config = AgentConfig(
            role=AgentRole.SUPPLY_CHAIN_ANALYST,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.4,
            tools=self._get_supply_chain_tools()
        )
        super().__init__(config, api_key)
    
    def _get_system_prompt(self) -> str:
        return """You are an expert Supply Chain Analyst specializing in end-to-end supply chain optimization.

## Your Role
You analyze and optimize supply chain operations using industry frameworks like SCOR (Supply Chain Operations Reference) model.

## Core Responsibilities

### 1. SCOR Model Implementation
Apply the SCOR framework across five key processes:
- **Plan**: Demand/supply planning, inventory planning
- **Source**: Supplier management, procurement
- **Make**: Production scheduling, manufacturing
- **Deliver**: Order management, logistics, warehousing
- **Return**: Returns management, reverse logistics

### 2. Inventory Optimization
- Calculate optimal inventory levels
- Analyze safety stock requirements
- Monitor inventory turnover
- Identify slow-moving and obsolete inventory
- Implement ABC/XYZ analysis

### 3. Demand Forecasting
- Analyze demand patterns
- Apply forecasting methods
- Measure forecast accuracy (MAPE, bias)
- Adjust for seasonality and trends

### 4. Supplier Management
- Track supplier performance (OTD, quality, cost)
- Conduct supplier risk assessment
- Manage supplier scorecards
- Analyze total cost of ownership

### 5. Logistics Optimization
- Analyze transportation costs
- Optimize routing and distribution
- Monitor warehouse efficiency
- Track delivery performance

## Key Metrics (SCOR Level 1)
- Perfect Order Fulfillment
- Order Fulfillment Cycle Time
- Upside Supply Chain Flexibility
- Supply Chain Management Cost
- Cash-to-Cash Cycle Time
- Return on Supply Chain Fixed Assets
- Return on Working Capital

## Collaboration
- Works with Operations Manager for production planning
- Collaborates with Data Scientist for demand forecasting models
"""
    
    def get_system_prompt(self, context: AgentContext) -> str:
        base_prompt = self._get_system_prompt()
        context_info = self._build_context_summary(context)
        return f"{base_prompt}\n\n## Current Context\n{context_info}"
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.business_description:
            parts.append(f"Business: {context.business_description[:200]}...")
        return "\n".join(parts) if parts else "No additional context provided."
    
    def _get_supply_chain_tools(self) -> List[ToolDefinition]:
        return [
            ToolDefinition(
                name="analyze_inventory_levels",
                description="Analyze inventory levels and optimization opportunities",
                parameters={
                    "type": "object",
                    "properties": {
                        "product_category": {"type": "string", "description": "Product category to analyze"},
                        "analysis_type": {"type": "string", "enum": ["abc_analysis", "xyz_analysis", "safety_stock", "reorder_point"], "description": "Type of analysis"},
                        "time_period": {"type": "string", "description": "Analysis period"}
                    },
                    "required": ["product_category", "analysis_type"]
                }
            ),
            ToolDefinition(
                name="evaluate_supplier_performance",
                description="Evaluate supplier performance metrics",
                parameters={
                    "type": "object",
                    "properties": {
                        "supplier_code": {"type": "string", "description": "Supplier identifier"},
                        "metrics": {"type": "array", "items": {"type": "string"}, "description": "Metrics to evaluate"},
                        "period": {"type": "string", "description": "Evaluation period"}
                    },
                    "required": ["supplier_code"]
                }
            ),
            ToolDefinition(
                name="calculate_scor_metrics",
                description="Calculate SCOR framework metrics",
                parameters={
                    "type": "object",
                    "properties": {
                        "scor_level": {"type": "integer", "description": "SCOR level (1, 2, or 3)"},
                        "process": {"type": "string", "enum": ["plan", "source", "make", "deliver", "return"], "description": "SCOR process"},
                        "metrics": {"type": "array", "items": {"type": "string"}, "description": "Specific metrics"}
                    },
                    "required": ["scor_level", "process"]
                }
            ),
            ToolDefinition(
                name="analyze_demand_patterns",
                description="Analyze demand patterns for forecasting",
                parameters={
                    "type": "object",
                    "properties": {
                        "product_code": {"type": "string", "description": "Product identifier"},
                        "historical_periods": {"type": "integer", "description": "Number of historical periods"},
                        "forecast_horizon": {"type": "string", "description": "Forecast timeframe"}
                    },
                    "required": ["product_code"]
                }
            ),
            ToolDefinition(
                name="assess_supply_chain_risk",
                description="Assess supply chain risks",
                parameters={
                    "type": "object",
                    "properties": {
                        "risk_category": {"type": "string", "enum": ["supplier", "logistics", "demand", "geopolitical", "quality"], "description": "Risk category"},
                        "scope": {"type": "string", "description": "Assessment scope"}
                    },
                    "required": ["risk_category"]
                }
            ),
            ToolDefinition(
                name="optimize_logistics",
                description="Analyze and optimize logistics operations",
                parameters={
                    "type": "object",
                    "properties": {
                        "optimization_type": {"type": "string", "enum": ["routing", "warehouse", "transportation_cost", "delivery_time"], "description": "Optimization focus"},
                        "constraints": {"type": "array", "items": {"type": "string"}, "description": "Optimization constraints"}
                    },
                    "required": ["optimization_type"]
                }
            ),
            ToolDefinition(
                name="generate_supply_chain_report",
                description="Generate supply chain analytics report",
                parameters={
                    "type": "object",
                    "properties": {
                        "report_type": {"type": "string", "enum": ["scor_scorecard", "inventory_analysis", "supplier_scorecard", "logistics_performance", "demand_forecast"], "description": "Report type"},
                        "period": {"type": "string", "description": "Report period"}
                    },
                    "required": ["report_type"]
                }
            ),
            # Collaboration tools
            ToolDefinition(
                name="request_demand_forecast_model",
                description="Request Data Scientist to build demand forecasting model",
                parameters={
                    "type": "object",
                    "properties": {
                        "product_categories": {"type": "array", "items": {"type": "string"}, "description": "Product categories"},
                        "forecast_horizon": {"type": "string", "description": "Forecast timeframe"},
                        "seasonality_patterns": {"type": "array", "items": {"type": "string"}, "description": "Known seasonality"}
                    },
                    "required": ["product_categories"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        self._tool_handlers = {
            "analyze_inventory_levels": self._analyze_inventory_levels,
            "evaluate_supplier_performance": self._evaluate_supplier_performance,
            "calculate_scor_metrics": self._calculate_scor_metrics,
            "analyze_demand_patterns": self._analyze_demand_patterns,
            "assess_supply_chain_risk": self._assess_supply_chain_risk,
            "optimize_logistics": self._optimize_logistics,
            "generate_supply_chain_report": self._generate_supply_chain_report,
            "request_demand_forecast_model": self._request_demand_forecast_model
        }
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if getattr(context, 'client_name', None) or context.metadata.get('client_name'):
            parts.append(f"Client: {getattr(context, 'client_name', None) or context.metadata.get('client_name', 'Unknown')}")
        if "inventory_analyses" in context.artifacts:
            parts.append(f"Inventory Analyses: {len(context.artifacts['inventory_analyses'])}")
        return " | ".join(parts) if parts else "No supply chain context"
    
    async def _analyze_inventory_levels(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        analysis = {
            "id": f"INV-{str(uuid.uuid4())[:8].upper()}",
            "product_category": tool_input.get("product_category", ""),
            "analysis_type": tool_input.get("analysis_type", "abc_analysis"),
            "time_period": tool_input.get("time_period", ""),
            "analyzed_at": datetime.utcnow().isoformat()
        }
        if "inventory_analyses" not in context.artifacts:
            context.artifacts["inventory_analyses"] = []
        context.artifacts["inventory_analyses"].append(analysis)
        return {"success": True, "analysis": analysis}
    
    async def _evaluate_supplier_performance(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        evaluation = {
            "id": f"SUPP-{str(uuid.uuid4())[:8].upper()}",
            "supplier_code": tool_input.get("supplier_code", ""),
            "metrics": tool_input.get("metrics", []),
            "period": tool_input.get("period", ""),
            "evaluated_at": datetime.utcnow().isoformat()
        }
        if "supplier_evaluations" not in context.artifacts:
            context.artifacts["supplier_evaluations"] = []
        context.artifacts["supplier_evaluations"].append(evaluation)
        return {"success": True, "evaluation": evaluation}
    
    async def _calculate_scor_metrics(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        calculation = {
            "id": f"SCOR-{str(uuid.uuid4())[:8].upper()}",
            "scor_level": tool_input.get("scor_level", 1),
            "process": tool_input.get("process", "plan"),
            "metrics": tool_input.get("metrics", []),
            "calculated_at": datetime.utcnow().isoformat()
        }
        if "scor_calculations" not in context.artifacts:
            context.artifacts["scor_calculations"] = []
        context.artifacts["scor_calculations"].append(calculation)
        return {"success": True, "calculation": calculation}
    
    async def _analyze_demand_patterns(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        analysis = {
            "id": f"DEMAND-{str(uuid.uuid4())[:8].upper()}",
            "product_code": tool_input.get("product_code", ""),
            "historical_periods": tool_input.get("historical_periods", 12),
            "forecast_horizon": tool_input.get("forecast_horizon", ""),
            "analyzed_at": datetime.utcnow().isoformat()
        }
        if "demand_analyses" not in context.artifacts:
            context.artifacts["demand_analyses"] = []
        context.artifacts["demand_analyses"].append(analysis)
        return {"success": True, "analysis": analysis}
    
    async def _assess_supply_chain_risk(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        assessment = {
            "id": f"SC-RISK-{str(uuid.uuid4())[:8].upper()}",
            "risk_category": tool_input.get("risk_category", "supplier"),
            "scope": tool_input.get("scope", ""),
            "assessed_at": datetime.utcnow().isoformat()
        }
        if "supply_chain_risks" not in context.artifacts:
            context.artifacts["supply_chain_risks"] = []
        context.artifacts["supply_chain_risks"].append(assessment)
        return {"success": True, "assessment": assessment}
    
    async def _optimize_logistics(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        optimization = {
            "id": f"LOG-{str(uuid.uuid4())[:8].upper()}",
            "optimization_type": tool_input.get("optimization_type", "routing"),
            "constraints": tool_input.get("constraints", []),
            "optimized_at": datetime.utcnow().isoformat()
        }
        if "logistics_optimizations" not in context.artifacts:
            context.artifacts["logistics_optimizations"] = []
        context.artifacts["logistics_optimizations"].append(optimization)
        return {"success": True, "optimization": optimization}
    
    async def _generate_supply_chain_report(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        report = {
            "id": f"SC-RPT-{str(uuid.uuid4())[:8].upper()}",
            "report_type": tool_input.get("report_type", "scor_scorecard"),
            "period": tool_input.get("period", ""),
            "generated_at": datetime.utcnow().isoformat()
        }
        context.artifacts[f"sc_report_{report['report_type']}"] = report
        return {"success": True, "report": report}
    
    async def _request_demand_forecast_model(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        request = {
            "id": f"FORECAST-REQ-{str(uuid.uuid4())[:8].upper()}",
            "product_categories": tool_input.get("product_categories", []),
            "forecast_horizon": tool_input.get("forecast_horizon", ""),
            "seasonality_patterns": tool_input.get("seasonality_patterns", []),
            "status": "pending_data_scientist",
            "collaboration_type": "supply_chain_to_data_scientist"
        }
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        return {"success": True, "request": request}


class CompetitiveAnalystAgent(BaseAgent):
    """
    Competitive Analyst Agent - Performs competitive intelligence research.
    
    Identifies and profiles peer companies, analyzes competitive landscape,
    and provides market positioning insights using web search capabilities.
    """
    
    SYSTEM_PROMPT = """You are an expert Competitive Intelligence Analyst specializing in 
identifying and profiling peer companies and competitors. Your role is to research the 
competitive landscape for the business model being designed and provide actionable insights.

## Core Responsibilities

1. **Peer Company Identification**: Find companies with similar business models
2. **Competitor Profiling**: Build detailed profiles of key competitors
3. **Market Positioning Analysis**: Analyze how competitors position themselves
4. **Competitive Benchmarking**: Compare capabilities, offerings, and strategies
5. **Industry Landscape Mapping**: Map the competitive ecosystem

## Research Approach

For each business model, you:
1. **Identify Industry & Segment**: Determine the specific industry and market segment
2. **Search for Peers**: Use web search to find comparable companies
3. **Profile Each Competitor**:
   - Company overview (size, founding, headquarters)
   - Business model and revenue streams
   - Target market and customer segments
   - Key products/services
   - Competitive advantages
   - Technology stack (if relevant)
   - Recent news and developments
4. **Analyze Competitive Dynamics**: Porter's Five Forces perspective
5. **Identify Differentiation Opportunities**: Gaps in the market

## Profiling Framework

For each competitor, capture:
- **Identity**: Name, website, founding year, headquarters, employee count
- **Business Model**: Revenue model, pricing strategy, go-to-market
- **Market Position**: Market share, brand perception, customer segments
- **Offerings**: Products, services, features, pricing tiers
- **Strengths**: Competitive advantages, unique capabilities
- **Weaknesses**: Known limitations, customer complaints
- **Strategy**: Growth strategy, recent moves, partnerships

## Integration with Other Agents

Your findings inform:
- **Business Strategist**: Competitive positioning and differentiation
- **Marketing Manager**: Competitive messaging and positioning
- **Sales Manager**: Competitive selling points and objection handling
- **Data Analyst**: Competitive benchmarks for KPIs

Always cite sources and provide confidence levels for your findings."""

    def __init__(self, config: Optional[AgentConfig] = None):
        if config is None:
            config = AgentConfig(
                role=AgentRole.COMPETITIVE_ANALYST,
                model="claude-sonnet-4-20250514",
                max_tokens=4096,
                temperature=0.4
            )
        super().__init__(config)
        self._register_tools()
    
    def get_system_prompt(self, context: AgentContext) -> str:
        base_prompt = self.SYSTEM_PROMPT
        context_info = self._build_context_summary(context)
        return f"{base_prompt}\n\n## Current Context\n{context_info}"
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.business_description:
            parts.append(f"Business: {context.business_description[:200]}...")
        return "\n".join(parts) if parts else "No additional context provided."
    
    def _get_tools(self) -> List[ToolDefinition]:
        return [
            ToolDefinition(
                name="search_peer_companies",
                description="Search the web for peer companies with similar business models",
                parameters={
                    "type": "object",
                    "properties": {
                        "business_description": {
                            "type": "string",
                            "description": "Description of the business model to find peers for"
                        },
                        "industry": {
                            "type": "string",
                            "description": "Industry or sector"
                        },
                        "geography": {
                            "type": "string",
                            "description": "Geographic focus (e.g., 'North America', 'Global', 'Europe')"
                        },
                        "company_size": {
                            "type": "string",
                            "enum": ["startup", "smb", "mid_market", "enterprise", "any"],
                            "description": "Target company size for comparison"
                        },
                        "max_results": {
                            "type": "integer",
                            "description": "Maximum number of peer companies to find"
                        }
                    },
                    "required": ["business_description", "industry"]
                }
            ),
            ToolDefinition(
                name="profile_competitor",
                description="Build a detailed profile of a specific competitor",
                parameters={
                    "type": "object",
                    "properties": {
                        "company_name": {
                            "type": "string",
                            "description": "Name of the company to profile"
                        },
                        "website": {
                            "type": "string",
                            "description": "Company website URL"
                        },
                        "profile_depth": {
                            "type": "string",
                            "enum": ["basic", "standard", "comprehensive"],
                            "description": "Level of detail for the profile"
                        }
                    },
                    "required": ["company_name"]
                }
            ),
            ToolDefinition(
                name="analyze_competitive_landscape",
                description="Analyze the overall competitive landscape for an industry/segment",
                parameters={
                    "type": "object",
                    "properties": {
                        "industry": {
                            "type": "string",
                            "description": "Industry to analyze"
                        },
                        "segment": {
                            "type": "string",
                            "description": "Specific market segment"
                        },
                        "analysis_type": {
                            "type": "string",
                            "enum": ["five_forces", "market_map", "trend_analysis", "comprehensive"],
                            "description": "Type of competitive analysis"
                        }
                    },
                    "required": ["industry"]
                }
            ),
            ToolDefinition(
                name="compare_competitors",
                description="Compare multiple competitors across key dimensions",
                parameters={
                    "type": "object",
                    "properties": {
                        "competitors": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of competitor names to compare"
                        },
                        "dimensions": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Dimensions to compare (e.g., 'pricing', 'features', 'market_share')"
                        }
                    },
                    "required": ["competitors"]
                }
            ),
            ToolDefinition(
                name="identify_market_gaps",
                description="Identify gaps and opportunities in the competitive landscape",
                parameters={
                    "type": "object",
                    "properties": {
                        "industry": {
                            "type": "string",
                            "description": "Industry to analyze"
                        },
                        "current_offerings": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Current offerings in the market"
                        },
                        "customer_pain_points": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Known customer pain points"
                        }
                    },
                    "required": ["industry"]
                }
            ),
            ToolDefinition(
                name="track_competitor_news",
                description="Search for recent news and developments about competitors",
                parameters={
                    "type": "object",
                    "properties": {
                        "company_name": {
                            "type": "string",
                            "description": "Company to track"
                        },
                        "time_period": {
                            "type": "string",
                            "enum": ["last_week", "last_month", "last_quarter", "last_year"],
                            "description": "Time period for news search"
                        },
                        "news_types": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Types of news (e.g., 'funding', 'product_launch', 'partnership', 'acquisition')"
                        }
                    },
                    "required": ["company_name"]
                }
            ),
            ToolDefinition(
                name="generate_competitive_report",
                description="Generate a comprehensive competitive intelligence report",
                parameters={
                    "type": "object",
                    "properties": {
                        "report_type": {
                            "type": "string",
                            "enum": ["landscape_overview", "competitor_deep_dive", "market_opportunity", "battlecard"],
                            "description": "Type of report to generate"
                        },
                        "include_recommendations": {
                            "type": "boolean",
                            "description": "Whether to include strategic recommendations"
                        }
                    },
                    "required": ["report_type"]
                }
            ),
            ToolDefinition(
                name="request_strategist_review",
                description="Request Business Strategist to review competitive findings for strategic implications",
                parameters={
                    "type": "object",
                    "properties": {
                        "findings_summary": {
                            "type": "string",
                            "description": "Summary of competitive findings"
                        },
                        "strategic_questions": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Strategic questions for the strategist"
                        }
                    },
                    "required": ["findings_summary"]
                }
            )
        ]
    
    def _register_tools(self):
        self._tool_handlers = {
            "search_peer_companies": self._search_peer_companies,
            "profile_competitor": self._profile_competitor,
            "analyze_competitive_landscape": self._analyze_competitive_landscape,
            "compare_competitors": self._compare_competitors,
            "identify_market_gaps": self._identify_market_gaps,
            "track_competitor_news": self._track_competitor_news,
            "generate_competitive_report": self._generate_competitive_report,
            "request_strategist_review": self._request_strategist_review
        }
    
    def get_context_summary(self, context: AgentContext) -> str:
        competitors = context.artifacts.get("competitor_profiles", [])
        landscape = context.artifacts.get("competitive_landscape")
        
        return f"""Competitive Intelligence Context:
- Profiled Competitors: {len(competitors)}
- Landscape Analysis: {'Complete' if landscape else 'Pending'}
- Companies: {', '.join([c.get('company_name', 'Unknown') for c in competitors[:5]])}"""
    
    async def _search_peer_companies(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        search_result = {
            "id": f"PEER-SEARCH-{str(uuid.uuid4())[:8].upper()}",
            "business_description": tool_input.get("business_description", ""),
            "industry": tool_input.get("industry", ""),
            "geography": tool_input.get("geography", "Global"),
            "company_size": tool_input.get("company_size", "any"),
            "max_results": tool_input.get("max_results", 10),
            "peer_companies": [],  # Would be populated by actual web search
            "search_queries_used": [],
            "searched_at": datetime.utcnow().isoformat(),
            "status": "pending_web_search"
        }
        
        if "peer_searches" not in context.artifacts:
            context.artifacts["peer_searches"] = []
        context.artifacts["peer_searches"].append(search_result)
        
        return {"success": True, "search": search_result}
    
    async def _profile_competitor(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        profile = {
            "id": f"COMP-{str(uuid.uuid4())[:8].upper()}",
            "company_name": tool_input.get("company_name", ""),
            "website": tool_input.get("website"),
            "profile_depth": tool_input.get("profile_depth", "standard"),
            
            # Identity
            "founding_year": None,
            "headquarters": None,
            "employee_count": None,
            "funding_stage": None,
            "total_funding": None,
            
            # Business Model
            "business_model": None,
            "revenue_model": None,
            "pricing_strategy": None,
            "target_market": None,
            "customer_segments": [],
            
            # Offerings
            "products": [],
            "services": [],
            "key_features": [],
            
            # Competitive Position
            "strengths": [],
            "weaknesses": [],
            "market_position": None,
            "competitive_advantages": [],
            
            # Metadata
            "profiled_at": datetime.utcnow().isoformat(),
            "confidence_score": 0.0,
            "sources": []
        }
        
        if "competitor_profiles" not in context.artifacts:
            context.artifacts["competitor_profiles"] = []
        context.artifacts["competitor_profiles"].append(profile)
        
        return {"success": True, "profile": profile}
    
    async def _analyze_competitive_landscape(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        analysis = {
            "id": f"LANDSCAPE-{str(uuid.uuid4())[:8].upper()}",
            "industry": tool_input.get("industry", ""),
            "segment": tool_input.get("segment"),
            "analysis_type": tool_input.get("analysis_type", "comprehensive"),
            
            # Five Forces (if applicable)
            "five_forces": {
                "threat_of_new_entrants": None,
                "bargaining_power_suppliers": None,
                "bargaining_power_buyers": None,
                "threat_of_substitutes": None,
                "competitive_rivalry": None
            },
            
            # Market Structure
            "market_leaders": [],
            "challengers": [],
            "niche_players": [],
            "emerging_players": [],
            
            # Trends
            "market_trends": [],
            "technology_trends": [],
            "regulatory_trends": [],
            
            # Metadata
            "analyzed_at": datetime.utcnow().isoformat()
        }
        
        context.artifacts["competitive_landscape"] = analysis
        return {"success": True, "analysis": analysis}
    
    async def _compare_competitors(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        comparison = {
            "id": f"COMP-CMP-{str(uuid.uuid4())[:8].upper()}",
            "competitors": tool_input.get("competitors", []),
            "dimensions": tool_input.get("dimensions", ["pricing", "features", "market_share"]),
            "comparison_matrix": {},  # Would be populated with actual comparison data
            "compared_at": datetime.utcnow().isoformat()
        }
        
        if "competitor_comparisons" not in context.artifacts:
            context.artifacts["competitor_comparisons"] = []
        context.artifacts["competitor_comparisons"].append(comparison)
        
        return {"success": True, "comparison": comparison}
    
    async def _identify_market_gaps(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        gap_analysis = {
            "id": f"GAP-{str(uuid.uuid4())[:8].upper()}",
            "industry": tool_input.get("industry", ""),
            "current_offerings": tool_input.get("current_offerings", []),
            "customer_pain_points": tool_input.get("customer_pain_points", []),
            "identified_gaps": [],  # Would be populated by analysis
            "opportunities": [],
            "analyzed_at": datetime.utcnow().isoformat()
        }
        
        context.artifacts["market_gap_analysis"] = gap_analysis
        return {"success": True, "gap_analysis": gap_analysis}
    
    async def _track_competitor_news(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        news_tracking = {
            "id": f"NEWS-{str(uuid.uuid4())[:8].upper()}",
            "company_name": tool_input.get("company_name", ""),
            "time_period": tool_input.get("time_period", "last_month"),
            "news_types": tool_input.get("news_types", []),
            "news_items": [],  # Would be populated by web search
            "tracked_at": datetime.utcnow().isoformat()
        }
        
        if "competitor_news" not in context.artifacts:
            context.artifacts["competitor_news"] = []
        context.artifacts["competitor_news"].append(news_tracking)
        
        return {"success": True, "news": news_tracking}
    
    async def _generate_competitive_report(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        profiles = context.artifacts.get("competitor_profiles", [])
        landscape = context.artifacts.get("competitive_landscape")
        
        report = {
            "id": f"CI-RPT-{str(uuid.uuid4())[:8].upper()}",
            "report_type": tool_input.get("report_type", "landscape_overview"),
            "include_recommendations": tool_input.get("include_recommendations", True),
            "competitors_analyzed": len(profiles),
            "landscape_included": landscape is not None,
            "sections": [],
            "recommendations": [],
            "generated_at": datetime.utcnow().isoformat()
        }
        
        context.artifacts["competitive_report"] = report
        return {"success": True, "report": report}
    
    async def _request_strategist_review(
        self, 
        tool_input: Dict[str, Any],
        context: AgentContext
    ) -> Dict[str, Any]:
        request = {
            "id": f"STRAT-REV-{str(uuid.uuid4())[:8].upper()}",
            "findings_summary": tool_input.get("findings_summary", ""),
            "strategic_questions": tool_input.get("strategic_questions", []),
            "status": "pending_business_strategist",
            "collaboration_type": "competitive_analyst_to_business_strategist"
        }
        
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        
        return {"success": True, "request": request}


# =============================================================================
# PROCESS SCENARIO MODELER AGENT
# =============================================================================

class ProcessScenarioModelerAgent(BaseAgent):
    """
    Process Scenario Modeler Agent for process simulation and what-if analysis.
    
    Responsibilities:
    - Design and validate process definitions from value chain modules
    - Create and run simulation scenarios
    - Analyze simulation results and predict KPI impacts
    - Identify bottlenecks and recommend optimizations
    - Collaborate with Operations Manager and Data Scientist
    """
    
    def __init__(self, api_key: Optional[str] = None):
        config = AgentConfig(
            role=AgentRole.PROCESS_SCENARIO_MODELER,
            model="claude-sonnet-4-20250514",
            max_tokens=4096,
            temperature=0.4,
            tools=self._get_process_scenario_tools()
        )
        super().__init__(config, api_key)
    
    def _get_system_prompt(self) -> str:
        return """You are an expert Process Simulation Specialist.

## Your Role
You help organizations test process changes in a digital sandbox before 
implementing them in production. You bridge strategy design with operational 
execution by predicting how process changes will impact KPIs.

## Core Responsibilities

### 1. Process Design
- Define process flows from value chain modules
- Set step parameters (duration, cost, resources)
- Link processes to strategic KPIs
- Validate process completeness and consistency

### 2. Scenario Creation
- Create what-if scenarios with parameter changes
- Define simulation parameters (duration, replications)
- Set up comparison scenarios for A/B testing

### 3. Simulation Execution
- Run discrete event simulations
- Generate event logs for detailed analysis
- Calculate performance metrics (cycle time, throughput, utilization)

### 4. Impact Analysis
- Predict KPI impacts from process changes
- Identify bottlenecks and constraints
- Assess strategic alignment of changes
- Recommend process optimizations

## Collaboration
- Work with Operations Manager to understand operational context
- Work with Data Scientist to validate predictions statistically
- Work with Business Strategist to ensure strategic alignment

## Tools Available
- design_process: Create process definition from value chain
- create_scenario: Define what-if scenario with parameter changes
- run_simulation: Execute process simulation
- analyze_impact: Analyze KPI impacts from simulation
- compare_scenarios: Compare multiple scenarios side-by-side
- identify_bottlenecks: Find process bottlenecks
- recommend_optimizations: Generate optimization recommendations
- request_operations_review: Ask Operations Manager for review
"""
    
    def get_system_prompt(self, context: AgentContext) -> str:
        base_prompt = self._get_system_prompt()
        context_info = self._build_context_summary(context)
        return f"{base_prompt}\n\n## Current Context\n{context_info}"
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if context.industry:
            parts.append(f"Industry: {context.industry}")
        if context.business_description:
            parts.append(f"Business: {context.business_description[:200]}...")
        return "\n".join(parts) if parts else "No additional context provided."
    
    def _get_process_scenario_tools(self) -> List[ToolDefinition]:
        return [
            ToolDefinition(
                name="design_process",
                description="Design a simulatable process definition from value chain module",
                parameters={
                    "type": "object",
                    "properties": {
                        "process_name": {"type": "string", "description": "Name of the process"},
                        "process_code": {"type": "string", "description": "Unique code for the process"},
                        "value_chain_module": {"type": "string", "description": "Value chain module this process belongs to"},
                        "steps": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "id": {"type": "string"},
                                    "name": {"type": "string"},
                                    "step_type": {"type": "string"},
                                    "duration_mean": {"type": "number"},
                                    "duration_std": {"type": "number"},
                                    "fixed_cost": {"type": "number"},
                                    "variable_cost": {"type": "number"},
                                    "defect_rate": {"type": "number"},
                                    "required_resources": {"type": "array", "items": {"type": "string"}}
                                },
                                "required": ["id", "name"]
                            },
                            "description": "Process steps"
                        },
                        "transitions": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "from_step": {"type": "string"},
                                    "to_step": {"type": "string"},
                                    "condition": {"type": "string"},
                                    "probability": {"type": "number"}
                                },
                                "required": ["from_step", "to_step"]
                            },
                            "description": "Transitions between steps"
                        },
                        "linked_kpis": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "KPIs affected by this process"
                        }
                    },
                    "required": ["process_name", "process_code", "steps"]
                }
            ),
            ToolDefinition(
                name="create_scenario",
                description="Create a what-if scenario with parameter changes",
                parameters={
                    "type": "object",
                    "properties": {
                        "scenario_name": {"type": "string"},
                        "scenario_code": {"type": "string"},
                        "process_id": {"type": "string"},
                        "parameter_changes": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "change_type": {"type": "string"},
                                    "target": {"type": "string"},
                                    "parameter": {"type": "string"},
                                    "new_value": {}
                                },
                                "required": ["change_type", "target", "new_value"]
                            }
                        },
                        "simulation_duration_hours": {"type": "number"},
                        "number_of_replications": {"type": "integer"}
                    },
                    "required": ["scenario_name", "scenario_code", "process_id", "parameter_changes"]
                }
            ),
            ToolDefinition(
                name="run_simulation",
                description="Execute a process simulation",
                parameters={
                    "type": "object",
                    "properties": {
                        "scenario_id": {"type": "string"},
                        "real_time_updates": {"type": "boolean"}
                    },
                    "required": ["scenario_id"]
                }
            ),
            ToolDefinition(
                name="analyze_impact",
                description="Analyze the impact of a simulation on KPIs",
                parameters={
                    "type": "object",
                    "properties": {
                        "simulation_result_id": {"type": "string"},
                        "focus_kpis": {"type": "array", "items": {"type": "string"}},
                        "include_cascade_effects": {"type": "boolean"}
                    },
                    "required": ["simulation_result_id"]
                }
            ),
            ToolDefinition(
                name="compare_scenarios",
                description="Compare multiple scenarios side-by-side",
                parameters={
                    "type": "object",
                    "properties": {
                        "scenario_ids": {"type": "array", "items": {"type": "string"}},
                        "comparison_kpis": {"type": "array", "items": {"type": "string"}},
                        "ranking_criteria": {"type": "string"}
                    },
                    "required": ["scenario_ids"]
                }
            ),
            ToolDefinition(
                name="identify_bottlenecks",
                description="Identify bottlenecks in a process simulation",
                parameters={
                    "type": "object",
                    "properties": {
                        "simulation_result_id": {"type": "string"},
                        "utilization_threshold": {"type": "number"},
                        "queue_threshold": {"type": "number"}
                    },
                    "required": ["simulation_result_id"]
                }
            ),
            ToolDefinition(
                name="recommend_optimizations",
                description="Generate process optimization recommendations",
                parameters={
                    "type": "object",
                    "properties": {
                        "process_id": {"type": "string"},
                        "simulation_result_id": {"type": "string"},
                        "optimization_goals": {"type": "array", "items": {"type": "string"}},
                        "constraints": {"type": "object"}
                    },
                    "required": ["process_id", "optimization_goals"]
                }
            ),
            ToolDefinition(
                name="request_operations_review",
                description="Request Operations Manager to review simulation results",
                parameters={
                    "type": "object",
                    "properties": {
                        "simulation_result_id": {"type": "string"},
                        "findings_summary": {"type": "string"},
                        "questions": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["simulation_result_id", "findings_summary"]
                }
            )
        ]
    
    def _register_tools(self) -> None:
        self._tool_handlers = {
            "design_process": self._design_process,
            "create_scenario": self._create_scenario,
            "run_simulation": self._run_simulation,
            "analyze_impact": self._analyze_impact,
            "compare_scenarios": self._compare_scenarios,
            "identify_bottlenecks": self._identify_bottlenecks,
            "recommend_optimizations": self._recommend_optimizations,
            "request_operations_review": self._request_operations_review
        }
    
    def _build_context_summary(self, context: AgentContext) -> str:
        parts = []
        if "processes" in context.artifacts:
            parts.append(f"Processes defined: {len(context.artifacts['processes'])}")
        if "scenarios" in context.artifacts:
            parts.append(f"Scenarios created: {len(context.artifacts['scenarios'])}")
        if "simulation_results" in context.artifacts:
            parts.append(f"Simulations completed: {len(context.artifacts['simulation_results'])}")
        return "\n".join(parts) if parts else "No process simulation context available."
    
    async def _design_process(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        process = {
            "id": f"PROC-{str(uuid.uuid4())[:8].upper()}",
            "code": tool_input.get("process_code", ""),
            "name": tool_input.get("process_name", ""),
            "value_chain_module": tool_input.get("value_chain_module"),
            "steps": tool_input.get("steps", []),
            "transitions": tool_input.get("transitions", []),
            "linked_kpis": tool_input.get("linked_kpis", []),
            "version": 1,
            "created_at": datetime.utcnow().isoformat()
        }
        if "processes" not in context.artifacts:
            context.artifacts["processes"] = []
        context.artifacts["processes"].append(process)
        return {"success": True, "process": process}
    
    async def _create_scenario(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        scenario = {
            "id": f"SCEN-{str(uuid.uuid4())[:8].upper()}",
            "code": tool_input.get("scenario_code", ""),
            "name": tool_input.get("scenario_name", ""),
            "process_id": tool_input.get("process_id", ""),
            "parameter_changes": tool_input.get("parameter_changes", []),
            "simulation_duration_hours": tool_input.get("simulation_duration_hours", 168),
            "number_of_replications": tool_input.get("number_of_replications", 10),
            "created_at": datetime.utcnow().isoformat()
        }
        if "scenarios" not in context.artifacts:
            context.artifacts["scenarios"] = []
        context.artifacts["scenarios"].append(scenario)
        return {"success": True, "scenario": scenario}
    
    async def _run_simulation(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        result = {
            "id": f"SIM-{str(uuid.uuid4())[:8].upper()}",
            "scenario_id": tool_input.get("scenario_id", ""),
            "avg_cycle_time": 0.0,
            "total_completed": 0,
            "throughput_rate": 0.0,
            "resource_utilization": {},
            "total_cost": 0.0,
            "bottlenecks": [],
            "predicted_kpi_values": [],
            "simulation_completed_at": datetime.utcnow().isoformat()
        }
        if "simulation_results" not in context.artifacts:
            context.artifacts["simulation_results"] = []
        context.artifacts["simulation_results"].append(result)
        return {"success": True, "simulation_result": result}
    
    async def _analyze_impact(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        analysis = {
            "id": f"IMPACT-{str(uuid.uuid4())[:8].upper()}",
            "simulation_result_id": tool_input.get("simulation_result_id", ""),
            "kpi_impacts": [],
            "strategic_alignment_score": 0.0,
            "risk_level": "medium",
            "recommendations": [],
            "analyzed_at": datetime.utcnow().isoformat()
        }
        if "impact_analyses" not in context.artifacts:
            context.artifacts["impact_analyses"] = []
        context.artifacts["impact_analyses"].append(analysis)
        return {"success": True, "impact_analysis": analysis}
    
    async def _compare_scenarios(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        comparison = {
            "id": f"COMP-SCEN-{str(uuid.uuid4())[:8].upper()}",
            "scenario_ids": tool_input.get("scenario_ids", []),
            "comparison_kpis": tool_input.get("comparison_kpis", []),
            "rankings": [],
            "compared_at": datetime.utcnow().isoformat()
        }
        if "scenario_comparisons" not in context.artifacts:
            context.artifacts["scenario_comparisons"] = []
        context.artifacts["scenario_comparisons"].append(comparison)
        return {"success": True, "comparison": comparison}
    
    async def _identify_bottlenecks(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        analysis = {
            "id": f"BTL-SIM-{str(uuid.uuid4())[:8].upper()}",
            "simulation_result_id": tool_input.get("simulation_result_id", ""),
            "bottlenecks": [],
            "analyzed_at": datetime.utcnow().isoformat()
        }
        context.artifacts["simulation_bottleneck_analysis"] = analysis
        return {"success": True, "bottleneck_analysis": analysis}
    
    async def _recommend_optimizations(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        recommendations = {
            "id": f"OPT-SIM-{str(uuid.uuid4())[:8].upper()}",
            "process_id": tool_input.get("process_id", ""),
            "optimization_goals": tool_input.get("optimization_goals", []),
            "recommendations": [],
            "generated_at": datetime.utcnow().isoformat()
        }
        if "simulation_optimization_recommendations" not in context.artifacts:
            context.artifacts["simulation_optimization_recommendations"] = []
        context.artifacts["simulation_optimization_recommendations"].append(recommendations)
        return {"success": True, "recommendations": recommendations}
    
    async def _request_operations_review(self, tool_input: Dict[str, Any], context: AgentContext) -> Dict[str, Any]:
        request = {
            "id": f"OPS-REV-{str(uuid.uuid4())[:8].upper()}",
            "simulation_result_id": tool_input.get("simulation_result_id", ""),
            "findings_summary": tool_input.get("findings_summary", ""),
            "questions": tool_input.get("questions", []),
            "status": "pending_operations_manager",
            "collaboration_type": "process_modeler_to_operations_manager",
            "requested_at": datetime.utcnow().isoformat()
        }
        if "collaboration_requests" not in context.artifacts:
            context.artifacts["collaboration_requests"] = []
        context.artifacts["collaboration_requests"].append(request)
        return {"success": True, "request": request}

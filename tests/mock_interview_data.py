"""
Mock Interview Data for Agent Testing

This module contains the CEO interview script designed to activate all agents
in the multi-agent system.
"""

from typing import List, Dict, Any

# All agents in the system that should be activated
ALL_AGENTS = [
    "coordinator",
    "architect", 
    "business_analyst",
    "data_analyst",
    "developer",
    "tester",
    "documenter",
    "deployment_specialist",
    "project_manager",
    "sales_manager",
    "accountant",
    "data_governance_specialist",
    "data_scientist",
    "marketing_manager",
    "ui_designer",
    "business_strategist",
    "operations_manager",
    "librarian_curator",
    "competitive_analyst"
]

# Mock CEO Interview - 7 turns designed to activate all agents
MOCK_CEO_INTERVIEW: List[Dict[str, Any]] = [
    {
        "turn": 1,
        "speaker": "CEO",
        "message": """Hi, I'm the CEO of TechFlow Solutions. We're a mid-sized B2B SaaS company 
specializing in supply chain optimization software. We have about 500 employees 
and serve manufacturing clients across North America and Europe.

Our main product helps manufacturers track inventory, optimize procurement, 
and manage supplier relationships. We process millions of transactions daily 
and our clients expect real-time visibility into their supply chains.""",
        "target_agents": ["coordinator", "business_analyst", "architect"],
        "topics": ["industry identification", "business model", "scale assessment"],
        "agent_triggers": {
            "coordinator": "Initial business understanding, session setup",
            "business_analyst": "Industry analysis (B2B SaaS, Supply Chain)",
            "architect": "System scale assessment (millions of transactions)"
        }
    },
    {
        "turn": 2,
        "speaker": "CEO",
        "message": """Our biggest challenge is measuring performance. We need KPIs for:
- Customer acquisition cost and lifetime value
- Product adoption and feature usage rates  
- Support ticket resolution and customer satisfaction
- Revenue per customer segment
- Churn prediction and retention metrics

I also want to benchmark against SCOR framework for our supply chain modules.
What existing KPI definitions do you have that we could reuse?""",
        "target_agents": ["librarian_curator", "data_analyst", "business_strategist"],
        "topics": ["KPI design", "SCOR framework", "catalog search", "reuse suggestions"],
        "agent_triggers": {
            "librarian_curator": "Search catalog for existing KPIs, suggest reuse, SCOR lookup",
            "data_analyst": "Set-based KPI calculation design",
            "business_strategist": "Strategic metrics alignment"
        }
    },
    {
        "turn": 3,
        "speaker": "CEO",
        "message": """From a technical perspective, we have data in multiple systems:
- Salesforce for CRM
- NetSuite for financials  
- Custom PostgreSQL databases for product data
- Snowflake for our data warehouse

We need to integrate all of this for unified analytics.
Our dev team uses Azure. What's the best architecture?""",
        "target_agents": ["architect", "developer", "deployment_specialist", "data_governance_specialist"],
        "topics": ["data integration", "architecture", "Azure deployment", "data governance"],
        "agent_triggers": {
            "architect": "Multi-source integration architecture design",
            "developer": "Schema design, integration code patterns",
            "deployment_specialist": "Azure deployment strategy",
            "data_governance_specialist": "Data lineage, quality, governance policies"
        }
    },
    {
        "turn": 4,
        "speaker": "CEO",
        "message": """I'm concerned about competition. Coupa, SAP Ariba, and Jaggaer 
are all expanding their analytics. What are they doing that we should know?

Also, what are the current industry best practices for supply chain analytics?
Can you research the latest trends and standards?""",
        "target_agents": ["competitive_analyst", "librarian_curator", "business_strategist"],
        "topics": ["competitive intelligence", "web search", "industry research", "best practices"],
        "agent_triggers": {
            "competitive_analyst": "Web search for competitor analysis",
            "librarian_curator": "Research best practices via web search",
            "business_strategist": "Strategic positioning recommendations"
        }
    },
    {
        "turn": 5,
        "speaker": "CEO",
        "message": """Our sales team needs forecasting tools - they use spreadsheets now.
Marketing wants campaign ROI and attribution analysis.
Finance needs revenue recognition and cash flow projections.

Can we design analytics that serve all these departments?
What machine learning models would help with forecasting?""",
        "target_agents": ["sales_manager", "marketing_manager", "accountant", "data_scientist"],
        "topics": ["sales forecasting", "marketing attribution", "financial metrics", "ML models"],
        "agent_triggers": {
            "sales_manager": "Sales pipeline and forecasting KPIs",
            "marketing_manager": "Campaign ROI, attribution models",
            "accountant": "Revenue recognition, cash flow metrics",
            "data_scientist": "ML forecasting models, predictive analytics"
        }
    },
    {
        "turn": 6,
        "speaker": "CEO",
        "message": """For the user interface, we want something modern and intuitive.
Our users are busy operations managers who need quick insights and actions.

Also, we need proper testing and documentation for SOC 2 and GDPR compliance.
What's your recommended approach for the UI and compliance documentation?""",
        "target_agents": ["ui_designer", "tester", "documenter", "data_governance_specialist"],
        "topics": ["UI/UX design", "testing strategy", "compliance docs", "GDPR/SOC2"],
        "agent_triggers": {
            "ui_designer": "Dashboard design, UX patterns for operations users",
            "tester": "Test strategy for compliance validation",
            "documenter": "SOC 2 and GDPR documentation",
            "data_governance_specialist": "Compliance requirements mapping"
        }
    },
    {
        "turn": 7,
        "speaker": "CEO",
        "message": """Our ops team manages deployment and monitoring - they follow ITIL.
They need system health dashboards, performance metrics, and incident management.

Finally, our project manager needs a timeline. How long will this take?
What are the implementation phases and milestones?""",
        "target_agents": ["operations_manager", "project_manager", "deployment_specialist"],
        "topics": ["ITIL practices", "monitoring", "project planning", "milestones"],
        "agent_triggers": {
            "operations_manager": "ITIL alignment, monitoring KPIs",
            "project_manager": "Project phases, timeline, resource planning",
            "deployment_specialist": "Infrastructure monitoring, deployment phases"
        }
    }
]


def get_interview_script() -> List[Dict[str, Any]]:
    """Return the full interview script."""
    return MOCK_CEO_INTERVIEW


def get_all_expected_agents() -> List[str]:
    """Return list of all agents expected to be activated."""
    return ALL_AGENTS


def get_turn_by_number(turn_num: int) -> Dict[str, Any]:
    """Get a specific turn by number."""
    for turn in MOCK_CEO_INTERVIEW:
        if turn["turn"] == turn_num:
            return turn
    return None


def get_expected_agents_for_turn(turn_num: int) -> List[str]:
    """Get expected agents for a specific turn."""
    turn = get_turn_by_number(turn_num)
    return turn["target_agents"] if turn else []

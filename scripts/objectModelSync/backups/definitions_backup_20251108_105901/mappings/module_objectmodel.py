"""
Module to ObjectModel Mappings

Defines which object models belong to which modules.
"""

from ..modules.registry import get_module
from ..object_models.registry import get_object_model


MODULE_OBJECTMODEL_MAP = {
    "BUS_DEV": [
        "ACCOUNT",
        "LEAD",
        "OPPORTUNITY",
        "DEAL",
        "SALE",
        "CUSTOMER",
        "SALES_REP",
        "SALES_TEAM",
        "PRODUCT",
        "CONTRACT",
        "DEMO",
        "SUPPORT_TICKET",
        "REFERRAL",
        "PARTNERSHIP",
        "SALES_QUOTA",
        "REVENUE_FORECAST"
    ],
    "CHANNEL_SALES": [
        "CHANNEL_PARTNER",
        "CHANNEL_DEAL",
        "LEAD",
        "PRODUCT",
        "CUSTOMER",
        "PARTNER_TRAINING",
        "SUPPORT_TICKET",
        "CO_MARKETING_CAMPAIGN",
        "CHANNEL_MARKET",
        "PARTNER_PORTAL",
        "PARTNER_INCENTIVE",
        "PARTNER_AGREEMENT",
        "PARTNER_PERFORMANCE_SCORECARD",
        "CHANNEL_CONFLICT"
    ],
    "CUSTOMER_RETENTION": [
        "CUSTOMER",
        "SUBSCRIPTION",
        "SUPPORT_TICKET",
        "CUSTOMER_FEEDBACK",
        "LOYALTY_PROGRAM",
        "CUSTOMER_ONBOARDING",
        "CUSTOMER_HEALTH_RECORD",
        "CUSTOMER_JOURNEY",
        "PRODUCT_USAGE",
        "CHURN_EVENT",
        "CUSTOMER_EDUCATION",
        "QUARTERLY_BUSINESS_REVIEW",
        "CUSTOMER_SEGMENT",
        "SERVICE_LEVEL_AGREEMENT",
        "PURCHASE_HISTORY",
        "PRODUCT",
        "REFERRAL"
    ],
    "CUSTOMER_SUCCESS": [
        "CUSTOMER",
        "CUSTOMER_SUCCESS_MANAGER",
        "CUSTOMER_ONBOARDING",
        "PRODUCT_ADOPTION",
        "CUSTOMER_GOAL",
        "QUARTERLY_BUSINESS_REVIEW",
        "CUSTOMER_COHORT",
        "CUSTOMER_COMMUNITY",
        "CUSTOMER_ADVOCACY_PROGRAM",
        "KNOWLEDGE_BASE",
        "CUSTOMER_EDUCATION",
        "CUSTOMER_HEALTH_RECORD",
        "RENEWAL_MANAGEMENT",
        "EXPANSION_OPPORTUNITY",
        "SUPPORT_TICKET",
        "CUSTOMER_FEEDBACK",
        "SERVICE_LEVEL_AGREEMENT",
        "SUBSCRIPTION",
        "PRODUCT",
        "CUSTOMER_SEGMENT"
    ],
    "INSIDE_SALES": [
        "LEAD",
        "OPPORTUNITY",
        "DEAL",
        "SALE",
        "CUSTOMER",
        "SALES_REP",
        "SALES_TEAM",
        "PRODUCT",
        "SALES_QUOTA",
        "DEMO",
        "CONTRACT",
        "SALES_ACTIVITY",
        "SALES_CALL",
        "SALES_EMAIL",
        "SALES_FORECAST",
        "LOST_SALE"
    ],
    "KEY_ACCOUNT_MANAGEMENT": [
        "KEY_ACCOUNT",
        "KEY_ACCOUNT_MANAGER",
        "ACCOUNT_PLAN",
        "STAKEHOLDER",
        "STRATEGIC_REVIEW",
        "ACCOUNT_PENETRATION",
        "ACCOUNT_RISK",
        "ACCOUNT",
        "CUSTOMER",
        "OPPORTUNITY",
        "DEAL",
        "PRODUCT",
        "CONTRACT",
        "SALES_TEAM",
        "REFERRAL"
    ],
    "OUTSIDE_SALES": [
        "SALES_TERRITORY",
        "FIELD_VISIT",
        "SALES_APPOINTMENT",
        "ACCOUNT",
        "LEAD",
        "OPPORTUNITY",
        "DEAL",
        "SALE",
        "CUSTOMER",
        "SALES_REP",
        "SALES_TEAM",
        "PRODUCT",
        "CONTRACT",
        "DEMO",
        "REFERRAL",
        "SALES_QUOTA",
        "REVENUE_FORECAST"
    ],
    "SALES_DEVELOPMENT": [
        "OUTBOUND_CALL",
        "APPOINTMENT",
        "PROSPECT_ENGAGEMENT",
        "LEAD_QUALIFICATION",
        "PROSPECT",
        "LEAD",
        "OPPORTUNITY",
        "ACCOUNT",
        "SALES_REP",
        "SALES_TEAM",
        "DEMO",
        "EMAIL_CAMPAIGN",
        "SALES_ACTIVITY",
        "SALES_QUOTA"
    ],
    "SALES_ENABLEMENT": [
        "SALES_TRAINING_PROGRAM",
        "SALES_CONTENT",
        "SALES_PLAYBOOK",
        "SALES_COACHING_SESSION",
        "SALES_ASSESSMENT",
        "ENABLEMENT_PLATFORM",
        "ENABLEMENT_FEEDBACK",
        "SALES_REP",
        "SALES_TEAM",
        "PRODUCT",
        "CUSTOMER"
    ],
    "SALES_OPERATIONS": [
        "SALES_DASHBOARD",
        "SALES_FORECAST",
        "TERRITORY_ASSIGNMENT",
        "QUOTA_PLAN",
        "SALES_PROCESS_WORKFLOW",
        "SALES_REP",
        "SALES_TEAM",
        "LEAD",
        "OPPORTUNITY",
        "DEAL",
        "CUSTOMER",
        "PRODUCT",
        "SALES_TERRITORY",
        "SALES_QUOTA",
        "REVENUE_FORECAST"
    ],
    "SALES_PERFORMANCE": [
        "PERFORMANCE_SCORECARD",
        "PERFORMANCE_BENCHMARK",
        "SALES_REP",
        "SALES_TEAM",
        "LEAD",
        "OPPORTUNITY",
        "DEAL",
        "CUSTOMER",
        "PRODUCT",
        "SALES_TERRITORY",
        "SALES_QUOTA",
        "REVENUE"
    ],
    "SALES_STRATEGY": [
        "MARKET_SEGMENT",
        "COMPETITIVE_ANALYSIS",
        "STRATEGIC_INITIATIVE",
        "MARKET",
        "COMPETITOR",
        "CUSTOMER",
        "PRODUCT",
        "SALES_TERRITORY",
        "CHANNEL",
        "SALES_TEAM",
        "REVENUE"
    ],
    "SALES_TRAINING_COACHING": [
        "SALES_TRAINING_PROGRAM",
        "SALES_COACHING_SESSION",
        "SALES_ASSESSMENT",
        "ENABLEMENT_PLATFORM",
        "ENABLEMENT_FEEDBACK",
        "SALES_REP",
        "SALES_TEAM",
        "PRODUCT",
        "CUSTOMER"
    ],
    "INVENTORY_MGMT": [
        "PRODUCT"
    ]
}


def setup_module_objectmodel_relationships():
    """Associate object models with modules based on mappings."""
    for mod_code, om_codes in MODULE_OBJECTMODEL_MAP.items():
        module = get_module(mod_code)
        if module:
            for om_code in om_codes:
                object_model = get_object_model(om_code)
                if object_model and object_model not in module.object_models:
                    module.object_models.append(object_model)

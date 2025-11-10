"""
ISO 28000 - Security Management Systems for the Supply Chain Module

ISO 28000 specifies requirements for a security management system in the supply chain.
Focuses on risk assessment, security controls, and incident management.
"""

ISO_28000 = {
    "code": "ISO_28000",
    "name": "ISO 28000 - Supply Chain Security",
    "description": "Supply chain security and risk management aligned with ISO 28000 standards",
    "is_active": True,
    "display_order": 12,
    "metadata_": {"value_chains": ["SUPPLY_CHAIN"], "industries": ["RETAIL", "MANUFACTURING", "LOGISTICS", "HEALTHCARE"], "associated_object_models": ["SUPPLIER", "SHIPMENT", "WAREHOUSE", "PRODUCT", "CONTRACT"], "associated_kpis": ["cargo_theft_rate", "cybersecurity_incident_impact_reduction", "incident_response_time", "security_training_completion_rate", "supply_chain_security_breach_frequency", "vendor_risk_management_efficiency", "supply_chain_vulnerability_assessment_frequency"], "standards": ["ISO_28000", "ISO_28001", "ISO_28003", "ISO_28004"], "focus_areas": ["security_management", "risk_assessment", "incident_response", "supply_chain_resilience"]},
    "value_chains": ["SUPPLY_CHAIN"],
}

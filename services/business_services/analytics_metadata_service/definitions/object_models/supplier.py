"""
Supplier Object Model

Represents suppliers and vendors in the supply chain.
Critical for supply chain flexibility and adaptability metrics.

Suppliers provide materials, components, and products. Supplier performance
and capacity are key factors in supply chain agility (SCOR AG metrics).

Key SCOR Metrics Enabled:
- AG.1.1: Upside Supply Chain Flexibility (supplier capacity)
- CO.1.1: Total Supply Chain Management Cost (supplier costs)
"""

from analytics_models import ObjectModel

SUPPLIER = ObjectModel(
    name="Supplier",
    code="SUPPLIER",
    description="Suppliers and vendors in the supply chain",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "suppliers",
        "class_name": "Supplier",
        "columns": [
            {
                "name": "supplier_id",
                "type": "Integer",
                "primary_key": True,
                "autoincrement": True,
                "description": "Unique supplier identifier"
            },
            {
                "name": "supplier_code",
                "type": "String",
                "length": 50,
                "unique": True,
                "nullable": False,
                "index": True,
                "description": "Business supplier code"
            },
            {
                "name": "supplier_name",
                "type": "String",
                "length": 200,
                "nullable": False,
                "index": True,
                "description": "Supplier company name"
            },
            {
                "name": "supplier_type",
                "type": "String",
                "length": 50,
                "description": "Supplier type (manufacturer, distributor, wholesaler)"
            },
            {
                "name": "supplier_status",
                "type": "String",
                "length": 50,
                "nullable": False,
                "description": "Supplier status (active, inactive, suspended, preferred)"
            },
            {
                "name": "supplier_tier",
                "type": "String",
                "length": 20,
                "description": "Supplier tier (tier_1, tier_2, tier_3)"
            },
            {
                "name": "is_preferred",
                "type": "Boolean",
                "default": False,
                "description": "Preferred supplier status"
            },
            {
                "name": "is_strategic",
                "type": "Boolean",
                "default": False,
                "description": "Strategic supplier"
            },
            {
                "name": "contact_name",
                "type": "String",
                "length": 100,
                "description": "Primary contact name"
            },
            {
                "name": "contact_email",
                "type": "String",
                "length": 200,
                "description": "Primary contact email"
            },
            {
                "name": "contact_phone",
                "type": "String",
                "length": 50,
                "description": "Primary contact phone"
            },
            {
                "name": "address",
                "type": "Text",
                "description": "Supplier address"
            },
            {
                "name": "city",
                "type": "String",
                "length": 100,
                "description": "City"
            },
            {
                "name": "state",
                "type": "String",
                "length": 50,
                "description": "State/province"
            },
            {
                "name": "country",
                "type": "String",
                "length": 50,
                "description": "Country"
            },
            {
                "name": "postal_code",
                "type": "String",
                "length": 20,
                "description": "Postal code"
            },
            {
                "name": "payment_terms",
                "type": "String",
                "length": 100,
                "description": "Payment terms (Net 30, Net 60, etc.)"
            },
            {
                "name": "payment_terms_days",
                "type": "Integer",
                "description": "Payment terms in days"
            },
            {
                "name": "currency",
                "type": "String",
                "length": 3,
                "description": "Default currency"
            },
            {
                "name": "lead_time_days",
                "type": "Integer",
                "description": "Standard lead time in days"
            },
            {
                "name": "minimum_order_quantity",
                "type": "Integer",
                "description": "Minimum order quantity"
            },
            {
                "name": "capacity_units_per_month",
                "type": "Integer",
                "description": "Monthly production capacity"
            },
            {
                "name": "current_utilization_percent",
                "type": "Float",
                "description": "Current capacity utilization %"
            },
            {
                "name": "can_scale_up",
                "type": "Boolean",
                "description": "Can increase capacity"
            },
            {
                "name": "scale_up_time_days",
                "type": "Integer",
                "description": "Days to scale up capacity by 20%"
            },
            {
                "name": "quality_rating",
                "type": "Float",
                "description": "Quality rating (0-5)"
            },
            {
                "name": "delivery_performance_percent",
                "type": "Float",
                "description": "On-time delivery %"
            },
            {
                "name": "defect_rate_percent",
                "type": "Float",
                "description": "Defect rate %"
            },
            {
                "name": "total_annual_spend",
                "type": "Float",
                "description": "Total annual spend with supplier"
            },
            {
                "name": "risk_level",
                "type": "String",
                "length": 20,
                "description": "Risk level (low, medium, high, critical)"
            },
            {
                "name": "risk_factors",
                "type": "JSON",
                "description": "Risk factors (geographic, financial, etc.)"
            },
            {
                "name": "certifications",
                "type": "JSON",
                "description": "Certifications (ISO, etc.)"
            },
            {
                "name": "contract_start_date",
                "type": "DateTime",
                "description": "Contract start date"
            },
            {
                "name": "contract_end_date",
                "type": "DateTime",
                "description": "Contract end date"
            },
            {
                "name": "last_audit_date",
                "type": "DateTime",
                "description": "Last supplier audit date"
            },
            {
                "name": "next_audit_date",
                "type": "DateTime",
                "description": "Next scheduled audit"
            },
            {
                "name": "notes",
                "type": "Text",
                "description": "Supplier notes"
            },
            {
                "name": "created_at",
                "type": "DateTime",
                "default": "now()",
                "nullable": False
            },
            {
                "name": "updated_at",
                "type": "DateTime",
                "default": "now()",
                "onupdate": "now()",
                "nullable": False
            }
        ],
        "indexes": [
            {
                "name": "ix_suppliers_supplier_code",
                "columns": ["supplier_code"],
                "unique": True
            },
            {
                "name": "ix_suppliers_supplier_name",
                "columns": ["supplier_name"]
            },
            {
                "name": "ix_suppliers_status",
                "columns": ["supplier_status"]
            },
            {
                "name": "ix_suppliers_country",
                "columns": ["country"]
            }
        ],
        "constraints": [
            {
                "type": "check",
                "name": "chk_quality_rating_range",
                "expression": "quality_rating IS NULL OR (quality_rating >= 0 AND quality_rating <= 5)"
            },
            {
                "type": "check",
                "name": "chk_percentages_valid",
                "expression": "delivery_performance_percent IS NULL OR (delivery_performance_percent >= 0 AND delivery_performance_percent <= 100)"
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
    Supplier "1" -- "0..*" Material : supplies
    Supplier "1" -- "0..*" PurchaseOrder : receives
    
    note right of Supplier
        Supplier capacity and performance
        Enables supply chain flexibility
        and agility metrics
    end note
    @enduml
    """,

    metadata_={
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "PROCUREMENT"],
        "related_kpis": [
            "UPSIDE_SUPPLY_CHAIN_FLEXIBILITY",
            "TOTAL_SUPPLY_CHAIN_MANAGEMENT_COST"
        ],
        "key_attributes": [
            "supplier_id",
            "supplier_code",
            "supplier_name",
            "supplier_status",
            "capacity_units_per_month",
            "can_scale_up",
            "scale_up_time_days",
            "quality_rating"
        ],
        "supplier_types": [
            "manufacturer",
            "distributor",
            "wholesaler",
            "contract_manufacturer",
            "service_provider"
        ],
        "supplier_statuses": [
            "active",
            "inactive",
            "suspended",
            "preferred",
            "under_review",
            "terminated"
        ],
        "supplier_tiers": [
            "tier_1",
            "tier_2",
            "tier_3"
        ],
        "scor_metrics": {
            "AG.1.1": {
                "name": "Upside Supply Chain Flexibility",
                "usage": "scale_up_time_days = days to achieve 20% capacity increase",
                "calculation": "MIN(scale_up_time_days) across all suppliers"
            },
            "CO.1.1": {
                "name": "Total Supply Chain Management Cost",
                "usage": "total_annual_spend contributes to source costs"
            }
        },
        "performance_metrics": {
            "quality": "quality_rating (0-5 scale)",
            "delivery": "delivery_performance_percent (on-time %)",
            "defects": "defect_rate_percent",
            "capacity": "current_utilization_percent"
        }
    }
)

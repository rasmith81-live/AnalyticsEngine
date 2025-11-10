"""
Cost Object Model

Represents costs across the supply chain (plan, source, make, deliver, return).
Essential for SCOR cost and profitability metrics.

Costs are tracked by activity, cost center, and SCOR process to enable
detailed cost analysis and Total Supply Chain Management Cost calculation.

Key SCOR Metrics Enabled:
- CO.1.1: Total Supply Chain Management Cost
- CO.1.2: Cost of Goods Sold
- PR.1.1: Return on Supply Chain Fixed Assets
"""

from analytics_models import ObjectModel

COST = ObjectModel(
    name="Cost",
    code="COST",
    description="Supply chain costs by activity, process, and cost center",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "costs",
        "class_name": "Cost",
        "is_hypertable": True,
        "time_column": "cost_date",
        "partition_interval": "1 month",
        "columns": [
            {
                "name": "cost_id",
                "type": "Integer",
                "primary_key": True,
                "autoincrement": True,
                "description": "Unique cost record identifier"
            },
            {
                "name": "cost_date",
                "type": "DateTime",
                "nullable": False,
                "index": True,
                "description": "Date cost was incurred"
            },
            {
                "name": "cost_type",
                "type": "String",
                "length": 50,
                "nullable": False,
                "index": True,
                "description": "Cost type (material, labor, overhead, freight, etc.)"
            },
            {
                "name": "cost_category",
                "type": "String",
                "length": 50,
                "nullable": False,
                "index": True,
                "description": "Cost category (direct, indirect, fixed, variable)"
            },
            {
                "name": "scor_process",
                "type": "String",
                "length": 50,
                "index": True,
                "description": "SCOR process (Plan, Source, Make, Deliver, Return)"
            },
            {
                "name": "scor_process_level_2",
                "type": "String",
                "length": 50,
                "description": "SCOR Level 2 process (P1, S1, M1, D1, R1, etc.)"
            },
            {
                "name": "activity_id",
                "type": "Integer",
                "foreign_key": "activities.activity_id",
                "index": True,
                "description": "Reference to activity"
            },
            {
                "name": "activity_name",
                "type": "String",
                "length": 200,
                "description": "Activity name (denormalized)"
            },
            {
                "name": "cost_center_id",
                "type": "Integer",
                "foreign_key": "cost_centers.cost_center_id",
                "index": True,
                "description": "Reference to cost center"
            },
            {
                "name": "cost_center_name",
                "type": "String",
                "length": 200,
                "description": "Cost center name (denormalized)"
            },
            {
                "name": "product_id",
                "type": "Integer",
                "foreign_key": "products.product_id",
                "index": True,
                "description": "Reference to product (if applicable)"
            },
            {
                "name": "order_id",
                "type": "Integer",
                "foreign_key": "orders.order_id",
                "index": True,
                "description": "Reference to order (if applicable)"
            },
            {
                "name": "supplier_id",
                "type": "Integer",
                "foreign_key": "suppliers.supplier_id",
                "index": True,
                "description": "Reference to supplier (if applicable)"
            },
            {
                "name": "facility_id",
                "type": "Integer",
                "index": True,
                "description": "Facility/warehouse"
            },
            {
                "name": "cost_amount",
                "type": "Float",
                "nullable": False,
                "description": "Cost amount"
            },
            {
                "name": "currency",
                "type": "String",
                "length": 3,
                "description": "Currency code"
            },
            {
                "name": "cost_amount_usd",
                "type": "Float",
                "description": "Cost in USD (for aggregation)"
            },
            {
                "name": "quantity",
                "type": "Float",
                "description": "Quantity (for unit cost calculation)"
            },
            {
                "name": "unit_cost",
                "type": "Float",
                "description": "Cost per unit"
            },
            {
                "name": "is_cogs",
                "type": "Boolean",
                "default": False,
                "description": "Part of Cost of Goods Sold"
            },
            {
                "name": "is_operating_expense",
                "type": "Boolean",
                "default": False,
                "description": "Operating expense"
            },
            {
                "name": "is_capital_expense",
                "type": "Boolean",
                "default": False,
                "description": "Capital expense"
            },
            {
                "name": "gl_account",
                "type": "String",
                "length": 50,
                "description": "General ledger account"
            },
            {
                "name": "invoice_number",
                "type": "String",
                "length": 100,
                "description": "Invoice number"
            },
            {
                "name": "payment_date",
                "type": "DateTime",
                "description": "Date payment was made"
            },
            {
                "name": "fiscal_year",
                "type": "Integer",
                "index": True,
                "description": "Fiscal year"
            },
            {
                "name": "fiscal_quarter",
                "type": "Integer",
                "description": "Fiscal quarter (1-4)"
            },
            {
                "name": "fiscal_month",
                "type": "Integer",
                "description": "Fiscal month (1-12)"
            },
            {
                "name": "region",
                "type": "String",
                "length": 100,
                "description": "Geographic region"
            },
            {
                "name": "notes",
                "type": "Text",
                "description": "Cost notes"
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
                "name": "ix_costs_cost_date",
                "columns": ["cost_date"]
            },
            {
                "name": "ix_costs_cost_type",
                "columns": ["cost_type"]
            },
            {
                "name": "ix_costs_scor_process",
                "columns": ["scor_process"]
            },
            {
                "name": "ix_costs_cost_center_id",
                "columns": ["cost_center_id"]
            },
            {
                "name": "ix_costs_product_id",
                "columns": ["product_id"]
            },
            {
                "name": "ix_costs_fiscal_year",
                "columns": ["fiscal_year"]
            },
            {
                "name": "ix_costs_composite",
                "columns": ["scor_process", "cost_date", "cost_type"],
                "description": "Common query pattern"
            }
        ],
        "constraints": [
            {
                "type": "check",
                "name": "chk_cost_amount_positive",
                "expression": "cost_amount >= 0"
            },
            {
                "type": "check",
                "name": "chk_fiscal_quarter_valid",
                "expression": "fiscal_quarter IS NULL OR (fiscal_quarter >= 1 AND fiscal_quarter <= 4)"
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
    Cost "*" -- "0..1" Activity : incurred_by
    Cost "*" -- "0..1" CostCenter : allocated_to
    Cost "*" -- "0..1" Product : related_to
    Cost "*" -- "0..1" Order : related_to
    Cost "*" -- "0..1" Supplier : paid_to
    
    note right of Cost
        TimescaleDB hypertable
        Tracks all SC costs by process
        Enables SCOR cost metrics
    end note
    @enduml
    """,

    metadata_={
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "FINANCE"],
        "related_kpis": [
            "TOTAL_SUPPLY_CHAIN_MANAGEMENT_COST",
            "COST_OF_GOODS_SOLD",
            "RETURN_ON_SUPPLY_CHAIN_FIXED_ASSETS"
        ],
        "key_attributes": [
            "cost_id",
            "cost_date",
            "cost_type",
            "scor_process",
            "cost_amount",
            "is_cogs"
        ],
        "cost_types": [
            "material",
            "labor",
            "overhead",
            "freight",
            "warehousing",
            "handling",
            "packaging",
            "utilities",
            "depreciation",
            "insurance"
        ],
        "cost_categories": [
            "direct",
            "indirect",
            "fixed",
            "variable",
            "semi_variable"
        ],
        "scor_processes": [
            "Plan",
            "Source",
            "Make",
            "Deliver",
            "Return",
            "Enable"
        ],
        "scor_metrics": {
            "CO.1.1": {
                "name": "Total Supply Chain Management Cost",
                "calculation": "SUM(cost_amount) WHERE scor_process IN ('Plan', 'Source', 'Make', 'Deliver', 'Return')"
            },
            "CO.1.2": {
                "name": "Cost of Goods Sold",
                "calculation": "SUM(cost_amount) WHERE is_cogs = TRUE"
            },
            "PR.1.1": {
                "name": "Return on Supply Chain Fixed Assets",
                "usage": "Operating expenses in numerator calculation"
            }
        },
        "timescaledb_features": {
            "compression": "After 90 days",
            "retention": "7 years (regulatory compliance)",
            "continuous_aggregates": ["monthly_costs_by_process", "quarterly_costs_by_center"]
        }
    }
)

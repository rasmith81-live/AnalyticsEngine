"""
Accounts Receivable Object Model

Represents amounts owed by customers for goods and services.
Critical for Cash-to-Cash cycle time calculation (Days Sales Outstanding).

Accounts Receivable tracks outstanding customer invoices and expected payments,
used to calculate DSO (Days Sales Outstanding) for SCOR asset management metrics.

Key SCOR Metrics Enabled:
- AM.1.1: Cash-to-Cash Cycle Time (DSO component)
- AM.1.2: Return on Working Capital (current assets)
"""

from analytics_models import ObjectModel

ACCOUNTS_RECEIVABLE = ObjectModel(
    name="Accounts Receivable",
    code="ACCOUNTS_RECEIVABLE",
    description="Amounts owed by customers for goods and services",

    table_schema={
        "table_name": "accounts_receivable",
        "class_name": "AccountsReceivable",
        "columns": [
            {"name": "ar_id", "type": "Integer", "primary_key": True, "autoincrement": True},
            {"name": "customer_id", "type": "Integer", "foreign_key": "customers.customer_id", "nullable": False, "index": True},
            {"name": "invoice_id", "type": "Integer", "foreign_key": "invoices.invoice_id", "nullable": False, "index": True},
            {"name": "invoice_date", "type": "DateTime", "nullable": False, "index": True},
            {"name": "due_date", "type": "DateTime", "nullable": False, "index": True},
            {"name": "invoice_amount", "type": "Float", "nullable": False},
            {"name": "amount_paid", "type": "Float", "default": 0},
            {"name": "amount_due", "type": "Float"},
            {"name": "currency", "type": "String", "length": 3},
            {"name": "payment_date", "type": "DateTime", "index": True},
            {"name": "days_to_payment", "type": "Integer", "description": "DSO calculation"},
            {"name": "is_paid", "type": "Boolean", "default": False, "index": True},
            {"name": "is_overdue", "type": "Boolean", "default": False, "index": True},
            {"name": "days_overdue", "type": "Integer"},
            {"name": "ar_status", "type": "String", "length": 50, "nullable": False, "index": True},
            {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False},
            {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}
        ]
    },

    schema_definition="""
    @startuml
    AccountsReceivable "*" -- "1" Customer : owed_by
    AccountsReceivable "1" -- "1" Invoice : tracks
    @enduml
    """,

    metadata_={
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "FINANCE"],
        "related_kpis": ["CASH_TO_CASH_CYCLE_TIME", "RETURN_ON_WORKING_CAPITAL"],
        "scor_metrics": {
            "AM.1.1": {"name": "Cash-to-Cash Cycle Time", "component": "Days Sales Outstanding"},
            "AM.1.2": {"name": "Return on Working Capital", "usage": "AR is part of current assets"}
        }
    }
)

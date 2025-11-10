"""
Payment Object Model

Represents payments received from customers for invoices.
Critical for Cash-to-Cash cycle time calculation (cash inflow tracking).

Payments track when cash is received from customers, completing the
Days Sales Outstanding (DSO) component of the Cash-to-Cash cycle.

Key SCOR Metrics Enabled:
- AM.1.1: Cash-to-Cash Cycle Time (cash receipt tracking)
- AM.1.2: Return on Working Capital (cash flow)
"""

from analytics_models import ObjectModel

PAYMENT = ObjectModel(
    name="Payment",
    code="PAYMENT",
    description="Customer payments received for invoices",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "payments",
        "class_name": "Payment",
        "columns": [
            {
                "name": "payment_id",
                "type": "Integer",
                "primary_key": True,
                "autoincrement": True,
                "description": "Unique payment identifier"
            },
            {
                "name": "payment_number",
                "type": "String",
                "length": 50,
                "unique": True,
                "nullable": False,
                "index": True,
                "description": "Business payment number"
            },
            {
                "name": "invoice_id",
                "type": "Integer",
                "foreign_key": "invoices.invoice_id",
                "nullable": False,
                "index": True,
                "description": "Reference to invoice"
            },
            {
                "name": "customer_id",
                "type": "Integer",
                "foreign_key": "customers.customer_id",
                "nullable": False,
                "index": True,
                "description": "Reference to customer"
            },
            {
                "name": "payment_date",
                "type": "DateTime",
                "nullable": False,
                "index": True,
                "description": "Date payment was received"
            },
            {
                "name": "payment_amount",
                "type": "Float",
                "nullable": False,
                "description": "Payment amount"
            },
            {
                "name": "currency",
                "type": "String",
                "length": 3,
                "description": "Currency code"
            },
            {
                "name": "payment_method",
                "type": "String",
                "length": 50,
                "nullable": False,
                "index": True,
                "description": "Payment method (credit_card, wire_transfer, check, ACH, etc.)"
            },
            {
                "name": "payment_status",
                "type": "String",
                "length": 50,
                "nullable": False,
                "index": True,
                "description": "Payment status (pending, cleared, failed, refunded)"
            },
            {
                "name": "transaction_id",
                "type": "String",
                "length": 100,
                "unique": True,
                "index": True,
                "description": "External transaction ID"
            },
            {
                "name": "reference_number",
                "type": "String",
                "length": 100,
                "description": "Check number or reference"
            },
            {
                "name": "bank_account",
                "type": "String",
                "length": 100,
                "description": "Bank account (last 4 digits)"
            },
            {
                "name": "processing_fee",
                "type": "Float",
                "default": 0,
                "description": "Payment processing fee"
            },
            {
                "name": "net_amount",
                "type": "Float",
                "description": "Net amount after fees"
            },
            {
                "name": "applied_to_invoice",
                "type": "Float",
                "description": "Amount applied to invoice"
            },
            {
                "name": "unapplied_amount",
                "type": "Float",
                "default": 0,
                "description": "Unapplied credit amount"
            },
            {
                "name": "deposit_date",
                "type": "DateTime",
                "description": "Date deposited to bank"
            },
            {
                "name": "cleared_date",
                "type": "DateTime",
                "description": "Date payment cleared"
            },
            {
                "name": "is_cleared",
                "type": "Boolean",
                "default": False,
                "description": "Payment has cleared"
            },
            {
                "name": "days_to_clear",
                "type": "Integer",
                "description": "Days from payment to cleared"
            },
            {
                "name": "payment_processor",
                "type": "String",
                "length": 100,
                "description": "Payment processor (Stripe, PayPal, etc.)"
            },
            {
                "name": "notes",
                "type": "Text",
                "description": "Payment notes"
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
            },
            {
                "name": "created_by",
                "type": "String",
                "length": 100,
                "description": "User who recorded payment"
            }
        ],
        "indexes": [
            {
                "name": "ix_payments_payment_number",
                "columns": ["payment_number"],
                "unique": True
            },
            {
                "name": "ix_payments_invoice_id",
                "columns": ["invoice_id"]
            },
            {
                "name": "ix_payments_customer_id",
                "columns": ["customer_id"]
            },
            {
                "name": "ix_payments_payment_date",
                "columns": ["payment_date"]
            },
            {
                "name": "ix_payments_transaction_id",
                "columns": ["transaction_id"]
            },
            {
                "name": "ix_payments_payment_method",
                "columns": ["payment_method"]
            },
            {
                "name": "ix_payments_status",
                "columns": ["payment_status"]
            }
        ],
        "constraints": [
            {
                "type": "check",
                "name": "chk_payment_amount_positive",
                "expression": "payment_amount > 0"
            },
            {
                "type": "check",
                "name": "chk_net_amount_calculation",
                "expression": "net_amount IS NULL OR net_amount = payment_amount - processing_fee"
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
    Payment "*" -- "1" Invoice : pays
    Payment "*" -- "1" Customer : paid_by
    
    note right of Payment
        Tracks cash receipts
        Completes DSO calculation
        for Cash-to-Cash cycle
    end note
    @enduml
    """,

    metadata_={
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "FINANCE"],
        "related_kpis": [
            "CASH_TO_CASH_CYCLE_TIME",
            "RETURN_ON_WORKING_CAPITAL"
        ],
        "key_attributes": [
            "payment_id",
            "payment_number",
            "invoice_id",
            "customer_id",
            "payment_date",
            "payment_amount",
            "is_cleared"
        ],
        "payment_methods": [
            "credit_card",
            "debit_card",
            "wire_transfer",
            "ACH",
            "check",
            "cash",
            "paypal",
            "stripe",
            "cryptocurrency"
        ],
        "payment_statuses": [
            "pending",
            "processing",
            "cleared",
            "failed",
            "refunded",
            "cancelled"
        ],
        "scor_metrics": {
            "AM.1.1": {
                "name": "Cash-to-Cash Cycle Time",
                "usage": "Payment date completes DSO calculation (invoice_date to payment_date)"
            },
            "AM.1.2": {
                "name": "Return on Working Capital",
                "usage": "Payment reduces accounts receivable, improving working capital"
            }
        }
    }
)

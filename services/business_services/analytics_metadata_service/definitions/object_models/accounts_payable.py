"""
Accounts Payable Object Model

Represents amounts owed to suppliers for goods and services.
Critical for Cash-to-Cash cycle time calculation (Days Payable Outstanding).

Accounts Payable tracks outstanding supplier invoices and payment obligations,
used to calculate DPO (Days Payable Outstanding) for SCOR asset management metrics.

Key SCOR Metrics Enabled:
- AM.1.1: Cash-to-Cash Cycle Time (DPO component)
- AM.1.2: Return on Working Capital (current liabilities)
"""

ACCOUNTS_PAYABLE = {
    "code": "ACCOUNTS_PAYABLE",
    "name": "Accounts Payable",
    "description": "Amounts owed to suppliers for goods and services",
    "table_schema": {"table_name": "accounts_payable", "class_name": "AccountsPayable", "columns": [{"name": "ap_id", "type": "Integer", "primary_key": True, "autoincrement": True, "description": "Unique AP identifier"}, {"name": "supplier_id", "type": "Integer", "foreign_key": "suppliers.supplier_id", "nullable": False, "index": True, "description": "Reference to supplier"}, {"name": "supplier_invoice_number", "type": "String", "length": 100, "index": True, "description": "Supplier's invoice number"}, {"name": "receipt_id", "type": "Integer", "foreign_key": "receipts.receipt_id", "index": True, "description": "Reference to receipt"}, {"name": "invoice_date", "type": "DateTime", "nullable": False, "index": True, "description": "Date of supplier invoice"}, {"name": "due_date", "type": "DateTime", "nullable": False, "index": True, "description": "Payment due date"}, {"name": "payment_terms", "type": "String", "length": 50, "description": "Payment terms (Net 30, Net 60, etc.)"}, {"name": "payment_terms_days", "type": "Integer", "description": "Payment terms in days"}, {"name": "invoice_amount", "type": "Float", "nullable": False, "description": "Total invoice amount"}, {"name": "amount_paid", "type": "Float", "default": 0, "description": "Amount paid so far"}, {"name": "amount_due", "type": "Float", "description": "Remaining amount due"}, {"name": "currency", "type": "String", "length": 3, "description": "Currency code"}, {"name": "payment_date", "type": "DateTime", "index": True, "description": "Date payment was made"}, {"name": "days_to_payment", "type": "Integer", "description": "Days from invoice to payment (DPO)"}, {"name": "is_paid", "type": "Boolean", "default": False, "index": True, "description": "Fully paid"}, {"name": "is_overdue", "type": "Boolean", "default": False, "index": True, "description": "Payment overdue"}, {"name": "days_overdue", "type": "Integer", "description": "Days past due date"}, {"name": "ap_status", "type": "String", "length": 50, "nullable": False, "index": True, "description": "AP status (pending, approved, scheduled, paid, disputed)"}, {"name": "gl_account", "type": "String", "length": 50, "description": "General ledger account"}, {"name": "cost_center_id", "type": "Integer", "foreign_key": "cost_centers.cost_center_id", "index": True, "description": "Cost center"}, {"name": "notes", "type": "Text", "description": "AP notes"}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_ap_supplier_id", "columns": ["supplier_id"]}, {"name": "ix_ap_invoice_date", "columns": ["invoice_date"]}, {"name": "ix_ap_due_date", "columns": ["due_date"]}, {"name": "ix_ap_payment_date", "columns": ["payment_date"]}, {"name": "ix_ap_is_paid", "columns": ["is_paid"]}, {"name": "ix_ap_status", "columns": ["ap_status"]}], "constraints": [{"type": "check", "name": "chk_amounts_positive", "expression": "invoice_amount >= 0 AND amount_paid >= 0"}]},
    "schema_definition": """
    @startuml
    AccountsPayable "*" -- "1" Supplier : owed_to
    AccountsPayable "*" -- "0..1" Receipt : related_to
    AccountsPayable "*" -- "0..1" CostCenter : allocated_to
    @enduml
    """,
    "metadata_": {"modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "FINANCE"], "related_kpis": ["CASH_TO_CASH_CYCLE_TIME", "RETURN_ON_WORKING_CAPITAL"], "scor_metrics": {"AM.1.1": {"name": "Cash-to-Cash Cycle Time", "calculation": "DPO = AVG(days_to_payment) OR (AP / COGS) * 365", "component": "Days Payable Outstanding"}, "AM.1.2": {"name": "Return on Working Capital", "usage": "AP is part of current liabilities in working capital"}}},
}

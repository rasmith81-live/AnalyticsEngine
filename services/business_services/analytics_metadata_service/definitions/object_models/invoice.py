"""
Invoice Object Model

Represents customer invoices for orders.
Critical for Cash-to-Cash cycle time calculation (Days Sales Outstanding).

Invoices track billing information, payment terms, and payment status.
Used to calculate DSO (Days Sales Outstanding) for SCOR asset management metrics.

Key SCOR Metrics Enabled:
- AM.1.1: Cash-to-Cash Cycle Time (DSO component)
- AM.1.2: Return on Working Capital (accounts receivable)
"""

INVOICE = {
    "code": "INVOICE",
    "name": "Invoice",
    "description": "Customer invoices for orders and services",
    "table_schema": {"table_name": "invoices", "class_name": "Invoice", "columns": [{"name": "invoice_id", "type": "Integer", "primary_key": True, "autoincrement": True, "description": "Unique invoice identifier"}, {"name": "invoice_number", "type": "String", "length": 50, "unique": True, "nullable": False, "index": True, "description": "Business invoice number"}, {"name": "order_id", "type": "Integer", "foreign_key": "orders.order_id", "nullable": False, "index": True, "description": "Reference to order"}, {"name": "customer_id", "type": "Integer", "foreign_key": "customers.customer_id", "nullable": False, "index": True, "description": "Reference to customer"}, {"name": "invoice_date", "type": "DateTime", "nullable": False, "index": True, "description": "Date invoice was issued"}, {"name": "due_date", "type": "DateTime", "nullable": False, "index": True, "description": "Payment due date"}, {"name": "payment_terms", "type": "String", "length": 50, "description": "Payment terms (Net 30, Net 60, etc.)"}, {"name": "payment_terms_days", "type": "Integer", "description": "Payment terms in days"}, {"name": "invoice_status", "type": "String", "length": 50, "nullable": False, "index": True, "description": "Invoice status (draft, sent, paid, overdue, cancelled)"}, {"name": "subtotal", "type": "Float", "nullable": False, "description": "Subtotal before tax"}, {"name": "tax_amount", "type": "Float", "default": 0, "description": "Tax amount"}, {"name": "discount_amount", "type": "Float", "default": 0, "description": "Discount amount"}, {"name": "shipping_amount", "type": "Float", "default": 0, "description": "Shipping charges"}, {"name": "total_amount", "type": "Float", "nullable": False, "description": "Total invoice amount"}, {"name": "amount_paid", "type": "Float", "default": 0, "description": "Amount paid so far"}, {"name": "amount_due", "type": "Float", "description": "Remaining amount due"}, {"name": "currency", "type": "String", "length": 3, "description": "Currency code"}, {"name": "payment_date", "type": "DateTime", "index": True, "description": "Date payment was received"}, {"name": "days_to_payment", "type": "Integer", "description": "Days from invoice to payment (DSO)"}, {"name": "is_paid", "type": "Boolean", "default": False, "index": True, "description": "Invoice fully paid"}, {"name": "is_overdue", "type": "Boolean", "default": False, "index": True, "description": "Payment overdue"}, {"name": "days_overdue", "type": "Integer", "description": "Days past due date"}, {"name": "billing_address", "type": "Text", "description": "Billing address"}, {"name": "shipping_address", "type": "Text", "description": "Shipping address"}, {"name": "purchase_order_number", "type": "String", "length": 100, "description": "Customer PO number"}, {"name": "notes", "type": "Text", "description": "Invoice notes"}, {"name": "sent_date", "type": "DateTime", "description": "Date invoice was sent to customer"}, {"name": "reminder_sent_count", "type": "Integer", "default": 0, "description": "Number of payment reminders sent"}, {"name": "last_reminder_date", "type": "DateTime", "description": "Date of last payment reminder"}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}, {"name": "created_by", "type": "String", "length": 100, "description": "User who created invoice"}], "indexes": [{"name": "ix_invoices_invoice_number", "columns": ["invoice_number"], "unique": True}, {"name": "ix_invoices_order_id", "columns": ["order_id"]}, {"name": "ix_invoices_customer_id", "columns": ["customer_id"]}, {"name": "ix_invoices_invoice_date", "columns": ["invoice_date"]}, {"name": "ix_invoices_due_date", "columns": ["due_date"]}, {"name": "ix_invoices_payment_date", "columns": ["payment_date"]}, {"name": "ix_invoices_status", "columns": ["invoice_status"]}, {"name": "ix_invoices_is_paid", "columns": ["is_paid"]}, {"name": "ix_invoices_composite", "columns": ["customer_id", "invoice_date", "is_paid"], "description": "Common query pattern for DSO calculation"}], "constraints": [{"type": "check", "name": "chk_amounts_positive", "expression": "total_amount >= 0 AND amount_paid >= 0"}, {"type": "check", "name": "chk_amount_due_calculation", "expression": "amount_due = total_amount - amount_paid"}, {"type": "check", "name": "chk_dates_logical", "expression": "due_date >= invoice_date"}]},
    "schema_definition": """
    @startuml
    Invoice "*" -- "1" Order : bills
    Invoice "*" -- "1" Customer : billed_to
    Invoice "1" -- "0..*" Payment : paid_via
    Invoice "1" -- "0..1" AccountsReceivable : creates
    
    note right of Invoice
        Tracks billing and payment
        Enables DSO calculation
        for Cash-to-Cash cycle
    end note
    @enduml
    """,
    "metadata_": {"modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "FINANCE"], "related_kpis": ["CASH_TO_CASH_CYCLE_TIME", "RETURN_ON_WORKING_CAPITAL"], "key_attributes": ["invoice_id", "invoice_number", "order_id", "customer_id", "invoice_date", "payment_date", "days_to_payment", "is_paid"], "invoice_statuses": ["draft", "sent", "viewed", "partial_payment", "paid", "overdue", "cancelled", "refunded"], "payment_terms": ["Due on Receipt", "Net 10", "Net 15", "Net 30", "Net 45", "Net 60", "Net 90", "2/10 Net 30"], "scor_metrics": {"AM.1.1": {"name": "Cash-to-Cash Cycle Time", "calculation": "DSO = AVG(days_to_payment) OR (AR / Revenue) * 365", "component": "Days Sales Outstanding"}, "AM.1.2": {"name": "Return on Working Capital", "usage": "Accounts Receivable (amount_due) is part of working capital"}}, "dso_calculation": {"method_1": "AVG(days_to_payment) for paid invoices", "method_2": "(Total AR / Total Revenue) * 365", "best_practice": "Calculate both and compare"}},
}

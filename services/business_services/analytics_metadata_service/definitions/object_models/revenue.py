"""
Revenue Object Model

Represents revenue generated from supply chain operations.
Essential for SCOR profitability and asset management metrics.

Revenue is tracked by order, product, and customer to enable
profitability analysis and return calculations.

Key SCOR Metrics Enabled:
- PR.1.1: Return on Supply Chain Fixed Assets
- AM.1.2: Return on Working Capital
"""

REVENUE = {
    "code": "REVENUE",
    "name": "Revenue",
    "description": "Revenue generated from supply chain operations",
    "table_schema": {"table_name": "revenue", "class_name": "Revenue", "is_hypertable": True, "time_column": "revenue_date", "partition_interval": "1 month", "columns": [{"name": "revenue_id", "type": "Integer", "primary_key": True, "autoincrement": True, "description": "Unique revenue record identifier"}, {"name": "revenue_date", "type": "DateTime", "nullable": False, "index": True, "description": "Date revenue was recognized"}, {"name": "revenue_type", "type": "String", "length": 50, "nullable": False, "index": True, "description": "Revenue type (product_sales, service, freight, other)"}, {"name": "order_id", "type": "Integer", "foreign_key": "orders.order_id", "nullable": False, "index": True, "description": "Reference to order"}, {"name": "order_line_id", "type": "Integer", "foreign_key": "order_lines.order_line_id", "index": True, "description": "Reference to order line"}, {"name": "customer_id", "type": "Integer", "foreign_key": "customers.customer_id", "nullable": False, "index": True, "description": "Reference to customer"}, {"name": "product_id", "type": "Integer", "foreign_key": "products.product_id", "index": True, "description": "Reference to product"}, {"name": "revenue_amount", "type": "Float", "nullable": False, "description": "Revenue amount"}, {"name": "currency", "type": "String", "length": 3, "description": "Currency code"}, {"name": "revenue_amount_usd", "type": "Float", "description": "Revenue in USD (for aggregation)"}, {"name": "quantity", "type": "Float", "description": "Quantity sold"}, {"name": "unit_price", "type": "Float", "description": "Price per unit"}, {"name": "discount_amount", "type": "Float", "default": 0, "description": "Discount amount"}, {"name": "tax_amount", "type": "Float", "default": 0, "description": "Tax amount"}, {"name": "cost_of_goods_sold", "type": "Float", "description": "COGS for this revenue"}, {"name": "gross_profit", "type": "Float", "description": "Gross profit (revenue - COGS)"}, {"name": "gross_margin_percent", "type": "Float", "description": "Gross margin percentage"}, {"name": "channel", "type": "String", "length": 50, "index": True, "description": "Sales channel (online, retail, wholesale, partner)"}, {"name": "region", "type": "String", "length": 100, "index": True, "description": "Geographic region"}, {"name": "sales_rep_id", "type": "Integer", "description": "Sales representative"}, {"name": "facility_id", "type": "Integer", "description": "Fulfillment facility"}, {"name": "invoice_id", "type": "Integer", "foreign_key": "invoices.invoice_id", "index": True, "description": "Reference to invoice"}, {"name": "invoice_number", "type": "String", "length": 100, "description": "Invoice number"}, {"name": "invoice_date", "type": "DateTime", "description": "Invoice date"}, {"name": "payment_date", "type": "DateTime", "description": "Date payment was received"}, {"name": "payment_method", "type": "String", "length": 50, "description": "Payment method"}, {"name": "is_recognized", "type": "Boolean", "default": False, "description": "Revenue has been recognized"}, {"name": "recognition_method", "type": "String", "length": 50, "description": "Revenue recognition method (point_of_sale, delivery, etc.)"}, {"name": "fiscal_year", "type": "Integer", "nullable": False, "index": True, "description": "Fiscal year"}, {"name": "fiscal_quarter", "type": "Integer", "description": "Fiscal quarter (1-4)"}, {"name": "fiscal_month", "type": "Integer", "description": "Fiscal month (1-12)"}, {"name": "gl_account", "type": "String", "length": 50, "description": "General ledger account"}, {"name": "notes", "type": "Text", "description": "Revenue notes"}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_revenue_revenue_date", "columns": ["revenue_date"]}, {"name": "ix_revenue_order_id", "columns": ["order_id"]}, {"name": "ix_revenue_customer_id", "columns": ["customer_id"]}, {"name": "ix_revenue_product_id", "columns": ["product_id"]}, {"name": "ix_revenue_channel", "columns": ["channel"]}, {"name": "ix_revenue_region", "columns": ["region"]}, {"name": "ix_revenue_fiscal_year", "columns": ["fiscal_year"]}, {"name": "ix_revenue_composite", "columns": ["revenue_date", "customer_id", "product_id"], "description": "Common query pattern"}], "constraints": [{"type": "check", "name": "chk_revenue_amount_positive", "expression": "revenue_amount >= 0"}, {"type": "check", "name": "chk_fiscal_quarter_valid", "expression": "fiscal_quarter IS NULL OR (fiscal_quarter >= 1 AND fiscal_quarter <= 4)"}, {"name": "chk_gross_margin_calculation", "expression": "gross_profit IS NULL OR gross_profit = revenue_amount - cost_of_goods_sold"}]},
    "schema_definition": """
    @startuml
    Revenue "*" -- "1" Order : generated_from
    Revenue "*" -- "0..1" OrderLine : line_detail
    Revenue "*" -- "1" Customer : paid_by
    Revenue "*" -- "0..1" Product : for_product
    Revenue "*" -- "0..1" Invoice : billed_via
    
    note right of Revenue
        TimescaleDB hypertable
        Tracks revenue by order/product
        Enables profitability metrics
    end note
    @enduml
    """,
    "metadata_": {"modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "FINANCE"], "related_kpis": ["RETURN_ON_SUPPLY_CHAIN_FIXED_ASSETS", "RETURN_ON_WORKING_CAPITAL"], "key_attributes": ["revenue_id", "revenue_date", "order_id", "customer_id", "revenue_amount", "gross_profit", "gross_margin_percent"], "revenue_types": ["product_sales", "service_revenue", "freight_revenue", "installation", "maintenance", "other"], "channels": ["online", "retail", "wholesale", "partner", "direct_sales", "marketplace"], "recognition_methods": ["point_of_sale", "delivery", "percentage_of_completion", "subscription", "milestone"], "scor_metrics": {"PR.1.1": {"name": "Return on Supply Chain Fixed Assets", "calculation": "(Revenue - COGS - Operating Expense) / SC Fixed Assets", "usage": "Revenue is numerator component"}, "AM.1.2": {"name": "Return on Working Capital", "calculation": "(Revenue - COGS - Operating Expense) / Working Capital", "usage": "Revenue is numerator component"}}, "profitability_calculations": {"gross_profit": "revenue_amount - cost_of_goods_sold", "gross_margin_percent": "(gross_profit / revenue_amount) * 100"}, "timescaledb_features": {"compression": "After 90 days", "retention": "7 years (regulatory compliance)", "continuous_aggregates": ["daily_revenue", "monthly_revenue", "quarterly_revenue"]}},
}

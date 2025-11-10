"""
Order Line Object Model

Represents individual line items within an order.
Essential for calculating order completeness and COGS in SCOR metrics.

Each order line represents a specific product/SKU with quantity and pricing.
Order lines are used to determine if an order is complete (all items delivered
in correct quantities) for Perfect Order Fulfillment calculations.

Key SCOR Metrics Enabled:
- RL.1.1: Perfect Order Fulfillment (completeness check)
- CO.1.2: Cost of Goods Sold (line-level COGS)
"""

ORDER_LINE = {
    "code": "ORDER_LINE",
    "name": "Order Line",
    "description": "Individual line items within customer orders",
    "table_schema": {"table_name": "order_lines", "class_name": "OrderLine", "columns": [{"name": "order_line_id", "type": "Integer", "primary_key": True, "autoincrement": True, "description": "Unique order line identifier"}, {"name": "order_id", "type": "Integer", "foreign_key": "orders.order_id", "nullable": False, "index": True, "description": "Reference to parent order"}, {"name": "line_number", "type": "Integer", "nullable": False, "description": "Line number within order (1, 2, 3...)"}, {"name": "product_id", "type": "Integer", "foreign_key": "products.product_id", "nullable": False, "index": True, "description": "Reference to product"}, {"name": "sku", "type": "String", "length": 100, "index": True, "description": "Product SKU/part number"}, {"name": "product_name", "type": "String", "length": 200, "description": "Product name (denormalized for reporting)"}, {"name": "quantity_ordered", "type": "Integer", "nullable": False, "description": "Quantity ordered"}, {"name": "quantity_shipped", "type": "Integer", "default": 0, "description": "Quantity shipped"}, {"name": "quantity_delivered", "type": "Integer", "default": 0, "description": "Quantity delivered"}, {"name": "quantity_returned", "type": "Integer", "default": 0, "description": "Quantity returned"}, {"name": "quantity_cancelled", "type": "Integer", "default": 0, "description": "Quantity cancelled"}, {"name": "unit_price", "type": "Float", "nullable": False, "description": "Unit price"}, {"name": "unit_cost", "type": "Float", "description": "Unit cost (COGS)"}, {"name": "discount_percent", "type": "Float", "default": 0, "description": "Discount percentage"}, {"name": "discount_amount", "type": "Float", "default": 0, "description": "Discount amount"}, {"name": "tax_amount", "type": "Float", "default": 0, "description": "Tax amount"}, {"name": "line_total", "type": "Float", "description": "Line total (quantity * unit_price - discount + tax)"}, {"name": "line_cost", "type": "Float", "description": "Line cost (quantity * unit_cost)"}, {"name": "line_margin", "type": "Float", "description": "Line margin (line_total - line_cost)"}, {"name": "line_margin_percent", "type": "Float", "description": "Line margin percentage"}, {"name": "is_complete", "type": "Boolean", "default": False, "description": "Quantity delivered = quantity ordered"}, {"name": "is_backordered", "type": "Boolean", "default": False, "description": "Item is on backorder"}, {"name": "is_damaged", "type": "Boolean", "default": False, "description": "Item was damaged"}, {"name": "line_status", "type": "String", "length": 50, "description": "Line status (pending, confirmed, picked, packed, shipped, delivered)"}, {"name": "warehouse_id", "type": "Integer", "description": "Fulfillment warehouse"}, {"name": "warehouse_location", "type": "String", "length": 100, "description": "Warehouse bin/location"}, {"name": "shipment_id", "type": "Integer", "foreign_key": "shipments.shipment_id", "index": True, "description": "Reference to shipment"}, {"name": "notes", "type": "Text", "description": "Line item notes"}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_order_lines_order_id", "columns": ["order_id"]}, {"name": "ix_order_lines_product_id", "columns": ["product_id"]}, {"name": "ix_order_lines_sku", "columns": ["sku"]}, {"name": "ix_order_lines_shipment_id", "columns": ["shipment_id"]}, {"name": "ix_order_lines_composite", "columns": ["order_id", "line_number"], "unique": True, "description": "Unique line number per order"}], "constraints": [{"type": "check", "name": "chk_quantities_positive", "expression": "quantity_ordered > 0 AND quantity_shipped >= 0 AND quantity_delivered >= 0"}, {"type": "check", "name": "chk_prices_positive", "expression": "unit_price >= 0 AND unit_cost >= 0"}]},
    "schema_definition": """
    @startuml
    OrderLine "*" -- "1" Order : belongs_to
    OrderLine "*" -- "1" Product : references
    OrderLine "*" -- "0..1" Shipment : shipped_via
    
    note right of OrderLine
        Line-level detail for orders
        Enables completeness checks
        for Perfect Order calculation
    end note
    @enduml
    """,
    "metadata_": {"modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "ORDER_MANAGEMENT"], "related_kpis": ["PERFECT_ORDER_FULFILLMENT", "COST_OF_GOODS_SOLD"], "key_attributes": ["order_line_id", "order_id", "product_id", "quantity_ordered", "quantity_delivered", "is_complete", "unit_cost", "line_cost"], "line_statuses": ["pending", "confirmed", "allocated", "picked", "packed", "shipped", "delivered", "cancelled", "returned"], "completeness_logic": {"is_complete": "quantity_delivered == quantity_ordered", "order_complete": "ALL order lines must be complete"}, "scor_metrics": {"RL.1.1": {"name": "Perfect Order Fulfillment", "usage": "Check all lines complete (quantity_delivered = quantity_ordered)"}, "CO.1.2": {"name": "Cost of Goods Sold", "calculation": "SUM(quantity_delivered * unit_cost)"}}},
}

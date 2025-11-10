"""
Receipt Object Model

Represents receipts of materials/goods from suppliers.
Critical for Cash-to-Cash cycle time calculation (Days Payable Outstanding).

Receipts track when goods are received from suppliers, starting the
Days Payable Outstanding (DPO) component of the Cash-to-Cash cycle.

Key SCOR Metrics Enabled:
- AM.1.1: Cash-to-Cash Cycle Time (DPO component)
"""

RECEIPT = {
    "code": "RECEIPT",
    "name": "Receipt",
    "description": "Receipts of materials and goods from suppliers",
    "table_schema": {"table_name": "receipts", "class_name": "Receipt", "columns": [{"name": "receipt_id", "type": "Integer", "primary_key": True, "autoincrement": True, "description": "Unique receipt identifier"}, {"name": "receipt_number", "type": "String", "length": 50, "unique": True, "nullable": False, "index": True, "description": "Business receipt number"}, {"name": "purchase_order_id", "type": "Integer", "index": True, "description": "Reference to purchase order"}, {"name": "supplier_id", "type": "Integer", "foreign_key": "suppliers.supplier_id", "nullable": False, "index": True, "description": "Reference to supplier"}, {"name": "receipt_date", "type": "DateTime", "nullable": False, "index": True, "description": "Date goods were received"}, {"name": "expected_date", "type": "DateTime", "description": "Expected receipt date"}, {"name": "is_on_time", "type": "Boolean", "description": "Received by expected date"}, {"name": "days_early_late", "type": "Integer", "description": "Days early (negative) or late (positive)"}, {"name": "warehouse_id", "type": "Integer", "index": True, "description": "Receiving warehouse"}, {"name": "received_by", "type": "String", "length": 100, "description": "Person who received goods"}, {"name": "receipt_status", "type": "String", "length": 50, "nullable": False, "index": True, "description": "Receipt status (pending, received, inspected, accepted, rejected)"}, {"name": "inspection_status", "type": "String", "length": 50, "description": "Quality inspection status"}, {"name": "inspection_date", "type": "DateTime", "description": "Date of quality inspection"}, {"name": "is_quality_approved", "type": "Boolean", "description": "Passed quality inspection"}, {"name": "defect_count", "type": "Integer", "default": 0, "description": "Number of defective items"}, {"name": "defect_rate_percent", "type": "Float", "description": "Defect rate percentage"}, {"name": "packing_slip_number", "type": "String", "length": 100, "description": "Supplier packing slip number"}, {"name": "carrier", "type": "String", "length": 100, "description": "Shipping carrier"}, {"name": "tracking_number", "type": "String", "length": 100, "description": "Shipment tracking number"}, {"name": "notes", "type": "Text", "description": "Receipt notes"}, {"name": "created_at", "type": "DateTime", "default": "now()", "nullable": False}, {"name": "updated_at", "type": "DateTime", "default": "now()", "onupdate": "now()", "nullable": False}], "indexes": [{"name": "ix_receipts_receipt_number", "columns": ["receipt_number"], "unique": True}, {"name": "ix_receipts_supplier_id", "columns": ["supplier_id"]}, {"name": "ix_receipts_receipt_date", "columns": ["receipt_date"]}, {"name": "ix_receipts_status", "columns": ["receipt_status"]}], "constraints": [{"type": "check", "name": "chk_defect_count_non_negative", "expression": "defect_count >= 0"}]},
    "schema_definition": """
    @startuml
    Receipt "*" -- "1" Supplier : received_from
    Receipt "*" -- "0..1" PurchaseOrder : fulfills
    Receipt "1" -- "0..*" ReceiptLine : contains
    
    note right of Receipt
        Tracks goods received
        Starts DPO calculation
        for Cash-to-Cash cycle
    end note
    @enduml
    """,
    "metadata_": {"modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "PROCUREMENT"], "related_kpis": ["CASH_TO_CASH_CYCLE_TIME"], "key_attributes": ["receipt_id", "receipt_number", "supplier_id", "receipt_date", "is_on_time", "is_quality_approved"], "receipt_statuses": ["pending", "in_transit", "received", "inspecting", "accepted", "rejected", "returned"], "scor_metrics": {"AM.1.1": {"name": "Cash-to-Cash Cycle Time", "usage": "Receipt date starts DPO calculation (receipt_date to payment_date)"}}},
}

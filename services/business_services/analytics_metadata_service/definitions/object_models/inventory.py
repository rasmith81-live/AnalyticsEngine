"""
Inventory Object Model

Represents inventory levels and movements across warehouses and locations.
Essential for Cash-to-Cash cycle time and working capital calculations.

Inventory tracks on-hand quantities, in-transit stock, and inventory movements.
Used to calculate Days Inventory Outstanding (DIO) for SCOR asset management metrics.

Key SCOR Metrics Enabled:
- AM.1.1: Cash-to-Cash Cycle Time (Days Inventory Outstanding)
- AM.1.2: Return on Working Capital (inventory value)
"""

from analytics_models import ObjectModel

INVENTORY = ObjectModel(
    name="Inventory",
    code="INVENTORY",
    description="Inventory levels and movements across warehouses",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "inventory",
        "class_name": "Inventory",
        "is_hypertable": True,
        "time_column": "snapshot_date",
        "partition_interval": "1 day",
        "columns": [
            {
                "name": "inventory_id",
                "type": "Integer",
                "primary_key": True,
                "autoincrement": True,
                "description": "Unique inventory record identifier"
            },
            {
                "name": "snapshot_date",
                "type": "DateTime",
                "nullable": False,
                "index": True,
                "description": "Date of inventory snapshot"
            },
            {
                "name": "product_id",
                "type": "Integer",
                "foreign_key": "products.product_id",
                "nullable": False,
                "index": True,
                "description": "Reference to product"
            },
            {
                "name": "sku",
                "type": "String",
                "length": 100,
                "index": True,
                "description": "Product SKU"
            },
            {
                "name": "warehouse_id",
                "type": "Integer",
                "nullable": False,
                "index": True,
                "description": "Warehouse location"
            },
            {
                "name": "warehouse_location",
                "type": "String",
                "length": 100,
                "description": "Specific bin/location in warehouse"
            },
            {
                "name": "quantity_on_hand",
                "type": "Integer",
                "nullable": False,
                "description": "Physical quantity available"
            },
            {
                "name": "quantity_allocated",
                "type": "Integer",
                "default": 0,
                "description": "Quantity allocated to orders"
            },
            {
                "name": "quantity_available",
                "type": "Integer",
                "description": "Available to promise (on_hand - allocated)"
            },
            {
                "name": "quantity_in_transit",
                "type": "Integer",
                "default": 0,
                "description": "Quantity in transit to warehouse"
            },
            {
                "name": "quantity_on_order",
                "type": "Integer",
                "default": 0,
                "description": "Quantity on purchase order"
            },
            {
                "name": "quantity_reserved",
                "type": "Integer",
                "default": 0,
                "description": "Quantity reserved for specific purposes"
            },
            {
                "name": "quantity_damaged",
                "type": "Integer",
                "default": 0,
                "description": "Damaged/defective quantity"
            },
            {
                "name": "reorder_point",
                "type": "Integer",
                "description": "Reorder point quantity"
            },
            {
                "name": "reorder_quantity",
                "type": "Integer",
                "description": "Standard reorder quantity"
            },
            {
                "name": "safety_stock",
                "type": "Integer",
                "description": "Safety stock level"
            },
            {
                "name": "max_stock_level",
                "type": "Integer",
                "description": "Maximum stock level"
            },
            {
                "name": "unit_cost",
                "type": "Float",
                "description": "Current unit cost"
            },
            {
                "name": "total_value",
                "type": "Float",
                "description": "Total inventory value (quantity * unit_cost)"
            },
            {
                "name": "last_received_date",
                "type": "DateTime",
                "description": "Date of last receipt"
            },
            {
                "name": "last_sold_date",
                "type": "DateTime",
                "description": "Date of last sale"
            },
            {
                "name": "days_on_hand",
                "type": "Float",
                "description": "Days of inventory on hand"
            },
            {
                "name": "inventory_turns_annual",
                "type": "Float",
                "description": "Annual inventory turns"
            },
            {
                "name": "is_below_reorder",
                "type": "Boolean",
                "description": "Quantity below reorder point"
            },
            {
                "name": "is_stockout",
                "type": "Boolean",
                "description": "Out of stock"
            },
            {
                "name": "is_overstock",
                "type": "Boolean",
                "description": "Above maximum stock level"
            },
            {
                "name": "lot_number",
                "type": "String",
                "length": 100,
                "description": "Lot/batch number"
            },
            {
                "name": "serial_numbers",
                "type": "JSON",
                "description": "Serial numbers for serialized items"
            },
            {
                "name": "expiration_date",
                "type": "DateTime",
                "description": "Expiration date (for perishables)"
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
                "name": "ix_inventory_snapshot_date",
                "columns": ["snapshot_date"]
            },
            {
                "name": "ix_inventory_product_id",
                "columns": ["product_id"]
            },
            {
                "name": "ix_inventory_sku",
                "columns": ["sku"]
            },
            {
                "name": "ix_inventory_warehouse_id",
                "columns": ["warehouse_id"]
            },
            {
                "name": "ix_inventory_composite",
                "columns": ["product_id", "warehouse_id", "snapshot_date"],
                "description": "Common query pattern"
            }
        ],
        "constraints": [
            {
                "type": "check",
                "name": "chk_quantities_non_negative",
                "expression": "quantity_on_hand >= 0 AND quantity_allocated >= 0"
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
    Inventory "*" -- "1" Product : tracks
    Inventory "*" -- "1" Warehouse : located_at
    
    note right of Inventory
        TimescaleDB hypertable
        Time-series inventory snapshots
        Enables DIO calculation
        for Cash-to-Cash cycle
    end note
    @enduml
    """,

    metadata_={
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "INVENTORY_MANAGEMENT"],
        "related_kpis": [
            "CASH_TO_CASH_CYCLE_TIME",
            "RETURN_ON_WORKING_CAPITAL"
        ],
        "key_attributes": [
            "inventory_id",
            "snapshot_date",
            "product_id",
            "warehouse_id",
            "quantity_on_hand",
            "quantity_available",
            "total_value",
            "days_on_hand"
        ],
        "scor_metrics": {
            "AM.1.1": {
                "name": "Cash-to-Cash Cycle Time",
                "calculation": "DIO = AVG(Inventory Value) / (COGS / 365)",
                "usage": "Days Inventory Outstanding component"
            },
            "AM.1.2": {
                "name": "Return on Working Capital",
                "calculation": "Inventory is part of working capital denominator"
            }
        },
        "inventory_calculations": {
            "available": "quantity_on_hand - quantity_allocated",
            "total_value": "quantity_on_hand * unit_cost",
            "days_on_hand": "quantity_on_hand / average_daily_usage",
            "turns": "COGS / average_inventory_value"
        },
        "timescaledb_features": {
            "compression": "After 90 days",
            "retention": "2 years hot, then archive to Layer 2a",
            "continuous_aggregates": ["daily_inventory", "weekly_inventory", "monthly_inventory"]
        }
    }
)

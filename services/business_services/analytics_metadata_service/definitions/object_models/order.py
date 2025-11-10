"""
Order Object Model

Represents customer orders in the supply chain.
Core entity for SCOR metrics including Perfect Order Fulfillment and Order Fulfillment Cycle Time.

An order represents a customer's request to purchase products or services.
Orders contain multiple order lines (items) and progress through various statuses
from creation to fulfillment.

Key SCOR Metrics Enabled:
- RL.1.1: Perfect Order Fulfillment
- RS.1.1: Order Fulfillment Cycle Time
- CO.1.2: Cost of Goods Sold
- AM.1.1: Cash-to-Cash Cycle Time
- AM.1.2: Return on Working Capital
"""

from analytics_models import ObjectModel

ORDER = ObjectModel(
    name="Order",
    code="ORDER",
    description="Customer orders for products or services in the supply chain",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "orders",
        "class_name": "Order",
        "columns": [
            {
                "name": "order_id",
                "type": "Integer",
                "primary_key": True,
                "autoincrement": True,
                "description": "Unique order identifier"
            },
            {
                "name": "order_number",
                "type": "String",
                "length": 50,
                "unique": True,
                "nullable": False,
                "index": True,
                "description": "Business order number (e.g., 'ORD-2024-001234')"
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
                "name": "order_date",
                "type": "DateTime",
                "nullable": False,
                "index": True,
                "description": "Date order was placed"
            },
            {
                "name": "requested_delivery_date",
                "type": "DateTime",
                "description": "Customer requested delivery date"
            },
            {
                "name": "promised_delivery_date",
                "type": "DateTime",
                "description": "Company promised delivery date"
            },
            {
                "name": "actual_delivery_date",
                "type": "DateTime",
                "index": True,
                "description": "Actual delivery date (for cycle time calculation)"
            },
            {
                "name": "order_status",
                "type": "String",
                "length": 50,
                "nullable": False,
                "index": True,
                "description": "Order status (pending, confirmed, processing, shipped, delivered, cancelled)"
            },
            {
                "name": "order_type",
                "type": "String",
                "length": 50,
                "description": "Order type (standard, rush, backorder, drop_ship)"
            },
            {
                "name": "priority",
                "type": "String",
                "length": 20,
                "description": "Order priority (low, normal, high, urgent)"
            },
            {
                "name": "channel",
                "type": "String",
                "length": 50,
                "description": "Sales channel (online, retail, wholesale, partner)"
            },
            {
                "name": "order_total",
                "type": "Float",
                "description": "Total order value"
            },
            {
                "name": "currency",
                "type": "String",
                "length": 3,
                "description": "Currency code (USD, EUR, etc.)"
            },
            {
                "name": "payment_status",
                "type": "String",
                "length": 50,
                "description": "Payment status (pending, paid, partial, refunded)"
            },
            {
                "name": "payment_method",
                "type": "String",
                "length": 50,
                "description": "Payment method (credit_card, wire_transfer, etc.)"
            },
            {
                "name": "shipping_address_id",
                "type": "Integer",
                "description": "Reference to shipping address"
            },
            {
                "name": "billing_address_id",
                "type": "Integer",
                "description": "Reference to billing address"
            },
            {
                "name": "is_complete",
                "type": "Boolean",
                "default": False,
                "description": "All items delivered in correct quantities"
            },
            {
                "name": "is_on_time",
                "type": "Boolean",
                "description": "Delivered by requested/promised date"
            },
            {
                "name": "is_damage_free",
                "type": "Boolean",
                "description": "No damaged items reported"
            },
            {
                "name": "has_correct_documentation",
                "type": "Boolean",
                "description": "All required documentation provided"
            },
            {
                "name": "is_perfect_order",
                "type": "Boolean",
                "description": "Meets all perfect order criteria (SCOR RL.1.1)"
            },
            {
                "name": "fulfillment_cycle_time_days",
                "type": "Float",
                "description": "Days from order to delivery (SCOR RS.1.1)"
            },
            {
                "name": "sales_rep_id",
                "type": "Integer",
                "description": "Reference to sales representative"
            },
            {
                "name": "region",
                "type": "String",
                "length": 100,
                "description": "Geographic region"
            },
            {
                "name": "facility_id",
                "type": "Integer",
                "description": "Fulfillment facility/warehouse"
            },
            {
                "name": "notes",
                "type": "Text",
                "description": "Order notes and comments"
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
                "description": "User who created the order"
            },
            {
                "name": "updated_by",
                "type": "String",
                "length": 100,
                "description": "User who last updated the order"
            }
        ],
        "indexes": [
            {
                "name": "ix_orders_order_number",
                "columns": ["order_number"],
                "unique": True
            },
            {
                "name": "ix_orders_customer_id",
                "columns": ["customer_id"]
            },
            {
                "name": "ix_orders_order_date",
                "columns": ["order_date"]
            },
            {
                "name": "ix_orders_order_status",
                "columns": ["order_status"]
            },
            {
                "name": "ix_orders_actual_delivery_date",
                "columns": ["actual_delivery_date"]
            },
            {
                "name": "ix_orders_is_perfect_order",
                "columns": ["is_perfect_order"]
            },
            {
                "name": "ix_orders_composite",
                "columns": ["customer_id", "order_date", "order_status"],
                "description": "Composite index for common queries"
            }
        ],
        "constraints": [
            {
                "type": "check",
                "name": "chk_order_total_positive",
                "expression": "order_total >= 0"
            },
            {
                "type": "check",
                "name": "chk_cycle_time_positive",
                "expression": "fulfillment_cycle_time_days IS NULL OR fulfillment_cycle_time_days >= 0"
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
    Order "1" -- "0..*" OrderLine : contains
    Order "*" -- "1" Customer : placed_by
    Order "1" -- "0..*" Shipment : fulfilled_by
    Order "1" -- "0..1" Delivery : delivered_via
    Order "*" -- "0..1" Invoice : billed_via
    Order "*" -- "0..*" Payment : paid_via
    
    note right of Order
        Core supply chain entity
        Enables SCOR metrics:
        - RL.1.1 (Perfect Order)
        - RS.1.1 (Cycle Time)
        - AM.1.1 (Cash-to-Cash)
    end note
    @enduml
    """,

    metadata_={
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "ORDER_MANAGEMENT"],
        "related_kpis": [
            "PERFECT_ORDER_FULFILLMENT",
            "ORDER_FULFILLMENT_CYCLE_TIME",
            "COST_OF_GOODS_SOLD",
            "CASH_TO_CASH_CYCLE_TIME",
            "RETURN_ON_WORKING_CAPITAL"
        ],
        "key_attributes": [
            "order_id",
            "order_number",
            "customer_id",
            "order_date",
            "order_status",
            "order_total",
            "is_perfect_order",
            "fulfillment_cycle_time_days"
        ],
        "order_statuses": [
            "pending",
            "confirmed",
            "processing",
            "picking",
            "packing",
            "shipped",
            "in_transit",
            "delivered",
            "cancelled",
            "returned"
        ],
        "order_types": [
            "standard",
            "rush",
            "backorder",
            "drop_ship",
            "pre_order"
        ],
        "priority_levels": [
            "low",
            "normal",
            "high",
            "urgent"
        ],
        "perfect_order_criteria": {
            "on_time": "Delivered by requested/promised date",
            "complete": "All items delivered in correct quantities",
            "damage_free": "No damaged items",
            "correct_documentation": "Invoice, packing slip, etc. correct"
        },
        "scor_metrics": {
            "RL.1.1": {
                "name": "Perfect Order Fulfillment",
                "calculation": "is_perfect_order = is_on_time AND is_complete AND is_damage_free AND has_correct_documentation"
            },
            "RS.1.1": {
                "name": "Order Fulfillment Cycle Time",
                "calculation": "fulfillment_cycle_time_days = actual_delivery_date - order_date"
            }
        },
        "data_quality_rules": {
            "required_fields": ["order_number", "customer_id", "order_date", "order_status"],
            "validation": {
                "order_total": "Must be >= 0",
                "cycle_time": "Must be >= 0 if calculated",
                "dates": "actual_delivery_date >= order_date"
            }
        }
    }
)

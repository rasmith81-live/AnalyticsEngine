"""
Delivery Object Model

Represents the final delivery event of a shipment to the customer.
Tracks delivery confirmation, condition, and documentation for Perfect Order calculation.

A delivery is the final step in the order fulfillment process, recording
when and how the shipment was received by the customer. This includes
verification of condition, completeness, and documentation.

Key SCOR Metrics Enabled:
- RL.1.1: Perfect Order Fulfillment (delivery confirmation)
- RS.1.1: Order Fulfillment Cycle Time (final timestamp)
"""

from analytics_models import ObjectModel

DELIVERY = ObjectModel(
    name="Delivery",
    code="DELIVERY",
    description="Final delivery events and confirmation for shipments",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "deliveries",
        "class_name": "Delivery",
        "columns": [
            {
                "name": "delivery_id",
                "type": "Integer",
                "primary_key": True,
                "autoincrement": True,
                "description": "Unique delivery identifier"
            },
            {
                "name": "shipment_id",
                "type": "Integer",
                "foreign_key": "shipments.shipment_id",
                "nullable": False,
                "unique": True,
                "index": True,
                "description": "Reference to shipment (1:1)"
            },
            {
                "name": "order_id",
                "type": "Integer",
                "foreign_key": "orders.order_id",
                "nullable": False,
                "index": True,
                "description": "Reference to order"
            },
            {
                "name": "delivery_date",
                "type": "DateTime",
                "nullable": False,
                "index": True,
                "description": "Date and time of delivery"
            },
            {
                "name": "delivery_status",
                "type": "String",
                "length": 50,
                "nullable": False,
                "description": "Delivery status (delivered, attempted, refused, returned)"
            },
            {
                "name": "delivery_method",
                "type": "String",
                "length": 50,
                "description": "Delivery method (front_door, mailbox, reception, etc.)"
            },
            {
                "name": "received_by",
                "type": "String",
                "length": 100,
                "description": "Name of person who received"
            },
            {
                "name": "signature_obtained",
                "type": "Boolean",
                "description": "Signature was obtained"
            },
            {
                "name": "signature_image_url",
                "type": "String",
                "length": 500,
                "description": "URL to signature image"
            },
            {
                "name": "photo_proof_url",
                "type": "String",
                "length": 500,
                "description": "URL to delivery photo"
            },
            {
                "name": "is_damage_free",
                "type": "Boolean",
                "default": True,
                "description": "No damage reported"
            },
            {
                "name": "damage_description",
                "type": "Text",
                "description": "Description of any damage"
            },
            {
                "name": "damage_photos",
                "type": "JSON",
                "description": "URLs to damage photos"
            },
            {
                "name": "is_complete",
                "type": "Boolean",
                "default": True,
                "description": "All items received"
            },
            {
                "name": "missing_items",
                "type": "Text",
                "description": "Description of missing items"
            },
            {
                "name": "has_correct_documentation",
                "type": "Boolean",
                "default": True,
                "description": "Invoice, packing slip correct"
            },
            {
                "name": "documentation_issues",
                "type": "Text",
                "description": "Description of documentation issues"
            },
            {
                "name": "customer_satisfaction",
                "type": "Integer",
                "description": "Customer satisfaction rating (1-5)"
            },
            {
                "name": "delivery_notes",
                "type": "Text",
                "description": "Delivery notes from carrier"
            },
            {
                "name": "customer_notes",
                "type": "Text",
                "description": "Notes from customer"
            },
            {
                "name": "delivery_attempts",
                "type": "Integer",
                "default": 1,
                "description": "Number of delivery attempts"
            },
            {
                "name": "first_attempt_date",
                "type": "DateTime",
                "description": "Date of first delivery attempt"
            },
            {
                "name": "was_refused",
                "type": "Boolean",
                "default": False,
                "description": "Delivery was refused"
            },
            {
                "name": "refusal_reason",
                "type": "String",
                "length": 200,
                "description": "Reason for refusal"
            },
            {
                "name": "requires_return",
                "type": "Boolean",
                "default": False,
                "description": "Requires return to sender"
            },
            {
                "name": "return_initiated_date",
                "type": "DateTime",
                "description": "Date return was initiated"
            },
            {
                "name": "delivery_location",
                "type": "String",
                "length": 200,
                "description": "Specific delivery location (front porch, mailbox, etc.)"
            },
            {
                "name": "weather_conditions",
                "type": "String",
                "length": 100,
                "description": "Weather at time of delivery"
            },
            {
                "name": "temperature",
                "type": "Float",
                "description": "Temperature at delivery (for sensitive items)"
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
                "name": "ix_deliveries_shipment_id",
                "columns": ["shipment_id"],
                "unique": True
            },
            {
                "name": "ix_deliveries_order_id",
                "columns": ["order_id"]
            },
            {
                "name": "ix_deliveries_delivery_date",
                "columns": ["delivery_date"]
            },
            {
                "name": "ix_deliveries_status",
                "columns": ["delivery_status"]
            }
        ],
        "constraints": [
            {
                "type": "check",
                "name": "chk_satisfaction_range",
                "expression": "customer_satisfaction IS NULL OR (customer_satisfaction >= 1 AND customer_satisfaction <= 5)"
            },
            {
                "type": "check",
                "name": "chk_attempts_positive",
                "expression": "delivery_attempts > 0"
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
    Delivery "1" -- "1" Shipment : confirms
    Delivery "*" -- "1" Order : completes
    
    note right of Delivery
        Final delivery confirmation
        Tracks condition and completeness
        for Perfect Order calculation
    end note
    @enduml
    """,

    metadata_={
        "modules": ["ASCM_SCOR", "SUPPLY_CHAIN", "LOGISTICS"],
        "related_kpis": [
            "PERFECT_ORDER_FULFILLMENT",
            "ORDER_FULFILLMENT_CYCLE_TIME"
        ],
        "key_attributes": [
            "delivery_id",
            "shipment_id",
            "order_id",
            "delivery_date",
            "is_damage_free",
            "is_complete",
            "has_correct_documentation"
        ],
        "delivery_statuses": [
            "delivered",
            "attempted",
            "refused",
            "returned_to_sender",
            "held_at_facility",
            "exception"
        ],
        "delivery_methods": [
            "front_door",
            "back_door",
            "side_door",
            "mailbox",
            "reception",
            "security_desk",
            "neighbor",
            "safe_location"
        ],
        "scor_metrics": {
            "RL.1.1": {
                "name": "Perfect Order Fulfillment",
                "perfect_delivery_criteria": {
                    "is_damage_free": True,
                    "is_complete": True,
                    "has_correct_documentation": True,
                    "delivery_status": "delivered"
                }
            },
            "RS.1.1": {
                "name": "Order Fulfillment Cycle Time",
                "usage": "delivery_date is final timestamp for cycle time calculation"
            }
        },
        "quality_checks": {
            "damage_free": "Visual inspection, no damage reported",
            "complete": "All items on packing slip received",
            "documentation": "Invoice matches order, packing slip correct"
        }
    }
)

"""
Shipment Object Model

Represents shipments of orders from warehouse to customer.
Critical for tracking delivery performance and cycle time in SCOR metrics.

A shipment contains one or more order lines being sent to a customer.
Shipments track carrier information, tracking numbers, and shipping dates
used to calculate on-time delivery and fulfillment cycle time.

Key SCOR Metrics Enabled:
- RL.1.1: Perfect Order Fulfillment (on-time delivery)
- RS.1.1: Order Fulfillment Cycle Time
"""

from analytics_models import ObjectModel

SHIPMENT = ObjectModel(
    name="Shipment",
    code="SHIPMENT",
    description="Shipments of orders from warehouse to customer",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "shipments",
        "class_name": "Shipment",
        "columns": [
            {
                "name": "shipment_id",
                "type": "Integer",
                "primary_key": True,
                "autoincrement": True,
                "description": "Unique shipment identifier"
            },
            {
                "name": "shipment_number",
                "type": "String",
                "length": 50,
                "unique": True,
                "nullable": False,
                "index": True,
                "description": "Business shipment number"
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
                "name": "shipment_date",
                "type": "DateTime",
                "nullable": False,
                "index": True,
                "description": "Date shipment was sent"
            },
            {
                "name": "estimated_delivery_date",
                "type": "DateTime",
                "description": "Estimated delivery date"
            },
            {
                "name": "actual_delivery_date",
                "type": "DateTime",
                "index": True,
                "description": "Actual delivery date"
            },
            {
                "name": "carrier",
                "type": "String",
                "length": 100,
                "index": True,
                "description": "Shipping carrier (FedEx, UPS, USPS, etc.)"
            },
            {
                "name": "carrier_service",
                "type": "String",
                "length": 100,
                "description": "Carrier service level (Ground, Express, Overnight)"
            },
            {
                "name": "tracking_number",
                "type": "String",
                "length": 100,
                "unique": True,
                "index": True,
                "description": "Carrier tracking number"
            },
            {
                "name": "shipment_status",
                "type": "String",
                "length": 50,
                "nullable": False,
                "index": True,
                "description": "Shipment status (pending, picked_up, in_transit, delivered, exception)"
            },
            {
                "name": "shipping_method",
                "type": "String",
                "length": 50,
                "description": "Shipping method (standard, expedited, overnight)"
            },
            {
                "name": "warehouse_id",
                "type": "Integer",
                "index": True,
                "description": "Origin warehouse"
            },
            {
                "name": "warehouse_location",
                "type": "String",
                "length": 200,
                "description": "Warehouse address"
            },
            {
                "name": "destination_address",
                "type": "Text",
                "description": "Delivery address"
            },
            {
                "name": "destination_city",
                "type": "String",
                "length": 100,
                "description": "Destination city"
            },
            {
                "name": "destination_state",
                "type": "String",
                "length": 50,
                "description": "Destination state/province"
            },
            {
                "name": "destination_country",
                "type": "String",
                "length": 50,
                "description": "Destination country"
            },
            {
                "name": "destination_postal_code",
                "type": "String",
                "length": 20,
                "description": "Destination postal code"
            },
            {
                "name": "weight",
                "type": "Float",
                "description": "Shipment weight"
            },
            {
                "name": "weight_unit",
                "type": "String",
                "length": 10,
                "description": "Weight unit (lbs, kg)"
            },
            {
                "name": "dimensions",
                "type": "String",
                "length": 100,
                "description": "Package dimensions (LxWxH)"
            },
            {
                "name": "number_of_packages",
                "type": "Integer",
                "default": 1,
                "description": "Number of packages in shipment"
            },
            {
                "name": "shipping_cost",
                "type": "Float",
                "description": "Shipping cost"
            },
            {
                "name": "insurance_cost",
                "type": "Float",
                "description": "Insurance cost"
            },
            {
                "name": "is_on_time",
                "type": "Boolean",
                "description": "Delivered by estimated date"
            },
            {
                "name": "is_damaged",
                "type": "Boolean",
                "default": False,
                "description": "Shipment was damaged"
            },
            {
                "name": "has_exception",
                "type": "Boolean",
                "default": False,
                "description": "Shipment had delivery exception"
            },
            {
                "name": "exception_reason",
                "type": "String",
                "length": 200,
                "description": "Reason for exception"
            },
            {
                "name": "transit_time_days",
                "type": "Float",
                "description": "Days in transit (delivery - shipment)"
            },
            {
                "name": "signature_required",
                "type": "Boolean",
                "default": False,
                "description": "Signature required for delivery"
            },
            {
                "name": "signature_obtained",
                "type": "Boolean",
                "description": "Signature was obtained"
            },
            {
                "name": "signed_by",
                "type": "String",
                "length": 100,
                "description": "Name of person who signed"
            },
            {
                "name": "notes",
                "type": "Text",
                "description": "Shipment notes"
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
                "description": "User who created shipment"
            }
        ],
        "indexes": [
            {
                "name": "ix_shipments_shipment_number",
                "columns": ["shipment_number"],
                "unique": True
            },
            {
                "name": "ix_shipments_order_id",
                "columns": ["order_id"]
            },
            {
                "name": "ix_shipments_tracking_number",
                "columns": ["tracking_number"]
            },
            {
                "name": "ix_shipments_shipment_date",
                "columns": ["shipment_date"]
            },
            {
                "name": "ix_shipments_actual_delivery_date",
                "columns": ["actual_delivery_date"]
            },
            {
                "name": "ix_shipments_carrier",
                "columns": ["carrier"]
            },
            {
                "name": "ix_shipments_status",
                "columns": ["shipment_status"]
            },
            {
                "name": "ix_shipments_composite",
                "columns": ["order_id", "shipment_date"],
                "description": "Common query pattern"
            }
        ],
        "constraints": [
            {
                "type": "check",
                "name": "chk_dates_logical",
                "expression": "actual_delivery_date IS NULL OR actual_delivery_date >= shipment_date"
            },
            {
                "type": "check",
                "name": "chk_transit_time_positive",
                "expression": "transit_time_days IS NULL OR transit_time_days >= 0"
            },
            {
                "type": "check",
                "name": "chk_packages_positive",
                "expression": "number_of_packages > 0"
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
    Shipment "*" -- "1" Order : fulfills
    Shipment "1" -- "0..*" OrderLine : contains
    Shipment "1" -- "0..1" Delivery : results_in
    
    note right of Shipment
        Tracks carrier and transit
        Enables on-time delivery
        and cycle time metrics
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
            "shipment_id",
            "shipment_number",
            "order_id",
            "shipment_date",
            "actual_delivery_date",
            "carrier",
            "tracking_number",
            "is_on_time",
            "transit_time_days"
        ],
        "shipment_statuses": [
            "pending",
            "ready_to_ship",
            "picked_up",
            "in_transit",
            "out_for_delivery",
            "delivered",
            "exception",
            "returned",
            "cancelled"
        ],
        "carriers": [
            "FedEx",
            "UPS",
            "USPS",
            "DHL",
            "Amazon Logistics",
            "Regional Carrier",
            "Freight"
        ],
        "scor_metrics": {
            "RL.1.1": {
                "name": "Perfect Order Fulfillment",
                "usage": "is_on_time AND NOT is_damaged for perfect order"
            },
            "RS.1.1": {
                "name": "Order Fulfillment Cycle Time",
                "calculation": "transit_time_days = actual_delivery_date - shipment_date"
            }
        },
        "on_time_logic": {
            "calculation": "is_on_time = (actual_delivery_date <= estimated_delivery_date)",
            "factors": ["carrier_performance", "weather", "address_accuracy", "customs"]
        }
    }
)

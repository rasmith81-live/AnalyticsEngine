"""
Customer Support Ticket Resolution Time KPI Definition
"""

CUSTOMER_SUPPORT_TICKET_RESOLUTION_TIME = {
    "code": "CUSTOMER_SUPPORT_TICKET_RESOLUTION_TIME",
    "name": "Customer Support Ticket Resolution Time",
    "display_name": "Customer Support Ticket Resolution Time",
    "description": "The average time it takes for the sales or support team to resolve customer issues or support tickets.",
    "formula": "Total Time Taken to Resolve Tickets / Number of Tickets Resolved",
    "unit": "count",
    "category": "Business Development",
    "aggregation_methods": ["average", "sum", "count"],
    "time_periods": ["custom"],
    "metadata_": {
        "modules": ["BUSINESS_DEVELOPMENT"],
        "required_objects": ["Customer", "PurchaseOrder", "SupportTicket"]
    },
    "modules": ["BUSINESS_DEVELOPMENT"],
    "module_code": "BUSINESS_DEVELOPMENT",
}

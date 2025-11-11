"""
Container Security Device Utilization Rate KPI Definition
"""

CONTAINER_SECURITY_DEVICE_UTILIZATION_RATE = {
    "code": "CONTAINER_SECURITY_DEVICE_UTILIZATION_RATE",
    "name": "Container Security Device Utilization Rate",
    "display_name": "Container Security Device Utilization Rate",
    "description": "The percentage of containers equipped with security devices, indicating the level of technology adoption to enhance shipment security.",
    "formula": "",
    "unit": "count",
    "category": "Iso 28000",
    "metadata_": {
        "modules": ["ISO_28000"],
        "required_objects": ["Shipment"]
    },
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
}

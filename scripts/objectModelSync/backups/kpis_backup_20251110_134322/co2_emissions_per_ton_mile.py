"""
CO2 Emissions per Ton-Mile KPI Definition
"""

CO2_EMISSIONS_PER_TON_MILE = {
    "code": "CO2_EMISSIONS_PER_TON_MILE",
    "name": "CO2 Emissions per Ton-Mile",
    "display_name": "CO2 Emissions per Ton-Mile",
    "description": "The amount of CO2 emitted for transporting one ton of material over one mile.",
    "formula": "",
    "unit": "count",
    "category": "Logistics",
    "metadata_": {
        "modules": ["LOGISTICS"],
        "required_objects": ["PurchaseOrder", "Shipment"]
    },
    "modules": ["LOGISTICS"],
    "module_code": "LOGISTICS",
}

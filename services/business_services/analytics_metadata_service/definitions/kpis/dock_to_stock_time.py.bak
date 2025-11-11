import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class DockToStockTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="DOCK_TO_STOCK_TIME",
            name_="Dock to Stock Time",
            description_="The time it takes for goods to move from the receiving dock to available inventory.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Inventory', 'Shipment'],
            formula_="Total Dock to Stock Time / Total Number of Shipments",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

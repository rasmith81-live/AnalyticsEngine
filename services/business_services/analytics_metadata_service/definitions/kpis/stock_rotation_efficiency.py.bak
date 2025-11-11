import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class StockRotationEfficiency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="STOCK_ROTATION_EFFICIENCY",
            name_="Stock Rotation Efficiency",
            description_="The effectiveness of inventory management practices in rotating stock before it becomes outdated or expires.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Inventory'],
            formula_="(Total Older Inventory Sold / Total Inventory Available) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

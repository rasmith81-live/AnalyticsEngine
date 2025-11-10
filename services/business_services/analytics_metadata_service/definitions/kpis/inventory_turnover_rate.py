import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class InventoryTurnoverRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="INVENTORY_TURNOVER_RATE",
            name_="Inventory Turnover Rate",
            description_="How many times inventory is sold and replaced within a given period. It helps determine if inventory levels are too high or too low, and if adjustments are needed to optimize inventory management.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Inventory'],
            formula_="Cost of Goods Sold / Average Inventory Value",
            aggregation_methods=['average', 'min'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

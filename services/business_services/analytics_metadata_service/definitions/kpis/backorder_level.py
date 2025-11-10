import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class BackorderLevel(BaseKPI):
    def __init__(self):
        super().__init__(
            code="BACKORDER_LEVEL",
            name_="Backorder Level",
            description_="The amount of orders that cannot be filled from current inventory.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Inventory', 'Order', 'Product'],
            formula_="Total Number of Backordered Items",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

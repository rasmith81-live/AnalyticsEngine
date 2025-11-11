import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class OrderValueAov(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ORDER_VALUE_AOV",
            name_="Average Order Value (AOV)",
            description_="The average value of orders shipped from the warehouse.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Order', 'Warehouse'],
            formula_="Total Revenue / Total Number of Orders",
            aggregation_methods=['average', 'sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

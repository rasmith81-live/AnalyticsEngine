import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class WarehouseLaborEfficiency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="WAREHOUSE_LABOR_EFFICIENCY",
            name_="Warehouse Labor Efficiency",
            description_="The overall efficiency of warehouse staff based on output over input.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Employee', 'Order', 'Warehouse'],
            formula_="Total Number of Orders Fulfilled / Total Labor Hours",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

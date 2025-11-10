import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class WarehouseOperatingCosts(BaseKPI):
    def __init__(self):
        super().__init__(
            code="WAREHOUSE_OPERATING_COSTS",
            name_="Warehouse Operating Costs",
            description_="The total operating costs of running a warehouse.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Warehouse'],
            formula_="Sum of all Warehouse Operating Costs",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

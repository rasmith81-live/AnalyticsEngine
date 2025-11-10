import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class InventoryCarryingCost(BaseKPI):
    def __init__(self):
        super().__init__(
            code="INVENTORY_CARRYING_COST",
            name_="Inventory Carrying Cost",
            description_="The total cost of holding inventory including storage, insurance, and taxes.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Inventory'],
            formula_="Sum of All Inventory-Related Costs / Total Value of Inventory",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

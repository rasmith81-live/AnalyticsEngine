import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class InventoryCarryingCostPercentage(BaseKPI):
    def __init__(self):
        super().__init__(
            code="INVENTORY_CARRYING_COST_PERCENTAGE",
            name_="Inventory Carrying Cost Percentage",
            description_="The percentage of total inventory value that represents the cost of holding inventory, including storage, insurance, and obsolescence.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['Inventory'],
            formula_="(Total Inventory Carrying Costs / Total Inventory Value) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

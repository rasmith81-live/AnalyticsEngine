import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SupplyChainPlanningCycleTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLY_CHAIN_PLANNING_CYCLE_TIME",
            name_="Supply Chain Planning Cycle Time",
            description_="The time required to create a supply chain plan, with shorter cycles allowing for more agility and responsiveness to changes.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['PurchaseOrder'],
            formula_="Total Planning Cycle Time",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

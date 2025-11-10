from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CostOfCarry(BaseKPI):
    def __init__(self):
        super().__init__(
            code="COST_OF_CARRY",
            name_="Cost of Carry",
            description_="The cost associated with holding inventory, including storage, insurance, and taxes.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Inventory'],
            formula_="Total Carrying Costs / Average Inventory Value",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

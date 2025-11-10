from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CostPerOrderPicked(BaseKPI):
    def __init__(self):
        super().__init__(
            code="COST_PER_ORDER_PICKED",
            name_="Cost per Order Picked",
            description_="The cost associated with picking each order.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Order'],
            formula_="Total Picking Costs / Total Number of Orders Picked",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

from analytics_models.definitions.kpis.base_kpi import BaseKPI

class InventoryTurnoverRatio(BaseKPI):
    def __init__(self):
        super().__init__(
            code="INVENTORY_TURNOVER_RATIO",
            name_="Inventory Turnover Ratio",
            description_="The rate at which inventory is used and replaced over a certain period.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Inventory'],
            formula_="Cost of Goods Sold (COGS) / Average Inventory for the period",
            aggregation_methods=['average'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

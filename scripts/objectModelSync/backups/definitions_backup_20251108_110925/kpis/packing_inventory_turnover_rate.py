from analytics_models.definitions.kpis.base_kpi import BaseKPI

class PackingInventoryTurnoverRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKING_INVENTORY_TURNOVER_RATE",
            name_="Packing Inventory Turnover Rate",
            description_="The rate at which packaging materials are used and replenished, indicating inventory management effectiveness.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=['Inventory'],
            formula_="Total Packing Materials Used / Average Packing Inventory",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

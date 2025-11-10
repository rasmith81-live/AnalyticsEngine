from analytics_models.definitions.kpis.base_kpi import BaseKPI

class StockoutFrequency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="STOCKOUT_FREQUENCY",
            name_="Stockout Frequency",
            description_="The frequency with which inventory items are out of stock.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Inventory', 'Product'],
            formula_="Total Number of Stockouts / Total Number of Inventory Checks",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

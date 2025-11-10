from analytics_models.definitions.kpis.base_kpi import BaseKPI

class BackorderRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="BACKORDER_RATE",
            name_="Backorder Rate",
            description_="The percentage of orders that cannot be filled immediately and are placed on backorder.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Inventory', 'Order', 'Product'],
            formula_="(Number of Backordered Items / Total Inventory Items) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

from analytics_models.definitions.kpis.base_kpi import BaseKPI

class YieldPerMile(BaseKPI):
    def __init__(self):
        super().__init__(
            code="YIELD_PER_MILE",
            name_="Yield per Mile",
            description_="The revenue or profit generated for each mile of transportation.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['PurchaseOrder'],
            formula_="Total Revenue / Total Miles Driven",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

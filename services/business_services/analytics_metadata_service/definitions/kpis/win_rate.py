from analytics_models.definitions.kpis.base_kpi import BaseKPI

class WinRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="WIN_RATE",
            name_="Win Rate",
            description_="The percentage of deals won out of the total number of opportunities.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Deal', 'PurchaseOrder'],
            formula_="(Number of Successful Sales / Total Number of Sales Opportunities) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

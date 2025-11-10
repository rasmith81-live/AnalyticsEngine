from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CostPerOpportunity(BaseKPI):
    def __init__(self):
        super().__init__(
            code="COST_PER_OPPORTUNITY",
            name_="Cost per Opportunity",
            description_="The average cost incurred to turn a lead into a sales opportunity.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Lead', 'Opportunity', 'PurchaseOrder'],
            formula_="Total Cost of Sales and Marketing / Total Number of Opportunities",
            aggregation_methods=['average', 'sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

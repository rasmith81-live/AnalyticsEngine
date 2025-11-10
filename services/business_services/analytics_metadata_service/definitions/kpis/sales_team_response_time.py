from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SalesTeamResponseTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SALES_TEAM_RESPONSE_TIME",
            name_="Sales Team Response Time",
            description_="The average time it takes for a sales representative to follow up on a lead or customer inquiry.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer', 'Lead', 'PurchaseOrder'],
            formula_="Average Time Taken by Sales Team to Respond to Inquiries",
            aggregation_methods=['average'],
            time_periods=['custom']
        )

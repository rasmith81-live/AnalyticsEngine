from analytics_models.definitions.kpis.base_kpi import BaseKPI

class LeadResponseTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="LEAD_RESPONSE_TIME",
            name_="Lead Response Time",
            description_="The time it takes for a sales representative to respond to a new lead.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Lead', 'PurchaseOrder'],
            formula_="Total Time Taken to Respond to Leads / Total Number of Leads",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

from analytics_models.definitions.kpis.base_kpi import BaseKPI

class LeadScore(BaseKPI):
    def __init__(self):
        super().__init__(
            code="LEAD_SCORE",
            name_="Average Lead Score",
            description_="The average score of all leads, calculated to assess the overall quality of leads being pursued by the business development team.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Lead', 'QualityMetric'],
            formula_="Sum of All Lead Scores / Total Number of Leads",
            aggregation_methods=['average', 'sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

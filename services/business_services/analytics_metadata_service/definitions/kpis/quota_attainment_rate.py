from analytics_models.definitions.kpis.base_kpi import BaseKPI

class QuotaAttainmentRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="QUOTA_ATTAINMENT_RATE",
            name_="Quota Attainment Rate",
            description_="The percentage of sales representatives reaching or exceeding their sales quotas.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=[],
            formula_="(Number of Sales Reps Meeting or Exceeding Quota / Total Number of Sales Reps) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

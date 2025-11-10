from analytics_models.definitions.kpis.base_kpi import BaseKPI

class ReferralRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="REFERRAL_RATE",
            name_="Referral Rate",
            description_="The percentage of new business that comes from referrals by existing customers, which can indicate customer satisfaction and advocacy.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer'],
            formula_="(Number of New Customers from Referrals / Total Number of New Customers) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )

from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SocialSellingEffectiveness(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SOCIAL_SELLING_EFFECTIVENESS",
            name_="Social Selling Effectiveness",
            description_="A measure of how effectively the sales team uses social media channels to engage with prospects, build relationships, and close deals.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Deal', 'Lead'],
            formula_="(Number of Leads or Sales Attributed to Social Media Efforts / Total Number of Leads or Sales) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

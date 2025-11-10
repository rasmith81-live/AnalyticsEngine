from analytics_models.definitions.kpis.base_kpi import BaseKPI

class StrategicPartnerDevelopmentIndex(BaseKPI):
    def __init__(self):
        super().__init__(
            code="STRATEGIC_PARTNER_DEVELOPMENT_INDEX",
            name_="Strategic Partner Development Index",
            description_="A measure of the effectiveness of developing strategic partnerships and alliances.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=[],
            formula_="(Sum of Partnership Scores Based on Defined Criteria) / (Total Number of Strategic Partnerships)",
            aggregation_methods=['sum', 'count'],
            time_periods=['quarterly', 'annually']
        )

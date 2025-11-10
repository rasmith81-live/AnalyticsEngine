from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SustainablePackagingUsageRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUSTAINABLE_PACKAGING_USAGE_RATE",
            name_="Sustainable Packaging Usage Rate",
            description_="The percentage of packaging materials that are recyclable, reusable, or biodegradable, in line with ISO 20400.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=[],
            formula_="(Sustainable Packaging Materials Used / Total Packaging Materials Used) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

from analytics_models.definitions.kpis.base_kpi import BaseKPI

class ConversionRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CONVERSION_RATE",
            name_="Conversion Rate",
            description_="The percentage of leads that convert into paying customers.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer', 'Lead'],
            formula_="(Number of New Customers / Number of Leads) * 100",
            aggregation_methods=['count'],
            time_periods=['custom']
        )

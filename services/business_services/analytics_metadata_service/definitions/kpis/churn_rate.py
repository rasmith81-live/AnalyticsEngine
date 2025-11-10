from analytics_models.definitions.kpis.base_kpi import BaseKPI

class ChurnRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CHURN_RATE",
            name_="Churn Rate",
            description_="The percentage of customers or subscribers who stop using a company's products or services within a certain timeframe.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer', 'Product'],
            formula_="(Number of Customers at Start of Period - Number of Customers at End of Period) / Number of Customers at Start of Period * 100",
            aggregation_methods=['count'],
            time_periods=['custom']
        )

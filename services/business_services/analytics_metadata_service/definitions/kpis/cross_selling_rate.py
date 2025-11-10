from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CrossSellingRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CROSS_SELLING_RATE",
            name_="Cross-selling Rate",
            description_="The percentage of customers who have been sold additional, complementary products or services.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer', 'Product'],
            formula_="(Number of Customers Who Made Additional Purchases / Total Number of Customers) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )

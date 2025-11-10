from analytics_models.definitions.kpis.base_kpi import BaseKPI

class RevenuePerUnitArpu(BaseKPI):
    def __init__(self):
        super().__init__(
            code="REVENUE_PER_UNIT_ARPU",
            name_="Average Revenue per Unit (ARPU)",
            description_="The average revenue generated per unit sold, which helps assess the value of a company's products or services.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer', 'Product'],
            formula_="Total Revenue / Total Number of Units or Customers",
            aggregation_methods=['average', 'sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

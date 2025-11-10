from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SalesCycleLength(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SALES_CYCLE_LENGTH",
            name_="Sales Cycle Length",
            description_="The length of time it takes for a lead to become a customer.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer', 'Deal', 'Lead'],
            formula_="Average Time from First Contact to Deal Closure",
            aggregation_methods=['average'],
            time_periods=['custom']
        )

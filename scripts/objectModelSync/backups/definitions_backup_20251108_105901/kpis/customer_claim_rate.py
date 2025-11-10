from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CustomerClaimRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CUSTOMER_CLAIM_RATE",
            name_="Customer Claim Rate",
            description_="The frequency at which customers make claims for undelivered or damaged goods.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Customer'],
            formula_="(Number of Customer Claims / Total Number of Deliveries) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )

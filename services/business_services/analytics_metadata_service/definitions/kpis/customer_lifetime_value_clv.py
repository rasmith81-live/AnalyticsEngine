import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class CustomerLifetimeValueClv(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CUSTOMER_LIFETIME_VALUE_CLV",
            name_="Customer Lifetime Value (CLV)",
            description_="The estimated value a customer will bring to the company over their lifetime.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer'],
            formula_="(Average Purchase Value * Average Purchase Frequency Rate) * Average Customer Lifespan",
            aggregation_methods=['average'],
            time_periods=['custom']
        )

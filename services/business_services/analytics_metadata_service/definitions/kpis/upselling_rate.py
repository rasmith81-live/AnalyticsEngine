import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class UpsellingRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="UPSELLING_RATE",
            name_="Upselling Rate",
            description_="The percentage of customers who have purchased a more expensive version or upgrade of the product or service they initially bought.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer', 'Product'],
            formula_="(Number of Customers Who Purchased Additional Services or Products / Total Number of Customers) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )

import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class RepeatPurchaseRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="REPEAT_PURCHASE_RATE",
            name_="Repeat Purchase Rate",
            description_="The percentage of customers who make more than one purchase, which can indicate customer loyalty and satisfaction with a company's products or services.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer', 'Product'],
            formula_="(Number of Customers Making Multiple Purchases / Total Number of Customers) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )

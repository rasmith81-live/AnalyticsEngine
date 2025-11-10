import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class CustomerSatisfactionIndex(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CUSTOMER_SATISFACTION_INDEX",
            name_="Customer Satisfaction Index",
            description_="A measure of how satisfied customers are with a company's products or services, often determined through surveys and feedback mechanisms.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer', 'Product', 'PurchaseOrder'],
            formula_="(Sum of Customer Satisfaction Scores / Number of Respondents) * 100",
            aggregation_methods=['sum', 'min', 'count'],
            time_periods=['custom']
        )

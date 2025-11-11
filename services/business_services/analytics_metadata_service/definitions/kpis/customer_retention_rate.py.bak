import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class CustomerRetentionRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CUSTOMER_RETENTION_RATE",
            name_="Customer Retention Rate",
            description_="The percentage of customers who remain with the company over a specified period, indicating the success of customer satisfaction and retention strategies.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer'],
            formula_="((Number of Customers at End of Period - Number of New Customers during Period) / Number of Customers at Start of Period) * 100",
            aggregation_methods=['count'],
            time_periods=['custom']
        )

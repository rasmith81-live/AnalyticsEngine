import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class CustomerAcquisitionCostCac(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CUSTOMER_ACQUISITION_COST_CAC",
            name_="Customer Acquisition Cost (CAC)",
            description_="The cost of acquiring a new customer, including marketing and sales expenses.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer'],
            formula_="(Total Cost of Sales and Marketing) / (Number of New Customers Acquired)",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )

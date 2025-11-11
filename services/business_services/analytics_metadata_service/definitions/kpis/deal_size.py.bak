import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class DealSize(BaseKPI):
    def __init__(self):
        super().__init__(
            code="DEAL_SIZE",
            name_="Deal Size",
            description_="The average value of closed deals.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Deal'],
            formula_="Total Revenue from Closed Deals / Number of Closed Deals",
            aggregation_methods=['average', 'sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

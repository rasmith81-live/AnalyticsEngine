import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class erfeitProductRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="COUNTERFEIT_PRODUCT_RATE",
            name_="Counterfeit Product Rate",
            description_="The rate at which counterfeit products are identified within the supply chain, indicating the effectiveness of security measures to protect product authenticity.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=['Product'],
            formula_="(Number of Counterfeit Incidents / Total Number of Products Sold) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

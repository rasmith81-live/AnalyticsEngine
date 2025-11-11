import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class LandAndExpandSuccessRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="LAND_AND_EXPAND_SUCCESS_RATE",
            name_="Land-and-Expand Success Rate",
            description_="The success rate at which initial sales to new customers lead to subsequent sales within the same account, often through additional products or user licenses.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer', 'Lead', 'Product'],
            formula_="(Revenue from Upselling and Cross-Selling to Existing Customers / Total Revenue from Existing Customers) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )

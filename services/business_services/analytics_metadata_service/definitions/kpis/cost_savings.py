import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class CostSavings(BaseKPI):
    def __init__(self):
        super().__init__(
            code="COST_SAVINGS",
            name_="Cost Savings",
            description_="The total cost savings achieved through the procurement process, including negotiated discounts, bulk purchasing, and efficient supply chain management.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=[],
            formula_="Baseline Spend - Current Spend",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

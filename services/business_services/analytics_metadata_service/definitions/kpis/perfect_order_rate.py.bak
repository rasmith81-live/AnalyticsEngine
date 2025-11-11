import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class PerfectOrderRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PERFECT_ORDER_RATE",
            name_="Perfect Order Rate",
            description_="The percentage of orders that are delivered on time, complete, and without damage, indicating flawless execution.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['Order'],
            formula_="(Number of Perfect Orders / Total Orders Shipped) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

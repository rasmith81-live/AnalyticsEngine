import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class CircularEconomyIntegration(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CIRCULAR_ECONOMY_INTEGRATION",
            name_="Circular Economy Integration",
            description_="The degree to which circular economy principles are integrated into procurement practices, as per ISO 20400.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=[],
            formula_="(Sum of Circular Economy Criteria Met / Total Number of Circular Economy Criteria) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

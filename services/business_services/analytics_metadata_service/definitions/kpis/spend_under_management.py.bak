import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SpendUnderManagement(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SPEND_UNDER_MANAGEMENT",
            name_="Total Spend Under Management",
            description_="The total value of expenditures that are actively managed by the procurement team.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=[],
            formula_="(Managed Spend / Total Organizational Spend) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

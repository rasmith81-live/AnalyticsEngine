import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class NonCompliantSpend(BaseKPI):
    def __init__(self):
        super().__init__(
            code="NON_COMPLIANT_SPEND",
            name_="Non-Compliant Spend",
            description_="The amount of spending that does not comply with procurement policies or contracts.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Contract', 'PurchaseOrder'],
            formula_="(Non-Compliant Spend / Total Spend) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

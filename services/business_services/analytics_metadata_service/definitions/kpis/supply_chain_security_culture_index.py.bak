import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SupplyChainSecurityCultureIndex(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLY_CHAIN_SECURITY_CULTURE_INDEX",
            name_="Supply Chain Security Culture Index",
            description_="A measure of how deeply security awareness and best practices are embedded within the organization's culture and operations.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=[],
            formula_="(Sum of Security Culture Survey Scores) / (Number of Survey Participants)",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

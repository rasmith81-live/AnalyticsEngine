import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SupplyChainSecurityInnovationIndex(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLY_CHAIN_SECURITY_INNOVATION_INDEX",
            name_="Supply Chain Security Innovation Index",
            description_="A measure of the organization's implementation of innovative security solutions in the supply chain.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=[],
            formula_="(Number of Innovative Security Solutions Implemented / Total Number of Security Solutions) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SupplyChainResilienceToClimateRisks(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLY_CHAIN_RESILIENCE_TO_CLIMATE_RISKS",
            name_="Supply Chain Resilience to Climate Risks",
            description_="A measure of the supply chain's ability to withstand and adapt to climate-related risks, in accordance with ISO 20400.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=['Supplier'],
            formula_="(Sum of Resilience Scores) / (Total Number of Suppliers * Maximum Score per Supplier)",
            aggregation_methods=['sum', 'max', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

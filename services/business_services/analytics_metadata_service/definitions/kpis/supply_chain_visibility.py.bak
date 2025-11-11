import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SupplyChainVisibility(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLY_CHAIN_VISIBILITY",
            name_="Supply Chain Visibility",
            description_="The degree to which stakeholders can access real-time data and track products throughout the supply chain, improving decision-making and responsiveness.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['Product', 'PurchaseOrder'],
            formula_="Visibility Score based on traceability and transparency criteria",
            aggregation_methods=['average', 'min', 'max'],
            time_periods=['daily', 'weekly', 'monthly']
        )

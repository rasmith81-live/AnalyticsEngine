import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SupplyChainCarbonFootprint(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLY_CHAIN_CARBON_FOOTPRINT",
            name_="Supply Chain Carbon Footprint",
            description_="The total amount of greenhouse gases produced directly or indirectly by supply chain activities, measured in carbon dioxide equivalent.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=[],
            formula_="Total Emissions (in CO2e) of the Supply Chain",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

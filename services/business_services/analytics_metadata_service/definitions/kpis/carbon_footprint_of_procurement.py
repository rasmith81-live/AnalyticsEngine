import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class CarbonFootprintOfProcurement(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CARBON_FOOTPRINT_OF_PROCUREMENT",
            name_="Carbon Footprint of Procurement",
            description_="The total greenhouse gas emissions associated with procurement activities, aiming to measure and reduce the carbon footprint as per ISO 20400 guidance.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=[],
            formula_="(Total CO2 Emissions from Procured Goods and Services / Total Procurement Spend) * 1,000,000",
            aggregation_methods=['sum', 'min'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class PackingStationUtilization(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKING_STATION_UTILIZATION",
            name_="Packing Station Utilization",
            description_="The percentage of packing stations that are actively in use, reflecting the operational efficiency of packing facilities.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=[],
            formula_="(Total Active Packing Time / Total Available Packing Time) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

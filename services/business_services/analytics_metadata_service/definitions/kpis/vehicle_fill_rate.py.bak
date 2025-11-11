import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class VehicleFillRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="VEHICLE_FILL_RATE",
            name_="Vehicle Fill Rate",
            description_="The percentage of a vehicle’s capacity that is filled with cargo.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=[],
            formula_="(Total Volume or Weight of Goods Loaded / Total Vehicle Capacity) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

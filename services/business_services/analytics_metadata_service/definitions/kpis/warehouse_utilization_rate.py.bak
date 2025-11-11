import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class WarehouseUtilizationRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="WAREHOUSE_UTILIZATION_RATE",
            name_="Warehouse Utilization Rate",
            description_="The percentage of warehouse capacity that is currently being used, indicating the effectiveness of space management.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['Warehouse'],
            formula_="(Used Warehouse Space / Total Warehouse Capacity) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class LoadingEfficiency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="LOADING_EFFICIENCY",
            name_="Loading Efficiency",
            description_="The speed and accuracy with which goods are loaded into outbound vehicles.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Shipment'],
            formula_="Total Time Taken for Loading / Total Number of Shipments Loaded",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

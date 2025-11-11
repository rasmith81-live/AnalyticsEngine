import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class LoadFactor(BaseKPI):
    def __init__(self):
        super().__init__(
            code="LOAD_FACTOR",
            name_="Load Factor",
            description_="The percentage of a transport vehicle’s available capacity that is being used.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['PurchaseOrder', 'Shipment'],
            formula_="(Total Weight of Shipments / Maximum Load Capacity) * 100",
            aggregation_methods=['sum', 'max'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

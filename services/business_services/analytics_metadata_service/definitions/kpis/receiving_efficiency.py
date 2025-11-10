import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class ReceivingEfficiency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="RECEIVING_EFFICIENCY",
            name_="Receiving Efficiency",
            description_="The speed and accuracy of processing incoming goods into the warehouse.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Shipment', 'Warehouse'],
            formula_="Total Time Taken for Receiving / Total Number of Shipments Received",
            aggregation_methods=['sum', 'min', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

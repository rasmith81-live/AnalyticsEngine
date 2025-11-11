import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class ShipmentLeadTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SHIPMENT_LEAD_TIME",
            name_="Shipment Lead Time",
            description_="The time it takes for a shipment to be delivered from the time it is ordered. A shorter lead time indicates more efficient transportation operations.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Delivery', 'Lead', 'Order', 'PurchaseOrder', 'Shipment'],
            formula_="Average Time from Shipment Ready to Delivery",
            aggregation_methods=['average'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

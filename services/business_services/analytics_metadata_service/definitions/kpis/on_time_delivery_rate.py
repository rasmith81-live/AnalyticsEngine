import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class OnTimeDeliveryRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ON_TIME_DELIVERY_RATE",
            name_="On-time Delivery Rate",
            description_="The percentage of shipments that are delivered on time. A higher rate indicates more efficient and reliable transportation operations.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Delivery', 'PurchaseOrder', 'Shipment'],
            formula_="(Number of On-time Deliveries / Total Number of Deliveries) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

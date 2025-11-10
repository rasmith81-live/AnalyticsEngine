import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class PickupAndDeliveryProductivity(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PICKUP_AND_DELIVERY_PRODUCTIVITY",
            name_="Pickup and Delivery Productivity",
            description_="The number of pickups and deliveries made in a given period relative to the resource used.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Delivery', 'Product'],
            formula_="Total Number of Pickups and Deliveries / (Total Hours or Resources Used)",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

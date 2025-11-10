import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class OrderTrackingEfficiency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ORDER_TRACKING_EFFICIENCY",
            name_="Order Tracking Efficiency",
            description_="The effectiveness of the system used to track order status throughout the delivery process.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Delivery', 'Order'],
            formula_="(Number of Successfully Tracked Orders / Total Number of Orders) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

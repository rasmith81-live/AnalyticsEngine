import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class OrderFulfillmentLeadTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ORDER_FULFILLMENT_LEAD_TIME",
            name_="Order Fulfillment Lead Time",
            description_="The total time from order receipt to packing and shipping, crucial for assessing the efficiency of order processing.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=['Lead', 'Order'],
            formula_="Total Order Fulfillment Time / Total Number of Orders",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

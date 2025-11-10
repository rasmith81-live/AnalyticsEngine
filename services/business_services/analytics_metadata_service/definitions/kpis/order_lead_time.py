import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class OrderLeadTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ORDER_LEAD_TIME",
            name_="Order Lead Time",
            description_="The time it takes to fulfill an order, from the moment it is placed to the moment it is delivered to the customer. It helps assess the efficiency of inventory management and order processing.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Customer', 'Delivery', 'Inventory', 'Lead', 'Order'],
            formula_="Total Time from Order Placement to Delivery / Total Number of Orders",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )

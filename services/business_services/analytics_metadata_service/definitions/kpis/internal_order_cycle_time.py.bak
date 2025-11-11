import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class InternalOrderCycleTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="INTERNAL_ORDER_CYCLE_TIME",
            name_="Internal Order Cycle Time",
            description_="The time it takes for the internal warehouse process from order receipt to shipment.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Order', 'Shipment', 'Warehouse'],
            formula_="Total Time for Internal Order Fulfillment / Total Number of Internal Orders",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

from analytics_models.definitions.kpis.base_kpi import BaseKPI

class PurchaseOrderCycleTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PURCHASE_ORDER_CYCLE_TIME",
            name_="Purchase Order Cycle Time",
            description_="The total time taken from the creation of a purchase order to the receipt of the goods or services ordered.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Order', 'PurchaseOrder'],
            formula_="Total Time for All Purchase Orders / Number of Purchase Orders",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

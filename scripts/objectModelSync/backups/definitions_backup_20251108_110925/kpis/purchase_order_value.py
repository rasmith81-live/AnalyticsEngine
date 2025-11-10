from analytics_models.definitions.kpis.base_kpi import BaseKPI

class PurchaseOrderValue(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PURCHASE_ORDER_VALUE",
            name_="Average Purchase Order Value",
            description_="The average value of purchase orders over a specific period, indicating purchasing patterns or trends.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Order', 'PurchaseOrder'],
            formula_="Total Spend / Total Number of Purchase Orders",
            aggregation_methods=['average', 'sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

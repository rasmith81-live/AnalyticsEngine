from analytics_models.definitions.kpis.base_kpi import BaseKPI

class PurchaseOrderAccuracy(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PURCHASE_ORDER_ACCURACY",
            name_="Purchase Order Accuracy",
            description_="The degree to which purchase order information is accurate and free from errors.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Order', 'PurchaseOrder'],
            formula_="(Number of Accurate Purchase Orders / Total Number of Purchase Orders) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

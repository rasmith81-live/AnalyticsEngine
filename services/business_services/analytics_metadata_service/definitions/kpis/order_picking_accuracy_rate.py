from analytics_models.definitions.kpis.base_kpi import BaseKPI

class OrderPickingAccuracyRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ORDER_PICKING_ACCURACY_RATE",
            name_="Order Picking Accuracy Rate",
            description_="The percentage of orders picked without errors.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Order'],
            formula_="(Total Error-Free Picked Orders / Total Picked Orders) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

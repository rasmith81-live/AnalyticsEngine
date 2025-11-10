from analytics_models.definitions.kpis.base_kpi import BaseKPI

class PickingAccuracy(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PICKING_ACCURACY",
            name_="Picking Accuracy",
            description_="The percentage of orders picked without errors from inventory.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Inventory', 'Order'],
            formula_="(Number of Error-free Picks / Total Number of Picks) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

from analytics_models.definitions.kpis.base_kpi import BaseKPI

class WarehouseEfficiency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="WAREHOUSE_EFFICIENCY",
            name_="Average Warehouse Efficiency",
            description_="The overall efficiency of warehouse operations based on output over input.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Inventory', 'Order', 'Warehouse'],
            formula_="(Total Orders Processed + Inventory Accuracy + Order Picking Accuracy) / Total Number of Metrics",
            aggregation_methods=['average', 'sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

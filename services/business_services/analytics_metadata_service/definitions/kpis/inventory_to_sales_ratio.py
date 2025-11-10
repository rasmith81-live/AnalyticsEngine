from analytics_models.definitions.kpis.base_kpi import BaseKPI

class InventoryToSalesRatio(BaseKPI):
    def __init__(self):
        super().__init__(
            code="INVENTORY_TO_SALES_RATIO",
            name_="Inventory to Sales Ratio",
            description_="The ratio of inventory on hand to the number of sales orders fulfilled.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Inventory', 'Order'],
            formula_="Average Inventory Value / Total Sales",
            aggregation_methods=['average', 'sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

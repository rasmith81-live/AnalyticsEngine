from analytics_models.definitions.kpis.base_kpi import BaseKPI

class WarehouseCapacity(BaseKPI):
    def __init__(self):
        super().__init__(
            code="WAREHOUSE_CAPACITY",
            name_="Average Warehouse Capacity",
            description_="The average amount of inventory a warehouse can hold over a certain period.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Inventory', 'Warehouse'],
            formula_="Total Available Warehouse Space for Inventory / Total Warehouse Capacity",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

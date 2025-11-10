from analytics_models.definitions.kpis.base_kpi import BaseKPI

class InventoryAccuracy(BaseKPI):
    def __init__(self):
        super().__init__(
            code="INVENTORY_ACCURACY",
            name_="Inventory Accuracy",
            description_="How well the inventory records match the physical inventory. The KPI is calculated as the number of items in inventory that match the records divided by the total number of items in inventory.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Inventory', 'Product'],
            formula_="(Number of Accurate Inventory Records / Total Inventory Records) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

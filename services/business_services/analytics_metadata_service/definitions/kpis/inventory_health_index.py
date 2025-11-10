from analytics_models.definitions.kpis.base_kpi import BaseKPI

class InventoryHealthIndex(BaseKPI):
    def __init__(self):
        super().__init__(
            code="INVENTORY_HEALTH_INDEX",
            name_="Inventory Health Index",
            description_="A composite measure assessing the health of inventory including age, turnover, and obsolescence.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Inventory', 'PurchaseOrder'],
            formula_="Sum of weighted inventory metrics / Total number of inventory metrics",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

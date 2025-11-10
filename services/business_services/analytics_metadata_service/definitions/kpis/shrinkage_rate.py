from analytics_models.definitions.kpis.base_kpi import BaseKPI

class ShrinkageRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SHRINKAGE_RATE",
            name_="Shrinkage Rate",
            description_="The percentage of inventory loss between manufacture and point of sale.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Inventory', 'PurchaseOrder'],
            formula_="(Inventory Loss / Total Inventory) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

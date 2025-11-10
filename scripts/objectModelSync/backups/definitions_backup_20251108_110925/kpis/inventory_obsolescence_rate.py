from analytics_models.definitions.kpis.base_kpi import BaseKPI

class InventoryObsolescenceRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="INVENTORY_OBSOLESCENCE_RATE",
            name_="Inventory Obsolescence Rate",
            description_="The percentage of inventory that becomes obsolete before it is sold or used, reflecting product lifecycle management effectiveness.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['Inventory', 'Product'],
            formula_="(Value of Obsolete Inventory / Total Inventory Value) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

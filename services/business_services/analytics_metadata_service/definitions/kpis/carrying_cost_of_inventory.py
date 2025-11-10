from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CarryingCostOfInventory(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CARRYING_COST_OF_INVENTORY",
            name_="Carrying Cost of Inventory",
            description_="The cost of storing and maintaining inventory, including warehousing, insurance, and depreciation. It helps identify opportunities to reduce inventory costs without sacrificing customer service levels.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Customer', 'Inventory', 'PurchaseOrder'],
            formula_="(Total Inventory Costs – Cost of Goods Sold) / Total Inventory Value",
            aggregation_methods=['sum'],
            time_periods=['custom']
        )

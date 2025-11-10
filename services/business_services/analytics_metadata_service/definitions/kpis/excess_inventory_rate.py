import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class ExcessInventoryRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="EXCESS_INVENTORY_RATE",
            name_="Excess Inventory Rate",
            description_="The percentage of inventory that exceeds the forecasted demand, indicating potential overstock and capital tie-up.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Inventory', 'PurchaseOrder'],
            formula_="(Excess Inventory Units / Total Inventory Units) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

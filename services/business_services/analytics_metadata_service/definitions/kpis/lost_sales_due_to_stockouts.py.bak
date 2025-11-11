import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class LostSalesDueToStockouts(BaseKPI):
    def __init__(self):
        super().__init__(
            code="LOST_SALES_DUE_TO_STOCKOUTS",
            name_="Lost Sales Due to Stockouts",
            description_="The estimated sales lost due to items being out of stock.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Inventory', 'Product'],
            formula_="Estimated Sales Value of Stockout Items",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

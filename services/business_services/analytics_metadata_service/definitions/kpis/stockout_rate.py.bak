import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class StockoutRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="STOCKOUT_RATE",
            name_="Stockout Rate",
            description_="The frequency and duration of stockouts (i.e., when a product is out of stock) within a given period. It helps assess the effectiveness of inventory forecasting and management.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Inventory', 'Order', 'Product'],
            formula_="(Total Stockouts / Total Orders Placed) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class StockOutRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="STOCK_OUT_RATE",
            name_="Stock-out Rate",
            description_="The percentage of orders that cannot be fulfilled because the requested item is out of stock. A low stock-out rate indicates good inventory management and strong relationships with suppliers.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Inventory', 'Order', 'Product', 'Supplier'],
            formula_="(Number of Stock-outs / Total Number of Inventory Checks) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

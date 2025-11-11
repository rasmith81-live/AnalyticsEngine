import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class StockKeepingUnitSkuRationalization(BaseKPI):
    def __init__(self):
        super().__init__(
            code="STOCK_KEEPING_UNIT_SKU_RATIONALIZATION",
            name_="Stock Keeping Unit (SKU) Rationalization",
            description_="The process of analyzing and streamlining the number of SKUs to optimize inventory management and reduce complexity in the supply chain.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['Inventory'],
            formula_="Number of Active SKUs After Rationalization / Number of Active SKUs Before Rationalization",
            aggregation_methods=['count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

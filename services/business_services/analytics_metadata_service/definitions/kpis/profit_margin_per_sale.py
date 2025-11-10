import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class ProfitMarginPerSale(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PROFIT_MARGIN_PER_SALE",
            name_="Profit Margin per Sale",
            description_="The percentage of profit made on each sale, indicating the profitability of the sales process.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=[],
            formula_="(Total Profit from Sales / Number of Sales)",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

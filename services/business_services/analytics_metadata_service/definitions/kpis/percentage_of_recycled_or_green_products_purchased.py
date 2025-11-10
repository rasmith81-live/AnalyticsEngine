import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class PercentageOfRecycledOrGreenProductsPurchased(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PERCENTAGE_OF_RECYCLED_OR_GREEN_PRODUCTS_PURCHASED",
            name_="Percentage of Recycled or Green Products Purchased",
            description_="The proportion of total purchases that are made up of environmentally friendly or sustainable products.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Product', 'PurchaseOrder'],
            formula_="(Spend on Green Products / Total Spend) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

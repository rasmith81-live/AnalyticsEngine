import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class ValueOfBackorders(BaseKPI):
    def __init__(self):
        super().__init__(
            code="VALUE_OF_BACKORDERS",
            name_="Value of Backorders",
            description_="The monetary value of all backordered items.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Order', 'Product'],
            formula_="Sum of Product Prices * Quantity Backordered",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

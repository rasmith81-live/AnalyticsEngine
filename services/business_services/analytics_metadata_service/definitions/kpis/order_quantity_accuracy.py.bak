import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class OrderQuantityAccuracy(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ORDER_QUANTITY_ACCURACY",
            name_="Order Quantity Accuracy",
            description_="The degree to which the quantity ordered matches the quantity needed, reducing overstock or stockouts.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Inventory', 'Order'],
            formula_="(Number of Orders with Correct Quantities / Total Number of Orders) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

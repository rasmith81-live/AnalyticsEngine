import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class EarlyPaymentDiscountsCaptured(BaseKPI):
    def __init__(self):
        super().__init__(
            code="EARLY_PAYMENT_DISCOUNTS_CAPTURED",
            name_="Early Payment Discounts Captured",
            description_="The percentage of available early payment discounts that are successfully obtained.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Payment'],
            formula_="Total Amount of Discounts for Early Payments / Total Number of Payments",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

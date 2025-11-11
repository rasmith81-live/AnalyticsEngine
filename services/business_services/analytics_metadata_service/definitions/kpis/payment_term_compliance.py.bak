import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class PaymentTermCompliance(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PAYMENT_TERM_COMPLIANCE",
            name_="Payment Term Compliance",
            description_="The rate at which payments to suppliers are made within the agreed-upon payment terms.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Payment', 'PurchaseOrder', 'Supplier'],
            formula_="(Number of Payments within Terms / Total Number of Payments) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

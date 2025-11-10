import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class InvoiceErrorRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="INVOICE_ERROR_RATE",
            name_="Invoice Error Rate",
            description_="The percentage of invoices that contain errors, requiring additional time and resources to resolve.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Invoice'],
            formula_="(Number of Invoices with Errors / Total Number of Invoices Processed) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

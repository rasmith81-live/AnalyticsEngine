import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class ProcurementProcessCompliance(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PROCUREMENT_PROCESS_COMPLIANCE",
            name_="Procurement Process Compliance",
            description_="The adherence to established procurement policies and procedures.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['PurchaseOrder'],
            formula_="(Number of Compliant Procurement Actions / Total Procurement Actions) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

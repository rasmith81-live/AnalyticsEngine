import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class ProcurementCycleTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PROCUREMENT_CYCLE_TIME",
            name_="Procurement Cycle Time",
            description_="The time taken to complete the procurement process from requisition to purchase order and receiving the goods or services.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['Order', 'PurchaseOrder'],
            formula_="Time of Purchase Order Creation - Time of Requisition",
            aggregation_methods=['average', 'min', 'max'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

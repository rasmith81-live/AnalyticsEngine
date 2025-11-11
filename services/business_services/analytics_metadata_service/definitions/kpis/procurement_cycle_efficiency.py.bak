import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class ProcurementCycleEfficiency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PROCUREMENT_CYCLE_EFFICIENCY",
            name_="Procurement Cycle Efficiency",
            description_="The efficiency of the procurement process from requisition to payment.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Payment'],
            formula_="Total Time for All Procurement Cycles / Number of Procurement Cycles",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

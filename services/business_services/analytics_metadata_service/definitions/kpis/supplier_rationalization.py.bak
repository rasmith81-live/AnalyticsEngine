import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SupplierRationalization(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_RATIONALIZATION",
            name_="Supplier Rationalization",
            description_="The process of analyzing and streamlining the supplier base to reduce complexity and costs.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Supplier'],
            formula_="Qualitative Assessment Score based on Rationalization Criteria",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

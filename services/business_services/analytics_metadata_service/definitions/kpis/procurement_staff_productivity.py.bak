import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class ProcurementStaffProductivity(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PROCUREMENT_STAFF_PRODUCTIVITY",
            name_="Procurement Staff Productivity",
            description_="The amount of procurement work (e.g., number of purchase orders) handled per staff member.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Employee', 'Order', 'Product', 'PurchaseOrder'],
            formula_="Total Output of Procurement Activities / Number of Procurement Staff",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

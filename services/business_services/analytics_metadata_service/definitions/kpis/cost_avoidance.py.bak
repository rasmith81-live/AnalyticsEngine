import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class CostAvoidance(BaseKPI):
    def __init__(self):
        super().__init__(
            code="COST_AVOIDANCE",
            name_="Cost Avoidance",
            description_="The reduction in costs achieved by negotiating better prices or finding more cost-effective purchasing solutions.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['PurchaseOrder'],
            formula_="Projected Cost without Procurement Intervention - Actual Cost Post-Intervention",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

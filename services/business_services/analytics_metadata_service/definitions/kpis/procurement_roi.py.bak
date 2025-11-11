import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class ProcurementRoi(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PROCUREMENT_ROI",
            name_="Procurement ROI",
            description_="The return on investment for procurement activities, measuring the cost-effectiveness of the procurement function.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Return'],
            formula_="(Cost Savings + Cost Avoidance) / Procurement Costs",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

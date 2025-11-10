import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class QualityInspectionRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="QUALITY_INSPECTION_RATE",
            name_="Quality Inspection Rate",
            description_="The percentage of incoming goods that undergo quality inspection.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Product', 'QualityMetric'],
            formula_="(Total Products Inspected / Total Products Produced or Received) * 100",
            aggregation_methods=['sum', 'min'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

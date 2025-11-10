import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class PackagingEfficiencyRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKAGING_EFFICIENCY_RATE",
            name_="Packaging Efficiency Rate",
            description_="The percentage of packaging operations completed within a set time frame, indicating the effectiveness of packing processes in fulfilling orders swiftly.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=['Order'],
            formula_="(Total Packed Orders / Total Packing Time) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class PackagingComplianceRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKAGING_COMPLIANCE_RATE",
            name_="Packaging Compliance Rate",
            description_="The percentage of packages that meet regulatory and safety standards, ensuring compliance with industry regulations.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=[],
            formula_="(Total Compliant Packages / Total Packages) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

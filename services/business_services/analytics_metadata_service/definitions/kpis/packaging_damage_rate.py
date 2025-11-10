import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class PackagingDamageRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKAGING_DAMAGE_RATE",
            name_="Packaging Damage Rate",
            description_="The percentage of packages that are damaged during packing or transit, indicating the need for improved packing materials or processes.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=[],
            formula_="(Total Damaged Packages / Total Packages Shipped) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

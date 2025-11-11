import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SustainablePackagingIndex(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUSTAINABLE_PACKAGING_INDEX",
            name_="Sustainable Packaging Index",
            description_="A measure of the percentage of packaging materials that are recyclable or biodegradable, reflecting environmentally friendly practices.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=[],
            formula_="(Total Sustainable Packaging Units / Total Packaging Units) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class PackagingSustainabilityScore(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKAGING_SUSTAINABILITY_SCORE",
            name_="Packaging Sustainability Score",
            description_="A composite score measuring various sustainability factors such as recyclability, biodegradability, and carbon footprint of packaging materials.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=['PurchaseOrder'],
            formula_="(Total Sustainability Score / Total Packaging Units)",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

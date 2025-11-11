import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class OverallEquipmentEffectivenessOeeInSupplyChain(BaseKPI):
    def __init__(self):
        super().__init__(
            code="OVERALL_EQUIPMENT_EFFECTIVENESS_OEE_IN_SUPPLY_CHAIN",
            name_="Overall Equipment Effectiveness (OEE) in Supply Chain",
            description_="The effectiveness of machinery and equipment used in supply chain processes, combining availability, performance, and quality metrics.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['QualityMetric'],
            formula_="(Availability Rate * Performance Rate * Quality Rate) * 100",
            aggregation_methods=['average'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

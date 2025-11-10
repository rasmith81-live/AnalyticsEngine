from analytics_models.definitions.kpis.base_kpi import BaseKPI

class PackingEquipmentUtilizationRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKING_EQUIPMENT_UTILIZATION_RATE",
            name_="Packing Equipment Utilization Rate",
            description_="The percentage of time that packing equipment is actively used compared to available operational time, indicating equipment efficiency.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=[],
            formula_="(Total Equipment Operating Time / Total Available Time) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

from analytics_models.definitions.kpis.base_kpi import BaseKPI

class PackingSafetyIncidentRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKING_SAFETY_INCIDENT_RATE",
            name_="Packing Safety Incident Rate",
            description_="The number of safety incidents occurring during packing operations, reflecting the safety and risk management of the packing process.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=[],
            formula_="(Total Safety Incidents / Total Packing Hours) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

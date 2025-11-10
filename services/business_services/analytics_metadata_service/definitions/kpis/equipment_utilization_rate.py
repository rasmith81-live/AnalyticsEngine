from analytics_models.definitions.kpis.base_kpi import BaseKPI

class EquipmentUtilizationRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="EQUIPMENT_UTILIZATION_RATE",
            name_="Equipment Utilization Rate",
            description_="The percentage of time warehouse equipment is used compared to its availability.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Warehouse'],
            formula_="Total Operating Time of Equipment / Total Available Time",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

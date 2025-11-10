from analytics_models.definitions.kpis.base_kpi import BaseKPI

class LaborCostPerPickingHour(BaseKPI):
    def __init__(self):
        super().__init__(
            code="LABOR_COST_PER_PICKING_HOUR",
            name_="Labor Cost per Picking Hour",
            description_="The labor cost associated with one hour of picking orders.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Order'],
            formula_="Total Labor Costs / Total Picking Hours",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

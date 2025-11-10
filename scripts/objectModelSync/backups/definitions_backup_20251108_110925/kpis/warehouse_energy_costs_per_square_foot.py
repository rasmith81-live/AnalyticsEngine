from analytics_models.definitions.kpis.base_kpi import BaseKPI

class WarehouseEnergyCostsPerSquareFoot(BaseKPI):
    def __init__(self):
        super().__init__(
            code="WAREHOUSE_ENERGY_COSTS_PER_SQUARE_FOOT",
            name_="Warehouse Energy Costs per Square Foot",
            description_="The cost of energy consumption per square foot of warehouse space.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Warehouse'],
            formula_="Total Energy Costs / Total Square Footage of Warehouse",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

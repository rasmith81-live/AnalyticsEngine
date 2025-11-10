from analytics_models.definitions.kpis.base_kpi import BaseKPI

class EnergyEfficiencyOfSuppliers(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ENERGY_EFFICIENCY_OF_SUPPLIERS",
            name_="Energy Efficiency of Suppliers",
            description_="The average level of energy efficiency among suppliers, reflecting adherence to ISO 20400's principles of sustainable procurement.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=['Supplier'],
            formula_="(Total Energy Consumed by Suppliers / Total Output from Suppliers)",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

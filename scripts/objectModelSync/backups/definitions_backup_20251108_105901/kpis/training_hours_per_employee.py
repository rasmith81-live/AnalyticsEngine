from analytics_models.definitions.kpis.base_kpi import BaseKPI

class TrainingHoursPerEmployee(BaseKPI):
    def __init__(self):
        super().__init__(
            code="TRAINING_HOURS_PER_EMPLOYEE",
            name_="Average Training Hours per Employee",
            description_="The average number of training hours provided to each warehouse employee.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Employee', 'Warehouse'],
            formula_="Total Training Hours / Total Number of Employees",
            aggregation_methods=['average', 'sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

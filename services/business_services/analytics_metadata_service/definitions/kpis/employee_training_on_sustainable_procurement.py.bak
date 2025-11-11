import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class EmployeeTrainingOnSustainableProcurement(BaseKPI):
    def __init__(self):
        super().__init__(
            code="EMPLOYEE_TRAINING_ON_SUSTAINABLE_PROCUREMENT",
            name_="Employee Training on Sustainable Procurement",
            description_="The percentage of procurement staff trained in sustainable procurement practices as outlined in ISO 20400.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=['Employee'],
            formula_="(Number of Employees Trained in Sustainable Procurement / Total Procurement Staff) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

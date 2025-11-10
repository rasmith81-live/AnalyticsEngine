import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SecurityTrainingCompletionRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SECURITY_TRAINING_COMPLETION_RATE",
            name_="Security Training Completion Rate",
            description_="The percentage of employees who have completed mandatory security training, reflecting the organization's commitment to staff education on supply chain security.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=['Employee'],
            formula_="(Number of Employees Who Completed Security Training / Total Number of Employees) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SalesTrainingCompletionRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SALES_TRAINING_COMPLETION_RATE",
            name_="Sales Training Completion Rate",
            description_="The percentage of sales representatives who have completed mandatory sales training programs.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=[],
            formula_="(Number of Sales Reps Who Completed Training / Total Number of Sales Reps) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

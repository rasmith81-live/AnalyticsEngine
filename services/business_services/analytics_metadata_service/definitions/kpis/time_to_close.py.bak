import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class TimeToClose(BaseKPI):
    def __init__(self):
        super().__init__(
            code="TIME_TO_CLOSE",
            name_="Time to Close",
            description_="The time it takes to close a deal from the initial contact with a lead.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Deal', 'Lead'],
            formula_="Total Time Taken to Close All Sales / Total Number of Sales Closed",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

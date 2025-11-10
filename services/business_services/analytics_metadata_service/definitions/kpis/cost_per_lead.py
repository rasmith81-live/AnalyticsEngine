import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class CostPerLead(BaseKPI):
    def __init__(self):
        super().__init__(
            code="COST_PER_LEAD",
            name_="Cost per Lead",
            description_="The average cost incurred to generate one lead, which helps to evaluate the efficiency of marketing campaigns.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Lead'],
            formula_="Total Cost of Lead Generation / Total Number of Leads",
            aggregation_methods=['average', 'sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

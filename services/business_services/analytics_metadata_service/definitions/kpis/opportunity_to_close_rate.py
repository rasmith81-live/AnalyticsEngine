import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class OpportunityToCloseRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="OPPORTUNITY_TO_CLOSE_RATE",
            name_="Opportunity-to-Close Rate",
            description_="The percentage of sales opportunities that are converted into actual sales, showing the effectiveness of the sales team's closing abilities.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Opportunity', 'PurchaseOrder'],
            formula_="(Number of Opportunities Closed as Wins / Total Number of Opportunities) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

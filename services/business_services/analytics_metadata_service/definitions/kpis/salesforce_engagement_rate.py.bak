import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SalesforceEngagementRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SALESFORCE_ENGAGEMENT_RATE",
            name_="Salesforce Engagement Rate",
            description_="The level of active use of the salesforce automation tools by the sales team, reflecting on tool adoption and efficiency.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=[],
            formula_="(Number of Active Users on Salesforce / Total Number of Sales Representatives) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

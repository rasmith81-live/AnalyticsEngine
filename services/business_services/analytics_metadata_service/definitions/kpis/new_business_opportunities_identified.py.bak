import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class NewBusinessOpportunitiesIdentified(BaseKPI):
    def __init__(self):
        super().__init__(
            code="NEW_BUSINESS_OPPORTUNITIES_IDENTIFIED",
            name_="New Business Opportunities Identified",
            description_="The number of new business opportunities identified by the team, indicating the potential for revenue growth.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['PurchaseOrder'],
            formula_="Total Number of New Opportunities Identified",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

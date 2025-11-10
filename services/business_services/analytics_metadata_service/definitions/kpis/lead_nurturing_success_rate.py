import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class LeadNurturingSuccessRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="LEAD_NURTURING_SUCCESS_RATE",
            name_="Lead Nurturing Success Rate",
            description_="The percentage of leads that become opportunities as a result of lead nurturing efforts.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Lead', 'PurchaseOrder'],
            formula_="(Number of Nurtured Leads Converted / Total Number of Nurtured Leads) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

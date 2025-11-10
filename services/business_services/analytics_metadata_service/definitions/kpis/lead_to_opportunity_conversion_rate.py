from analytics_models.definitions.kpis.base_kpi import BaseKPI

class LeadToOpportunityConversionRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="LEAD_TO_OPPORTUNITY_CONVERSION_RATE",
            name_="Lead-to-Opportunity Conversion Rate",
            description_="The percentage of leads that become sales opportunities, indicating the effectiveness of the lead qualification process.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Lead', 'Opportunity', 'PurchaseOrder'],
            formula_="(Number of Leads Converted to Opportunities / Total Number of Leads) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

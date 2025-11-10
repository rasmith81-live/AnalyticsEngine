import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SalesQualifiedLeadsSql(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SALES_QUALIFIED_LEADS_SQL",
            name_="Sales Qualified Leads (SQL)",
            description_="The number of leads that have been vetted by both marketing and sales teams and are deemed ready for the next step in the sales process.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Lead'],
            formula_="Number of Leads Meeting SQL Criteria",
            aggregation_methods=['count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

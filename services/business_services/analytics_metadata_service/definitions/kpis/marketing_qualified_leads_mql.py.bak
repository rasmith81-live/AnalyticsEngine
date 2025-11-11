import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class MarketingQualifiedLeadsMql(BaseKPI):
    def __init__(self):
        super().__init__(
            code="MARKETING_QUALIFIED_LEADS_MQL",
            name_="Marketing Qualified Leads (MQL)",
            description_="The number of leads that have shown interest in a company's offerings and are considered more likely to become customers than other leads.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer', 'Lead'],
            formula_="Number of Leads Meeting MQL Criteria",
            aggregation_methods=['count'],
            time_periods=['custom']
        )

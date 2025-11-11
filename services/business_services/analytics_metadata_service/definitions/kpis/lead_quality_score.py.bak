import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class LeadQualityScore(BaseKPI):
    def __init__(self):
        super().__init__(
            code="LEAD_QUALITY_SCORE",
            name_="Lead Quality Score",
            description_="A score assigned to leads based on their perceived value, taking into account factors like job title, industry, company size, and engagement level.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Lead', 'QualityMetric'],
            formula_="(Various metrics depending on the lead scoring criteria used)",
            aggregation_methods=['count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

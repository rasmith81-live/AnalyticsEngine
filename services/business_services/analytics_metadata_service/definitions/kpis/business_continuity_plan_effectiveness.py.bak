import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class BusinessContinuityPlanEffectiveness(BaseKPI):
    def __init__(self):
        super().__init__(
            code="BUSINESS_CONTINUITY_PLAN_EFFECTIVENESS",
            name_="Business Continuity Plan Effectiveness",
            description_="The effectiveness of the business continuity plan as it relates to supply chain operations, which is essential for maintaining operations during and after security incidents.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=[],
            formula_="(Number of Successful Recovery Tests + Actual Recoveries) / (Total Number of Tests + Disruptions) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

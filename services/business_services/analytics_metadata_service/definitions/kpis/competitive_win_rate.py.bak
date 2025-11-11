import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class CompetitiveWinRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="COMPETITIVE_WIN_RATE",
            name_="Competitive Win Rate",
            description_="The percentage of deals won against competitors, indicating the sales team's effectiveness in competitive situations.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Deal'],
            formula_="(Number of Deals Won Against Competitors / Total Number of Competitive Deals) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

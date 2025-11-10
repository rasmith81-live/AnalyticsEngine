from analytics_models.definitions.kpis.base_kpi import BaseKPI

class TransportationModeSecurityEvaluation(BaseKPI):
    def __init__(self):
        super().__init__(
            code="TRANSPORTATION_MODE_SECURITY_EVALUATION",
            name_="Transportation Mode Security Evaluation",
            description_="The evaluation of security measures specific to different modes of transportation within the supply chain.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=['PurchaseOrder'],
            formula_="(Sum of Security Evaluation Scores for Each Mode) / (Number of Modes Evaluated)",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SupplierEngagementScore(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SUPPLIER_ENGAGEMENT_SCORE",
            name_="Supplier Engagement Score",
            description_="The level of supplier involvement in sustainability initiatives, supporting the goals of ISO 20400.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=['PurchaseOrder', 'Supplier'],
            formula_="(Sum of Supplier Engagement Scores) / (Total Number of Suppliers * Maximum Score per Supplier)",
            aggregation_methods=['sum', 'max', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CustomerSatisfactionWithPackaging(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CUSTOMER_SATISFACTION_WITH_PACKAGING",
            name_="Customer Satisfaction with Packaging",
            description_="The level of customer satisfaction with the quality and condition of packaging upon delivery, impacting customer loyalty.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=['Customer', 'Delivery', 'PurchaseOrder', 'QualityMetric'],
            formula_="(Total Customer Satisfaction Score / Total Responses) * 100",
            aggregation_methods=['sum'],
            time_periods=['custom']
        )

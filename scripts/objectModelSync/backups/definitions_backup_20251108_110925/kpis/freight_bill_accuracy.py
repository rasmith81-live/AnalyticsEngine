from analytics_models.definitions.kpis.base_kpi import BaseKPI

class FreightBillAccuracy(BaseKPI):
    def __init__(self):
        super().__init__(
            code="FREIGHT_BILL_ACCURACY",
            name_="Freight Bill Accuracy",
            description_="The accuracy of freight costs and billing, reducing discrepancies and overcharges in transportation expenses.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['PurchaseOrder'],
            formula_="(Number of Error-Free Freight Bills / Total Freight Bills Processed) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

from analytics_models.definitions.kpis.base_kpi import BaseKPI

class OrderPackingAccuracy(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ORDER_PACKING_ACCURACY",
            name_="Order Packing Accuracy",
            description_="The percentage of orders packed correctly according to customer specifications, indicating the precision of packing operations.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=['Customer', 'Order'],
            formula_="(Total Accurate Orders / Total Orders Packed) * 100",
            aggregation_methods=['sum'],
            time_periods=['custom']
        )

from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CustomerSatisfactionWithDelivery(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CUSTOMER_SATISFACTION_WITH_DELIVERY",
            name_="Customer Satisfaction with Delivery",
            description_="Customer satisfaction with the company's delivery operations. A higher satisfaction rate indicates that customers are receiving their orders in a timely and efficient manner.",
            category_="Logistics",
            modules_=["LOGISTICS"],
            required_objects=['Customer', 'Delivery', 'Order'],
            formula_="Average of Customer Delivery Satisfaction Scores",
            aggregation_methods=['average'],
            time_periods=['custom']
        )

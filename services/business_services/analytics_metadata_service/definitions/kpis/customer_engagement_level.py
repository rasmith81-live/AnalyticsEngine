from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CustomerEngagementLevel(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CUSTOMER_ENGAGEMENT_LEVEL",
            name_="Customer Engagement Level",
            description_="The degree to which customers interact with the brand through various channels and activities, indicating their interest and loyalty.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer'],
            formula_="(Various metrics depending on the engagement channels used)",
            aggregation_methods=['average', 'sum'],
            time_periods=['custom']
        )

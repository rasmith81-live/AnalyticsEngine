from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SalesPitchLength(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SALES_PITCH_LENGTH",
            name_="Average Sales Pitch Length",
            description_="The average duration of sales pitches or presentations, which can influence customer engagement and decision-making.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer'],
            formula_="Total Duration of All Sales Pitches / Number of Sales Pitches",
            aggregation_methods=['average', 'sum', 'count'],
            time_periods=['custom']
        )

from analytics_models.definitions.kpis.base_kpi import BaseKPI

class DemandForecastAccuracy(BaseKPI):
    def __init__(self):
        super().__init__(
            code="DEMAND_FORECAST_ACCURACY",
            name_="Demand Forecast Accuracy",
            description_="The accuracy of prediction for future demand compared to actual demand, impacting inventory levels and customer satisfaction.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['Customer', 'Inventory'],
            formula_="(1 - (Absolute Value of (Actual Demand - Forecasted Demand) / Actual Demand)) * 100",
            aggregation_methods=['average', 'sum'],
            time_periods=['custom']
        )

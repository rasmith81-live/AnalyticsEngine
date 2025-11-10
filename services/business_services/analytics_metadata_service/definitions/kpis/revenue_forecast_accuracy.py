import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class RevenueForecastAccuracy(BaseKPI):
    def __init__(self):
        super().__init__(
            code="REVENUE_FORECAST_ACCURACY",
            name_="Revenue Forecast Accuracy",
            description_="The accuracy of the sales team's revenue forecasts compared to actual revenue results.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=[],
            formula_="(Absolute Value of (Actual Revenue - Forecasted Revenue) / Actual Revenue) * 100",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

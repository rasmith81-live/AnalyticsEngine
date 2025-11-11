import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class SalesToolUtilizationRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SALES_TOOL_UTILIZATION_RATE",
            name_="Sales Tool Utilization Rate",
            description_="The rate at which sales tools provided to the sales team are actually used in their day-to-day activities.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=[],
            formula_="(Number of Sales Representatives Using Sales Tools / Total Number of Sales Representatives) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly']
        )

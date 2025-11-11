import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class DemoToClosingRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="DEMO_TO_CLOSING_RATE",
            name_="Demo-to-Closing Rate",
            description_="The percentage of product or service demonstrations that result in a closed sale.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Deal', 'Product'],
            formula_="(Number of Closed Deals after a Demo / Number of Demos Conducted) * 100",
            aggregation_methods=['count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

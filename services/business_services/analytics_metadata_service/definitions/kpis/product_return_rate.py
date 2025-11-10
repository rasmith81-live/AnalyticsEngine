import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class ProductReturnRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PRODUCT_RETURN_RATE",
            name_="Product Return Rate",
            description_="The percentage of products that are returned by customers, which can signal issues with product satisfaction or quality.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['Customer', 'Product', 'QualityMetric', 'Return'],
            formula_="(Number of Products Returned / Total Number of Products Sold) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['custom']
        )

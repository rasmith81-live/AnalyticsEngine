import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class ReturnRateDueToPackingErrors(BaseKPI):
    def __init__(self):
        super().__init__(
            code="RETURN_RATE_DUE_TO_PACKING_ERRORS",
            name_="Return Rate due to Packing Errors",
            description_="The percentage of products returned due to errors in packing, serving as an indicator of the quality and accuracy of packing processes.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=['Product', 'QualityMetric', 'Return'],
            formula_="(Total Returns Due to Packing Errors / Total Returns) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

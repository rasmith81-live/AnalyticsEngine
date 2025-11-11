import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class PipelineGrowthRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PIPELINE_GROWTH_RATE",
            name_="Pipeline Growth Rate",
            description_="The rate at which the sales pipeline is growing, indicating the potential for future sales.",
            category_="Business Development",
            modules_=["BUSINESS_DEVELOPMENT"],
            required_objects=['PurchaseOrder'],
            formula_="((Number of Opportunities at End of Period - Number of Opportunities at Start of Period) / Number of Opportunities at Start of Period) * 100",
            aggregation_methods=['count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

from analytics_models.definitions.kpis.base_kpi import BaseKPI

class PackagingReturnOnInvestmentRoi(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKAGING_RETURN_ON_INVESTMENT_ROI",
            name_="Packaging Return on Investment (ROI)",
            description_="The financial return achieved from investments in packaging improvements, indicating the value of packaging enhancements.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=['Return'],
            formula_="(Total Benefits from Packaging - Total Packaging Costs) / Total Packaging Costs",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

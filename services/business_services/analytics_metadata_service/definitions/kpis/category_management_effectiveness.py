from analytics_models.definitions.kpis.base_kpi import BaseKPI

class CategoryManagementEffectiveness(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CATEGORY_MANAGEMENT_EFFECTIVENESS",
            name_="Category Management Effectiveness",
            description_="The performance of procurement in managing different categories of goods and services.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=[],
            formula_="Sum of Performance Metrics within a Category / Total Number of Metrics for Category",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

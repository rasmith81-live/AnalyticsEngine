from analytics_models.definitions.kpis.base_kpi import BaseKPI

class MaverickSpend(BaseKPI):
    def __init__(self):
        super().__init__(
            code="MAVERICK_SPEND",
            name_="Maverick Spend",
            description_="The percentage of total spend that occurs outside of pre-negotiated contracts or preferred suppliers.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Contract', 'Supplier'],
            formula_="Total Maverick Spend / Total Spend",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

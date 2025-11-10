from analytics_models.definitions.kpis.base_kpi import BaseKPI

class PackingFlexibility(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PACKING_FLEXIBILITY",
            name_="Packing Flexibility",
            description_="A measure of the ability to adapt packing operations to changes in demand or product types, indicating operational agility.",
            category_="Packing",
            modules_=["PACKING"],
            required_objects=['Order', 'Product'],
            formula_="(Total Orders Packed with Changes / Total Orders Packed) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

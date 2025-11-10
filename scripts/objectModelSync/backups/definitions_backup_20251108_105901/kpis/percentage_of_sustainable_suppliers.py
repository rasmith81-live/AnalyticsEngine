from analytics_models.definitions.kpis.base_kpi import BaseKPI

class PercentageOfSustainableSuppliers(BaseKPI):
    def __init__(self):
        super().__init__(
            code="PERCENTAGE_OF_SUSTAINABLE_SUPPLIERS",
            name_="Percentage of Sustainable Suppliers",
            description_="The proportion of suppliers that meet the organization's sustainability criteria as per ISO 20400 guidelines.",
            category_="Iso 20400",
            modules_=["ISO_20400"],
            required_objects=['PurchaseOrder', 'Supplier'],
            formula_="(Number of Sustainable Suppliers / Total Number of Suppliers) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

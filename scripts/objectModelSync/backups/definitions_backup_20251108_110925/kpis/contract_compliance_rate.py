from analytics_models.definitions.kpis.base_kpi import BaseKPI

class ContractComplianceRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CONTRACT_COMPLIANCE_RATE",
            name_="Contract Compliance Rate",
            description_="The percentage of orders placed that are in compliance with the terms of the company's contracts with suppliers. A high compliance rate indicates good contract management and minimizes the risk of disputes or penalties.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Contract', 'Order', 'Supplier'],
            formula_="(Number of Contract-Compliant Purchases / Total Number of Purchases) * 100",
            aggregation_methods=['sum', 'min', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

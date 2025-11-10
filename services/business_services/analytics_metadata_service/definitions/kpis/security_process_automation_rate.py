from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SecurityProcessAutomationRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SECURITY_PROCESS_AUTOMATION_RATE",
            name_="Security Process Automation Rate",
            description_="The extent to which security processes are automated, demonstrating the organization's innovation in security management.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=[],
            formula_="(Number of Automated Security Processes / Total Security Processes) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

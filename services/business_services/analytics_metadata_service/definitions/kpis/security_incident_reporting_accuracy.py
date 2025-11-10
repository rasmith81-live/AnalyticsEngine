from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SecurityIncidentReportingAccuracy(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SECURITY_INCIDENT_REPORTING_ACCURACY",
            name_="Security Incident Reporting Accuracy",
            description_="The accuracy of security incident reporting, which is crucial for effective incident management and continuous improvement.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=['PurchaseOrder'],
            formula_="(Number of Accurately Reported Incidents / Total Number of Reported Incidents) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

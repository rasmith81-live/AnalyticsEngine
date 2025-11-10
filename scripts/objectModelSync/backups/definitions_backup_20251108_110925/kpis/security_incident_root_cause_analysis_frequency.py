from analytics_models.definitions.kpis.base_kpi import BaseKPI

class SecurityIncidentRootCauseAnalysisFrequency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="SECURITY_INCIDENT_ROOT_CAUSE_ANALYSIS_FREQUENCY",
            name_="Security Incident Root Cause Analysis Frequency",
            description_="The regularity with which root cause analyses are conducted following security incidents, which is critical for preventing future occurrences.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=[],
            formula_="Total Number of Root Cause Analyses / Number of Security Incidents",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

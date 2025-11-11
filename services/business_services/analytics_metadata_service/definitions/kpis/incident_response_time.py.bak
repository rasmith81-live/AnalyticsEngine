import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class IncidentResponseTime(BaseKPI):
    def __init__(self):
        super().__init__(
            code="INCIDENT_RESPONSE_TIME",
            name_="Incident Response Time",
            description_="The average time it takes for the organization to respond to a supply chain security incident, reflecting the efficiency and preparedness of the response team.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=['PurchaseOrder'],
            formula_="Sum of Response Times for All Incidents / Number of Incidents",
            aggregation_methods=['average', 'sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

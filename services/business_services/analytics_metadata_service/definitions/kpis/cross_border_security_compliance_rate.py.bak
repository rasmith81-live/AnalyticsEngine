import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class CrossBorderSecurityComplianceRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="CROSS_BORDER_SECURITY_COMPLIANCE_RATE",
            name_="Cross-Border Security Compliance Rate",
            description_="The rate at which the organization complies with cross-border security regulations, reflecting the ability to operate internationally without security-related disruptions.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=['Order', 'Shipment'],
            formula_="(Number of Compliant Cross-Border Shipments / Total Number of Cross-Border Shipments) * 100",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

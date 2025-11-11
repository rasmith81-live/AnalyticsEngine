import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class VendorRiskManagementEfficiency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="VENDOR_RISK_MANAGEMENT_EFFICIENCY",
            name_="Vendor Risk Management Efficiency",
            description_="The efficiency of the vendor risk management process, indicating the ability to identify and mitigate risks posed by third-party vendors.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=['PurchaseOrder', 'Supplier'],
            formula_="(Successful Risk Mitigations / Total Vendor Risks Identified) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class EmergencyProcedureTestingFrequency(BaseKPI):
    def __init__(self):
        super().__init__(
            code="EMERGENCY_PROCEDURE_TESTING_FREQUENCY",
            name_="Emergency Procedure Testing Frequency",
            description_="The frequency at which emergency procedures are tested, indicating the preparedness for potential supply chain disruptions.",
            category_="Iso 28000",
            modules_=["ISO_28000"],
            required_objects=['PurchaseOrder'],
            formula_="Total Number of Emergency Tests and Drills / Time Period",
            aggregation_methods=['sum', 'count'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

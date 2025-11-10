import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class VendorManagedInventoryVmiEffectiveness(BaseKPI):
    def __init__(self):
        super().__init__(
            code="VENDOR_MANAGED_INVENTORY_VMI_EFFECTIVENESS",
            name_="Vendor Managed Inventory (VMI) Effectiveness",
            description_="The success of VMI programs in optimizing inventory levels and reducing stockouts through supplier management of inventory.",
            category_="Iso 22004",
            modules_=["ISO_22004"],
            required_objects=['Inventory', 'Supplier'],
            formula_="Performance Metrics (e.g., Fulfillment Rate, Inventory Levels)",
            aggregation_methods=['average'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

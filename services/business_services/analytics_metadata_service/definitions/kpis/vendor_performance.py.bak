import sys; from pathlib import Path; sys.path.insert(0, str(Path(__file__).parent)); from base_kpi import BaseKPI

class VendorPerformance(BaseKPI):
    def __init__(self):
        super().__init__(
            code="VENDOR_PERFORMANCE",
            name_="Vendor Performance",
            description_="The overall performance of the company's suppliers, including factors such as delivery speed, quality of products or services, and responsiveness to requests.",
            category_="Sourcing",
            modules_=["SOURCING"],
            required_objects=['Delivery', 'Product', 'PurchaseOrder', 'QualityMetric', 'Supplier'],
            formula_="Qualitative and Quantitative Score based on Predefined Performance Criteria",
            aggregation_methods=['average', 'sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

from analytics_models.definitions.kpis.base_kpi import BaseKPI

class OrderAccuracyRate(BaseKPI):
    def __init__(self):
        super().__init__(
            code="ORDER_ACCURACY_RATE",
            name_="Order Accuracy Rate",
            description_="The percentage of orders that are accurately fulfilled without errors, such as wrong items, wrong quantities, or damaged products. It helps assess the effectiveness of inventory management and order processing, and identify areas for improvement in the supply chain process.",
            category_="Inventory Management",
            modules_=["INVENTORY_MANAGEMENT"],
            required_objects=['Inventory', 'Order', 'Product'],
            formula_="(Total Error-Free Orders / Total Orders Shipped) * 100",
            aggregation_methods=['sum'],
            time_periods=['daily', 'weekly', 'monthly', 'quarterly', 'annually']
        )

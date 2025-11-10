"""
Retail Industry Definition
"""

from analytics_models import Industry

RETAIL = Industry(
    name="Retail",
    code="RETAIL",
    description="Retail industry analytics including stores and e-commerce",
    is_active=True,
    metadata_={
        "sector": "Consumer",
        "typical_metrics": ["sales_per_sqft", "inventory_turnover", "customer_traffic"],
        "common_kpis": ["conversion_rate", "average_transaction_value", "customer_lifetime_value"]
    }
)

"""
Manufacturing Industry Definition
"""

from analytics_models import Industry

MANUFACTURING = Industry(
    name="Manufacturing",
    code="MANUFACTURING",
    description="Manufacturing operations and production analytics",
    is_active=True,
    metadata_={
        "sector": "Industrial",
        "typical_metrics": ["oee", "cycle_time", "defect_rate"],
        "common_kpis": ["production_throughput", "quality_yield", "equipment_uptime"]
    }
)

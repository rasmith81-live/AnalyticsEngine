"""
KPI Registry

Automatically discovers and registers all KPI definitions.
"""

from analytics_models import KPI
from ..base_registry import BaseRegistry


class KPIRegistry(BaseRegistry):
    """Registry for all KPIs."""
    
    def __init__(self):
        super().__init__(
            entity_class=KPI,
            module_path='definitions.kpis'
        )
    
    def get_by_category(self, category: str) -> list[KPI]:
        """Get all KPIs in a specific category."""
        return [
            kpi for kpi in self.get_all()
            if kpi.category == category
        ]
    
    def get_by_module(self, module_code: str) -> list[KPI]:
        """Get all KPIs for a specific module."""
        return [
            kpi for kpi in self.get_all()
            if kpi.metadata_ and module_code in kpi.metadata_.get('modules', [])
        ]


# Create singleton instance
kpis = KPIRegistry()


# Convenience functions
def get_kpi(code: str) -> KPI:
    """Get KPI by code."""
    return kpis.get(code)


def get_all_kpis() -> list[KPI]:
    """Get all KPIs."""
    return kpis.get_all()


def get_kpis_by_category(category: str) -> list[KPI]:
    """Get KPIs by category."""
    return kpis.get_by_category(category)


def list_kpi_codes() -> list[str]:
    """List all KPI codes."""
    return kpis.list_codes()

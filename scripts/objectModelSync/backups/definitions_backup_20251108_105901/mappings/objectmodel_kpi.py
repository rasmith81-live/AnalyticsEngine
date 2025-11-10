"""
ObjectModel to KPI Mappings

Defines which KPIs belong to which object models.
"""

from ..object_models.registry import get_object_model
from ..kpis.registry import get_kpi


OBJECTMODEL_KPI_MAP = {
    # Add mappings as object models are created
}


def setup_objectmodel_kpi_relationships():
    """Associate KPIs with object models based on mappings."""
    for om_code, kpi_codes in OBJECTMODEL_KPI_MAP.items():
        object_model = get_object_model(om_code)
        if object_model:
            for kpi_code in kpi_codes:
                kpi = get_kpi(kpi_code)
                if kpi and kpi not in object_model.kpis:
                    object_model.kpis.append(kpi)

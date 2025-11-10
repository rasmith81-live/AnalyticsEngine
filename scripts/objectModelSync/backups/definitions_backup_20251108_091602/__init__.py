"""
Definitions Package

Auto-discovers and registers all entities, then sets up relationships.
"""

from .industries.registry import industries, get_industry, get_all_industries, list_industry_codes
from .value_chains.registry import value_chains, get_value_chain, get_all_value_chains, list_value_chain_codes
from .modules.registry import modules, get_module, get_all_modules, list_module_codes
from .object_models.registry import object_models, get_object_model, get_all_object_models, list_object_model_codes
from .attributes.registry import attributes, get_attribute, get_all_attributes, list_attribute_codes
from .kpis.registry import kpis, get_kpi, get_all_kpis, list_kpi_codes
from .benchmarks.registry import benchmarks, get_benchmark, get_all_benchmarks, list_benchmark_codes

from .mappings.industry_valuechain import setup_industry_valuechain_relationships
from .mappings.valuechain_module import setup_valuechain_module_relationships
from .mappings.module_objectmodel import setup_module_objectmodel_relationships
from .mappings.objectmodel_kpi import setup_objectmodel_kpi_relationships
from .mappings.kpi_benchmark import setup_kpi_benchmark_relationships


def setup_all_relationships():
    """
    Set up all entity relationships.
    
    Call this once during application initialization.
    """
    print("=" * 80)
    print("Setting up Analytics Model Relationships")
    print("=" * 80)
    
    print("\n├─ Industry → ValueChain...")
    setup_industry_valuechain_relationships()
    
    print("├─ ValueChain → Module...")
    setup_valuechain_module_relationships()
    
    print("├─ Module → ObjectModel...")
    setup_module_objectmodel_relationships()
    
    print("├─ ObjectModel ← Attribute (dynamic)...")
    attributes.link_to_object_models()
    
    print("├─ ObjectModel → KPI...")
    setup_objectmodel_kpi_relationships()
    
    print("└─ KPI → Benchmark...")
    setup_kpi_benchmark_relationships()
    
    print(f"\n{'=' * 80}")
    print("Registry Summary")
    print("=" * 80)
    print(f"✓ Registered {len(industries)} industries")
    print(f"✓ Registered {len(value_chains)} value chains")
    print(f"✓ Registered {len(modules)} modules")
    print(f"✓ Registered {len(object_models)} object models (unified model + instance)")
    print(f"✓ Registered {len(attributes)} attributes")
    print(f"✓ Registered {len(kpis)} KPIs")
    print(f"✓ Registered {len(benchmarks)} benchmarks")
    print(f"{'=' * 80}\n")


__all__ = [
    # Registries
    'industries',
    'value_chains',
    'modules',
    'object_models',
    'attributes',
    'kpis',
    'benchmarks',
    
    # Getters
    'get_industry',
    'get_all_industries',
    'list_industry_codes',
    'get_value_chain',
    'get_all_value_chains',
    'list_value_chain_codes',
    'get_module',
    'get_all_modules',
    'list_module_codes',
    'get_object_model',
    'get_all_object_models',
    'list_object_model_codes',
    'get_attribute',
    'get_all_attributes',
    'list_attribute_codes',
    'get_kpi',
    'get_all_kpis',
    'list_kpi_codes',
    'get_benchmark',
    'get_all_benchmarks',
    'list_benchmark_codes',
    
    # Setup
    'setup_all_relationships',
]

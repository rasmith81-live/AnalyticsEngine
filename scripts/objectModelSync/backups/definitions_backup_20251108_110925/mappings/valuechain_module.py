"""
ValueChain to Module Mappings

Defines which modules belong to which value chains.
"""

from ..value_chains.registry import get_value_chain
from ..modules.registry import get_module


VALUECHAIN_MODULE_MAP = {
    "SALES_MGMT": [
        "INVENTORY_MGMT",
        "BUS_DEV",
    ],
    "SUPPLY_CHAIN": [
        "INVENTORY_MGMT",
    ],
}


def setup_valuechain_module_relationships():
    """Associate modules with value chains based on mappings."""
    for vc_code, module_codes in VALUECHAIN_MODULE_MAP.items():
        value_chain = get_value_chain(vc_code)
        if value_chain:
            for mod_code in module_codes:
                module = get_module(mod_code)
                if module and module not in value_chain.modules:
                    value_chain.modules.append(module)

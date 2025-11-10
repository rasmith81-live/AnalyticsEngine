"""
Industry to ValueChain Mappings

Defines which value chains belong to which industries.
"""

from ..industries.registry import get_industry
from ..value_chains.registry import get_value_chain


INDUSTRY_VALUECHAIN_MAP = {
    "RETAIL": [
        "SALES_MGMT",
        "SUPPLY_CHAIN",
    ],
    "MANUFACTURING": [
        "SALES_MGMT",
        "SUPPLY_CHAIN",
    ],
}


def setup_industry_valuechain_relationships():
    """Associate value chains with industries based on mappings."""
    for industry_code, valuechain_codes in INDUSTRY_VALUECHAIN_MAP.items():
        industry = get_industry(industry_code)
        if industry:
            for vc_code in valuechain_codes:
                value_chain = get_value_chain(vc_code)
                if value_chain and value_chain not in industry.value_chains:
                    industry.value_chains.append(value_chain)

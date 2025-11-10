"""
Sales Strategy Module

Focuses on strategic planning, market analysis, competitive positioning,
and long-term sales growth strategies.
"""

from analytics_models import Module

SALES_STRATEGY = Module(
    name="Sales Strategy",
    code="SALES_STRATEGY",
    description="Strategic planning, market analysis, competitive positioning, and growth strategies",
    is_active=True,
    display_order=12,
    metadata_={
        "value_chains": ["SALES_MGMT", "STRATEGY"],
        "industries": ["ALL"],
        "focus_areas": [
            "Market Analysis & Segmentation",
            "Competitive Intelligence",
            "Strategic Planning",
            "Growth Strategy",
            "Market Positioning",
            "Strategic Partnerships",
            "Long-term Revenue Planning"
        ]
    }
)

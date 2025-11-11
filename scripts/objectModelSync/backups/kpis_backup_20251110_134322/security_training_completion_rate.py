"""
Security Training Completion Rate KPI Definition
"""

SECURITY_TRAINING_COMPLETION_RATE = {
    "code": "SECURITY_TRAINING_COMPLETION_RATE",
    "name": "Security Training Completion Rate",
    "display_name": "Security Training Completion Rate",
    "description": "The percentage of employees who have completed mandatory security training, reflecting the organization",
    "formula": "",
    "unit": "count",
    "category": "Iso 28000",
    "metadata_": {
        "modules": ["ISO_28000"],
        "required_objects": ["Employee"]
    },
    "modules": ["ISO_28000"],
    "module_code": "ISO_28000",
}

"""
SCOR Practice Object Model - REFERENCE ONLY

This is a REFERENCE/CATALOG object that describes SCOR best practices.
It does NOT create a Layer 2 table. SCOR practices are stored as metadata in Layer 1.

Represents SCOR best practices categorized by:
- Type: Technology, Process, Organizational
- Pillar: Planning, Execution, Enablement
- Classification: Emerging, Parity, Advantage

Practice Types:
- Technology: Technology-based practices (automation, systems, tools)
- Process: Process improvement practices (methodologies, workflows)
- Organizational: Organizational practices (structure, culture, governance)

Practice Pillars:
- Planning: Strategic planning and forecasting practices
- Execution: Operational execution and delivery practices
- Enablement: Enabling capabilities (IT, HR, training)

Practice Classifications:
- Emerging: Cutting-edge practices, early adoption stage
- Parity: Industry standard practices, competitive necessity
- Advantage: Best-in-class practices, competitive differentiator

Example Practices:
- "Advanced Planning Systems" (Technology, Planning, Advantage)
- "Collaborative Planning, Forecasting, and Replenishment" (Process, Planning, Parity)
- "Cross-functional Supply Chain Teams" (Organizational, Enablement, Parity)
"""

from analytics_models import ObjectModel

SCOR_PRACTICE = ObjectModel(
    name="SCOR Practice",
    code="SCOR_PRACTICE",
    description="SCOR best practices for supply chain excellence, categorized by type, pillar, and classification",

    # Table Schema - For CQRS table creation
    table_schema={
        "table_name": "scor_practice",
        "class_name": "SCOR Practice",
        "columns": [
            {
                "name": "id",
                "type": "String",
                "length": 50,
                "primary_key": True,
                "autoincrement": True
            },
            {
                "name": "name",
                "type": "String",
                "length": 200
            },
            {
                "name": "description",
                "type": "String",
                "length": 1000
            },
            {
                "name": "type",
                "type": "String",
                "length": 50
            },
            {
                "name": "pillar",
                "type": "String",
                "length": 50
            },
            {
                "name": "classification",
                "type": "String",
                "length": 50
            },
            {
                "name": "implementation_complexity",
                "type": "String",
                "length": 20
            },
            {
                "name": "expected_benefits",
                "type": "String",
                "length": 1000
            },
            {
                "name": "prerequisites",
                "type": "String",
                "length": 500
            },
            {
                "name": "created_at",
                "type": "DateTime"
            },
            {
                "name": "updated_at",
                "type": "DateTime"
            },
            {
                "name": "processes",
                "type": "List"
            },
            {
                "name": "skills",
                "type": "List"
            }
        ],
        "indexes": [
            {
                "name": "ix_scor_practice_created_at",
                "columns": ["created_at"]
            }
        ]
    },

    # UML Relationships - For documentation
    schema_definition="""
    @startuml
    SCORPractice "0..*" -- "0..*" SCORProcess : supports
    SCORPractice "0..*" -- "0..*" SCORSkill : requires
    note right of SCORPractice
@enduml
    """,

    metadata_={
        "is_reference_only": True,
        "creates_layer_2_table": False,
        "stored_in_layer_1": True,
        "implementation_note": "SCOR practices are framework references, not data records",
        "modules": ["ASCM_SCOR"],
        "practice_types": [
            "TECHNOLOGY",
            "PROCESS",
            "ORGANIZATIONAL"
        ],
        "practice_pillars": [
            "PLANNING",
            "EXECUTION",
            "ENABLEMENT"
        ],
        "practice_classifications": [
            "EMERGING",
            "PARITY",
            "ADVANTAGE"
        ],
        "implementation_complexity_levels": [
            "LOW",
            "MEDIUM",
            "HIGH"
        ],
        "example_practices": {
            "technology": [
                {
                    "name": "Advanced Planning and Scheduling (APS) Systems",
                    "pillar": "PLANNING",
                    "classification": "PARITY",
                    "complexity": "HIGH",
                    "benefits": "Optimized production schedules, reduced lead times, improved resource utilization"
                }
            ]
        }
    }
)

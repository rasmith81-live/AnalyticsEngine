"""
SCOR Process Object Model - REFERENCE ONLY

This is a REFERENCE/CATALOG object that describes the SCOR process framework.
It does NOT create a Layer 2 table. SCOR processes are stored as metadata in Layer 1.

Represents the hierarchical SCOR process structure from Level 0 (top-level framework)
to Level 4 (implementation activities).

Process Hierarchy:
- Level 0: SCOR Framework (top-level)
- Level 1: Process Types (OE, P, S, T, F, R)
- Level 2: Process Categories (e.g., P1, P2, S1, S2)
- Level 3: Process Elements (e.g., P1.1, P1.2, S1.1)
- Level 4: Implementation Activities (company-specific)

Process Types:
- OE (Orchestrate): Strategic planning and governance
- P (Plan): Demand and supply planning
- S (Source): Procurement and supplier management
- T (Transform): Manufacturing and production
- F (Fulfill): Order management and delivery
- R (Return): Returns and reverse logistics

Example Process Hierarchy:
L0: SCOR
L1: P (Plan)
L2: P1 (Plan Supply Chain)
L3: P1.1 (Identify, Prioritize, and Aggregate Supply Chain Requirements)
L4: P1.1.1 (Collect and Validate Supply Chain Data)
"""

SCOR_PROCESS = {
    "code": "SCOR_PROCESS",
    "name": "SCOR Process",
    "description": "Hierarchical SCOR process structure representing supply chain activities from strategic planning to operational execution",
    "table_schema": {"table_name": "scor_process", "class_name": "SCOR Process", "columns": [{"name": "id", "type": "String", "length": 50, "primary_key": True, "autoincrement": True}, {"name": "type", "type": "Enum"}, {"name": "level", "type": "Enum"}, {"name": "name", "type": "String", "length": 200}, {"name": "description", "type": "String", "length": 1000}, {"name": "parent_process_id", "type": "String", "length": 50}, {"name": "created_at", "type": "DateTime"}, {"name": "updated_at", "type": "DateTime"}, {"name": "parent_process", "type": "SCORProcess"}, {"name": "child_processes", "type": "List"}, {"name": "metrics", "type": "List"}, {"name": "practices", "type": "List"}], "indexes": [{"name": "ix_scor_process_created_at", "columns": ["created_at"]}]},
    "schema_definition": """
    @startuml
    SCORProcess "1" -- "0..*" SCORProcess : parent/child
    SCORProcess "0..*" -- "0..*" SCORMetric : measures
    SCORProcess "0..*" -- "0..*" SCORPractice : implements
    note right of SCORProcess
@enduml
    """,
    "metadata_": {"modules": ["ASCM_SCOR"], "is_reference_only": True, "creates_layer_2_table": False, "stored_in_layer_1": True, "implementation_note": "SCOR processes are framework references, not data records", "is_hierarchical": True, "max_depth": 5, "supports_parent_child": True, "example_processes": {"level_0": ["SCOR"], "level_1": ["OE", "P", "S", "T", "F", "R"], "level_2": {"Plan": ["P1", "P2", "P3", "P4", "P5"], "Source": ["S1", "S2", "S3"], "Transform": ["T1", "T2", "T3"], "Fulfill": ["F1", "F2", "F3"], "Return": ["R1", "R2", "R3"]}}},
}

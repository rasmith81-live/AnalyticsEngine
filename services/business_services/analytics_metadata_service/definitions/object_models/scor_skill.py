"""
SCOR Skill Object Model - REFERENCE ONLY

This is a REFERENCE/CATALOG object that describes SCOR skills and competencies.
It does NOT create a Layer 2 table. SCOR skills are stored as metadata in Layer 1.

Represents skills and competencies required for supply chain excellence and practices.
Includes competency levels from Novice (1) to Expert (5).

Competency Levels:
1. Novice: Basic awareness and understanding, requires close supervision
2. Beginner: Limited experience, can perform simple tasks with guidance
3. Competent: Practical application, works independently on routine tasks
4. Proficient: Advanced expertise, handles complex situations, mentors others
5. Expert: Recognized authority, drives innovation, thought leader

Skill Categories:
- Analytical: Data analysis, forecasting, optimization
- Technical: Systems, tools, technology proficiency
- Leadership: Team management, change leadership, strategic thinking
- Operational: Process execution, problem-solving, quality management
- Strategic: Business acumen, strategic planning, innovation

Example Skills:
- "Demand Planning" (Analytical, Level 3 required)
- "ERP Systems" (Technical, Level 3 required)
- "Supplier Relationship Management" (Leadership, Level 4 required)
- "Lean Six Sigma" (Operational, Level 3 required)
"""

SCOR_SKILL = {
    "code": "SCOR_SKILL",
    "name": "SCOR Skill",
    "description": "SCOR skills and competencies with proficiency levels required for supply chain excellence",
    "table_schema": {"table_name": "scor_skill", "class_name": "SCOR Skill", "columns": [{"name": "id", "type": "String", "length": 50, "primary_key": True, "autoincrement": True}, {"name": "code", "type": "String", "length": 50, "unique": True}, {"name": "name", "type": "String", "length": 200}, {"name": "description", "type": "String", "length": 1000}, {"name": "category", "type": "String", "length": 50}, {"name": "required_competency", "type": "Enum"}, {"name": "experience_codes", "type": "String", "length": 500}, {"name": "training_codes", "type": "String", "length": 500}, {"name": "certification_available", "type": "Boolean"}, {"name": "created_at", "type": "DateTime"}, {"name": "updated_at", "type": "DateTime"}, {"name": "practices", "type": "List"}], "indexes": [{"name": "ix_scor_skill_code", "columns": ["code"], "unique": True}, {"name": "ix_scor_skill_created_at", "columns": ["created_at"]}]},
    "schema_definition": """
    @startuml
    SCORSkill "0..*" -- "0..*" SCORPractice : supports
    note right of SCORSkill
@enduml
    """,
    "metadata_": {"is_reference_only": True, "creates_layer_2_table": False, "stored_in_layer_1": True, "implementation_note": "SCOR skills are framework references, not data records", "modules": ["ASCM_SCOR"], "competency_levels": {"1": {"name": "Novice", "description": "Basic awareness and understanding", "characteristics": ["Limited or no experience", "Requires close supervision", "Follows prescribed procedures", "Learning fundamental concepts"], "typical_role": "Entry-level, trainee"}}},
}

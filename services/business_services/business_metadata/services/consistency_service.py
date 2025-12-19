"""Service for validating metadata consistency and integrity."""

import re
import logging
from typing import Dict, List, Any, Set, Tuple

from ..repositories import MetadataQueryRepository

logger = logging.getLogger(__name__)

class ConsistencyService:
    """Checks referential integrity and consistency of the ontology."""

    def __init__(self, query_repo: MetadataQueryRepository):
        self.query_repo = query_repo

    async def check_integrity(self) -> Dict[str, List[str]]:
        """Run a full integrity check on the metadata graph.
        
        Checks:
        1. Relationship validity (endpoints exist)
        2. Metric requirements (required_objects exist)
        3. Formula validity (referenced attributes exist)
        """
        errors = {
            "relationships": [],
            "metrics": [],
            "formulas": []
        }
        
        # 1. Fetch all definitions
        try:
            entities_raw = await self.query_repo.get_all_by_kind("entity_definition")
            metrics_raw = await self.query_repo.get_all_by_kind("metric_definition")
            relationships_raw = await self.query_repo.get_all_by_kind("relationship_definition")
            
            # Extract codes/data
            entities = {e['data']['code']: e['data'] for e in entities_raw}
            metrics = {m['data']['code']: m['data'] for m in metrics_raw}
            relationships = [r['data'] for r in relationships_raw]
            
        except Exception as e:
            logger.error(f"Failed to fetch definitions for integrity check: {e}")
            return {"error": [str(e)]}

        # 2. Check Relationships
        for rel in relationships:
            rel_id = rel.get('id', 'unknown')
            from_ent = rel.get('from_entity')
            to_ent = rel.get('to_entity')
            
            if from_ent and from_ent not in entities:
                errors["relationships"].append(f"Relationship {rel_id}: Source entity '{from_ent}' not found")
            
            if to_ent and to_ent not in entities:
                errors["relationships"].append(f"Relationship {rel_id}: Target entity '{to_ent}' not found")

        # 3. Prepare Entity Schema Map for Formula Checking
        entity_attributes = {}
        for code, data in entities.items():
            schema = data.get('table_schema', {})
            # Handle both object and dict access depending on how it's stored
            if isinstance(schema, dict):
                columns = schema.get('columns', [])
            else:
                columns = [] # Should not happen if data is dict
                
            attrs = set()
            for col in columns:
                if isinstance(col, dict):
                    attrs.add(col.get('name'))
            
            entity_attributes[code] = attrs

        # 4. Check Metrics
        for code, data in metrics.items():
            # Check required_objects
            req_objects = data.get('required_objects', [])
            for obj in req_objects:
                if obj not in entities:
                    errors["metrics"].append(f"Metric '{code}': Required object '{obj}' not found")

            # Check Formula
            formula = data.get('formula')
            if formula:
                # Find "Entity.Attribute" patterns
                # Regex: Word.Word (where Word is alphanumeric + underscore)
                refs = re.findall(r'\b([A-Za-z0-9_]+)\.([A-Za-z0-9_]+)\b', formula)
                
                for ent_code, attr_name in refs:
                    # Skip numeric values (e.g. 1.5) - \b boundary check helps but 1.5 matches [0-9]+.[0-9]+
                    # If ent_code is purely numeric, skip
                    if ent_code.isdigit():
                        continue
                        
                    if ent_code in entities:
                        if attr_name not in entity_attributes[ent_code]:
                            errors["formulas"].append(f"Metric '{code}': Formula references unknown attribute '{ent_code}.{attr_name}'")
                    else:
                        # If it's not a known entity, it might be an issue OR a table alias
                        # But in our strict ontology, it should reference entities.
                        # We can be strict here.
                        errors["formulas"].append(f"Metric '{code}': Formula references unknown entity '{ent_code}'")

        return errors

    async def generate_plantuml(self) -> str:
        """Generate PlantUML diagram of the current ontology."""
        try:
            entities_raw = await self.query_repo.get_all_by_kind("entity_definition")
            relationships_raw = await self.query_repo.get_all_by_kind("relationship_definition")
            
            entities = {e['data']['code']: e['data'] for e in entities_raw}
            relationships = [r['data'] for r in relationships_raw]
            
        except Exception as e:
            logger.error(f"Failed to fetch definitions for UML generation: {e}")
            return f"' Error: {str(e)}"
            
        uml = ["@startuml", "skinparam linetype ortho", "hide empty members"]
        
        # Add Entities
        for code, data in entities.items():
            name = data.get('name', code)
            # Clean code for PlantUML (remove spaces/special chars if any)
            safe_code = re.sub(r'[^a-zA-Z0-9_]', '_', code)
            
            uml.append(f"class \"{code}\" as {safe_code} << {name} >> {{")
            
            # Attributes
            schema = data.get('table_schema', {})
            if isinstance(schema, dict):
                columns = schema.get('columns', [])
                for col in columns:
                    if isinstance(col, dict):
                        col_name = col.get('name')
                        col_type = col.get('type')
                        uml.append(f"  {col_name} : {col_type}")
            uml.append("}")
            
        # Add Relationships
        for rel in relationships:
            from_ent = rel.get('from_entity')
            to_ent = rel.get('to_entity')
            rel_type = rel.get('relationship_type')
            
            if from_ent in entities and to_ent in entities:
                safe_from = re.sub(r'[^a-zA-Z0-9_]', '_', from_ent)
                safe_to = re.sub(r'[^a-zA-Z0-9_]', '_', to_ent)
                
                # Try to interpret cardinality
                from_card = rel.get('from_cardinality', '')
                to_card = rel.get('to_cardinality', '')
                
                label = rel_type
                if from_card or to_card:
                    label += f"\\n({from_card}..{to_card})"
                
                uml.append(f"{safe_from} --> {safe_to} : {label}")
                
        uml.append("@enduml")
        
        return "\n".join(uml)

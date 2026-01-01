"""
Decomposition Orchestrator
Coordinates the multi-stage KPI decomposition pipeline.
"""

from typing import Dict, List, Any, Optional
import logging
import httpx
from .entity_extractor import EntityExtractor
from .semantic_mapping import KPIDecomposer

logger = logging.getLogger(__name__)


class DecompositionOrchestrator:
    """
    Orchestrates the KPI decomposition pipeline:
    1. Entity extraction from descriptions
    2. Value chain inference
    3. Module assignment
    4. Formula decomposition
    5. Ontology synchronization
    """
    
    def __init__(
        self,
        business_metadata_url: str = "http://business_metadata:8000",
        entity_resolution_url: str = "http://entity_resolution_service:8000"
    ):
        """
        Initialize the orchestrator.
        
        Args:
            business_metadata_url: URL of Business Metadata Service
            entity_resolution_url: URL of Entity Resolution Service
        """
        self.business_metadata_url = business_metadata_url
        self.entity_resolution_url = entity_resolution_url
        self.entity_extractor = EntityExtractor(entity_resolution_url)
        self.kpi_decomposer = KPIDecomposer(entity_resolution_url)
    
    async def decompose_kpi(self, kpi_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run full decomposition pipeline on a single KPI.
        
        Args:
            kpi_data: KPI dictionary with name, description, formula, etc.
            
        Returns:
            Enriched KPI data with extracted metadata
        """
        try:
            # 1. Extract entities from description and formula
            entities = self.entity_extractor.extract_entities(kpi_data)
            logger.info(f"Extracted entities for KPI '{kpi_data.get('name')}': {entities}")
            
            # 2. Infer value chain (domain is now the value chain code from BMS)
            value_chain_code = self.entity_extractor.infer_domain(kpi_data) or "general_business"
            logger.info(f"Inferred value chain: '{value_chain_code}'")
            
            # 3. Infer module
            module_code = self.entity_extractor.infer_module(kpi_data)
            logger.info(f"Inferred module: {module_code}")
            
            # 4. Decompose formula (if present) into set_based_definition
            formula_entities = []
            normalized_formula = None
            set_based_definition = None
            calculation_type = "simple"  # Default to simple
            
            if kpi_data.get("formula"):
                try:
                    decomposed = await self.kpi_decomposer.decompose_formula(kpi_data["formula"])
                    formula_entities = decomposed.get("identified_attributes", [])
                    normalized_formula = decomposed.get("normalized_formula")
                    
                    # Check if this is a set-based calculation
                    set_based_definition = decomposed.get("set_based_definition")
                    if set_based_definition:
                        calculation_type = "set_based"
                        logger.info(f"Formula decomposed to set_based_definition with {len(set_based_definition.get('steps', []))} steps")
                    else:
                        # Legacy: simple formula
                        logger.info(f"Formula decomposition found: entities={formula_entities}")
                    
                    if normalized_formula != kpi_data["formula"]:
                        logger.info(f"Formula normalized: '{kpi_data['formula']}' -> '{normalized_formula}'")
                except Exception as e:
                    logger.warning(f"Formula decomposition failed: {e}")
            
            # 5. Enrich KPI data with extracted metadata
            enriched_kpi = kpi_data.copy()
            
            # Store normalized formula (time-agnostic version)
            if normalized_formula:
                enriched_kpi["formula"] = normalized_formula
            
            # Store calculation type and set_based_definition
            enriched_kpi["calculation_type"] = calculation_type
            if set_based_definition:
                enriched_kpi["set_based_definition"] = set_based_definition
            
            # Update required_objects - use formula entities (all nouns from formula)
            enriched_kpi["required_objects"] = formula_entities if formula_entities else []
            
            # NOTE: We do NOT embed module references in KPIs - relationships handle this
            # Add decomposition metadata (import-time info only, not math_expression)
            if "metadata" not in enriched_kpi:
                enriched_kpi["metadata"] = {}
            
            enriched_kpi["metadata"]["decomposition"] = {
                "value_chain": value_chain_code,
                "module": module_code,
                "extracted_entities": entities,
                "formula_entities": formula_entities,
                "extraction_method": "spacy",
                "original_formula": kpi_data.get("formula") if normalized_formula else None
            }
            
            return enriched_kpi
            
        except Exception as e:
            logger.error(f"Decomposition failed for KPI '{kpi_data.get('name')}': {e}", exc_info=True)
            # Return original KPI data on failure
            return kpi_data
    
    async def decompose_batch(self, kpis: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Run decomposition on a batch of KPIs.
        Uses batch entity extraction (single LLM call) for efficiency.
        
        Args:
            kpis: List of KPI dictionaries
            
        Returns:
            List of enriched KPI dictionaries
        """
        if not kpis:
            return []
        
        # Step 1: Batch extract entities from all KPIs in ONE LLM call
        kpi_texts = []
        for kpi in kpis:
            text_parts = [
                str(kpi.get("name", "") or ""),
                str(kpi.get("description", "") or ""),
                str(kpi.get("formula", "") or "")
            ]
            kpi_texts.append(" ".join(filter(None, text_parts)))
        
        batch_entities = await self._batch_extract_entities(kpi_texts)
        logger.info(f"Batch extracted {len(batch_entities)} distinct entities for {len(kpis)} KPIs")
        
        # Step 2: Decompose each KPI (entity extraction now skipped, uses batch result)
        enriched_kpis = []
        for kpi in kpis:
            enriched_kpi = await self._decompose_kpi_with_entities(kpi, batch_entities)
            enriched_kpis.append(enriched_kpi)
        
        return enriched_kpis
    
    async def _batch_extract_entities(self, kpi_texts: List[str]) -> List[str]:
        """Extract entities from all KPIs in a single LLM call."""
        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(
                    f"{self.entity_resolution_url}/api/v1/entity-resolution/semantic/extract-batch",
                    json={"kpi_texts": kpi_texts}
                )
                response.raise_for_status()
                result = response.json()
                return result.get("entities", [])
        except Exception as e:
            logger.warning(f"Batch entity extraction failed: {e}")
            return []
    
    async def _decompose_kpi_with_entities(self, kpi_data: Dict[str, Any], batch_entities: List[str]) -> Dict[str, Any]:
        """Decompose a single KPI using pre-extracted batch entities."""
        try:
            # Use batch entities instead of individual extraction
            entities = batch_entities
            
            # Infer value chain
            value_chain_code = self.entity_extractor.infer_domain(kpi_data) or "general_business"
            logger.info(f"Inferred value chain for '{kpi_data.get('name')}': '{value_chain_code}'")
            
            # Infer module
            module_code = self.entity_extractor.infer_module(kpi_data)
            
            # Decompose formula (if present)
            formula_entities = []
            normalized_formula = None
            if kpi_data.get("formula"):
                try:
                    decomposed = await self.kpi_decomposer.decompose_formula(kpi_data["formula"])
                    formula_entities = decomposed.get("identified_attributes", [])
                    normalized_formula = decomposed.get("normalized_formula")
                except Exception as e:
                    logger.warning(f"Formula decomposition failed: {e}")
            
            # Enrich KPI data
            enriched_kpi = kpi_data.copy()
            enriched_kpi.setdefault("metadata", {})
            enriched_kpi["metadata"]["decomposition"] = {
                "value_chain": value_chain_code,
                "module": module_code,
                "extracted_entities": entities,
                "formula_entities": formula_entities,
                "original_formula": kpi_data.get("formula") if normalized_formula else None
            }
            
            return enriched_kpi
            
        except Exception as e:
            logger.error(f"Decomposition failed for KPI '{kpi_data.get('name')}': {e}")
            return kpi_data
    
    async def sync_ontology(self, enriched_kpis: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Synchronize discovered ontology objects with Business Metadata Service.
        Creates value chains, modules, and entities as needed.
        
        Args:
            enriched_kpis: List of KPIs with decomposition metadata
            
        Returns:
            Summary of created/updated ontology objects
        """
        summary = {
            "value_chains_created": [],
            "modules_created": [],
            "entities_created": [],
            "relationships_created": [],
            "errors": []
        }
        
        try:
            # Collect unique value chains and modules
            value_chains = set()
            modules = {}  # module_code -> {value_chain, kpis}
            entities = set()
            
            for kpi in enriched_kpis:
                # Try multiple sources for value chain and module data
                # 1. First check nested decomposition structure
                decomp = kpi.get("metadata", {}).get("decomposition", {})
                
                # 2. Fall back to top-level fields
                # Use category as value chain if decomposition.value_chain is not present
                vc = decomp.get("value_chain") or kpi.get("category")
                if vc:
                    # Normalize the value chain code
                    vc_code = str(vc).lower().replace(" ", "_").replace("-", "_")
                    value_chains.add(vc_code)
                
                # Use modules array from top-level if decomposition.module is not present
                kpi_modules = decomp.get("module")
                if kpi_modules:
                    kpi_modules = [kpi_modules] if isinstance(kpi_modules, str) else kpi_modules
                else:
                    kpi_modules = kpi.get("modules", [])
                    if isinstance(kpi_modules, str):
                        kpi_modules = [kpi_modules]
                
                for module_name in kpi_modules:
                    if module_name:
                        # Normalize the module code
                        module_code = str(module_name).lower().replace(" ", "_").replace("-", "_")
                        if module_code not in modules:
                            modules[module_code] = {
                                "value_chain": vc_code if vc else None,
                                "kpis": []
                            }
                        modules[module_code]["kpis"].append(kpi.get("code"))
                
                # Extract entities from decomposition metadata
                decomp_entities = decomp.get("extracted_entities", [])
                if decomp_entities:
                    entities.update(decomp_entities)
                # Include formula_entities (nouns extracted from formula)
                formula_entities = decomp.get("formula_entities", [])
                if formula_entities:
                    entities.update(formula_entities)
                # Also include required_objects if present (same as formula_entities but at top level)
                required_objs = kpi.get("required_objects", [])
                if required_objs:
                    entities.update(required_objs)
                    logger.debug(f"KPI '{kpi.get('code')}' has required_objects: {required_objs}")
            
            # Create value chain definitions
            for vc_code in value_chains:
                try:
                    await self._create_value_chain(vc_code)
                    summary["value_chains_created"].append(vc_code)
                except Exception as e:
                    logger.warning(f"Failed to create value chain '{vc_code}': {e}")
                    summary["errors"].append(f"Value chain {vc_code}: {str(e)}")
            
            # Create module definitions and module->value_chain relationships
            for module_code, module_data in modules.items():
                try:
                    await self._create_module(
                        module_code,
                        module_data["value_chain"],
                        module_data["kpis"]
                    )
                    summary["modules_created"].append(module_code)
                    
                    # Create module -> value_chain relationship
                    if module_data["value_chain"]:
                        await self._create_relationship(
                            from_code=module_code,
                            to_code=module_data["value_chain"],
                            relationship_type="belongs_to_value_chain"
                        )
                        summary["relationships_created"].append(f"{module_code} -> {module_data['value_chain']}")
                except Exception as e:
                    logger.warning(f"Failed to create module '{module_code}': {e}")
                    summary["errors"].append(f"Module {module_code}: {str(e)}")
            
            # Create entity definitions
            logger.info(f"Collected {len(entities)} unique entities to create: {list(entities)[:10]}...")
            for entity_code in entities:
                try:
                    await self._create_entity(entity_code)
                    summary["entities_created"].append(entity_code)
                    logger.info(f"Created entity: {entity_code}")
                except Exception as e:
                    logger.warning(f"Failed to create entity '{entity_code}': {e}")
                    summary["errors"].append(f"Entity {entity_code}: {str(e)}")
            
            # Create relationships between KPIs and ontology objects
            # Hierarchy: ValueChain <- Module <- KPI -> Entity
            # - Module belongs_to_value_chain ValueChain (already created above)
            # - KPI belongs_to_module Module
            # - KPI uses Entity
            # NOTE: KPIs do NOT directly relate to ValueChains - they relate via Modules
            logger.info(f"Creating relationships for {len(enriched_kpis)} KPIs...")
            for kpi in enriched_kpis:
                kpi_code = kpi.get("code")
                decomp = kpi.get("metadata", {}).get("decomposition", {})
                
                # KPI -> Module relationships (use modules array as fallback)
                kpi_modules = decomp.get("module")
                if kpi_modules:
                    kpi_modules = [kpi_modules] if isinstance(kpi_modules, str) else kpi_modules
                else:
                    kpi_modules = kpi.get("modules", [])
                    if isinstance(kpi_modules, str):
                        kpi_modules = [kpi_modules]
                
                for module_name in kpi_modules:
                    if module_name:
                        module_code = str(module_name).lower().replace(" ", "_").replace("-", "_")
                        try:
                            await self._create_relationship(
                                from_code=kpi_code,
                                to_code=module_code,
                                relationship_type="belongs_to_module"
                            )
                            summary["relationships_created"].append(f"{kpi_code} -[belongs_to_module]-> {module_code}")
                        except Exception as e:
                            logger.warning(f"Failed to create KPI->Module relationship: {e}")
                
                # KPI -> Entity relationships (uses)
                # Get entities from required_objects (formula entities) and decomposition
                kpi_entities = set()
                
                # From required_objects (top-level, extracted from formula)
                required_objs = kpi.get("required_objects", [])
                if required_objs:
                    kpi_entities.update(required_objs)
                
                # From decomposition metadata
                formula_entities = decomp.get("formula_entities", [])
                if formula_entities:
                    kpi_entities.update(formula_entities)
                
                extracted_entities = decomp.get("extracted_entities", [])
                if extracted_entities:
                    kpi_entities.update(extracted_entities)
                
                for entity_name in kpi_entities:
                    if entity_name:
                        entity_code = str(entity_name).lower().replace(" ", "_").replace("-", "_")
                        try:
                            await self._create_relationship(
                                from_code=kpi_code,
                                to_code=entity_code,
                                relationship_type="uses"
                            )
                            summary["relationships_created"].append(f"{kpi_code} -[uses]-> {entity_code}")
                        except Exception as e:
                            logger.warning(f"Failed to create KPI->Entity relationship: {e}")
            
            logger.info(f"Ontology sync complete. Value chains: {list(value_chains)}, Modules: {list(modules.keys())}, Relationships: {len(summary['relationships_created'])}")
            
        except Exception as e:
            logger.error(f"Ontology sync failed: {e}", exc_info=True)
            summary["errors"].append(f"Sync error: {str(e)}")
        
        return summary
    
    async def _create_value_chain(self, code: str) -> None:
        """Create a value chain definition in Business Metadata Service."""
        # Generate display name from code
        display_name = code.replace("_", " ").title()
        
        definition = {
            "kind": "value_chain_pattern_definition",
            "code": code,
            "name": display_name,
            "description": f"Auto-generated value chain for {display_name}",
            "domain": "industry",
            "metadata_": {
                "auto_generated": True,
                "source": "excel_import_decomposition"
            }
        }
        
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{self.business_metadata_url}/api/v1/metadata/definitions",
                json=definition,
                params={"created_by": "system"}
            )
            response.raise_for_status()
    
    async def _create_module(self, code: str, value_chain: str, kpis: List[str]) -> None:
        """Create a module definition in Business Metadata Service.
        
        NOTE: We do NOT embed value_chain or kpis in module - relationships handle this.
        """
        # Generate display name from code
        display_name = code.replace("_", " ").title()
        
        definition = {
            "kind": "business_process_definition",
            "code": code,
            "name": display_name,
            "description": f"Auto-generated module for {display_name}",
            "process_type": "support",  # Required field: core, support, or management
            "metadata_": {
                "auto_generated": True,
                "source": "excel_import_decomposition"
            }
        }
        
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{self.business_metadata_url}/api/v1/metadata/definitions",
                json=definition,
                params={"created_by": "system"}
            )
            response.raise_for_status()
    
    async def _create_entity(self, code: str) -> None:
        """Create an entity definition in Business Metadata Service."""
        # Generate display name from code
        display_name = code.replace("_", " ").title()
        
        definition = {
            "kind": "entity_definition",
            "code": code,
            "name": display_name,
            "description": f"Auto-generated entity for {display_name}",
            "table_schema": {
                "table_name": code.lower(),
                "columns": [
                    {
                        "name": "id",
                        "data_type": "UUID",
                        "is_primary_key": True
                    },
                    {
                        "name": "created_at",
                        "data_type": "TIMESTAMP"
                    }
                ]
            },
            "metadata_": {
                "auto_generated": True,
                "source": "excel_import_decomposition"
            }
        }
        
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{self.business_metadata_url}/api/v1/metadata/definitions",
                json=definition,
                params={"created_by": "system"}
            )
            response.raise_for_status()
    
    async def _create_relationship(
        self, 
        from_code: str, 
        to_code: str, 
        relationship_type: str
    ) -> None:
        """Create a relationship between two entities in Business Metadata Service."""
        relationship = {
            "from_entity_code": from_code,
            "to_entity_code": to_code,
            "relationship_type": relationship_type,
            "metadata_": {
                "auto_generated": True,
                "source": "excel_import_decomposition"
            }
        }
        
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                f"{self.business_metadata_url}/api/v1/metadata/relationships",
                json=relationship,
                params={"created_by": "system"}
            )
            response.raise_for_status()
    
    async def sync_edited_ontology(self, edited_ontology: Dict[str, Any], user: str = "system") -> Dict[str, Any]:
        """
        Synchronize user-edited ontology items with Business Metadata Service.
        Called when user has manually added/edited value chains, modules, or entities on the Ontology tab.
        
        Args:
            edited_ontology: Dictionary with keys: value_chains, modules, entities, relationships
            user: User performing the sync
            
        Returns:
            Summary of created ontology objects
        """
        summary = {
            "value_chains_created": [],
            "modules_created": [],
            "entities_created": [],
            "relationships_processed": [],
            "errors": []
        }
        
        try:
            # Create value chains
            for vc_name in edited_ontology.get("value_chains", []):
                vc_code = str(vc_name).lower().replace(" ", "_").replace("-", "_")
                try:
                    await self._create_value_chain(vc_code)
                    summary["value_chains_created"].append(vc_code)
                    logger.info(f"Created value chain: {vc_code}")
                except httpx.HTTPStatusError as e:
                    if e.response.status_code == 409:  # Already exists
                        logger.info(f"Value chain '{vc_code}' already exists, skipping")
                    else:
                        logger.warning(f"Failed to create value chain '{vc_code}': {e}")
                        summary["errors"].append(f"Value chain {vc_code}: {str(e)}")
                except Exception as e:
                    logger.warning(f"Failed to create value chain '{vc_code}': {e}")
                    summary["errors"].append(f"Value chain {vc_code}: {str(e)}")
            
            # Create modules
            for mod_name in edited_ontology.get("modules", []):
                mod_code = str(mod_name).lower().replace(" ", "_").replace("-", "_")
                try:
                    await self._create_module(mod_code, None, [])
                    summary["modules_created"].append(mod_code)
                    logger.info(f"Created module: {mod_code}")
                except httpx.HTTPStatusError as e:
                    if e.response.status_code == 409:  # Already exists
                        logger.info(f"Module '{mod_code}' already exists, skipping")
                    else:
                        logger.warning(f"Failed to create module '{mod_code}': {e}")
                        summary["errors"].append(f"Module {mod_code}: {str(e)}")
                except Exception as e:
                    logger.warning(f"Failed to create module '{mod_code}': {e}")
                    summary["errors"].append(f"Module {mod_code}: {str(e)}")
            
            # Create entities
            for entity_name in edited_ontology.get("entities", []):
                entity_code = str(entity_name).lower().replace(" ", "_").replace("-", "_")
                try:
                    await self._create_entity(entity_code)
                    summary["entities_created"].append(entity_code)
                    logger.info(f"Created entity: {entity_code}")
                except httpx.HTTPStatusError as e:
                    if e.response.status_code == 409:  # Already exists
                        logger.info(f"Entity '{entity_code}' already exists, skipping")
                    else:
                        logger.warning(f"Failed to create entity '{entity_code}': {e}")
                        summary["errors"].append(f"Entity {entity_code}: {str(e)}")
                except Exception as e:
                    logger.warning(f"Failed to create entity '{entity_code}': {e}")
                    summary["errors"].append(f"Entity {entity_code}: {str(e)}")
            
            # Process relationships (format: "FROM_CODE -> TO_CODE")
            # Hierarchy: ValueChain <- Module <- KPI -> Entity
            # - Module -> VC = belongs_to_value_chain
            # - Module -> KPI = contains (module contains KPIs)
            # - KPI -> Entity = uses
            # Normalize for comparison: lowercase for VC/Module/Entity names (which have spaces)
            # But preserve original case for codes that are already formatted (like KPI codes which are UPPERCASE)
            vc_codes_lower = set(str(vc).lower().replace(" ", "_").replace("-", "_") for vc in edited_ontology.get("value_chains", []))
            mod_codes_lower = set(str(mod).lower().replace(" ", "_").replace("-", "_") for mod in edited_ontology.get("modules", []))
            entity_codes_lower = set(str(e).lower().replace(" ", "_").replace("-", "_") for e in edited_ontology.get("entities", []))
            
            for rel in edited_ontology.get("relationships", []):
                try:
                    parts = rel.split(" -> ")
                    if len(parts) == 2:
                        from_code = parts[0].strip()
                        to_code = parts[1].strip()
                        
                        # Normalize to lowercase with underscores for both comparison and storage
                        # This matches how all entities are stored in the database
                        from_code_normalized = from_code.lower().replace(" ", "_").replace("-", "_")
                        to_code_normalized = to_code.lower().replace(" ", "_").replace("-", "_")
                        
                        # Determine relationship type based on source and target
                        if from_code_normalized in mod_codes_lower and to_code_normalized in vc_codes_lower:
                            # Module -> ValueChain
                            rel_type = "belongs_to_value_chain"
                        elif from_code_normalized in mod_codes_lower:
                            # Module -> KPI (module contains KPIs)
                            rel_type = "contains"
                        elif to_code_normalized in entity_codes_lower or (to_code_normalized not in vc_codes_lower and to_code_normalized not in mod_codes_lower):
                            # KPI -> Entity
                            rel_type = "uses"
                        else:
                            rel_type = "uses"  # Default
                        
                        try:
                            await self._create_relationship(
                                from_code=from_code_normalized,
                                to_code=to_code_normalized,
                                relationship_type=rel_type
                            )
                            summary["relationships_processed"].append(f"{from_code_normalized} -[{rel_type}]-> {to_code_normalized}")
                            logger.info(f"Created relationship: {from_code_normalized} -[{rel_type}]-> {to_code_normalized}")
                        except httpx.HTTPStatusError as e:
                            if e.response.status_code == 409:  # Already exists
                                logger.info(f"Relationship '{from_code} -> {to_code}' already exists, skipping")
                            else:
                                logger.warning(f"Failed to create relationship '{rel}': {e}")
                                summary["errors"].append(f"Relationship {rel}: {str(e)}")
                except Exception as e:
                    logger.warning(f"Failed to parse relationship '{rel}': {e}")
            
            logger.info(f"Edited ontology sync complete: {summary}")
            
        except Exception as e:
            logger.error(f"Edited ontology sync failed: {e}", exc_info=True)
            summary["errors"].append(f"Sync error: {str(e)}")
        
        return summary
        

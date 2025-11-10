"""
Definition Loader - Loads KPI, Object Model, Module, and Value Chain definitions
"""

import os
import importlib.util
from typing import Dict, List, Any, Optional
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class DefinitionLoader:
    """Loads definitions from Python files in the definitions directory."""
    
    def __init__(self, definitions_path: str = None):
        """
        Initialize definition loader.
        
        Args:
            definitions_path: Path to definitions directory
        """
        if definitions_path is None:
            # Default to definitions/ in same directory as this file
            current_dir = Path(__file__).parent
            definitions_path = current_dir / "definitions"
        
        self.definitions_path = Path(definitions_path)
        self._cache: Dict[str, Dict[str, Any]] = {
            "kpis": {},
            "object_models": {},
            "modules": {},
            "value_chains": {},
            "industries": {},
            "benchmarks": {},
            "attributes": {}
        }
        self._loaded = False
    
    def load_all(self):
        """Load all definitions into cache."""
        if self._loaded:
            return
        
        logger.info("Loading all definitions...")
        
        self._load_kpis()
        self._load_object_models()
        self._load_modules()
        self._load_value_chains()
        self._load_industries()
        self._load_benchmarks()
        self._load_attributes()
        
        self._loaded = True
        logger.info(f"Loaded {len(self._cache['kpis'])} KPIs")
        logger.info(f"Loaded {len(self._cache['object_models'])} object models")
        logger.info(f"Loaded {len(self._cache['modules'])} modules")
        logger.info(f"Loaded {len(self._cache['value_chains'])} value chains")
    
    def _load_kpis(self):
        """Load all KPI definitions."""
        kpis_path = self.definitions_path / "kpis"
        if not kpis_path.exists():
            logger.warning(f"KPIs directory not found: {kpis_path}")
            return
        
        for file_path in kpis_path.glob("*.py"):
            if file_path.name.startswith("_"):
                continue
            
            try:
                kpi_def = self._load_definition_from_file(file_path)
                if kpi_def and isinstance(kpi_def, dict):
                    kpi_code = kpi_def.get("code")
                    if kpi_code:
                        self._cache["kpis"][kpi_code] = kpi_def
            except Exception as e:
                logger.error(f"Error loading KPI from {file_path}: {e}")
    
    def _load_object_models(self):
        """Load all object model definitions."""
        models_path = self.definitions_path / "object_models"
        if not models_path.exists():
            logger.warning(f"Object models directory not found: {models_path}")
            return
        
        for file_path in models_path.glob("*.py"):
            if file_path.name.startswith("_"):
                continue
            
            try:
                model_def = self._load_definition_from_file(file_path)
                if model_def and isinstance(model_def, dict):
                    model_code = model_def.get("code") or model_def.get("name")
                    if model_code:
                        self._cache["object_models"][model_code] = model_def
            except Exception as e:
                logger.error(f"Error loading object model from {file_path}: {e}")
    
    def _load_modules(self):
        """Load all module definitions."""
        modules_path = self.definitions_path / "modules"
        if not modules_path.exists():
            logger.warning(f"Modules directory not found: {modules_path}")
            return
        
        for file_path in modules_path.glob("*.py"):
            if file_path.name.startswith("_"):
                continue
            
            try:
                module_def = self._load_definition_from_file(file_path)
                if module_def and isinstance(module_def, dict):
                    module_code = module_def.get("code")
                    if module_code:
                        self._cache["modules"][module_code] = module_def
            except Exception as e:
                logger.error(f"Error loading module from {file_path}: {e}")
    
    def _load_value_chains(self):
        """Load all value chain definitions."""
        vc_path = self.definitions_path / "value_chains"
        if not vc_path.exists():
            logger.warning(f"Value chains directory not found: {vc_path}")
            return
        
        for file_path in vc_path.glob("*.py"):
            if file_path.name.startswith("_"):
                continue
            
            try:
                vc_def = self._load_definition_from_file(file_path)
                if vc_def and isinstance(vc_def, dict):
                    vc_code = vc_def.get("code")
                    if vc_code:
                        self._cache["value_chains"][vc_code] = vc_def
            except Exception as e:
                logger.error(f"Error loading value chain from {file_path}: {e}")
    
    def _load_industries(self):
        """Load all industry definitions."""
        industries_path = self.definitions_path / "industries"
        if not industries_path.exists():
            return
        
        for file_path in industries_path.glob("*.py"):
            if file_path.name.startswith("_"):
                continue
            
            try:
                industry_def = self._load_definition_from_file(file_path)
                if industry_def and isinstance(industry_def, dict):
                    industry_code = industry_def.get("code")
                    if industry_code:
                        self._cache["industries"][industry_code] = industry_def
            except Exception as e:
                logger.error(f"Error loading industry from {file_path}: {e}")
    
    def _load_benchmarks(self):
        """Load all benchmark definitions."""
        benchmarks_path = self.definitions_path / "benchmarks"
        if not benchmarks_path.exists():
            return
        
        for file_path in benchmarks_path.glob("*.py"):
            if file_path.name.startswith("_"):
                continue
            
            try:
                benchmark_def = self._load_definition_from_file(file_path)
                if benchmark_def and isinstance(benchmark_def, dict):
                    benchmark_code = benchmark_def.get("code")
                    if benchmark_code:
                        self._cache["benchmarks"][benchmark_code] = benchmark_def
            except Exception as e:
                logger.error(f"Error loading benchmark from {file_path}: {e}")
    
    def _load_attributes(self):
        """Load all attribute definitions."""
        attributes_path = self.definitions_path / "attributes"
        if not attributes_path.exists():
            return
        
        for file_path in attributes_path.glob("*.py"):
            if file_path.name.startswith("_"):
                continue
            
            try:
                attr_def = self._load_definition_from_file(file_path)
                if attr_def and isinstance(attr_def, dict):
                    attr_code = attr_def.get("code")
                    if attr_code:
                        self._cache["attributes"][attr_code] = attr_def
            except Exception as e:
                logger.error(f"Error loading attribute from {file_path}: {e}")
    
    def _load_definition_from_file(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """
        Load definition from a Python file.
        
        Looks for a module-level variable (usually uppercase) that contains
        the definition dictionary.
        
        Args:
            file_path: Path to Python file
            
        Returns:
            Definition dictionary or None
        """
        spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
        if not spec or not spec.loader:
            return None
        
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Look for uppercase variables (convention for definitions)
        for name in dir(module):
            if name.isupper() and not name.startswith("_"):
                value = getattr(module, name)
                if isinstance(value, dict):
                    return value
        
        return None
    
    # ========================================================================
    # Public API
    # ========================================================================
    
    def get_kpi(self, kpi_code: str) -> Optional[Dict[str, Any]]:
        """Get KPI definition by code."""
        if not self._loaded:
            self.load_all()
        return self._cache["kpis"].get(kpi_code)
    
    def get_all_kpis(self) -> Dict[str, Dict[str, Any]]:
        """Get all KPI definitions."""
        if not self._loaded:
            self.load_all()
        return self._cache["kpis"]
    
    def get_object_model(self, model_code: str) -> Optional[Dict[str, Any]]:
        """Get object model definition by code."""
        if not self._loaded:
            self.load_all()
        return self._cache["object_models"].get(model_code)
    
    def get_all_object_models(self) -> Dict[str, Dict[str, Any]]:
        """Get all object model definitions."""
        if not self._loaded:
            self.load_all()
        return self._cache["object_models"]
    
    def get_module(self, module_code: str) -> Optional[Dict[str, Any]]:
        """Get module definition by code."""
        if not self._loaded:
            self.load_all()
        return self._cache["modules"].get(module_code)
    
    def get_all_modules(self) -> Dict[str, Dict[str, Any]]:
        """Get all module definitions."""
        if not self._loaded:
            self.load_all()
        return self._cache["modules"]
    
    def get_value_chain(self, vc_code: str) -> Optional[Dict[str, Any]]:
        """Get value chain definition by code."""
        if not self._loaded:
            self.load_all()
        return self._cache["value_chains"].get(vc_code)
    
    def get_all_value_chains(self) -> Dict[str, Dict[str, Any]]:
        """Get all value chain definitions."""
        if not self._loaded:
            self.load_all()
        return self._cache["value_chains"]
    
    def get_industry(self, industry_code: str) -> Optional[Dict[str, Any]]:
        """Get industry definition by code."""
        if not self._loaded:
            self.load_all()
        return self._cache["industries"].get(industry_code)
    
    def get_all_industries(self) -> Dict[str, Dict[str, Any]]:
        """Get all industry definitions."""
        if not self._loaded:
            self.load_all()
        return self._cache["industries"]
    
    def search_kpis(
        self,
        module_code: Optional[str] = None,
        value_chain_code: Optional[str] = None,
        industry_code: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Search KPIs by filters.
        
        Args:
            module_code: Filter by module
            value_chain_code: Filter by value chain
            industry_code: Filter by industry
            
        Returns:
            List of matching KPI definitions
        """
        if not self._loaded:
            self.load_all()
        
        results = []
        for kpi in self._cache["kpis"].values():
            metadata = kpi.get("metadata_", {})
            
            # Filter by module
            if module_code:
                modules = metadata.get("modules", [])
                if module_code not in modules:
                    continue
            
            # Filter by value chain
            if value_chain_code:
                value_chains = metadata.get("value_chains", [])
                if value_chain_code not in value_chains:
                    continue
            
            # Filter by industry
            if industry_code:
                industries = metadata.get("industries", [])
                if industry_code not in industries:
                    continue
            
            results.append(kpi)
        
        return results
    
    def get_stats(self) -> Dict[str, int]:
        """Get statistics about loaded definitions."""
        if not self._loaded:
            self.load_all()
        
        return {
            "kpis": len(self._cache["kpis"]),
            "object_models": len(self._cache["object_models"]),
            "modules": len(self._cache["modules"]),
            "value_chains": len(self._cache["value_chains"]),
            "industries": len(self._cache["industries"]),
            "benchmarks": len(self._cache["benchmarks"]),
            "attributes": len(self._cache["attributes"])
        }


# Global loader instance
_loader: Optional[DefinitionLoader] = None


def get_loader() -> DefinitionLoader:
    """Get global definition loader instance."""
    global _loader
    if _loader is None:
        _loader = DefinitionLoader()
    return _loader

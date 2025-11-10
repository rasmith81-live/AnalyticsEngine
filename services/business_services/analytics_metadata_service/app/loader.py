"""
Definition Loader - Loads KPI, Object Model, Module, and Value Chain definitions
"""

import os
import sys
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
            # Default to definitions/ in parent directory (service root)
            current_dir = Path(__file__).parent
            definitions_path = current_dir.parent / "definitions"
        
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
    
    def _parse_definition_file(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """
        Parse a Python definition file as text to extract the definition.
        Used as fallback when imports fail.
        
        Args:
            file_path: Path to Python file
            
        Returns:
            Definition dictionary or None
        """
        try:
            import ast
            
            content = file_path.read_text()
            
            # Parse the Python file as AST
            tree = ast.parse(content)
            
            # Find the assignment statement
            for node in ast.walk(tree):
                if isinstance(node, ast.Assign):
                    # Check if it's a call to Module, ValueChain, etc.
                    if isinstance(node.value, ast.Call):
                        if isinstance(node.value.func, ast.Name):
                            if node.value.func.id in ['Module', 'ValueChain', 'Industry', 'ObjectModel']:
                                # Extract keyword arguments
                                definition = {}
                                for keyword in node.value.keywords:
                                    key = keyword.arg
                                    try:
                                        # Try to evaluate the value
                                        value = ast.literal_eval(keyword.value)
                                        definition[key] = value
                                    except:
                                        # If it can't be evaluated, skip it
                                        pass
                                
                                # Extract fields from metadata_ if present
                                if 'metadata_' in definition and isinstance(definition['metadata_'], dict):
                                    metadata = definition['metadata_']
                                    # For modules: extract value_chains
                                    if 'value_chains' in metadata:
                                        definition['value_chains'] = metadata['value_chains']
                                    # For KPIs: extract modules and set module_code
                                    if 'modules' in metadata:
                                        definition['modules'] = metadata['modules']
                                        # Set module_code to first module
                                        if metadata['modules']:
                                            definition['module_code'] = metadata['modules'][0]
                                
                                return definition if definition else None
            
        except Exception as e:
            logger.error(f"Error parsing {file_path}: {e}")
        
        return None
    
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
        # Add parent directory to sys.path to enable relative imports
        parent_dir = str(file_path.parent)
        if parent_dir not in sys.path:
            sys.path.insert(0, parent_dir)
        
        try:
            spec = importlib.util.spec_from_file_location(file_path.stem, file_path)
            if not spec or not spec.loader:
                return None
            
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
        except ImportError as e:
            # If import fails due to missing analytics_models, try to parse the file directly
            logger.warning(f"Import error for {file_path}, attempting direct parsing: {e}")
            return self._parse_definition_file(file_path)
        except Exception as e:
            logger.error(f"Error loading {file_path}: {e}")
            return None
        finally:
            # Remove from sys.path after loading
            if parent_dir in sys.path:
                sys.path.remove(parent_dir)
        
        # Look for uppercase variables (convention for definitions)
        for name in dir(module):
            if name.isupper() and not name.startswith("_"):
                value = getattr(module, name)
                if isinstance(value, dict):
                    return value
        
        # If no uppercase dict found, look for class instances with to_dict method
        for name in dir(module):
            if not name.startswith("_"):
                value = getattr(module, name)
                # Check if it's a class (not an instance)
                if isinstance(value, type):
                    try:
                        # Try to instantiate and convert to dict
                        instance = value()
                        if hasattr(instance, 'to_dict'):
                            return instance.to_dict()
                    except:
                        pass
                # Check if it's an object instance (old analytics_models format)
                elif hasattr(value, '__dict__') and not callable(value):
                    try:
                        # Try to convert object to dict
                        if hasattr(value, 'to_dict'):
                            return value.to_dict()
                        elif hasattr(value, '__dict__'):
                            # Extract attributes from object
                            obj_dict = {}
                            for attr_name in dir(value):
                                if not attr_name.startswith('_') and not callable(getattr(value, attr_name)):
                                    obj_dict[attr_name] = getattr(value, attr_name)
                            # Ensure we have at least a code field
                            if 'code' in obj_dict or 'name' in obj_dict:
                                return obj_dict
                    except:
                        pass
        
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

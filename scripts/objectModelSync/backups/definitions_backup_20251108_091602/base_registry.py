"""
Base registry class for auto-discovering and registering entities.
"""

import importlib
import inspect
from pathlib import Path
from typing import Dict, List, Type, Any, Optional


class BaseRegistry:
    """
    Base class for entity registries.
    
    Automatically discovers and imports entity definitions from individual files.
    """
    
    def __init__(self, entity_class: Type, module_path: str, file_pattern: str = "*.py"):
        """
        Initialize registry.
        
        Args:
            entity_class: The class type to register (e.g., Industry, ValueChain)
            module_path: Python module path (e.g., 'definitions.industries')
            file_pattern: Pattern for files to import (default: *.py)
        """
        self.entity_class = entity_class
        self.module_path = module_path
        self.file_pattern = file_pattern
        self._registry: Dict[str, Any] = {}
        self._discover_and_register()
    
    def _discover_and_register(self):
        """Discover and register all entities from individual files."""
        try:
            # Get the directory path
            module = importlib.import_module(self.module_path)
            module_dir = Path(module.__file__).parent
            
            # Find all Python files (except __init__ and registry)
            for file_path in module_dir.glob(self.file_pattern):
                if file_path.stem in ['__init__', 'registry', 'base_registry']:
                    continue
                
                # Import the module
                module_name = f"{self.module_path}.{file_path.stem}"
                try:
                    imported_module = importlib.import_module(module_name)
                    
                    # Find all instances of entity_class in the module
                    for name, obj in inspect.getmembers(imported_module):
                        if isinstance(obj, self.entity_class):
                            # Register by code
                            if hasattr(obj, 'code'):
                                self._registry[obj.code] = obj
                                
                except Exception as e:
                    print(f"Warning: Could not import {module_name}: {e}")
                    
        except Exception as e:
            print(f"Warning: Could not initialize registry for {self.module_path}: {e}")
    
    def get(self, code: str) -> Optional[Any]:
        """Get entity by code."""
        return self._registry.get(code)
    
    def get_all(self) -> List[Any]:
        """Get all registered entities."""
        return list(self._registry.values())
    
    def get_by_name(self, name: str) -> Optional[Any]:
        """Get entity by name."""
        for entity in self._registry.values():
            if hasattr(entity, 'name') and entity.name == name:
                return entity
        return None
    
    def list_codes(self) -> List[str]:
        """List all registered entity codes."""
        return list(self._registry.keys())
    
    def count(self) -> int:
        """Count registered entities."""
        return len(self._registry)
    
    def __contains__(self, code: str) -> bool:
        """Check if code is registered."""
        return code in self._registry
    
    def __getitem__(self, code: str) -> Any:
        """Get entity by code using bracket notation."""
        return self._registry[code]
    
    def __iter__(self):
        """Iterate over all entities."""
        return iter(self._registry.values())
    
    def __len__(self) -> int:
        """Return count of registered entities."""
        return len(self._registry)

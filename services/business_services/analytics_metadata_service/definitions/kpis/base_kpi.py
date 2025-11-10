"""
Base KPI Class - Compatible with dictionary-based loader
"""

class BaseKPI:
    """Base class for KPI definitions that converts to dictionary format."""
    
    def __init__(
        self,
        code: str,
        name_: str,
        description_: str,
        category_: str = None,
        modules_: list = None,
        required_objects: list = None,
        formula_: str = None,
        unit_: str = None,
        data_type_: str = "decimal",
        aggregation_methods: list = None,
        time_periods: list = None,
        dimensions_: list = None,
        benchmarks_: dict = None,
        metadata_: dict = None,
        **kwargs
    ):
        """
        Initialize KPI definition.
        
        Args:
            code: Unique KPI code (e.g., "SUPPLIER_LEAD_TIME")
            name_: Display name
            description_: KPI description
            category_: Category (optional)
            modules_: List of module codes this KPI belongs to
            required_objects: List of required object model codes
            formula_: Calculation formula
            unit_: Unit of measurement (e.g., "days", "dollars", "percent")
            data_type_: Data type (decimal, integer, boolean, etc.)
            aggregation_methods: List of aggregation methods (average, sum, min, max, count)
            time_periods: List of time periods (daily, weekly, monthly, etc.)
            dimensions_: List of dimension codes
            benchmarks_: Dictionary of benchmark values
            metadata_: Additional metadata
        """
        self.code = code
        self.name = name_
        self.display_name = name_  # Use name as display_name
        self.description = description_
        self.category = category_
        self.modules = modules_ or []
        self.required_objects = required_objects or []
        self.formula = formula_
        self.unit = unit_
        self.data_type = data_type_
        self.aggregation_methods = aggregation_methods or ["average"]
        self.time_periods = time_periods or ["daily", "weekly", "monthly"]
        self.dimensions = dimensions_ or []
        self.benchmarks = benchmarks_ or {}
        self.metadata_ = metadata_ or {}
        
        # Store module_code (first module in list)
        self.module_code = modules_[0] if modules_ else None
        
        # Store any additional kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def to_dict(self):
        """Convert to dictionary format for loader."""
        return {
            "code": self.code,
            "name": self.name,
            "display_name": self.display_name,
            "description": self.description,
            "category": self.category,
            "modules": self.modules,
            "module_code": self.module_code,
            "required_objects": self.required_objects,
            "formula": self.formula,
            "unit": self.unit,
            "data_type": self.data_type,
            "aggregation_methods": self.aggregation_methods,
            "time_periods": self.time_periods,
            "dimensions": self.dimensions,
            "benchmarks": self.benchmarks,
            "metadata_": self.metadata_
        }


# Auto-convert: When a KPI file is loaded, create the instance and export as uppercase dict
def create_kpi_definition(kpi_class):
    """Helper to create KPI definition from class instance."""
    instance = kpi_class()
    return instance.to_dict()

# Generic Calculation Engine Architecture

## Overview

The Calculation Engine is a **generic, reusable abstraction layer** that sits between the API Gateway and domain-specific calculation services (SCOR, CRM, Sales, etc.).

## Architecture Layers

```
┌─────────────────────────────────────────────────────────────┐
│ API Gateway (8090)                                          │
│ └─ Routes calculation requests                              │
└─────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────┐
│ Calculation Engine Service (8020)                           │
│ ├─ Generic calculation orchestration                        │
│ ├─ KPI routing and aggregation                             │
│ ├─ Caching layer                                            │
│ ├─ Result aggregation                                       │
│ └─ Abstract base classes                                    │
└─────────────────────────────────────────────────────────────┘
                           ↓
        ┌──────────────────┼──────────────────┐
        ↓                  ↓                   ↓
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ SCOR Handler │  │ CRM Handler  │  │ Sales Handler│
│ (inherits)   │  │ (inherits)   │  │ (inherits)   │
│              │  │              │  │              │
│ Implements:  │  │ Implements:  │  │ Implements:  │
│ - calculate()│  │ - calculate()│  │ - calculate()│
│ - validate() │  │ - validate() │  │ - validate() │
│ - cache_key()│  │ - cache_key()│  │ - cache_key()│
└──────────────┘  └──────────────┘  └──────────────┘
        ↓                  ↓                   ↓
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ scor_data    │  │ crm_data     │  │ sales_data   │
└──────────────┘  └──────────────┘  └──────────────┘
```

## Core Components

### 1. Base Calculation Handler (Abstract)
```python
class BaseCalculationHandler(ABC):
    """Abstract base for all value chain calculation handlers."""
    
    @abstractmethod
    async def calculate(self, kpi_code: str, params: dict) -> CalculationResult:
        """Calculate KPI value."""
        pass
    
    @abstractmethod
    async def validate_params(self, kpi_code: str, params: dict) -> bool:
        """Validate calculation parameters."""
        pass
    
    @abstractmethod
    def get_cache_key(self, kpi_code: str, params: dict) -> str:
        """Generate cache key."""
        pass
```

### 2. Calculation Engine Orchestrator
- Routes requests to appropriate handler
- Manages caching
- Aggregates multi-KPI requests
- Handles parallel execution

### 3. Value Chain Handlers
- SCOR Handler (heavy calculations)
- CRM Handler (light calculations)
- Sales Handler (medium calculations)
- Each inherits from BaseCalculationHandler

## Benefits

✅ **Single Responsibility** - Each handler focuses on domain logic
✅ **Reusability** - Common patterns in base class
✅ **Scalability** - Handlers can be scaled independently
✅ **Maintainability** - Changes to one handler don't affect others
✅ **Testability** - Mock handlers for testing

## Implementation

See `/services/business_services/calculation_engine/` for full implementation.

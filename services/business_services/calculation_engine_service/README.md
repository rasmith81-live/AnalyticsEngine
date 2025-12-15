# Generic Calculation Engine Architecture

## Overview

The Calculation Engine is a **generic, reusable abstraction layer** that sits between the API Gateway and the data layer. It dynamically executes KPI calculations based on metadata definitions using a `DynamicCalculationHandler`.

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
│ ├─ KPI routing and aggregation                              │
│ ├─ Caching layer                                            │
│ ├─ Result aggregation                                       │
│ └─ Abstract base classes                                    │
└─────────────────────────────────────────────────────────────┘
                           ↓
        ┌──────────────────┼──────────────────┐
        ↓                  ↓                  ↓
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ Dynamic Handler │  │ Dynamic Handler │  │ Dynamic Handler │
│ (Supply Chain)  │  │ (Finance)       │  │ (Sales)         │
│                 │  │                 │  │                 │
│ Implements:     │  │ Implements:     │  │ Implements:     │
│ - calculate()   │  │ - calculate()   │  │ - calculate()   │
│ - validate()    │  │ - validate()    │  │ - validate()    │
│ - cache_key()   │  │ - cache_key()   │  │ - cache_key()   │
└─────────────────┘  └─────────────────┘  └─────────────────┘
        ↓                  ↓                  ↓
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│ Generic Schema  │  │ Generic Schema  │  │ Generic Schema  │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

## Core Components

### 1. Base Calculation Handler (Abstract)
```python
class BaseCalculationHandler(ABC):
    """Abstract base class for calculation handlers."""
    
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

### 3. Dynamic Calculation Handler
- Fetches KPI definitions from Metadata Service
- Parses formulas into AST
- Generates optimized SQL using `TimescaleManager` and `SQLGenerator`
- Executes queries against generic schemas

## Benefits

✅ **Single Responsibility** - Engine focuses on execution, not business logic
✅ **Reusability** - One handler class supports infinite KPIs
✅ **Scalability** - Handlers can be scaled independently
✅ **Maintainability** - Changes to formulas happen in metadata, not code
✅ **Testability** - Mock metadata for testing

## Implementation

See `/services/business_services/calculation_engine/` for full implementation.

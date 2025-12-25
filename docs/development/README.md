# Development Guide - Analytics Engine

**Standards, practices, and guidelines for developers**

---

## Table of Contents

1. [Development Setup](#development-setup)
2. [Coding Standards](#coding-standards)
3. [Testing Guidelines](#testing-guidelines)
4. [Git Workflow](#git-workflow)
5. [Code Review Process](#code-review-process)
6. [Debugging](#debugging)
7. [Contributing](#contributing)

---

## Development Setup

### Local Environment

**Prerequisites**:
- Python 3.11+
- Docker Desktop
- VS Code or PyCharm
- Git

**Setup Steps**:

```powershell
# 1. Clone repository
git clone https://github.com/your-org/AnalyticsEngine.git
cd AnalyticsEngine

# 2. Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 4. Install pre-commit hooks
pre-commit install

# 5. Configure environment
cp .env.example .env
# Edit .env with your settings

# 6. Start infrastructure
docker-compose up -d timescaledb redis

# 7. Run migrations
$env:DATABASE_URL="postgresql+asyncpg://multiservice_user:multiservice_password@localhost:5432/multiservice_db"
alembic upgrade head
```

### IDE Configuration

#### **VS Code**

**Recommended Extensions**:
- Python (Microsoft)
- Pylance
- Docker
- GitLens
- REST Client
- YAML

**Settings** (`.vscode/settings.json`):
```json
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": false,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "python.testing.pytestEnabled": true,
  "editor.formatOnSave": true,
  "editor.rulers": [88],
  "[python]": {
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  }
}
```

#### **PyCharm**

**Configuration**:
1. Set Python interpreter to virtual environment
2. Enable Black formatter
3. Configure pytest as test runner
4. Enable type checking with MyPy
5. Configure Docker integration

---

## Coding Standards

### Python Style Guide

**Follow PEP 8** with these specifics:

**Line Length**: 88 characters (Black default)

**Imports**:
```python
# Standard library
import os
from datetime import datetime

# Third-party
from fastapi import FastAPI, Depends
from pydantic import BaseModel

# Local
from app.services import MyService
from app.models import MyModel
```

**Type Hints**:
```python
# Always use type hints
def calculate_kpi(
    data: List[Dict[str, Any]],
    timeframe: str,
    filters: Optional[Dict[str, str]] = None
) -> Dict[str, float]:
    """Calculate KPI with proper type hints."""
    pass
```

**Docstrings**:
```python
def process_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Process raw data for analysis.
    
    Args:
        data: Raw data DataFrame with columns [id, value, timestamp]
        
    Returns:
        Processed DataFrame with cleaned and transformed data
        
    Raises:
        ValueError: If data is empty or missing required columns
    """
    pass
```

### Pydantic Models

**Use Pydantic v2 Style**:
```python
from pydantic import BaseModel, Field, ConfigDict

class KPIRequest(BaseModel):
    """Request model for KPI calculation."""
    
    model_config = ConfigDict(str_strip_whitespace=True)
    
    kpi_id: str = Field(..., description="KPI identifier")
    timeframe: str = Field(..., pattern="^(daily|weekly|monthly)$")
    filters: dict[str, Any] = Field(default_factory=dict)
```

### FastAPI Endpoints

**Standard Structure**:
```python
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List

router = APIRouter(prefix="/api/v1/kpis", tags=["KPIs"])

@router.get("/{kpi_id}", response_model=KPIResponse)
async def get_kpi(
    kpi_id: str,
    service: KPIService = Depends(get_kpi_service)
) -> KPIResponse:
    """
    Get KPI by ID.
    
    Args:
        kpi_id: KPI identifier
        service: Injected KPI service
        
    Returns:
        KPI details
        
    Raises:
        HTTPException: 404 if KPI not found
    """
    kpi = await service.get_kpi(kpi_id)
    if not kpi:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"KPI {kpi_id} not found"
        )
    return kpi
```

### Error Handling

**Consistent Error Responses**:
```python
from fastapi import HTTPException, status

# Not found
raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Resource not found"
)

# Validation error
raise HTTPException(
    status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    detail="Invalid input data"
)

# Internal error
raise HTTPException(
    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="Internal server error"
)
```

### Logging

**Standard Logging**:
```python
import logging

logger = logging.getLogger(__name__)

# Log levels
logger.debug("Detailed diagnostic information")
logger.info("General informational message")
logger.warning("Warning message")
logger.error("Error message", exc_info=True)
logger.critical("Critical error")

# Structured logging
logger.info(
    "KPI calculated",
    extra={
        "kpi_id": kpi_id,
        "timeframe": timeframe,
        "duration_ms": duration
    }
)
```

---

## Testing Guidelines

### Test Structure

**Directory Layout**:
```
tests/
├── unit/                  ← Unit tests
│   ├── test_services.py
│   └── test_models.py
├── integration/           ← Integration tests
│   ├── test_api.py
│   └── test_database.py
├── e2e/                   ← End-to-end tests
│   └── test_workflows.py
├── conftest.py           ← Pytest fixtures
└── __init__.py
```

### Unit Tests

**Example**:
```python
import pytest
from app.services import KPICalculator

def test_kpi_calculator_basic():
    """Test basic KPI calculation."""
    calculator = KPICalculator()
    result = calculator.calculate(
        data=[{"value": 100}, {"value": 200}],
        formula="SUM(value)"
    )
    assert result == 300

def test_kpi_calculator_empty_data():
    """Test KPI calculation with empty data."""
    calculator = KPICalculator()
    with pytest.raises(ValueError, match="Data cannot be empty"):
        calculator.calculate(data=[], formula="SUM(value)")
```

### Integration Tests

**Example**:
```python
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_get_kpi_endpoint():
    """Test GET /api/v1/kpis/{kpi_id} endpoint."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/api/v1/kpis/test-kpi-1")
        assert response.status_code == 200
        data = response.json()
        assert data["kpi_id"] == "test-kpi-1"
```

### Test Fixtures

**Common Fixtures** (`conftest.py`):
```python
import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

@pytest.fixture
async def db_session():
    """Provide database session for tests."""
    engine = create_async_engine("sqlite+aiosqlite:///:memory:")
    async with AsyncSession(engine) as session:
        yield session

@pytest.fixture
def sample_kpi_data():
    """Provide sample KPI data."""
    return {
        "kpi_id": "test-kpi-1",
        "name": "Test KPI",
        "formula": "SUM(value)",
        "timeframe": "daily"
    }
```

### Running Tests

**Commands**:
```powershell
# Run all tests
pytest

# Run specific test file
pytest tests/unit/test_services.py

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test
pytest tests/unit/test_services.py::test_kpi_calculator_basic

# Run with verbose output
pytest -v

# Run and stop on first failure
pytest -x
```

### Test Coverage

**Minimum Coverage**: 80%

**Check Coverage**:
```powershell
pytest --cov=app --cov-report=term-missing
```

---

## Git Workflow

### Branch Strategy

**Branch Types**:
- `main` - Production-ready code
- `develop` - Integration branch
- `feature/*` - New features
- `bugfix/*` - Bug fixes
- `hotfix/*` - Production hotfixes

**Branch Naming**:
```
feature/add-kpi-calculation
bugfix/fix-database-connection
hotfix/security-patch
```

### Commit Messages

**Format**:
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting
- `refactor`: Code restructuring
- `test`: Tests
- `chore`: Maintenance

**Examples**:
```
feat(kpi): add new KPI calculation endpoint

Implement POST /api/v1/kpis/calculate endpoint for on-demand
KPI calculations with caching support.

Closes #123
```

```
fix(database): resolve connection pool exhaustion

Increase connection pool size and add connection recycling
to prevent pool exhaustion under high load.

Fixes #456
```

### Pull Request Process

**PR Checklist**:
- [ ] Code follows style guidelines
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] All tests passing
- [ ] Code reviewed
- [ ] No merge conflicts

**PR Template**:
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added
- [ ] Integration tests added
- [ ] Manual testing completed

## Checklist
- [ ] Code follows style guide
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] Tests passing
```

---

## Code Review Process

### Review Checklist

**Code Quality**:
- [ ] Follows coding standards
- [ ] Proper error handling
- [ ] Appropriate logging
- [ ] Type hints used
- [ ] Docstrings present

**Testing**:
- [ ] Tests cover new code
- [ ] Tests are meaningful
- [ ] Edge cases covered
- [ ] Tests pass

**Architecture**:
- [ ] Follows CQRS pattern
- [ ] Service boundaries respected
- [ ] Dependencies injected
- [ ] No circular dependencies

**Security**:
- [ ] No hardcoded secrets
- [ ] Input validation
- [ ] SQL injection prevention
- [ ] Authentication/authorization

### Review Comments

**Constructive Feedback**:
```
✅ Good: "Consider using a list comprehension here for better performance"
❌ Bad: "This code is terrible"

✅ Good: "This could cause a race condition. Consider using a lock"
❌ Bad: "This won't work"
```

---

## Debugging

### Local Debugging

**VS Code Launch Configuration** (`.vscode/launch.json`):
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "FastAPI",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": [
        "app.main:app",
        "--reload",
        "--port",
        "8000"
      ],
      "jinja": true,
      "env": {
        "DATABASE_URL": "postgresql+asyncpg://user:pass@localhost:5432/db"
      }
    }
  ]
}
```

### Docker Debugging

**Attach to Running Container**:
```powershell
# Execute bash in container
docker-compose exec business_metadata bash

# View logs
docker-compose logs -f business_metadata

# Check environment
docker-compose exec business_metadata env
```

### Database Debugging

**Query Analysis**:
```sql
-- Enable query logging
ALTER SYSTEM SET log_statement = 'all';
SELECT pg_reload_conf();

-- View slow queries
SELECT query, calls, total_time, mean_time
FROM pg_stat_statements
ORDER BY mean_time DESC
LIMIT 10;

-- Check active queries
SELECT pid, query, state, query_start
FROM pg_stat_activity
WHERE state != 'idle';
```

---

## Contributing

### Getting Started

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Update documentation
6. Submit pull request

### Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Help others learn and grow

### Documentation

**Update Documentation When**:
- Adding new features
- Changing APIs
- Modifying architecture
- Fixing bugs (if relevant)

---

## Related Documentation

- **[Getting Started](../getting-started/README.md)** - Setup guide
- **[Architecture](../architecture/README.md)** - System architecture
- **[Testing Guide](./testing.md)** - Detailed testing guide
- **[API Documentation](../api/README.md)** - API reference

---

**Next**: [Testing Guide](./testing.md) | [API Documentation](../api/README.md)


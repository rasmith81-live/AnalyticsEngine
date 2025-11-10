# Client Authorization & Access Control Guide

## Overview

The Client Authorization system implements **multi-tenancy** and **role-based access control (RBAC)** with fine-grained permissions at multiple levels:

- **Client Level**: Controls which modules are visible
- **Role Level**: Defines permissions within a client
- **ObjectModel Level**: Controls access to specific object models
- **Object Level**: Controls access to specific objects with row-level security
- **KPI Level**: Controls which KPIs are visible
- **Attribute Level**: Controls field-level access with data masking

---

## Architecture

```
Client (Tenant/Organization)
  │
  ├── ClientModulePermission (Which modules client can access)
  │    └── Only explicitly listed modules are available
  │
  └── ClientRole (Roles within the client)
       │
       ├── RoleObjectModelPermission (Which object models role can access)
       ├── RoleObjectPermission (Which objects role can access)
       │    └── row_filter: Row-level security filters
       ├── RoleKPIPermission (Which KPIs role can view)
       └── RoleAttributePermission (Which attributes role can view)
            └── is_masked: Field-level data masking
```

---

## Models

### 1. Client

**Purpose**: Represents a tenant/organization with access to specific modules

**Key Fields**:
- `name`, `code` - Client identification
- `is_active` - Whether client is active
- `config` - Client-specific configuration
- `contact_email`, `contact_phone` - Contact information

**Relationships**:
- One-to-many with `ClientRole`
- One-to-many with `ClientModulePermission`

**Access Control**:
- Only modules explicitly listed in `ClientModulePermission` are available
- All other modules are hidden from the client

### 2. ClientRole

**Purpose**: Defines roles within a client organization

**Key Fields**:
- `client_id` - Parent client
- `name`, `code` - Role identification
- `is_active` - Whether role is active
- `permissions` - Role-specific permissions (JSON)

**Relationships**:
- Many-to-one with `Client`
- One-to-many with various permission models

**Permission Types**:
- ObjectModel permissions
- Object permissions (with row-level security)
- KPI permissions
- Attribute permissions (with masking)

### 3. ClientModulePermission

**Purpose**: Controls which modules a client can access

**Key Fields**:
- `client_id`, `module_id` - Client-Module relationship
- `can_view`, `can_create`, `can_update`, `can_delete` - CRUD permissions
- `config` - Module-specific configuration

**Behavior**:
- **Whitelist approach**: Only explicitly listed modules are accessible
- Modules not listed are completely hidden from the client

### 4. RoleObjectModelPermission

**Purpose**: Controls which object models a role can access

**Key Fields**:
- `role_id`, `object_model_id` - Role-ObjectModel relationship
- `can_view`, `can_create`, `can_update`, `can_delete` - CRUD permissions
- `config` - ObjectModel-specific configuration

### 5. RoleObjectPermission

**Purpose**: Controls access to specific objects with row-level security

**Key Fields**:
- `role_id`, `object_id` - Role-Object relationship
- `can_view`, `can_update`, `can_delete` - CUD permissions
- `row_filter` - Row-level security filter (JSON)
- `config` - Object-specific configuration

**Row-Level Security**:
```json
{
  "attribute_filters": {
    "REGION": {"eq": "US-WEST"},
    "CUSTOMER_TYPE": {"in": ["enterprise", "wholesale"]},
    "REVENUE": {"gte": 10000}
  }
}
```

### 6. RoleKPIPermission

**Purpose**: Controls which KPIs a role can view

**Key Fields**:
- `role_id`, `kpi_id` - Role-KPI relationship
- `can_view`, `can_update` - View/Update permissions
- `config` - KPI-specific configuration

### 7. RoleAttributePermission

**Purpose**: Controls attribute-level access with data masking

**Key Fields**:
- `role_id`, `attribute_id` - Role-Attribute relationship
- `can_view`, `can_update` - View/Update permissions
- `is_masked` - Whether to mask the attribute value
- `mask_type` - Masking type: `partial`, `full`, `hash`, `encrypt`
- `config` - Attribute-specific configuration

**Masking Types**:
- **partial**: Show only part of the value (e.g., "John D***")
- **full**: Completely hide the value (e.g., "***")
- **hash**: Show hashed value (e.g., "a3f2b9...")
- **encrypt**: Show encrypted value

---

## Usage Examples

### Example 1: Create Client with Module Access

```python
from analytics_models import Client, ClientModulePermission, Module

# Create client
acme_corp = Client(
    name="ACME Corporation",
    code="ACME",
    description="ACME Corp - Enterprise Client",
    contact_email="admin@acme.com",
    config={
        "max_users": 100,
        "features": ["advanced_analytics", "custom_reports"]
    }
)

# Grant access to specific modules
sales_module = Module.query.filter_by(code="SALES").first()
finance_module = Module.query.filter_by(code="FINANCE").first()

# Client can only access Sales and Finance modules
sales_permission = ClientModulePermission(
    client_id=acme_corp.id,
    module_id=sales_module.id,
    can_view=True,
    can_create=True,
    can_update=True,
    can_delete=False
)

finance_permission = ClientModulePermission(
    client_id=acme_corp.id,
    module_id=finance_module.id,
    can_view=True,
    can_create=False,
    can_update=False,
    can_delete=False  # Read-only access
)

# Marketing module is NOT listed, so it's completely hidden from ACME
```

### Example 2: Create Roles with Different Permissions

```python
from analytics_models import ClientRole, RoleObjectModelPermission

# Admin role - full access
admin_role = ClientRole(
    client_id=acme_corp.id,
    name="Administrator",
    code="ADMIN",
    description="Full access to all client resources",
    permissions={
        "is_admin": True,
        "can_manage_users": True
    }
)

# Analyst role - read-only access
analyst_role = ClientRole(
    client_id=acme_corp.id,
    name="Analyst",
    code="ANALYST",
    description="Read-only access for data analysis",
    permissions={
        "is_admin": False,
        "can_export_data": True
    }
)

# Grant ObjectModel permissions
sales_txn_model = ObjectModel.query.filter_by(code="SALES_TXN").first()

# Admin can do everything
admin_om_perm = RoleObjectModelPermission(
    role_id=admin_role.id,
    object_model_id=sales_txn_model.id,
    can_view=True,
    can_create=True,
    can_update=True,
    can_delete=True
)

# Analyst can only view
analyst_om_perm = RoleObjectModelPermission(
    role_id=analyst_role.id,
    object_model_id=sales_txn_model.id,
    can_view=True,
    can_create=False,
    can_update=False,
    can_delete=False
)
```

### Example 3: Row-Level Security

```python
from analytics_models import RoleObjectPermission

# Regional Manager role - can only see their region's data
regional_mgr_role = ClientRole(
    client_id=acme_corp.id,
    name="Regional Manager - West",
    code="REGIONAL_MGR_WEST"
)

# Grant access to sales transactions with row-level filter
sales_txn_1 = Object.query.filter_by(code="TXN_001").first()

regional_perm = RoleObjectPermission(
    role_id=regional_mgr_role.id,
    object_id=sales_txn_1.id,
    can_view=True,
    can_update=True,
    can_delete=False,
    row_filter={
        "attribute_filters": {
            "REGION": {"eq": "US-WEST"},
            "CUSTOMER_TYPE": {"in": ["enterprise", "wholesale"]}
        }
    }
)

# This role can only see objects where:
# - REGION = "US-WEST"
# - CUSTOMER_TYPE in ["enterprise", "wholesale"]
```

### Example 4: Attribute-Level Security with Masking

```python
from analytics_models import RoleAttributePermission

# Customer Service role - can see customer data but sensitive fields are masked
cs_role = ClientRole(
    client_id=acme_corp.id,
    name="Customer Service",
    code="CUSTOMER_SERVICE"
)

# Allow viewing customer name (no masking)
name_attr = ObjectAttribute.query.filter_by(code="CUSTOMER_NAME").first()
name_perm = RoleAttributePermission(
    role_id=cs_role.id,
    attribute_id=name_attr.id,
    can_view=True,
    can_update=False,
    is_masked=False
)

# Mask credit card number (partial masking)
cc_attr = ObjectAttribute.query.filter_by(code="CREDIT_CARD").first()
cc_perm = RoleAttributePermission(
    role_id=cs_role.id,
    attribute_id=cc_attr.id,
    can_view=True,
    can_update=False,
    is_masked=True,
    mask_type="partial",  # Show last 4 digits only
    config={
        "mask_pattern": "****-****-****-{last4}"
    }
)

# Completely hide SSN (full masking)
ssn_attr = ObjectAttribute.query.filter_by(code="SSN").first()
ssn_perm = RoleAttributePermission(
    role_id=cs_role.id,
    attribute_id=ssn_attr.id,
    can_view=True,
    can_update=False,
    is_masked=True,
    mask_type="full",  # Show as ***-**-****
    config={
        "mask_pattern": "***-**-****"
    }
)
```

### Example 5: KPI Access Control

```python
from analytics_models import RoleKPIPermission

# Executive role - can see all KPIs
exec_role = ClientRole(
    client_id=acme_corp.id,
    name="Executive",
    code="EXECUTIVE"
)

# Sales Manager role - can only see sales-related KPIs
sales_mgr_role = ClientRole(
    client_id=acme_corp.id,
    name="Sales Manager",
    code="SALES_MGR"
)

# Grant KPI permissions
revenue_kpi = KPI.query.filter_by(code="REVENUE").first()
profit_margin_kpi = KPI.query.filter_by(code="PROFIT_MARGIN").first()
employee_cost_kpi = KPI.query.filter_by(code="EMPLOYEE_COST").first()

# Executive can see all KPIs
for kpi in [revenue_kpi, profit_margin_kpi, employee_cost_kpi]:
    RoleKPIPermission(
        role_id=exec_role.id,
        kpi_id=kpi.id,
        can_view=True,
        can_update=True
    )

# Sales Manager can only see revenue and profit margin
for kpi in [revenue_kpi, profit_margin_kpi]:
    RoleKPIPermission(
        role_id=sales_mgr_role.id,
        kpi_id=kpi.id,
        can_view=True,
        can_update=False  # Read-only
    )

# Employee cost KPI is hidden from Sales Manager
```

---

## Permission Hierarchy

### Access Control Flow

1. **Client Level**: Check if module is in `ClientModulePermission`
   - If NO → Access denied, module is hidden
   - If YES → Proceed to role level

2. **Role Level**: Check role's permissions
   - Check `RoleObjectModelPermission` for object model access
   - Check `RoleObjectPermission` for object access
   - Check `RoleKPIPermission` for KPI access
   - Check `RoleAttributePermission` for attribute access

3. **Row-Level Security**: Apply `row_filter` if defined
   - Filter objects based on attribute conditions
   - Only show matching rows

4. **Field-Level Security**: Apply masking if defined
   - Mask sensitive attributes based on `mask_type`
   - Return masked values to user

---

## Row-Level Security Filters

### Filter Syntax

```json
{
  "attribute_filters": {
    "ATTRIBUTE_CODE": {
      "operator": "value"
    }
  }
}
```

### Supported Operators

- **eq**: Equal to
  ```json
  {"REGION": {"eq": "US-WEST"}}
  ```

- **ne**: Not equal to
  ```json
  {"STATUS": {"ne": "deleted"}}
  ```

- **in**: In list
  ```json
  {"CUSTOMER_TYPE": {"in": ["enterprise", "wholesale"]}}
  ```

- **not_in**: Not in list
  ```json
  {"CATEGORY": {"not_in": ["test", "demo"]}}
  ```

- **gt**, **gte**: Greater than (or equal)
  ```json
  {"REVENUE": {"gte": 10000}}
  ```

- **lt**, **lte**: Less than (or equal)
  ```json
  {"QUANTITY": {"lte": 100}}
  ```

- **contains**: String contains
  ```json
  {"DESCRIPTION": {"contains": "premium"}}
  ```

- **startswith**: String starts with
  ```json
  {"CODE": {"startswith": "PROD-"}}
  ```

- **between**: Value between range
  ```json
  {"PRICE": {"between": [100, 500]}}
  ```

### Complex Filters

```json
{
  "attribute_filters": {
    "REGION": {"in": ["US-WEST", "US-EAST"]},
    "REVENUE": {"gte": 50000},
    "CUSTOMER_TYPE": {"eq": "enterprise"},
    "STATUS": {"ne": "cancelled"}
  },
  "logic": "AND"  // All conditions must match
}
```

---

## Data Masking

### Masking Types

#### 1. Partial Masking
Show only part of the value:
```python
# Original: "John Smith"
# Masked: "John S***"

# Original: "4532-1234-5678-9012"
# Masked: "****-****-****-9012"
```

#### 2. Full Masking
Completely hide the value:
```python
# Original: "123-45-6789"
# Masked: "***-**-****"

# Original: "john@example.com"
# Masked: "***@***.***"
```

#### 3. Hash Masking
Show hashed value:
```python
# Original: "SecretData123"
# Masked: "a3f2b9c4d5e6..."
```

#### 4. Encrypt Masking
Show encrypted value (reversible with key):
```python
# Original: "SensitiveInfo"
# Masked: "U2FsdGVkX1..."
```

---

## Query Examples

### Get Client's Available Modules

```python
def get_client_modules(client_id: int):
    """Get all modules available to a client."""
    permissions = session.query(ClientModulePermission)\
        .filter(ClientModulePermission.client_id == client_id)\
        .filter(ClientModulePermission.can_view == True)\
        .all()
    
    module_ids = [p.module_id for p in permissions]
    modules = session.query(Module)\
        .filter(Module.id.in_(module_ids))\
        .filter(Module.is_active == True)\
        .all()
    
    return modules
```

### Get Role's Accessible Object Models

```python
def get_role_object_models(role_id: int):
    """Get all object models accessible to a role."""
    permissions = session.query(RoleObjectModelPermission)\
        .filter(RoleObjectModelPermission.role_id == role_id)\
        .filter(RoleObjectModelPermission.can_view == True)\
        .all()
    
    return [p.object_model for p in permissions]
```

### Apply Row-Level Security

```python
def apply_row_filter(objects: List[Object], row_filter: dict) -> List[Object]:
    """Filter objects based on row-level security rules."""
    if not row_filter or "attribute_filters" not in row_filter:
        return objects
    
    filtered_objects = []
    for obj in objects:
        matches = True
        for attr_code, condition in row_filter["attribute_filters"].items():
            value = obj.data_values.get(attr_code)
            
            # Check condition
            for operator, expected in condition.items():
                if operator == "eq" and value != expected:
                    matches = False
                elif operator == "in" and value not in expected:
                    matches = False
                elif operator == "gte" and value < expected:
                    matches = False
                # ... other operators
        
        if matches:
            filtered_objects.append(obj)
    
    return filtered_objects
```

### Apply Attribute Masking

```python
def mask_attribute_value(value: str, mask_type: str, config: dict = None) -> str:
    """Mask an attribute value based on mask type."""
    if mask_type == "partial":
        # Show last 4 characters
        if len(value) > 4:
            return "*" * (len(value) - 4) + value[-4:]
        return value
    
    elif mask_type == "full":
        return "*" * len(value)
    
    elif mask_type == "hash":
        import hashlib
        return hashlib.sha256(value.encode()).hexdigest()[:16]
    
    elif mask_type == "encrypt":
        # Implement encryption
        pass
    
    return value
```

---

## Best Practices

### 1. Principle of Least Privilege
- Grant minimum necessary permissions
- Start with read-only access
- Escalate permissions only when needed

### 2. Module Whitelisting
- Explicitly list all modules a client can access
- Review module permissions regularly
- Remove unused module permissions

### 3. Role Design
- Create roles based on job functions
- Avoid creating too many granular roles
- Use role hierarchies when possible

### 4. Row-Level Security
- Define clear filter criteria
- Test filters thoroughly
- Document filter logic

### 5. Data Masking
- Mask sensitive data by default
- Use appropriate masking types
- Audit masked data access

### 6. Permission Auditing
- Log all permission changes
- Review permissions regularly
- Monitor access patterns

---

## Database Tables

### Tables Created

1. **clients** - Client/tenant definitions
2. **client_roles** - Roles within clients
3. **client_module_permissions** - Client-level module access
4. **role_objectmodel_permissions** - Role-level object model access
5. **role_object_permissions** - Role-level object access with row filters
6. **role_kpi_permissions** - Role-level KPI access
7. **role_attribute_permissions** - Role-level attribute access with masking

### Indexes

All permission tables have composite unique indexes on their relationship keys to prevent duplicate permissions.

---

## Conclusion

The Client Authorization system provides comprehensive multi-tenancy and role-based access control with:

- ✅ **Module-level access control** (whitelist approach)
- ✅ **Role-based permissions** (RBAC)
- ✅ **Row-level security** (data filtering)
- ✅ **Field-level security** (attribute masking)
- ✅ **Fine-grained CRUD permissions**
- ✅ **Flexible configuration** (JSON config fields)

This enables secure, scalable multi-tenant analytics with granular access control at every level.

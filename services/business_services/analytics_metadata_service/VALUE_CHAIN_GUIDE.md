# Value Chain Guide

## Overview

The **ValueChain** model provides an intermediate organizational layer between Industry and Module, representing sequences of business activities that create value. This enables more flexible and granular organization of analytics capabilities.

---

## Hierarchy Structure

### New Hierarchy

```
Industry (e.g., Retail)
  └── ValueChain (e.g., Supply Chain Management)
       └── Module (e.g., Inventory Management)
            └── ObjectModel (e.g., Product Inventory)
                 ├── Objects
                 └── KPIs
```

### Previous Hierarchy (for reference)

```
Industry
  └── Module
       └── ObjectModel
            ├── Objects
            └── KPIs
```

---

## Key Features

✅ **Many-to-Many Relationships** - Value chains can be shared across industries  
✅ **Flexible Organization** - Additional layer for organizing modules  
✅ **Client Access Control** - Clients can access specific value chains  
✅ **Industry Agnostic** - Same value chain can apply to multiple industries  

---

## Database Model

### ValueChain Model

```python
class ValueChain(Base, TimestampMixin):
    __tablename__ = "value_chains"
    
    id: Mapped[int]
    name: Mapped[str]  # e.g., "Supply Chain Management"
    code: Mapped[str]  # e.g., "SUPPLY_CHAIN"
    description: Mapped[Optional[str]]
    is_active: Mapped[bool]
    display_order: Mapped[int]
    metadata_: Mapped[Optional[dict]]
    
    # Relationships
    industries: Mapped[List["Industry"]]  # Many-to-many
    modules: Mapped[List["Module"]]       # Many-to-many
    clients: Mapped[List["Client"]]       # Many-to-many
```

### Association Tables

**industry_valuechain_association**
- Links Industries to ValueChains (many-to-many)

**valuechain_module_association**
- Links ValueChains to Modules (many-to-many)

**client_valuechain_association**
- Links Clients to ValueChains (many-to-many)

---

## Relationships

### Industry ↔ ValueChain (Many-to-Many)

An industry can have multiple value chains, and a value chain can belong to multiple industries.

```python
# Industry model
value_chains: Mapped[List["ValueChain"]] = relationship(
    "ValueChain",
    secondary=industry_valuechain_association,
    back_populates="industries"
)

# ValueChain model
industries: Mapped[List["Industry"]] = relationship(
    "Industry",
    secondary=industry_valuechain_association,
    back_populates="value_chains"
)
```

### ValueChain ↔ Module (Many-to-Many)

A value chain can contain multiple modules, and a module can belong to multiple value chains.

```python
# ValueChain model
modules: Mapped[List["Module"]] = relationship(
    "Module",
    secondary=valuechain_module_association,
    back_populates="value_chains"
)

# Module model
value_chains: Mapped[List["ValueChain"]] = relationship(
    "ValueChain",
    secondary=valuechain_module_association,
    back_populates="modules"
)
```

### Client ↔ ValueChain (Many-to-Many)

A client can access multiple value chains, and a value chain can be accessed by multiple clients.

```python
# Client model
value_chains: Mapped[List["ValueChain"]] = relationship(
    "ValueChain",
    secondary=client_valuechain_association,
    back_populates="clients"
)

# ValueChain model
clients: Mapped[List["Client"]] = relationship(
    "Client",
    secondary=client_valuechain_association,
    back_populates="value_chains"
)
```

---

## Usage Examples

### Example 1: Create Value Chains for Retail Industry

```python
from analytics_models import Industry, ValueChain, Module

# Create Retail Industry
retail = Industry(
    name="Retail",
    code="RETAIL",
    description="Retail industry analytics"
)

# Create Value Chains
supply_chain = ValueChain(
    name="Supply Chain Management",
    code="SUPPLY_CHAIN",
    description="End-to-end supply chain analytics",
    display_order=1
)

customer_experience = ValueChain(
    name="Customer Experience",
    code="CUST_EXPERIENCE",
    description="Customer journey and experience analytics",
    display_order=2
)

merchandising = ValueChain(
    name="Merchandising & Planning",
    code="MERCHANDISING",
    description="Product planning and merchandising analytics",
    display_order=3
)

# Associate value chains with industry
retail.value_chains.extend([supply_chain, customer_experience, merchandising])

# Create Modules for Supply Chain
inventory_module = Module(
    name="Inventory Management",
    code="INVENTORY",
    description="Inventory tracking and optimization"
)

logistics_module = Module(
    name="Logistics & Distribution",
    code="LOGISTICS",
    description="Logistics and distribution analytics"
)

procurement_module = Module(
    name="Procurement",
    code="PROCUREMENT",
    description="Procurement and vendor management"
)

# Associate modules with supply chain value chain
supply_chain.modules.extend([inventory_module, logistics_module, procurement_module])
```

### Example 2: Cross-Industry Value Chains

```python
# Create multiple industries
retail = Industry(name="Retail", code="RETAIL")
manufacturing = Industry(name="Manufacturing", code="MFG")
healthcare = Industry(name="Healthcare", code="HEALTH")

# Create a value chain that applies to multiple industries
supply_chain = ValueChain(
    name="Supply Chain Management",
    code="SUPPLY_CHAIN",
    description="Universal supply chain analytics"
)

# Associate with multiple industries
supply_chain.industries.extend([retail, manufacturing, healthcare])

# Each industry can now access the same supply chain value chain
```

### Example 3: Client Access to Value Chains

```python
from analytics_models import Client

# Create client
retail_client = Client(
    name="Acme Retail Corp",
    code="ACME_RETAIL",
    naics_code="452210",  # Department Stores
    country_id=usa.id,
    region_id=california.id
)

# Grant access to specific value chains
supply_chain = ValueChain.query.filter_by(code="SUPPLY_CHAIN").first()
customer_exp = ValueChain.query.filter_by(code="CUST_EXPERIENCE").first()

retail_client.value_chains.extend([supply_chain, customer_exp])

# Client now has access to:
# - Supply Chain Management value chain (and all its modules)
# - Customer Experience value chain (and all its modules)
```

### Example 4: Manufacturing Industry Value Chains

```python
# Create Manufacturing Industry
manufacturing = Industry(
    name="Manufacturing",
    code="MFG",
    description="Manufacturing industry analytics"
)

# Create Value Chains
production = ValueChain(
    name="Production Operations",
    code="PRODUCTION",
    description="Production line and operations analytics",
    display_order=1
)

quality = ValueChain(
    name="Quality Management",
    code="QUALITY",
    description="Quality control and assurance analytics",
    display_order=2
)

maintenance = ValueChain(
    name="Maintenance & Reliability",
    code="MAINTENANCE",
    description="Equipment maintenance and reliability analytics",
    display_order=3
)

# Associate with manufacturing
manufacturing.value_chains.extend([production, quality, maintenance])

# Create modules for Production value chain
production_planning = Module(
    name="Production Planning",
    code="PROD_PLAN",
    description="Production scheduling and planning"
)

shop_floor = Module(
    name="Shop Floor Management",
    code="SHOP_FLOOR",
    description="Real-time shop floor analytics"
)

production.modules.extend([production_planning, shop_floor])
```

---

## Common Value Chains by Industry

### Retail
- **Supply Chain Management** - Inventory, logistics, procurement
- **Customer Experience** - Customer journey, engagement, satisfaction
- **Merchandising & Planning** - Product planning, assortment, pricing
- **Store Operations** - Store performance, workforce, compliance
- **E-commerce** - Online sales, digital marketing, fulfillment

### Manufacturing
- **Production Operations** - Production planning, shop floor, scheduling
- **Quality Management** - Quality control, inspection, compliance
- **Maintenance & Reliability** - Preventive maintenance, asset management
- **Supply Chain** - Procurement, inventory, logistics
- **Product Development** - R&D, design, prototyping

### Financial Services
- **Risk Management** - Credit risk, market risk, operational risk
- **Customer Management** - Customer acquisition, retention, lifetime value
- **Compliance & Regulatory** - Regulatory reporting, compliance monitoring
- **Trading & Investment** - Trading operations, portfolio management
- **Operations** - Transaction processing, reconciliation

### Healthcare
- **Patient Care** - Patient outcomes, treatment effectiveness
- **Clinical Operations** - Clinical workflows, resource utilization
- **Revenue Cycle** - Billing, collections, reimbursement
- **Quality & Safety** - Patient safety, quality metrics, compliance
- **Population Health** - Population analytics, preventive care

---

## Query Examples

### Get All Value Chains for an Industry

```python
industry = session.query(Industry).filter_by(code="RETAIL").first()
value_chains = industry.value_chains
```

### Get All Modules in a Value Chain

```python
value_chain = session.query(ValueChain).filter_by(code="SUPPLY_CHAIN").first()
modules = value_chain.modules
```

### Get All Value Chains a Client Has Access To

```python
client = session.query(Client).filter_by(code="ACME_RETAIL").first()
accessible_value_chains = client.value_chains
```

### Get All Clients with Access to a Value Chain

```python
value_chain = session.query(ValueChain).filter_by(code="SUPPLY_CHAIN").first()
clients = value_chain.clients
```

### Get Industries Using a Specific Value Chain

```python
value_chain = session.query(ValueChain).filter_by(code="SUPPLY_CHAIN").first()
industries = value_chain.industries
```

---

## Pydantic Schemas

### ValueChainBase
```python
class ValueChainBase(BaseModel):
    name: str
    code: str
    description: Optional[str]
    is_active: bool = True
    display_order: int = 0
    metadata_: Optional[Dict[str, Any]]
```

### ValueChainCreate
```python
class ValueChainCreate(ValueChainBase):
    industry_ids: List[int] = []  # Industries to associate with
```

### ValueChainUpdate
```python
class ValueChainUpdate(BaseModel):
    name: Optional[str]
    code: Optional[str]
    description: Optional[str]
    is_active: Optional[bool]
    display_order: Optional[int]
    metadata_: Optional[Dict[str, Any]]
```

### ValueChainRead
```python
class ValueChainRead(ValueChainBase):
    id: int
    created_at: datetime
    updated_at: datetime
```

### ValueChainWithModules
```python
class ValueChainWithModules(ValueChainRead):
    modules: List[ModuleRead] = []
```

---

## Benefits

### For Organization
✅ **Better Structure** - Additional layer for organizing analytics  
✅ **Reusability** - Share value chains across industries  
✅ **Flexibility** - Modules can belong to multiple value chains  

### For Clients
✅ **Granular Access** - Access specific value chains instead of all modules  
✅ **Relevant Content** - Only see value chains relevant to their business  
✅ **Simplified Navigation** - Organized by business processes  

### For Administration
✅ **Easier Management** - Group related modules together  
✅ **Cross-Industry** - Same value chain for multiple industries  
✅ **Scalability** - Add new value chains without restructuring  

---

## Migration from Old Structure

### Old Structure
```
Industry → Module → ObjectModel
```

### New Structure
```
Industry → ValueChain → Module → ObjectModel
```

### Migration Steps

1. **Create Value Chains** - Define value chains for each industry
2. **Associate Modules** - Link existing modules to value chains
3. **Update Client Access** - Migrate client module permissions to value chain access
4. **Update Queries** - Update application queries to use new hierarchy

---

## API Endpoints (Suggested)

```
# Value Chains
GET    /value-chains                    - List all value chains
POST   /value-chains                    - Create value chain
GET    /value-chains/{id}               - Get value chain
PUT    /value-chains/{id}               - Update value chain
DELETE /value-chains/{id}               - Delete value chain

# Value Chain Relationships
GET    /value-chains/{id}/industries    - Get industries for value chain
POST   /value-chains/{id}/industries    - Add industry to value chain
DELETE /value-chains/{id}/industries/{industry_id}  - Remove industry

GET    /value-chains/{id}/modules       - Get modules in value chain
POST   /value-chains/{id}/modules       - Add module to value chain
DELETE /value-chains/{id}/modules/{module_id}  - Remove module

GET    /value-chains/{id}/clients       - Get clients with access
POST   /value-chains/{id}/clients       - Grant client access
DELETE /value-chains/{id}/clients/{client_id}  - Revoke client access

# Industry Value Chains
GET    /industries/{id}/value-chains    - Get value chains for industry

# Client Value Chains
GET    /clients/{id}/value-chains       - Get value chains client can access
POST   /clients/{id}/value-chains       - Grant access to value chain
DELETE /clients/{id}/value-chains/{vc_id}  - Revoke access
```

---

## Best Practices

### 1. **Meaningful Names**
Use clear, business-oriented names for value chains that reflect actual business processes.

### 2. **Logical Grouping**
Group related modules together in value chains based on business function.

### 3. **Reuse When Possible**
If a value chain applies to multiple industries, share it rather than duplicating.

### 4. **Display Order**
Use display_order to control how value chains appear in UI.

### 5. **Client Access**
Grant clients access to value chains, not individual modules, for easier management.

---

## Conclusion

The ValueChain model provides a flexible intermediate layer between Industry and Module, enabling better organization, reusability, and client access control for analytics capabilities.

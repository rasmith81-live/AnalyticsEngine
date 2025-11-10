# UML Class Diagram Schema Guide (Entity-Level)

## Overview

The `schema_definition` field in the **ObjectModel** uses UML (Unified Modeling Language) class diagram notation to represent **entity-level classes and their relationships ONLY**. 

**Important:** Attributes and methods are **NOT** defined in the UML schema. They are defined separately using the **ObjectAttribute** model, which provides flexibility, reusability, and dynamic schema management.

---

## Design Philosophy

### Entity-Level Only

The UML schema defines:
✅ **Classes** - Entity names and stereotypes  
✅ **Relationships** - How entities relate to each other  
✅ **Multiplicities** - Cardinality of relationships  

The UML schema does NOT define:
❌ **Attributes** - Defined via ObjectAttribute model  
❌ **Methods** - Defined via ObjectAttribute model (method type)  
❌ **Data Types** - Managed by ObjectAttribute  
❌ **Constraints** - Managed by ObjectAttribute  

### Why Separate Attributes?

1. **Flexibility** - Add/modify attributes without changing UML schema
2. **Reusability** - Share attributes across multiple object models
3. **Dynamic Schemas** - Change attributes at runtime
4. **Versioning** - Track attribute changes independently
5. **Validation** - Centralized attribute validation rules

---

## UML Class Diagram Structure

### Complete Schema Format

```json
{
  "classes": [
    {
      "name": "ClassName",
      "stereotype": "entity|interface|abstract|enum|value_object",
      "isAbstract": false,
      "description": "Description of the class",
      "constraints": ["constraint1", "constraint2"]
    }
  ],
  "relationships": [
    {
      "type": "association|aggregation|composition|inheritance|realization|dependency",
      "from": "SourceClass",
      "to": "TargetClass",
      "fromMultiplicity": "0..1|1|*|0..*|1..*|n..m",
      "toMultiplicity": "0..1|1|*|0..*|1..*|n..m",
      "fromNavigable": true,
      "toNavigable": true,
      "fromRole": "roleName",
      "toRole": "roleName",
      "label": "relationshipLabel",
      "constraints": ["constraint1"]
    }
  ],
  "notes": [
    {
      "text": "Additional notes or documentation",
      "attachedTo": "ClassName"
    }
  ]
}
```

---

## Class Definition

### Class Structure (Entity-Level Only)

```json
{
  "name": "Customer",
  "stereotype": "entity",
  "isAbstract": false,
  "description": "Customer entity representing a buyer in the system",
  "constraints": ["unique_email", "active_status_required"]
}
```

### Class Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `name` | string | Yes | Class/entity name (PascalCase) |
| `stereotype` | string | Yes | Type of class (see stereotypes below) |
| `isAbstract` | boolean | No | Whether class is abstract (default: false) |
| `description` | string | No | Description of the class purpose |
| `constraints` | array | No | Class-level constraints |

### Stereotypes

| Stereotype | Description | Usage |
|------------|-------------|-------|
| `entity` | Domain entity with identity | Business objects with unique ID |
| `value_object` | Object without identity | Immutable objects like Money, Address |
| `interface` | Interface definition | Contract for implementations |
| `abstract` | Abstract class | Base class for inheritance |
| `enum` | Enumeration | Fixed set of values |
| `aggregate_root` | DDD aggregate root | Main entity in an aggregate |
| `service` | Service class | Business logic services |

---

## Attributes & Methods

**Attributes and methods are NOT defined in the UML schema.**

They are defined separately using the **ObjectAttribute** model:

```python
# Define attributes for Customer class
customer_id_attr = ObjectAttribute(
    object_model_id=customer_model.id,
    name="customerId",
    code="CUSTOMER_ID",
    data_type="string",
    is_required=True,
    is_unique=True,
    attribute_type="field"
)

customer_email_attr = ObjectAttribute(
    object_model_id=customer_model.id,
    name="email",
    code="EMAIL",
    data_type="string",
    is_required=True,
    is_unique=True,
    validation_rules={"pattern": "^[\\w.-]+@[\\w.-]+\\.\\w+$"}
)

# Define method for Customer class
place_order_method = ObjectAttribute(
    object_model_id=customer_model.id,
    name="placeOrder",
    code="PLACE_ORDER",
    data_type="Order",
    attribute_type="method",
    validation_rules={
        "parameters": [
            {"name": "items", "type": "array<OrderItem>"}
        ]
    }
)
```

See **OBJECT_ATTRIBUTES_GUIDE.md** for complete attribute definition documentation.

---

## Relationships

### Relationship Types

#### 1. **Association** (knows-a)
General relationship between classes.

```json
{
  "type": "association",
  "from": "Customer",
  "to": "Order",
  "fromMultiplicity": "1",
  "toMultiplicity": "*",
  "label": "places"
}
```

**UML Notation:** `Customer -------- Order`

#### 2. **Aggregation** (has-a, weak)
Whole-part relationship where parts can exist independently.

```json
{
  "type": "aggregation",
  "from": "Department",
  "to": "Employee",
  "fromMultiplicity": "1",
  "toMultiplicity": "*",
  "label": "employs"
}
```

**UML Notation:** `Department ◇-------- Employee`

#### 3. **Composition** (has-a, strong)
Strong whole-part relationship where parts cannot exist without the whole.

```json
{
  "type": "composition",
  "from": "Order",
  "to": "OrderLine",
  "fromMultiplicity": "1",
  "toMultiplicity": "1..*",
  "label": "contains"
}
```

**UML Notation:** `Order ◆-------- OrderLine`

#### 4. **Inheritance** (is-a)
Generalization/specialization relationship.

```json
{
  "type": "inheritance",
  "from": "SavingsAccount",
  "to": "Account",
  "label": "extends"
}
```

**UML Notation:** `SavingsAccount -------|> Account`

#### 5. **Realization** (implements)
Class implements an interface.

```json
{
  "type": "realization",
  "from": "EmailNotifier",
  "to": "Notifier",
  "label": "implements"
}
```

**UML Notation:** `EmailNotifier - - - - |> Notifier`

#### 6. **Dependency** (uses)
One class depends on another.

```json
{
  "type": "dependency",
  "from": "OrderService",
  "to": "EmailService",
  "label": "uses"
}
```

**UML Notation:** `OrderService - - - - > EmailService`

### Multiplicities

| Notation | Meaning |
|----------|---------|
| `1` | Exactly one |
| `0..1` | Zero or one |
| `*` | Zero or more |
| `0..*` | Zero or more (explicit) |
| `1..*` | One or more |
| `n..m` | Between n and m |
| `n` | Exactly n |

### Navigability

- **`fromNavigable: true`** - Can navigate from source to target
- **`toNavigable: true`** - Can navigate from target to source
- **Bidirectional** - Both true
- **Unidirectional** - Only one true

---

## Complete Examples

### Example 1: E-commerce Order System (Entity-Level Only)

```json
{
  "classes": [
    {
      "name": "Customer",
      "stereotype": "entity",
      "description": "Customer entity representing a buyer in the e-commerce system"
    },
    {
      "name": "Order",
      "stereotype": "entity",
      "description": "Order placed by a customer"
    },
    {
      "name": "OrderItem",
      "stereotype": "value_object",
      "description": "Line item within an order"
    },
    {
      "name": "Product",
      "stereotype": "entity",
      "description": "Product available for purchase"
    },
    {
      "name": "OrderStatus",
      "stereotype": "enum",
      "description": "Status of an order"
    }
  ],
  "relationships": [
    {
      "type": "association",
      "from": "Customer",
      "to": "Order",
      "fromMultiplicity": "1",
      "toMultiplicity": "*",
      "fromNavigable": true,
      "toNavigable": true,
      "fromRole": "customer",
      "toRole": "orders",
      "label": "places"
    },
    {
      "type": "composition",
      "from": "Order",
      "to": "OrderItem",
      "fromMultiplicity": "1",
      "toMultiplicity": "1..*",
      "fromNavigable": true,
      "toNavigable": false,
      "fromRole": "order",
      "toRole": "items",
      "label": "contains"
    },
    {
      "type": "association",
      "from": "OrderItem",
      "to": "Product",
      "fromMultiplicity": "*",
      "toMultiplicity": "1",
      "fromNavigable": true,
      "toNavigable": false,
      "label": "references"
    },
    {
      "type": "association",
      "from": "Order",
      "to": "OrderStatus",
      "fromMultiplicity": "*",
      "toMultiplicity": "1",
      "label": "has"
    }
  ]
}
```

**Note:** Attributes for each class (customerId, email, name, etc.) are defined separately using ObjectAttribute model.

### Example 2: Banking System (Entity-Level Only)

```json
{
  "classes": [
    {
      "name": "Account",
      "stereotype": "abstract",
      "isAbstract": true,
      "description": "Abstract base class for all account types"
    },
    {
      "name": "SavingsAccount",
      "stereotype": "entity",
      "description": "Savings account with interest"
    },
    {
      "name": "CheckingAccount",
      "stereotype": "entity",
      "description": "Checking account with overdraft"
    },
    {
      "name": "Customer",
      "stereotype": "entity",
      "description": "Bank customer"
    },
    {
      "name": "Transaction",
      "stereotype": "entity",
      "description": "Financial transaction"
    },
    {
      "name": "AccountStatus",
      "stereotype": "enum",
      "description": "Status of an account"
    },
    {
      "name": "TransactionType",
      "stereotype": "enum",
      "description": "Type of transaction"
    }
  ],
  "relationships": [
    {
      "type": "inheritance",
      "from": "SavingsAccount",
      "to": "Account",
      "label": "extends"
    },
    {
      "type": "inheritance",
      "from": "CheckingAccount",
      "to": "Account",
      "label": "extends"
    },
    {
      "type": "aggregation",
      "from": "Customer",
      "to": "Account",
      "fromMultiplicity": "1",
      "toMultiplicity": "*",
      "fromNavigable": true,
      "toNavigable": true,
      "label": "owns"
    },
    {
      "type": "association",
      "from": "Account",
      "to": "Transaction",
      "fromMultiplicity": "1",
      "toMultiplicity": "*",
      "fromNavigable": true,
      "toNavigable": false,
      "label": "has"
    }
  ]
}
```

**Note:** Attributes like accountNumber, balance, interestRate, etc. are defined using ObjectAttribute model.

### Example 3: Healthcare System (Entity-Level Only)

```json
{
  "classes": [
    {
      "name": "Patient",
      "stereotype": "entity",
      "description": "Patient receiving medical care"
    },
    {
      "name": "Doctor",
      "stereotype": "entity",
      "description": "Medical practitioner"
    },
    {
      "name": "Appointment",
      "stereotype": "entity",
      "description": "Scheduled medical appointment"
    },
    {
      "name": "MedicalRecord",
      "stereotype": "entity",
      "description": "Patient medical history record"
    },
    {
      "name": "Prescription",
      "stereotype": "entity",
      "description": "Medication prescription"
    },
    {
      "name": "AppointmentStatus",
      "stereotype": "enum",
      "description": "Status of an appointment"
    }
  ],
  "relationships": [
    {
      "type": "association",
      "from": "Patient",
      "to": "Appointment",
      "fromMultiplicity": "1",
      "toMultiplicity": "*",
      "label": "schedules"
    },
    {
      "type": "association",
      "from": "Doctor",
      "to": "Appointment",
      "fromMultiplicity": "1",
      "toMultiplicity": "*",
      "label": "attends"
    },
    {
      "type": "composition",
      "from": "Patient",
      "to": "MedicalRecord",
      "fromMultiplicity": "1",
      "toMultiplicity": "*",
      "label": "has"
    },
    {
      "type": "association",
      "from": "Doctor",
      "to": "Prescription",
      "fromMultiplicity": "1",
      "toMultiplicity": "*",
      "label": "writes"
    },
    {
      "type": "association",
      "from": "Patient",
      "to": "Prescription",
      "fromMultiplicity": "1",
      "toMultiplicity": "*",
      "label": "receives"
    }
  ]
}
```

**Note:** Patient attributes (patientId, name, dateOfBirth, etc.) are defined using ObjectAttribute model.

---

## Defining Attributes Separately

After creating the UML schema with entity-level classes, define attributes using ObjectAttribute:

```python
from analytics_models import ObjectModel, ObjectAttribute

# Create ObjectModel with UML schema (entities only)
ecommerce_model = ObjectModel(
    name="E-commerce System",
    code="ECOMM",
    schema_definition={
        "classes": [
            {
                "name": "Customer",
                "stereotype": "entity",
                "description": "Customer entity"
            },
            {
                "name": "Order",
                "stereotype": "entity",
                "description": "Order entity"
            }
        ],
        "relationships": [
            {
                "type": "association",
                "from": "Customer",
                "to": "Order",
                "fromMultiplicity": "1",
                "toMultiplicity": "*",
                "label": "places"
            }
        ]
    }
)

# Define attributes for Customer class
customer_id = ObjectAttribute(
    object_model_id=ecommerce_model.id,
    name="customerId",
    code="CUSTOMER_ID",
    data_type="string",
    is_required=True,
    is_unique=True,
    attribute_type="field",
    description="Unique customer identifier"
)

customer_email = ObjectAttribute(
    object_model_id=ecommerce_model.id,
    name="email",
    code="EMAIL",
    data_type="string",
    is_required=True,
    is_unique=True,
    attribute_type="field",
    validation_rules={"pattern": "^[\\w.-]+@[\\w.-]+\\.\\w+$"}
)

# Define attributes for Order class
order_id = ObjectAttribute(
    object_model_id=ecommerce_model.id,
    name="orderId",
    code="ORDER_ID",
    data_type="string",
    is_required=True,
    is_unique=True,
    attribute_type="field"
)

order_date = ObjectAttribute(
    object_model_id=ecommerce_model.id,
    name="orderDate",
    code="ORDER_DATE",
    data_type="datetime",
    is_required=True,
    attribute_type="field"
)
```

---

## Old Format (Not Recommended)

The old format with attributes and methods embedded in the UML schema is deprecated:

```json
{
  "classes": [
    {
      "name": "Customer",
      "stereotype": "entity",
      "attributes": [
        {
          "name": "customerId",
          "type": "string",
          "visibility": "private",
          "constraints": ["primary_key", "not_null"]
        },
        {
          "name": "email",
          "type": "string",
          "visibility": "private",
          "constraints": ["unique", "not_null"]
        },
        {
          "name": "name",
          "type": "string",
          "visibility": "private"
        },
        {
          "name": "registrationDate",
          "type": "datetime",
          "visibility": "private",
          "isReadOnly": true
        }
      ],
      "methods": [
        {
          "name": "placeOrder",
          "returnType": "Order",
          "visibility": "public",
          "parameters": [
            {
              "name": "items",
              "type": "array<OrderItem>"
            }
          ]
        },
        {
          "name": "getOrderHistory",
          "returnType": "array<Order>",
          "visibility": "public"
        }
      ]
    },
    {
      "name": "Order",
      "stereotype": "entity",
      "attributes": [
        {
          "name": "orderId",
          "type": "string",
          "visibility": "private",
          "constraints": ["primary_key"]
        },
        {
          "name": "orderDate",
          "type": "datetime",
          "visibility": "private",
          "isReadOnly": true
        },
        {
          "name": "status",
          "type": "OrderStatus",
          "visibility": "private"
        },
        {
          "name": "totalAmount",
          "type": "decimal",
          "visibility": "private"
        }
      ],
      "methods": [
        {
          "name": "addItem",
          "returnType": "void",
          "visibility": "public",
          "parameters": [
            {
              "name": "item",
              "type": "OrderItem"
            }
          ]
        },
        {
          "name": "calculateTotal",
          "returnType": "decimal",
          "visibility": "public"
        },
        {
          "name": "submit",
          "returnType": "boolean",
          "visibility": "public"
        }
      ]
    },
    {
      "name": "OrderItem",
      "stereotype": "value_object",
      "attributes": [
        {
          "name": "productId",
          "type": "string",
          "visibility": "private"
        },
        {
          "name": "quantity",
          "type": "integer",
          "visibility": "private",
          "constraints": ["min:1"]
        },
        {
          "name": "unitPrice",
          "type": "decimal",
          "visibility": "private"
        },
        {
          "name": "subtotal",
          "type": "decimal",
          "visibility": "private",
          "isReadOnly": true
        }
      ],
      "methods": [
        {
          "name": "calculateSubtotal",
          "returnType": "decimal",
          "visibility": "public"
        }
      ]
    },
    {
      "name": "Product",
      "stereotype": "entity",
      "attributes": [
        {
          "name": "productId",
          "type": "string",
          "visibility": "private",
          "constraints": ["primary_key"]
        },
        {
          "name": "name",
          "type": "string",
          "visibility": "private"
        },
        {
          "name": "price",
          "type": "decimal",
          "visibility": "private"
        },
        {
          "name": "stockQuantity",
          "type": "integer",
          "visibility": "private"
        }
      ],
      "methods": [
        {
          "name": "isInStock",
          "returnType": "boolean",
          "visibility": "public"
        },
        {
          "name": "reduceStock",
          "returnType": "void",
          "visibility": "public",
          "parameters": [
            {
              "name": "quantity",
              "type": "integer"
            }
          ]
        }
      ]
    },
    {
      "name": "OrderStatus",
      "stereotype": "enum",
      "attributes": [
        {
          "name": "PENDING",
          "type": "string",
          "isStatic": true,
          "isReadOnly": true
        },
        {
          "name": "CONFIRMED",
          "type": "string",
          "isStatic": true,
          "isReadOnly": true
        },
        {
          "name": "SHIPPED",
          "type": "string",
          "isStatic": true,
          "isReadOnly": true
        },
        {
          "name": "DELIVERED",
          "type": "string",
          "isStatic": true,
          "isReadOnly": true
        },
        {
          "name": "CANCELLED",
          "type": "string",
          "isStatic": true,
          "isReadOnly": true
        }
      ]
    }
  ],
  "relationships": [
    {
      "type": "association",
      "from": "Customer",
      "to": "Order",
      "fromMultiplicity": "1",
      "toMultiplicity": "*",
      "fromNavigable": true,
      "toNavigable": true,
      "fromRole": "customer",
      "toRole": "orders",
      "label": "places"
    },
    {
      "type": "composition",
      "from": "Order",
      "to": "OrderItem",
      "fromMultiplicity": "1",
      "toMultiplicity": "1..*",
      "fromNavigable": true,
      "toNavigable": false,
      "fromRole": "order",
      "toRole": "items",
      "label": "contains"
    },
    {
      "type": "association",
      "from": "OrderItem",
      "to": "Product",
      "fromMultiplicity": "*",
      "toMultiplicity": "1",
      "fromNavigable": true,
      "toNavigable": false,
      "label": "references"
    },
    {
      "type": "association",
      "from": "Order",
      "to": "OrderStatus",
      "fromMultiplicity": "*",
      "toMultiplicity": "1",
      "label": "has"
    }
  ]
}
```

### Example 2: Banking System

```json
{
  "classes": [
    {
      "name": "Account",
      "stereotype": "abstract",
      "isAbstract": true,
      "attributes": [
        {
          "name": "accountNumber",
          "type": "string",
          "visibility": "protected",
          "constraints": ["primary_key"]
        },
        {
          "name": "balance",
          "type": "decimal",
          "visibility": "protected"
        },
        {
          "name": "openDate",
          "type": "date",
          "visibility": "protected"
        }
      ],
      "methods": [
        {
          "name": "deposit",
          "returnType": "void",
          "visibility": "public",
          "isAbstract": true,
          "parameters": [
            {
              "name": "amount",
              "type": "decimal"
            }
          ]
        },
        {
          "name": "withdraw",
          "returnType": "boolean",
          "visibility": "public",
          "isAbstract": true,
          "parameters": [
            {
              "name": "amount",
              "type": "decimal"
            }
          ]
        },
        {
          "name": "getBalance",
          "returnType": "decimal",
          "visibility": "public"
        }
      ]
    },
    {
      "name": "SavingsAccount",
      "stereotype": "entity",
      "attributes": [
        {
          "name": "interestRate",
          "type": "decimal",
          "visibility": "private"
        },
        {
          "name": "minimumBalance",
          "type": "decimal",
          "visibility": "private"
        }
      ],
      "methods": [
        {
          "name": "deposit",
          "returnType": "void",
          "visibility": "public",
          "parameters": [
            {
              "name": "amount",
              "type": "decimal"
            }
          ]
        },
        {
          "name": "withdraw",
          "returnType": "boolean",
          "visibility": "public",
          "parameters": [
            {
              "name": "amount",
              "type": "decimal"
            }
          ]
        },
        {
          "name": "calculateInterest",
          "returnType": "decimal",
          "visibility": "public"
        }
      ]
    },
    {
      "name": "CheckingAccount",
      "stereotype": "entity",
      "attributes": [
        {
          "name": "overdraftLimit",
          "type": "decimal",
          "visibility": "private"
        },
        {
          "name": "monthlyFee",
          "type": "decimal",
          "visibility": "private"
        }
      ],
      "methods": [
        {
          "name": "deposit",
          "returnType": "void",
          "visibility": "public",
          "parameters": [
            {
              "name": "amount",
              "type": "decimal"
            }
          ]
        },
        {
          "name": "withdraw",
          "returnType": "boolean",
          "visibility": "public",
          "parameters": [
            {
              "name": "amount",
              "type": "decimal"
            }
          ]
        },
        {
          "name": "writeCheck",
          "returnType": "boolean",
          "visibility": "public",
          "parameters": [
            {
              "name": "amount",
              "type": "decimal"
            },
            {
              "name": "payee",
              "type": "string"
            }
          ]
        }
      ]
    },
    {
      "name": "Customer",
      "stereotype": "entity",
      "attributes": [
        {
          "name": "customerId",
          "type": "string",
          "visibility": "private",
          "constraints": ["primary_key"]
        },
        {
          "name": "name",
          "type": "string",
          "visibility": "private"
        },
        {
          "name": "ssn",
          "type": "string",
          "visibility": "private",
          "constraints": ["unique"]
        }
      ],
      "methods": [
        {
          "name": "openAccount",
          "returnType": "Account",
          "visibility": "public",
          "parameters": [
            {
              "name": "accountType",
              "type": "string"
            }
          ]
        }
      ]
    },
    {
      "name": "Transaction",
      "stereotype": "entity",
      "attributes": [
        {
          "name": "transactionId",
          "type": "string",
          "visibility": "private",
          "constraints": ["primary_key"]
        },
        {
          "name": "timestamp",
          "type": "datetime",
          "visibility": "private"
        },
        {
          "name": "amount",
          "type": "decimal",
          "visibility": "private"
        },
        {
          "name": "type",
          "type": "TransactionType",
          "visibility": "private"
        }
      ]
    },
    {
      "name": "TransactionType",
      "stereotype": "enum",
      "attributes": [
        {"name": "DEPOSIT", "type": "string", "isStatic": true},
        {"name": "WITHDRAWAL", "type": "string", "isStatic": true},
        {"name": "TRANSFER", "type": "string", "isStatic": true}
      ]
    }
  ],
  "relationships": [
    {
      "type": "inheritance",
      "from": "SavingsAccount",
      "to": "Account",
      "label": "extends"
    },
    {
      "type": "inheritance",
      "from": "CheckingAccount",
      "to": "Account",
      "label": "extends"
    },
    {
      "type": "aggregation",
      "from": "Customer",
      "to": "Account",
      "fromMultiplicity": "1",
      "toMultiplicity": "*",
      "label": "owns"
    },
    {
      "type": "association",
      "from": "Account",
      "to": "Transaction",
      "fromMultiplicity": "1",
      "toMultiplicity": "*",
      "label": "has"
    }
  ]
}
```

---

## Best Practices

### 1. **Use Appropriate Stereotypes**
Choose stereotypes that clearly indicate the purpose of each class.

### 2. **Define Clear Relationships**
Use the correct relationship type (association, aggregation, composition, inheritance).

### 3. **Specify Multiplicities**
Always define multiplicities to clarify cardinality.

### 4. **Use Visibility Appropriately**
- Public for API/interface methods
- Private for internal implementation
- Protected for inheritance

### 5. **Document Constraints**
Include validation rules and constraints on attributes.

### 6. **Keep Methods Focused**
Each method should have a single, clear purpose.

### 7. **Use Value Objects**
For immutable concepts like Money, Address, DateRange.

### 8. **Define Enumerations**
Use enum stereotype for fixed sets of values.

---

## Validation Rules

The schema_definition should be validated for:

✅ **Valid JSON structure**  
✅ **Required fields present** (name for classes, type for relationships)  
✅ **Valid relationship types**  
✅ **Valid multiplicities**  
✅ **Valid visibility values**  
✅ **Referenced classes exist** (in relationships)  
✅ **No circular inheritance**  
✅ **Consistent naming** (camelCase for attributes/methods, PascalCase for classes)  

---

## Conclusion

Using UML class diagram notation in the `schema_definition` provides a rich, standardized way to define object models with clear semantics for attributes, methods, and relationships. This enables better understanding, documentation, and code generation from the models.

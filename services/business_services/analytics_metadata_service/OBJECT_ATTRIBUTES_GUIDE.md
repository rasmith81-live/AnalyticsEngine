# Object Attributes & KPI Formula References Guide

## Overview

Objects now have **explicit attributes** (like database table fields) defined through the `ObjectAttribute` model. KPIs reference these specific attributes in their formulas, creating a strongly-typed, traceable calculation system.

---

## Architecture

```
ObjectModel
  ├── ObjectAttribute (defines schema/structure)
  │   ├── name: "Revenue"
  │   ├── code: "REVENUE"
  │   ├── data_type: "float"
  │   └── validation_rules: {"min": 0}
  │
  ├── Object (instances with data)
  │   └── data_values: {"REVENUE": 100000, "COST": 60000}
  │
  └── KPI (calculations using attributes)
      ├── formula: "Profit Margin = (Revenue - Cost) / Revenue * 100"
      ├── calculation_formula: "(REVENUE - COST) / REVENUE * 100"
      └── attribute_references: {"revenue": "REVENUE", "cost": "COST"}
```

---

## ObjectAttribute Model

### Fields

- **name**: Human-readable attribute name (e.g., "Revenue")
- **code**: Unique code for referencing in formulas (e.g., "REVENUE")
- **data_type**: Data type - `string`, `integer`, `float`, `boolean`, `date`, `datetime`, `json`
- **is_required**: Whether the attribute must have a value
- **is_active**: Whether the attribute is currently active
- **default_value**: Default value if not provided
- **validation_rules**: JSON rules for validation (min, max, pattern, enum, etc.)
- **display_order**: Order for displaying attributes
- **metadata_**: Additional metadata

### Example: Creating Object Attributes

```python
from analytics_models import ObjectModel, ObjectAttribute

# Create an ObjectModel for Sales Transactions
sales_model = ObjectModel(
    name="Sales Transaction",
    code="SALES_TXN",
    description="Individual sales transaction record"
)

# Define attributes (like table columns)
revenue_attr = ObjectAttribute(
    object_model_id=sales_model.id,
    name="Revenue",
    code="REVENUE",
    data_type="float",
    is_required=True,
    validation_rules={
        "min": 0,
        "description": "Total revenue from the transaction"
    },
    display_order=1
)

cost_attr = ObjectAttribute(
    object_model_id=sales_model.id,
    name="Cost",
    code="COST",
    data_type="float",
    is_required=True,
    validation_rules={
        "min": 0,
        "description": "Total cost of goods sold"
    },
    display_order=2
)

quantity_attr = ObjectAttribute(
    object_model_id=sales_model.id,
    name="Quantity",
    code="QUANTITY",
    data_type="integer",
    is_required=True,
    validation_rules={
        "min": 1,
        "description": "Number of units sold"
    },
    display_order=3
)

transaction_date_attr = ObjectAttribute(
    object_model_id=sales_model.id,
    name="Transaction Date",
    code="TXN_DATE",
    data_type="date",
    is_required=True,
    display_order=4
)

customer_type_attr = ObjectAttribute(
    object_model_id=sales_model.id,
    name="Customer Type",
    code="CUSTOMER_TYPE",
    data_type="string",
    is_required=False,
    validation_rules={
        "enum": ["retail", "wholesale", "enterprise"],
        "description": "Type of customer"
    },
    display_order=5
)
```

---

## Object Data Values

Objects store their attribute values in the `data_values` JSON field, using attribute codes as keys:

```python
from analytics_models import Object

# Create an object instance with data
sales_txn = Object(
    name="Transaction #12345",
    code="TXN_12345",
    data_values={
        "REVENUE": 100000.00,
        "COST": 60000.00,
        "QUANTITY": 500,
        "TXN_DATE": "2024-01-15",
        "CUSTOMER_TYPE": "enterprise"
    }
)

# Associate with the object model
sales_txn.object_models.append(sales_model)
```

---

## KPI Formula References

KPIs explicitly reference object attributes in their formulas:

### Example: Profit Margin KPI

```python
from analytics_models import KPI

profit_margin_kpi = KPI(
    name="Profit Margin",
    code="PROFIT_MARGIN",
    
    # Human-readable formula
    formula="Profit Margin = (Revenue - Cost) / Revenue * 100",
    
    # Calculation formula using attribute codes
    calculation_formula="(REVENUE - COST) / REVENUE * 100",
    
    # Explicit attribute references
    attribute_references={
        "revenue": "REVENUE",
        "cost": "COST"
    },
    
    unit_of_measure="percentage",
    
    kpi_definition="""
    Profit Margin measures the percentage of revenue that remains as profit
    after deducting the cost of goods sold. It indicates pricing effectiveness
    and cost efficiency.
    """,
    
    target_value=40.0,
    threshold_warning=30.0,
    threshold_critical=20.0
)

# Associate with object model
profit_margin_kpi.object_models.append(sales_model)
```

### Example: Average Revenue Per Unit KPI

```python
avg_revenue_per_unit_kpi = KPI(
    name="Average Revenue Per Unit",
    code="AVG_REVENUE_PER_UNIT",
    
    formula="Average Revenue Per Unit = Revenue / Quantity",
    
    calculation_formula="REVENUE / QUANTITY",
    
    attribute_references={
        "revenue": "REVENUE",
        "quantity": "QUANTITY"
    },
    
    unit_of_measure="USD",
    
    kpi_definition="""
    Average Revenue Per Unit measures the average selling price per unit sold.
    This helps track pricing trends and identify opportunities for price optimization.
    """
)

avg_revenue_per_unit_kpi.object_models.append(sales_model)
```

### Example: Cost Ratio KPI

```python
cost_ratio_kpi = KPI(
    name="Cost Ratio",
    code="COST_RATIO",
    
    formula="Cost Ratio = Cost / Revenue * 100",
    
    calculation_formula="COST / REVENUE * 100",
    
    attribute_references={
        "cost": "COST",
        "revenue": "REVENUE"
    },
    
    unit_of_measure="percentage",
    
    kpi_definition="""
    Cost Ratio measures the percentage of revenue consumed by costs.
    Lower ratios indicate better cost efficiency.
    """,
    
    target_value=60.0,
    threshold_warning=70.0,
    threshold_critical=80.0
)

cost_ratio_kpi.object_models.append(sales_model)
```

---

## Data Types

### Supported Data Types

1. **string** - Text values
   - Example: Customer names, product codes, categories
   - Validation: pattern, enum, min_length, max_length

2. **integer** - Whole numbers
   - Example: Quantities, counts, IDs
   - Validation: min, max, enum

3. **float** - Decimal numbers
   - Example: Revenue, cost, percentages, ratios
   - Validation: min, max, precision

4. **boolean** - True/False values
   - Example: Is active, is paid, is verified
   - Validation: None typically needed

5. **date** - Date values (YYYY-MM-DD)
   - Example: Transaction date, birth date
   - Validation: min_date, max_date, format

6. **datetime** - Date and time values
   - Example: Created timestamp, updated timestamp
   - Validation: min_datetime, max_datetime, format

7. **json** - Complex nested data
   - Example: Metadata, configurations, nested objects
   - Validation: schema, required_keys

---

## Validation Rules

### Common Validation Patterns

```python
# Numeric validations
validation_rules = {
    "min": 0,
    "max": 1000000,
    "precision": 2  # Decimal places
}

# String validations
validation_rules = {
    "min_length": 1,
    "max_length": 255,
    "pattern": "^[A-Z]{3}-[0-9]{4}$",  # Regex pattern
    "enum": ["option1", "option2", "option3"]
}

# Date validations
validation_rules = {
    "min_date": "2020-01-01",
    "max_date": "2030-12-31",
    "format": "YYYY-MM-DD"
}

# JSON schema validation
validation_rules = {
    "schema": {
        "type": "object",
        "properties": {
            "address": {"type": "string"},
            "city": {"type": "string"}
        },
        "required": ["address"]
    }
}
```

---

## Complete Example: E-Commerce Order System

### 1. Define ObjectModel

```python
order_model = ObjectModel(
    name="E-Commerce Order",
    code="ECOM_ORDER",
    description="Customer order in e-commerce system"
)
```

### 2. Define Attributes

```python
attributes = [
    ObjectAttribute(
        object_model_id=order_model.id,
        name="Order Total",
        code="ORDER_TOTAL",
        data_type="float",
        is_required=True,
        validation_rules={"min": 0, "precision": 2}
    ),
    ObjectAttribute(
        object_model_id=order_model.id,
        name="Shipping Cost",
        code="SHIPPING_COST",
        data_type="float",
        is_required=True,
        validation_rules={"min": 0, "precision": 2}
    ),
    ObjectAttribute(
        object_model_id=order_model.id,
        name="Tax Amount",
        code="TAX_AMOUNT",
        data_type="float",
        is_required=True,
        validation_rules={"min": 0, "precision": 2}
    ),
    ObjectAttribute(
        object_model_id=order_model.id,
        name="Discount Amount",
        code="DISCOUNT_AMOUNT",
        data_type="float",
        is_required=False,
        default_value="0",
        validation_rules={"min": 0, "precision": 2}
    ),
    ObjectAttribute(
        object_model_id=order_model.id,
        name="Item Count",
        code="ITEM_COUNT",
        data_type="integer",
        is_required=True,
        validation_rules={"min": 1}
    ),
    ObjectAttribute(
        object_model_id=order_model.id,
        name="Order Status",
        code="ORDER_STATUS",
        data_type="string",
        is_required=True,
        validation_rules={
            "enum": ["pending", "processing", "shipped", "delivered", "cancelled"]
        }
    ),
    ObjectAttribute(
        object_model_id=order_model.id,
        name="Order Date",
        code="ORDER_DATE",
        data_type="datetime",
        is_required=True
    ),
]
```

### 3. Create KPIs

```python
# Average Order Value
aov_kpi = KPI(
    name="Average Order Value",
    code="AOV",
    formula="AOV = Order Total / Item Count",
    calculation_formula="ORDER_TOTAL / ITEM_COUNT",
    attribute_references={
        "order_total": "ORDER_TOTAL",
        "item_count": "ITEM_COUNT"
    },
    unit_of_measure="USD"
)

# Effective Discount Rate
discount_rate_kpi = KPI(
    name="Effective Discount Rate",
    code="DISCOUNT_RATE",
    formula="Discount Rate = Discount Amount / (Order Total + Discount Amount) * 100",
    calculation_formula="DISCOUNT_AMOUNT / (ORDER_TOTAL + DISCOUNT_AMOUNT) * 100",
    attribute_references={
        "discount_amount": "DISCOUNT_AMOUNT",
        "order_total": "ORDER_TOTAL"
    },
    unit_of_measure="percentage"
)

# Shipping Cost Ratio
shipping_ratio_kpi = KPI(
    name="Shipping Cost Ratio",
    code="SHIPPING_RATIO",
    formula="Shipping Ratio = Shipping Cost / Order Total * 100",
    calculation_formula="SHIPPING_COST / ORDER_TOTAL * 100",
    attribute_references={
        "shipping_cost": "SHIPPING_COST",
        "order_total": "ORDER_TOTAL"
    },
    unit_of_measure="percentage",
    target_value=10.0,
    threshold_warning=15.0,
    threshold_critical=20.0
)

# Net Revenue (after tax and shipping)
net_revenue_kpi = KPI(
    name="Net Revenue",
    code="NET_REVENUE",
    formula="Net Revenue = Order Total - Tax Amount - Shipping Cost",
    calculation_formula="ORDER_TOTAL - TAX_AMOUNT - SHIPPING_COST",
    attribute_references={
        "order_total": "ORDER_TOTAL",
        "tax_amount": "TAX_AMOUNT",
        "shipping_cost": "SHIPPING_COST"
    },
    unit_of_measure="USD"
)
```

### 4. Create Object Instances

```python
order_1 = Object(
    name="Order #ORD-2024-001",
    code="ORD_2024_001",
    data_values={
        "ORDER_TOTAL": 250.00,
        "SHIPPING_COST": 15.00,
        "TAX_AMOUNT": 20.00,
        "DISCOUNT_AMOUNT": 25.00,
        "ITEM_COUNT": 3,
        "ORDER_STATUS": "delivered",
        "ORDER_DATE": "2024-01-15T10:30:00Z"
    }
)

order_2 = Object(
    name="Order #ORD-2024-002",
    code="ORD_2024_002",
    data_values={
        "ORDER_TOTAL": 450.00,
        "SHIPPING_COST": 20.00,
        "TAX_AMOUNT": 36.00,
        "DISCOUNT_AMOUNT": 0.00,
        "ITEM_COUNT": 5,
        "ORDER_STATUS": "shipped",
        "ORDER_DATE": "2024-01-16T14:20:00Z"
    }
)
```

---

## Benefits

### 1. **Type Safety**
- Attributes have explicit data types
- Validation rules ensure data quality
- Formulas reference known attributes

### 2. **Traceability**
- Clear mapping between KPI formulas and object attributes
- Easy to understand what data drives each KPI
- Audit trail of attribute definitions

### 3. **Reusability**
- Define attributes once, use in multiple KPIs
- Share attribute definitions across object models
- Consistent naming and validation

### 4. **Maintainability**
- Change attribute definition in one place
- KPIs automatically reference updated attributes
- Clear documentation of data requirements

### 5. **Validation**
- Enforce data quality at attribute level
- Prevent invalid calculations
- Clear error messages when validation fails

---

## Best Practices

### 1. **Attribute Naming**
- Use clear, descriptive names
- Use UPPERCASE for codes (e.g., "REVENUE", "COST")
- Be consistent across object models

### 2. **Data Types**
- Choose the most specific type possible
- Use `float` for monetary values
- Use `integer` for counts
- Use `string` with enum for categorical data

### 3. **Validation Rules**
- Always set `min` for numeric values that can't be negative
- Use `enum` for fixed sets of values
- Set `is_required` appropriately

### 4. **Formula Documentation**
- Provide both human-readable and calculation formulas
- List all attribute references explicitly
- Document any assumptions or edge cases

### 5. **Attribute Organization**
- Use `display_order` for logical grouping
- Keep related attributes together
- Consider using metadata for categorization

---

## Query Examples

### Get All Attributes for an ObjectModel

```python
attributes = session.query(ObjectAttribute)\
    .filter(ObjectAttribute.object_model_id == object_model.id)\
    .filter(ObjectAttribute.is_active == True)\
    .order_by(ObjectAttribute.display_order)\
    .all()
```

### Get All KPIs Using a Specific Attribute

```python
# Find KPIs that reference "REVENUE" attribute
kpis_using_revenue = session.query(KPI)\
    .filter(KPI.attribute_references.contains({"revenue": "REVENUE"}))\
    .all()
```

### Validate Object Data Against Attributes

```python
def validate_object_data(obj: Object, object_model: ObjectModel):
    """Validate object data against attribute definitions."""
    errors = []
    
    for attr in object_model.attributes:
        if not attr.is_active:
            continue
            
        value = obj.data_values.get(attr.code)
        
        # Check required
        if attr.is_required and value is None:
            errors.append(f"Required attribute {attr.code} is missing")
            continue
        
        if value is None:
            continue
        
        # Validate based on data type and rules
        if attr.data_type == "float" and attr.validation_rules:
            if "min" in attr.validation_rules and value < attr.validation_rules["min"]:
                errors.append(f"{attr.code} below minimum: {value} < {attr.validation_rules['min']}")
            if "max" in attr.validation_rules and value > attr.validation_rules["max"]:
                errors.append(f"{attr.code} above maximum: {value} > {attr.validation_rules['max']}")
    
    return errors
```

---

## Conclusion

The ObjectAttribute system provides a robust, type-safe way to define object schemas and create KPIs with explicit attribute references. This ensures data quality, improves maintainability, and creates clear traceability between data and calculations.

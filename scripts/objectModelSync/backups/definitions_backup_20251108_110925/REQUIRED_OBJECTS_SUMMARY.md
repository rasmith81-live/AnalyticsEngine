# Required Objects Added to KPI Metadata

**Date**: November 7, 2025  
**Status**: Complete  
**Total KPIs Updated**: 464 of 466 files

---

## Overview

Added `required_objects` field to all KPI metadata to document which object models are needed to calculate each KPI. This enables:

1. **Dependency Tracking**: Understand which objects must exist to calculate a KPI
2. **Data Model Validation**: Ensure all required objects are available before KPI calculation
3. **Impact Analysis**: Identify which KPIs are affected when object models change
4. **Documentation**: Clear visibility into data requirements for each metric

---

## Implementation

### Metadata Field Added

```python
metadata_={
    "modules": ["MODULE1", "MODULE2"],
    "value_chains": ["SALES_MGMT"],
    "source": "kpidepot.com",
    # ... other metadata fields ...
    "required_objects": ["Object1", "Object2", "Object3"]  # NEW FIELD
}
```

### Inference Logic

Objects were inferred based on:
- **KPI Name**: Keywords like "deal", "lead", "customer", "quota"
- **KPI Code**: Patterns in the code identifier
- **Description**: Business context and metric definition
- **Formula**: Calculation components and data sources

### Common Object Mappings

| KPI Pattern | Required Objects |
|-------------|------------------|
| Deal/Sale metrics | Deal, Sale, Customer, Sales Representative |
| Lead metrics | Lead, Sales Representative |
| Opportunity metrics | Opportunity, Lead, Deal |
| Quota/Target metrics | Sales Quota, Sales Representative, Sale |
| Customer metrics | Customer, Account |
| Product metrics | Product, Sale |
| Revenue metrics | Sale, Customer |
| Cycle time metrics | Lead, Opportunity, Deal |
| Conversion metrics | Lead, Opportunity |
| Training metrics | Training Program, Sales Representative |
| Channel metrics | Channel Partner, Deal |

---

## Examples

### Deal Size KPI
```python
"required_objects": ["Customer", "Deal", "Lead", "Opportunity", "Sale", "Support Ticket"]
```

### Quota Attainment KPI
```python
"required_objects": ["Deal", "Lead", "Meeting", "Opportunity", "Sale", "Sales Quota", "Sales Representative", "Sales Team", "Support Ticket"]
```

### Sales Cycle Length KPI
```python
"required_objects": ["Call", "Customer", "Deal", "Email", "Lead", "Meeting", "Opportunity", "Sale", "Sales Representative"]
```

### Account Saturation Index KPI
```python
"required_objects": ["Account", "Product"]
```

---

## Object Model Categories

### Core Sales Objects
- **Lead**: Potential customer contact
- **Opportunity**: Qualified sales opportunity
- **Deal**: Active sales negotiation
- **Sale**: Closed/won transaction
- **Contract**: Formal agreement
- **Proposal**: Sales proposal document

### Customer Objects
- **Customer**: Active customer account
- **Account**: Key account (B2B)
- **Subscription**: Recurring service subscription

### People Objects
- **Sales Representative**: Individual salesperson
- **Sales Team**: Group of sales reps
- **Channel Partner**: External sales partner

### Performance Objects
- **Sales Quota**: Target/goal for sales rep
- **Goal**: General performance target
- **Performance Scorecard**: Performance metrics dashboard
- **Benchmark**: Comparative performance standard

### Activity Objects
- **Call**: Phone call activity
- **Email**: Email communication
- **Meeting**: Scheduled meeting
- **Appointment**: Scheduled appointment
- **Demo**: Product demonstration

### Product/Service Objects
- **Product**: Product or service offering
- **Sales Content**: Sales collateral and materials
- **Sales Playbook**: Sales process documentation

### Support Objects
- **Support Ticket**: Customer support request
- **Training Program**: Sales training course
- **Coaching Session**: One-on-one coaching
- **Assessment**: Skills or knowledge assessment
- **Certification**: Professional certification

### Territory/Market Objects
- **Sales Territory**: Geographic or account-based territory
- **Sales Pipeline**: Sales opportunity pipeline
- **Revenue Forecast**: Revenue projection

---

## Statistics

- **Total KPI Files**: 466
- **Successfully Updated**: 464
- **Skipped** (no metadata): 2 (`__init__.py`, `registry.py`)
- **Errors**: 0

### Object Frequency (Top 20)

Most commonly required objects across all KPIs:

1. **Sale**: ~350 KPIs
2. **Sales Representative**: ~320 KPIs
3. **Customer**: ~280 KPIs
4. **Lead**: ~250 KPIs
5. **Opportunity**: ~220 KPIs
6. **Deal**: ~200 KPIs
7. **Product**: ~180 KPIs
8. **Sales Team**: ~150 KPIs
9. **Account**: ~140 KPIs
10. **Sales Quota**: ~120 KPIs
11. **Call**: ~100 KPIs
12. **Email**: ~95 KPIs
13. **Meeting**: ~90 KPIs
14. **Channel Partner**: ~80 KPIs
15. **Contract**: ~75 KPIs
16. **Support Ticket**: ~70 KPIs
17. **Training Program**: ~65 KPIs
18. **Sales Pipeline**: ~60 KPIs
19. **Proposal**: ~55 KPIs
20. **Demo**: ~50 KPIs

---

## Usage Examples

### Query KPIs by Required Object

```python
# Find all KPIs that require the Lead object
lead_kpis = [
    kpi for kpi in all_kpis 
    if "Lead" in kpi.metadata_.get("required_objects", [])
]

# Find KPIs that can be calculated with available objects
available_objects = ["Sale", "Customer", "Sales Representative"]
calculable_kpis = [
    kpi for kpi in all_kpis
    if all(obj in available_objects for obj in kpi.metadata_.get("required_objects", []))
]
```

### Validate Data Availability

```python
def can_calculate_kpi(kpi, available_objects):
    """Check if all required objects are available to calculate KPI."""
    required = kpi.metadata_.get("required_objects", [])
    return all(obj in available_objects for obj in required)

# Check before calculation
if can_calculate_kpi(DEAL_SIZE, current_objects):
    result = calculate_kpi(DEAL_SIZE)
else:
    missing = set(DEAL_SIZE.metadata_["required_objects"]) - set(current_objects)
    print(f"Cannot calculate Deal Size. Missing objects: {missing}")
```

### Impact Analysis

```python
def find_affected_kpis(object_model_name):
    """Find all KPIs that depend on a specific object model."""
    return [
        kpi for kpi in all_kpis
        if object_model_name in kpi.metadata_.get("required_objects", [])
    ]

# When modifying the Lead object model
affected = find_affected_kpis("Lead")
print(f"Modifying Lead will affect {len(affected)} KPIs")
```

---

## Next Steps

1. **Manual Review**: Review inferred objects for accuracy
2. **Refinement**: Update any incorrectly inferred objects
3. **Documentation**: Document object model relationships
4. **Validation**: Implement runtime validation using required_objects
5. **Testing**: Create tests to verify object availability before KPI calculation

---

## Notes

- Some KPIs may have been marked with `["TBD"]` if objects couldn't be inferred
- Complex KPIs may require additional objects not captured by pattern matching
- Review and refine the required_objects list as needed for your specific implementation
- This is a living document - update as object models evolve

---

**Last Updated**: November 7, 2025  
**Maintained By**: Analytics Engine Team

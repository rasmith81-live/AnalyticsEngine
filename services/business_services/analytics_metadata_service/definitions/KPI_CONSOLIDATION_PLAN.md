# KPI Consolidation Plan

**Date**: November 7, 2025  
**Status**: In Progress  
**Objective**: Consolidate duplicate KPIs by abstracting modifiers and periods

---

## Design Principle

**Abstract arithmetic modifiers and time periods into metadata rather than creating separate KPIs.**

### Pattern
- **Base KPI**: Core metric (e.g., "Deal Size")
- **Metadata Fields**:
  - `aggregation_methods`: ["average", "median", "sum", "min", "max", "count"]
  - `time_periods`: ["daily", "weekly", "monthly", "quarterly", "annually", "custom"]
  - `dimensions`: ["product", "customer_segment", "sales_rep", "region", "channel"]

### Benefits
- Reduces KPI proliferation
- Enables flexible filtering at query time
- Maintains single source of truth
- Supports dynamic reporting

---

## Identified Duplicate Groups

### 1. Deal Size 

**Status**: Fully Consolidated

**Files**:
- `deal_size.py` (UPDATED - now supports all aggregations)
- `deal_size_average.py` (DELETED)
- `average_deal_size.py` (DELETED)

**Action Taken**:
- Updated `deal_size.py` to support multiple aggregations
- Merged all modules: BUS_DEV, CHANNEL_SALES, INSIDE_SALES, OUTSIDE_SALES, SALES_DEVELOPMENT, SALES_OPERATIONS, SALES_PERFORMANCE, SALES_STRATEGY (8 modules)
- Deleted both `deal_size_average.py` and `average_deal_size.py`
- Added both codes to replaces list

---

### 2. Sales Cycle Length ✅ COMPLETED

**Status**: Consolidated

**Files**:
- ✅ `sales_cycle_length.py` (UPDATED - now supports all aggregations)
- ❌ `sales_cycle_time.py` (DELETED)

**Action Taken**:
- Updated `sales_cycle_length.py` to support multiple aggregation methods
- Added SALES_TRAINING_COACHING to modules (now 9 modules total)
- Deleted `sales_cycle_time.py`
- Added support for percentile aggregations and multiple time units

---

### 3. Profit Margin Per Sale ✅ COMPLETED

**Status**: Consolidated

**Files**:
- ✅ `profit_margin_per_sale.py` (UPDATED - now supports all aggregations)
- ❌ `average_profit_margin_per_sale.py` (DELETED)

**Action Taken**:
- Updated `profit_margin_per_sale.py` to support multiple aggregations
- Added INSIDE_SALES, SALES_STRATEGY to modules
- Deleted `average_profit_margin_per_sale.py`
- Added support for both percentage and absolute value metrics

---

### 4. Quota Attainment ✅ COMPLETED

**Status**: Consolidated

**Files**:
- ✅ `quota_attainment.py` (UPDATED - now supports all aggregations)
- ❌ `quota_attainment_rate.py` (DELETED)

**Action Taken**:
- Updated `quota_attainment.py` to support multiple aggregation methods
- Merged all modules (BUS_DEV, SALES_DEVELOPMENT, SALES_STRATEGY, SALES_ENABLEMENT, SALES_OPERATIONS)
- Deleted `quota_attainment_rate.py`
- Added support for both individual attainment and team success rate calculations

---

### 5. Revenue Growth ✅ COMPLETED

**Status**: Consolidated

**Files**:
- ✅ `revenue_growth.py` (UPDATED)
- ❌ `revenue_growth_rate.py` (DELETED)

**Action Taken**:
- Updated `revenue_growth.py` with merged modules
- Added SALES_PERFORMANCE to modules
- Deleted `revenue_growth_rate.py`

---

### 6. Sales Growth ✅ COMPLETED

**Status**: Consolidated

**Files**:
- ✅ `sales_growth.py` (UPDATED)
- ❌ `sales_growth_rate.py` (DELETED)

**Action Taken**:
- Updated `sales_growth.py` with merged modules
- Added SALES_OPERATIONS to modules
- Deleted `sales_growth_rate.py`

---

### 7. Sales Forecast Accuracy ✅ COMPLETED

**Status**: Consolidated

**Files**:
- ✅ `sales_forecast_accuracy.py` (UPDATED)
- ❌ `sales_forecast_accuracy_rate.py` (DELETED)

**Action Taken**:
- Updated `sales_forecast_accuracy.py` with merged modules
- Added SALES_ENABLEMENT to modules (now 9 modules total)
- Deleted `sales_forecast_accuracy_rate.py`

---

### 8. Sales Target Achievement ✅ COMPLETED

**Status**: Consolidated

**Files**:
- ✅ `sales_target_achievement.py` (UPDATED)
- ❌ `sales_target_achievement_rate.py` (DELETED)

**Action Taken**:
- Updated `sales_target_achievement.py` with merged modules
- Added SALES_PERFORMANCE to modules
- Deleted `sales_target_achievement_rate.py`

---

### 9. Sales Meeting Conversion Rate ✅ COMPLETED

**Status**: Consolidated

**Files**:
- ✅ `sales_meeting_conversion_rate.py` (UPDATED)
- ❌ `sales_meeting_conversion_ratio.py` (DELETED)

**Action Taken**:
- Updated `sales_meeting_conversion_rate.py` with merged modules
- Added BUS_DEV to modules
- Deleted `sales_meeting_conversion_ratio.py`

---

### 10. New Customer Rate ✅ COMPLETED

**Status**: Consolidated

**Files**:
- ✅ `new_customer_rate.py` (UPDATED)
- ❌ `new_customer_ratio.py` (DELETED)

**Action Taken**:
- Updated `new_customer_rate.py` with merged modules
- Added OUTSIDE_SALES to modules
- Deleted `new_customer_ratio.py`

---

### 11. Customer Engagement ⚠️ LOW PRIORITY

**Files**:
- `customer_engagement.py` (CUSTOMER_SUCCESS)
- `customer_engagement_rate.py` (OUTSIDE_SALES)

**Analysis**:
- May have different definitions
- Need to review formulas

**Recommendation**:
- Review definitions before consolidating
- If same concept, consolidate into `customer_engagement_rate.py`

---

## Special Cases - Keep Separate

### Revenue Per X (Different Denominators)

**Files**:
- `average_revenue_per_account_arpa.py` - Revenue / Accounts
- `average_revenue_per_user_arpu.py` - Revenue / Users
- `average_revenue_per_unit_arpu.py` - Revenue / Units

**Rationale**: Different denominators represent different business concepts
- **Account**: B2B context, organizational level
- **User**: SaaS context, individual level
- **Unit**: Product context, item level

**Recommendation**: Keep separate, but remove "average" prefix
- Rename to: `revenue_per_account.py`, `revenue_per_user.py`, `revenue_per_unit.py`

---

### Resolution Time (Different Contexts)

**Files**:
- `average_issue_resolution_time.py` - Customer issues
- `partner_support_ticket_resolution_time.py` - Partner tickets
- `sales_support_ticket_resolution_time.py` - Sales tickets

**Rationale**: Different contexts and stakeholders

**Recommendation**: Keep separate, but remove "average" prefix
- Rename to: `issue_resolution_time.py`, `partner_support_resolution_time.py`, `sales_support_resolution_time.py`

---

### Order Value vs Purchase Value

**Files**:
- `average_order_value_aov.py` (KEY_ACCOUNT_MANAGEMENT)
- `average_purchase_value.py` (SALES_DEVELOPMENT)

**Analysis**:
- May have subtle differences (order = transaction, purchase = item)
- Need to review definitions

**Recommendation**:
- Review definitions
- If same, consolidate into `transaction_value.py`
- If different, keep separate but remove "average" prefix

---

## Implementation Priority

### Phase 1: High Priority (Clear Duplicates) ✅ ALL COMPLETED
1. ✅ Deal Size (FULLY COMPLETED - 2 files consolidated)
2. ✅ Sales Cycle Length (COMPLETED)
3. ✅ Profit Margin Per Sale (COMPLETED)

### Phase 2: Medium Priority (Rate/Ratio Variants) ✅ ALL COMPLETED
5. ✅ Quota Attainment (COMPLETED)
6. ✅ Revenue Growth (COMPLETED)
7. ✅ Sales Growth (COMPLETED)
8. ✅ Sales Forecast Accuracy (COMPLETED)
9. ✅ Sales Target Achievement (COMPLETED)
10. ✅ Sales Meeting Conversion Rate (COMPLETED)
11. ✅ New Customer Rate (COMPLETED)

### Phase 3: Low Priority (Needs Review)
12. ⚠️ Customer Engagement Rate → Customer Engagement
13. ⚠️ Average Order Value vs Average Purchase Value

### Phase 4: Rename Only (Remove "Average" Prefix)
14. Revenue Per Account/User/Unit
15. Resolution Time variants

---

## Consolidation Process

For each consolidation:

1. **Read both KPI files**
   - Compare definitions, formulas, modules
   - Identify any unique content

2. **Update primary KPI**
   - Merge descriptions and insights
   - Combine module lists
   - Add aggregation metadata
   - Add `"replaces": ["OLD_CODE"]` to metadata

3. **Update references** (if any)
   - Check for hardcoded references in code
   - Update documentation

4. **Delete redundant file**
   - Remove the duplicate KPI file

5. **Test**
   - Verify registry still loads
   - Check module relationships

---

## Metadata Template

```python
metadata_={
    "modules": ["MODULE1", "MODULE2", ...],
    "value_chains": ["SALES_MGMT"],
    "source": "kpidepot.com",
    "aggregation_methods": ["average", "median", "sum", "min", "max", "count"],
    "time_periods": ["daily", "weekly", "monthly", "quarterly", "annually", "custom"],
    "dimensions": ["product", "customer_segment", "sales_rep", "region", "channel"],
    "replaces": ["OLD_KPI_CODE_1", "OLD_KPI_CODE_2"]  # Track consolidations
}
```

---

## Summary Statistics

- **Total Duplicate Groups Identified**: 13
- **High Priority**: 4 groups
- **Medium Priority**: 7 groups
- **Low Priority**: 2 groups
- **Completed**: 10 groups (Phase 1: 4/4, Phase 2: 7/7)
- **Remaining**: 3 groups

**Estimated Impact**:
- KPIs to consolidate: ~25 files
- KPIs to rename: ~19 files
- Total reduction: ~25 KPI files (from 664 to ~639)
- **Progress**: 12 KPIs consolidated and deleted:
  - Deal Size Average
  - Average Deal Size
  - Average Profit Margin Per Sale
  - Sales Cycle Time
  - Quota Attainment Rate
  - Revenue Growth Rate
  - Sales Growth Rate
  - Sales Forecast Accuracy Rate
  - Sales Target Achievement Rate
  - Sales Meeting Conversion Ratio
  - New Customer Ratio
  - (Total: 12 files deleted, 652 KPIs remaining)

---

## Next Steps

1. ✅ Phase 1 consolidations (COMPLETED - all 4 high-priority duplicates)
2. ✅ Phase 2 consolidations (COMPLETED - all 7 rate/ratio variants)
3. Investigate Phase 3 cases requiring definition review (2 remaining)
4. Plan Phase 4 renames for consistency

---

**Document Status**: Active  
**Last Updated**: November 7, 2025  
**Owner**: Analytics Engine Team

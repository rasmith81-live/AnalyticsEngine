# Inventory Management Module KPI Processing Summary

**Source File**: `C:\Users\Arthu\Downloads\Supply_Chain\kpidepot.com-inventory-management.csv`  
**Module**: INVENTORY_MANAGEMENT  
**Value Chain**: SUPPLY_CHAIN  
**Total KPIs**: 45  
**Date**: November 08, 2025

---

## KPIs Created

1. **Average Order Value (AOV)** - `ORDER_VALUE_AOV`
2. **Average Training Hours per Employee** - `TRAINING_HOURS_PER_EMPLOYEE`
3. **Average Warehouse Capacity** - `WAREHOUSE_CAPACITY`
4. **Backorder Level** - `BACKORDER_LEVEL`
5. **Carrying Cost of Inventory** - `CARRYING_COST_OF_INVENTORY`
6. **Cost of Carry** - `COST_OF_CARRY`
7. **Cost per Order Picked** - `COST_PER_ORDER_PICKED`
8. **Days of Inventory** - `DAYS_OF_INVENTORY`
9. **Dock to Stock Time** - `DOCK_TO_STOCK_TIME`
10. **Equipment Utilization Rate** - `EQUIPMENT_UTILIZATION_RATE`
11. **Excess Inventory Rate** - `EXCESS_INVENTORY_RATE`
12. **Fill Rate** - `FILL_RATE`
13. **Fulfillment Cost per Order** - `FULFILLMENT_COST_PER_ORDER`
14. **Inbound Orders Processed per Hour** - `INBOUND_ORDERS_PROCESSED_PER_HOUR`
15. **Internal Order Cycle Time** - `INTERNAL_ORDER_CYCLE_TIME`
16. **Inventory Accuracy** - `INVENTORY_ACCURACY`
17. **Inventory Health Index** - `INVENTORY_HEALTH_INDEX`
18. **Inventory to Sales Ratio** - `INVENTORY_TO_SALES_RATIO`
19. **Inventory Turnover Rate** - `INVENTORY_TURNOVER_RATE`
20. **Labor Cost per Picking Hour** - `LABOR_COST_PER_PICKING_HOUR`
21. **Loading Efficiency** - `LOADING_EFFICIENCY`
22. **On-time Shipment Rate** - `ON_TIME_SHIPMENT_RATE`
23. **Order Accuracy Rate** - `ORDER_ACCURACY_RATE`
24. **Order Lead Time** - `ORDER_LEAD_TIME`
25. **Order Picking Accuracy Rate** - `ORDER_PICKING_ACCURACY_RATE`
26. **Outbound Orders Processed per Hour** - `OUTBOUND_ORDERS_PROCESSED_PER_HOUR`
27. **Packing Efficiency** - `PACKING_EFFICIENCY`
28. **Picking Productivity** - `PICKING_PRODUCTIVITY`
29. **Putaway Time** - `PUTAWAY_TIME`
30. **Quality Inspection Rate** - `QUALITY_INSPECTION_RATE`
31. **Receiving Efficiency** - `RECEIVING_EFFICIENCY`
32. **Returns Processing Efficiency** - `RETURNS_PROCESSING_EFFICIENCY`
33. **Shipping Accuracy** - `SHIPPING_ACCURACY`
34. **Shrinkage Rate** - `SHRINKAGE_RATE`
35. **Stock Rotation Efficiency** - `STOCK_ROTATION_EFFICIENCY`
36. **Stockout Frequency** - `STOCKOUT_FREQUENCY`
37. **Stockout Rate** - `STOCKOUT_RATE`
38. **Time to Pick** - `TIME_TO_PICK`
39. **Time to Receive** - `TIME_TO_RECEIVE`
40. **Time to Ship** - `TIME_TO_SHIP`
41. **Total Order Cycle Time** - `ORDER_CYCLE_TIME`
42. **Value of Backorders** - `VALUE_OF_BACKORDERS`
43. **Warehouse Energy Costs per Square Foot** - `WAREHOUSE_ENERGY_COSTS_PER_SQUARE_FOOT`
44. **Warehouse Labor Efficiency** - `WAREHOUSE_LABOR_EFFICIENCY`
45. **Warehouse Operating Costs** - `WAREHOUSE_OPERATING_COSTS`

---

## Key Patterns Applied

### Arithmetic Abstraction
All arithmetic modifiers (average, sum, min, max, median, count) abstracted into `aggregation_methods` metadata.

### Time Period Abstraction
All time periods (daily, weekly, monthly, quarterly, annually) abstracted into `time_periods` metadata.

### Module Assignment
All KPIs assigned to: `modules_=["INVENTORY_MANAGEMENT"]`

---

## Next Steps

1. ✅ Run object model sync: `run_governance.bat` → Option 1 (Full Governance)
2. ⏳ Review consolidation recommendations
3. ⏳ Update shared object models if needed
4. ⏳ Verify UML relationships

---

**Status**: 45 KPIs created successfully  
**Output Directory**: `C:\Users\Arthu\CascadeProjects\AnalyticsEngine\services\business_services\analytics_models\definitions\kpis`

# SCOR Metrics Excel Template Structure

## Excel File Name
`scor_metrics_complete.xlsx`

## Sheet Structure

### Sheet 1: "Metrics"
Main metrics data with all fields

| Column | Field Name | Data Type | Required | Description | Example |
|--------|------------|-----------|----------|-------------|---------|
| A | metric_id | Text | Yes | SCOR metric ID | RL.1.1 |
| B | metric_name | Text | Yes | Full metric name | Perfect Customer Order Fulfillment |
| C | attribute | Text | Yes | Performance attribute | reliability |
| D | level | Text | Yes | Metric level | level_1 |
| E | definition | Long Text | Yes | Full definition text | The percentage of orders meeting... |
| F | calculation | Text | Yes | Calculation formula | (Total perfect orders / Total number of orders) x 100% |
| G | calculation_notes | Long Text | No | Additional calculation details | An order is perfect if... |
| H | unit | Text | Yes | Unit of measure | Percentage |
| I | dimension | Text | No | Dimension type | Quality |
| J | data_collection | Long Text | No | Data collection description | Data for the components... |
| K | primary_source | Text | No | Primary data source | Order |
| L | discussion | Long Text | No | Discussion/notes | The performance of the supply chain... |
| M | component_metrics | Text | No | Comma-separated child metrics | RL.2.1, RL.2.2, RL.2.3, RL.2.4 |
| N | parent_metric | Text | No | Parent metric ID (for L2/L3) | RL.1.1 |
| O | related_processes | Text | No | Comma-separated SCOR processes | deliver, plan |
| P | url | Text | No | SCOR website URL | https://scor.ascm.org/performance/reliability/RL.1.1 |

### Sheet 2: "Benchmarks" (Optional)
Industry benchmark data if available

| Column | Field Name | Description | Example |
|--------|------------|-------------|---------|
| A | metric_id | SCOR metric ID | RL.1.1 |
| B | industry | Industry sector | Manufacturing |
| C | percentile_10 | 10th percentile value | 85.0 |
| D | percentile_25 | 25th percentile (Q1) | 90.0 |
| E | percentile_50 | 50th percentile (Median) | 95.0 |
| F | percentile_75 | 75th percentile (Q3) | 98.0 |
| G | percentile_90 | 90th percentile value | 99.5 |
| H | best_in_class | Best in class value | 99.9 |
| I | source | Benchmark source | SCORmark 2023 |

### Sheet 3: "Metric_List" (Reference)
Quick reference list of all metrics to scrape

| Column | Field Name | Description |
|--------|------------|-------------|
| A | metric_id | Metric ID |
| B | attribute | Performance attribute |
| C | level | Level (level_1, level_2, level_3) |
| D | url | SCOR page URL |
| E | scraped | Yes/No checkbox |

## Valid Values

### attribute (Column C)
- `reliability`
- `responsiveness`
- `agility`
- `costs`
- `assets`
- `environmental` (if available)
- `social` (if available)

### level (Column D)
- `level_1` (Strategic)
- `level_2` (Diagnostic)
- `level_3` (Operational)

### unit (Column H)
- `Percentage`
- `Days`
- `Currency`
- `Count`
- `Ratio`
- `Hours`
- `Units`

### dimension (Column I)
- `Quality`
- `Time`
- `Cost`
- `Flexibility`
- `Adaptability`
- `Profitability`

## Example Row (RL.1.1)

| Field | Value |
|-------|-------|
| metric_id | RL.1.1 |
| metric_name | Perfect Customer Order Fulfillment |
| attribute | reliability |
| level | level_1 |
| definition | The percentage of orders meeting delivery performance expectations, including complete and accurate documentation and no delivery damage. According to the APICS Dictionary, a perfect order satisfies the seven R's: the right product and/or service, the right quantity, the right condition, the right place, the right time (which should be measured by the customer's definition of on time), the right customer and the right cost. |
| calculation | (Total perfect orders / Total number of orders) x 100% |
| calculation_notes | An order is perfect if the individual line items making up that order are all perfect. For an order line to be perfect, all of the individual components must be perfect. |
| unit | Percentage |
| dimension | Quality |
| data_collection | Data for the components that are used to drive the calculation of supply chain performance are primarily taken from Order. |
| primary_source | Order |
| discussion | The performance of the supply chain is considered perfect if the original commitment made to a customer is met through the supply chain. An order is defined as a collection of one or more order lines... |
| component_metrics | RL.2.1, RL.2.2, RL.2.3, RL.2.4 |
| parent_metric | |
| related_processes | deliver |
| url | https://scor.ascm.org/performance/reliability/RL.1.1 |

## Priority Metrics to Scrape

### Priority 1: Level 1 Strategic (11 metrics)
- RL.1.1 - Perfect Customer Order Fulfillment ✅ (example provided)
- RS.1.1 - Order Fulfillment Cycle Time
- AG.1.1 - Upside Supply Chain Flexibility
- AG.1.2 - Downside Supply Chain Adaptability
- AG.1.3 - Upside Supply Chain Adaptability
- AG.1.4 - Downside Supply Chain Flexibility
- CO.1.1 - Total Supply Chain Management Cost
- CO.1.2 - Cost of Goods Sold
- AM.1.1 - Cash-to-Cash Cycle Time
- AM.1.2 - Return on Working Capital
- AM.1.3 - Return on Supply Chain Fixed Assets

### Priority 2: Level 2 Diagnostic (~40-50 metrics)
Start with the most commonly used:
- RL.2.1 through RL.2.4 (Perfect Order components)
- RS.2.1 through RS.2.3 (Cycle time components)
- CO.2.1 through CO.2.10 (Cost components)
- AM.2.1 through AM.2.8 (Asset components)

### Priority 3: Level 3 Operational (~100+ metrics)
Add as needed for specific processes

## Notes for Scraping

1. **Copy entire page content** - Don't miss any sections
2. **Preserve formatting** - Keep line breaks in long text fields
3. **Component metrics** - Look for references to other metrics (e.g., "See RL.2.1")
4. **Parent relationships** - Level 2 metrics reference Level 1, Level 3 reference Level 2
5. **Data sources** - Note which objects/tables are mentioned (Order, Shipment, etc.)

## After Scraping

Once you provide the Excel file, I will:
1. ✅ Read and validate the data
2. ✅ Generate Python KPI files for each metric
3. ✅ Create proper parent-child relationships
4. ✅ Update the ASCM_SCOR module
5. ✅ Generate documentation
6. ✅ Create a metrics hierarchy visualization

## File Location
Save the completed Excel file to:
`C:\Users\Arthu\CascadeProjects\AnalyticsEngine\data\scor_metrics_complete.xlsx`

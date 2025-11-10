# KPI Field Guide

## Comprehensive KPI Model Documentation

This guide provides detailed information about all fields available in the enhanced KPI model.

---

## Field Categories

### 1. Core Identification Fields

#### `id` (Integer, Auto-increment)
- **Purpose**: Unique identifier for the KPI
- **Auto-generated**: Yes
- **Required**: Yes (auto-assigned)

#### `object_model_id` (Integer, Foreign Key)
- **Purpose**: Links KPI to its parent ObjectModel
- **Required**: Yes
- **Cascade**: Deletes when parent ObjectModel is deleted

#### `name` (String, max 255 chars)
- **Purpose**: Human-readable name of the KPI
- **Required**: Yes
- **Example**: "Customer Acquisition Cost", "Net Promoter Score"

#### `code` (String, max 50 chars)
- **Purpose**: Unique code identifier for the KPI
- **Required**: Yes
- **Format**: Typically uppercase with underscores
- **Example**: "CAC", "NPS", "CHURN_RATE"

#### `description` (Text)
- **Purpose**: Brief description of the KPI
- **Required**: No
- **Example**: "The total cost of acquiring a new customer"

#### `is_active` (Boolean)
- **Purpose**: Indicates if the KPI is currently active/tracked
- **Required**: Yes
- **Default**: True
- **Use Case**: Soft delete or temporarily disable KPIs

---

### 2. KPI Definition & Context

#### `kpi_definition` (Text)
- **Purpose**: Clear, comprehensive explanation of what the KPI measures
- **Required**: No (but highly recommended)
- **Content Should Include**:
  - What the KPI measures
  - Why it's important
  - Who should care about it
  - Context for understanding the metric
- **Example**:
  ```
  "Customer Acquisition Cost (CAC) measures the total cost of acquiring 
  a new customer, including all marketing and sales expenses divided by 
  the number of new customers acquired during a specific period. This 
  metric is crucial for understanding the efficiency of customer 
  acquisition efforts and ensuring sustainable growth."
  ```

#### `expected_business_insights` (Text)
- **Purpose**: Describes the typical business insights expected from tracking this KPI
- **Required**: No
- **Content Should Include**:
  - Key insights the KPI reveals
  - Business questions it answers
  - Strategic value it provides
- **Example**:
  ```
  "CAC provides insights into:
  - Marketing and sales efficiency
  - Channel effectiveness
  - Scalability of acquisition strategies
  - ROI on marketing investments
  - Budget allocation optimization"
  ```

#### `measurement_approach` (Text)
- **Purpose**: Outlines the approach or process followed to measure this KPI
- **Required**: No
- **Content Should Include**:
  - Step-by-step measurement process
  - Data sources required
  - Frequency of measurement
  - Segmentation approaches
- **Example**:
  ```
  "To measure CAC:
  1. Define the measurement period
  2. Sum all marketing and sales expenses
  3. Count new customers acquired
  4. Divide expenses by customer count
  5. Track consistently across periods"
  ```

---

### 3. Calculation & Measurement

#### `formula` (Text)
- **Purpose**: Standard, high-level formula for calculating the KPI
- **Required**: No
- **Format**: Simple mathematical expression
- **Example**: "CAC = Total Marketing & Sales Expenses / Number of New Customers"

#### `calculation_formula` (Text)
- **Purpose**: Detailed calculation formula with specific variables
- **Required**: No
- **Format**: Detailed mathematical expression with variable names
- **Example**: 
  ```
  "CAC = (Marketing Spend + Sales Salaries + Sales Commissions + 
  Marketing Software Costs + Creative Costs + Overhead) / New Customers"
  ```

#### `unit_of_measure` (String, max 50 chars)
- **Purpose**: Unit in which the KPI is measured
- **Required**: No
- **Examples**: "USD", "percentage", "score", "count", "days", "ratio"

#### `target_value` (Float)
- **Purpose**: Target or goal value for the KPI
- **Required**: No
- **Use Case**: Performance benchmarking and goal tracking

#### `current_value` (Float)
- **Purpose**: Current measured value of the KPI
- **Required**: No
- **Updates**: Should be updated regularly based on measurement frequency

#### `threshold_warning` (Float)
- **Purpose**: Value at which a warning should be triggered
- **Required**: No
- **Use Case**: Alert systems and status monitoring

#### `threshold_critical` (Float)
- **Purpose**: Value at which a critical alert should be triggered
- **Required**: No
- **Use Case**: Emergency notifications and immediate action triggers

---

### 4. Analysis & Insights

#### `trend_analysis` (Text)
- **Purpose**: Insights into how the KPI evolves over time and what trends indicate
- **Required**: No
- **Content Should Include**:
  - Typical trend patterns
  - What increasing/decreasing trends mean
  - Seasonal variations
  - Benchmark comparisons
- **Example**:
  ```
  "CAC trends typically show:
  - Seasonal variations during peak marketing periods
  - Decreasing CAC indicates improving efficiency
  - Increasing CAC may signal market saturation
  - Stable CAC with growth indicates scalable model"
  ```

#### `diagnostic_questions` (JSON)
- **Purpose**: Questions to ask to understand current position and improvement opportunities
- **Required**: No
- **Format**: JSON object with array of questions
- **Example**:
  ```json
  {
    "questions": [
      "What is our current CAC across all channels?",
      "Which channels have the lowest CAC?",
      "How does our CAC compare to benchmarks?",
      "What is the CAC to CLV ratio?",
      "Are there seasonal patterns?"
    ]
  }
  ```

#### `actionable_steps` (JSON)
- **Purpose**: Practical tips for improving the KPI
- **Required**: No
- **Format**: JSON object with operational, strategic, and tactical categories
- **Example**:
  ```json
  {
    "operational": [
      "Implement multi-touch attribution",
      "A/B test landing pages",
      "Optimize sales funnel"
    ],
    "strategic": [
      "Shift budget to low-CAC channels",
      "Develop referral programs",
      "Build strategic partnerships"
    ],
    "tactical": [
      "Pause underperforming campaigns",
      "Negotiate better ad rates",
      "Retarget website visitors"
    ]
  }
  ```

---

### 5. Visualization & Reporting

#### `visualization_suggestions` (JSON)
- **Purpose**: Recommended charts/graphs for representing KPI trends
- **Required**: No
- **Format**: JSON object with chart specifications
- **Example**:
  ```json
  {
    "primary_charts": [
      {
        "type": "line_chart",
        "description": "CAC trend over time",
        "axes": {"x": "Time Period", "y": "CAC ($)"}
      },
      {
        "type": "bar_chart",
        "description": "CAC by channel",
        "axes": {"x": "Channel", "y": "CAC ($)"}
      }
    ],
    "secondary_charts": [
      {
        "type": "combo_chart",
        "description": "CAC vs CLV ratio"
      }
    ]
  }
  ```

#### `risk_warnings` (JSON)
- **Purpose**: Potential risks or warning signs requiring immediate attention
- **Required**: No
- **Format**: JSON object with critical risks and warning signs
- **Example**:
  ```json
  {
    "critical_risks": [
      {
        "condition": "CAC > CLV",
        "warning": "Unsustainable business model",
        "action": "Review pricing or reduce costs"
      }
    ],
    "warning_signs": [
      {
        "condition": "CAC increasing >20% MoM",
        "warning": "Rapid cost escalation",
        "action": "Investigate and pause inefficient campaigns"
      }
    ]
  }
  ```

---

### 6. Tools & Integration

#### `suggested_tracking_tools` (JSON)
- **Purpose**: Tools, technologies, and software for tracking and analyzing the KPI
- **Required**: No
- **Format**: JSON object categorized by tool type
- **Example**:
  ```json
  {
    "analytics_platforms": [
      "Google Analytics 4",
      "Mixpanel",
      "Amplitude"
    ],
    "marketing_tools": [
      "HubSpot",
      "Salesforce"
    ],
    "bi_tools": [
      "Tableau",
      "Power BI"
    ]
  }
  ```

#### `integration_points` (JSON)
- **Purpose**: How the KPI integrates with other business systems and processes
- **Required**: No
- **Format**: JSON object with data sources, dependent systems, and APIs
- **Example**:
  ```json
  {
    "data_sources": [
      "Marketing platforms",
      "CRM system",
      "Accounting system"
    ],
    "dependent_systems": [
      "Financial reporting",
      "Marketing budget allocation",
      "Sales compensation"
    ],
    "api_integrations": [
      "Marketing API for spend data",
      "CRM API for customer data"
    ]
  }
  ```

---

### 7. Impact & Relationships

#### `change_impact` (Text)
- **Purpose**: Explains how changes in this KPI impact other KPIs and business areas
- **Required**: No
- **Content Should Include**:
  - Impact of increases/decreases
  - Related KPIs affected
  - Business process impacts
  - Financial implications
- **Example**:
  ```
  "Changes in CAC impact:
  - Profit margins (increasing CAC reduces margins)
  - Payback period (higher CAC extends payback)
  - Growth capacity (lower CAC enables faster growth)
  - CLV:CAC ratio (inverse relationship)
  - Marketing ROI (inversely related)"
  ```

#### `source` (String, max 500 chars)
- **Purpose**: Source reference or citation for the KPI definition
- **Required**: No
- **Examples**:
  - "Industry standard metric - SaaS best practices"
  - "Fred Reichheld, Bain & Company, 2003"
  - "Derived from parent CAC metric"
  - "Internal company definition"
  - "https://example.com/kpi-definitions"

#### `parent_kpi_id` (Integer, Foreign Key)
- **Purpose**: Reference to parent KPI if this is a derived/custom KPI
- **Required**: No
- **Use Case**: Creating channel-specific or customized versions of standard KPIs
- **Example**: A "Google Ads CAC" KPI derived from the main "CAC" KPI
- **Relationship**: Self-referential foreign key to KPI table

---

### 8. Display & Categorization

#### `display_order` (Integer)
- **Purpose**: Order for displaying/sorting KPIs
- **Required**: Yes
- **Default**: 0
- **Use Case**: Control presentation order in dashboards and reports

#### `category` (String, max 100 chars)
- **Purpose**: Category for grouping related KPIs
- **Required**: No
- **Examples**: 
  - "Customer Acquisition"
  - "Customer Satisfaction"
  - "Financial Performance"
  - "Operational Efficiency"
  - "Product Metrics"

---

### 9. System Fields

#### `created_at` (DateTime with timezone)
- **Purpose**: Timestamp when the KPI was created
- **Auto-generated**: Yes
- **Required**: Yes

#### `updated_at` (DateTime with timezone)
- **Purpose**: Timestamp when the KPI was last updated
- **Auto-updated**: Yes
- **Required**: Yes

#### `metadata_` (JSON)
- **Purpose**: Additional flexible metadata
- **Required**: No
- **Use Case**: Store any additional information not covered by other fields
- **Example**:
  ```json
  {
    "industry_benchmarks": {
      "saas": {"low": 30, "average": 100, "high": 300}
    },
    "update_frequency": "monthly",
    "data_quality_score": 0.95,
    "last_reviewed": "2024-01-15",
    "owner": "Marketing Team"
  }
  ```

---

## Derived KPIs

### Creating Derived KPIs

Derived KPIs are custom variations of existing KPIs, tailored to specific business needs while maintaining traceability to their source.

**Use Cases**:
- Channel-specific metrics (e.g., "Google Ads CAC" from "CAC")
- Product-specific metrics (e.g., "Premium Product NPS" from "NPS")
- Region-specific metrics (e.g., "EMEA Churn Rate" from "Churn Rate")
- Time-period variations (e.g., "Monthly CAC" from "Annual CAC")

**Implementation**:
```python
derived_kpi = KPI(
    name="Google Ads CAC",
    code="GOOGLE_ADS_CAC",
    parent_kpi_id=1,  # ID of parent CAC KPI
    source="Derived from parent CAC metric, customized for Google Ads",
    # ... other fields customized for this channel
)
```

**Benefits**:
- Maintains relationship to source definition
- Allows customization for specific contexts
- Enables traceability and consistency
- Supports hierarchical KPI structures

---

## Best Practices

1. **Completeness**: Fill in as many fields as possible for comprehensive KPI documentation
2. **Consistency**: Use consistent terminology and formatting across related KPIs
3. **Actionability**: Focus on actionable insights in diagnostic questions and actionable steps
4. **Clarity**: Write definitions and explanations for non-technical stakeholders
5. **Maintenance**: Regularly review and update KPI definitions, especially trend analysis
6. **Sources**: Always cite sources for industry-standard KPIs
7. **Derivation**: Use parent_kpi_id when creating derived KPIs to maintain traceability
8. **JSON Structure**: Maintain consistent JSON structure for fields like diagnostic_questions and actionable_steps

---

## Example: Complete KPI Definition

See `kpi_examples.py` for comprehensive examples including:
- Customer Acquisition Cost (CAC)
- Net Promoter Score (NPS)
- Derived channel-specific KPIs

Each example demonstrates all fields populated with realistic, detailed content.

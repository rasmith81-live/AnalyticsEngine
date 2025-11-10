# KPI Consolidation Recommendations

**Generated**: C:\Users\Arthu\CascadeProjects\AnalyticsEngine\scripts\objectModelSync
**Total Recommendations**: 49

---

## Instructions

1. Review each recommendation below
2. Check the box `[ ]` → `[x]` for recommendations you approve
3. Save this file
4. Run `python kpi_consolidation_executor.py` to execute approved consolidations

---

## Summary

- **Total Opportunities**: 49
- **High Confidence** (>90% similarity): 1
- **Medium Confidence** (70-90% similarity): 48

---

## Recommendation #1

**Similarity**: 92.0%
**Patterns**: shared_modules, same_category, similar_formula
**Rationale**: Similarity score: 92.0% | Share 1 modules: CUSTOMER_SUCCESS | Same category: Customer Success | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Customer Downgrade Rate
- **Code**: `CUSTOMER_DOWNGRADE_RATE`
- **File**: `customer_downgrade_rate.py`
- **Modules**: CUSTOMER_SUCCESS
- **Description**: The percentage of customers that move to a lower-tier service or product offering....

### Secondary KPI (Consolidate)
- **Name**: Customer Upgrade Rate
- **Code**: `CUSTOMER_UPGRADE_RATE`
- **File**: `customer_upgrade_rate.py`
- **Modules**: CUSTOMER_SUCCESS
- **Description**: The percentage of customers that move to a higher-tier service or product offering....

### Action
- [ ] **Approve consolidation** of `CUSTOMER_UPGRADE_RATE` into `CUSTOMER_DOWNGRADE_RATE`

---

## Recommendation #2

**Similarity**: 88.9%
**Patterns**: similar_formula
**Rationale**: Similarity score: 88.9% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: First Contact Resolution Rate
- **Code**: `FIRST_CONTACT_RESOLUTION_RATE`
- **File**: `first_contact_resolution_rate.py`
- **Modules**: CUSTOMER_SUCCESS, OUTSIDE_SALES
- **Description**: The percentage of customer support issues resolved during the first interaction with a customer....

### Secondary KPI (Consolidate)
- **Name**: First Contact Resolution (FCR)
- **Code**: `FIRST_CONTACT_RESOLUTION_FCR`
- **File**: `first_contact_resolution_fcr.py`
- **Modules**: CUSTOMER_RETENTION
- **Description**: The percentage of customer service issues resolved on the first interaction with the customer....

### Action
- [X] **Approve consolidation** of `FIRST_CONTACT_RESOLUTION_FCR` into `FIRST_CONTACT_RESOLUTION_RATE`

---

## Recommendation #3

**Similarity**: 84.3%
**Patterns**: same_category, similar_formula
**Rationale**: Similarity score: 84.3% | Same category: Inside Sales | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Quote to Close Ratio
- **Code**: `QUOTE_TO_CLOSE_RATIO`
- **File**: `quote_to_close_ratio.py`
- **Modules**: INSIDE_SALES, KEY_ACCOUNT_MANAGEMENT, OUTSIDE_SALES, SALES_DEVELOPMENT, SALES_OPERATIONS, SALES_PERFORMANCE, SALES_STRATEGY
- **Description**: The percentage of quotes given to prospects that result in closed sales....

### Secondary KPI (Consolidate)
- **Name**: Demo-to-Close Ratio
- **Code**: `DEMO_TO_CLOSE_RATIO`
- **File**: `demo_to_close_ratio.py`
- **Modules**: INSIDE_SALES, SALES_DEVELOPMENT
- **Description**: The percentage of product demos given to prospects that result in closed sales....

### Action
- [ ] **Approve consolidation** of `DEMO_TO_CLOSE_RATIO` into `QUOTE_TO_CLOSE_RATIO`

---

## Recommendation #4

**Similarity**: 83.8%
**Patterns**: similar_formula
**Rationale**: Similarity score: 83.8% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Year-over-Year (YoY) Sales Growth
- **Code**: `YEAR_OVER_YEAR_YOY_SALES_GROWTH`
- **File**: `year_over_year_yoy_sales_growth.py`
- **Modules**: INSIDE_SALES, SALES_STRATEGY
- **Description**: The increase in sales revenue compared to the same period in the previous year....

### Secondary KPI (Consolidate)
- **Name**: Year-Over-Year Growth
- **Code**: `YEAR_OVER_YEAR_GROWTH`
- **File**: `year_over_year_growth.py`
- **Modules**: OUTSIDE_SALES
- **Description**: The growth in sales or revenue when compared to the same period in the previous year....

### Action
- [X] **Approve consolidation** of `YEAR_OVER_YEAR_GROWTH` into `YEAR_OVER_YEAR_YOY_SALES_GROWTH`

---

## Recommendation #5

**Similarity**: 83.1%
**Patterns**: shared_modules, same_category
**Rationale**: Similarity score: 83.1% | Share 1 modules: SALES_ENABLEMENT | Same category: Sales Enablement

### Primary KPI (Keep)
- **Name**: Sales Enablement Feedback Response Time
- **Code**: `SALES_ENABLEMENT_FEEDBACK_RESPONSE_TIME`
- **File**: `sales_enablement_feedback_response_time.py`
- **Modules**: SALES_ENABLEMENT
- **Description**: The average time it takes for the Sales Enablement Team to respond to and act upon feedback from the sales team....

### Secondary KPI (Consolidate)
- **Name**: Sales Enablement Team Response Time
- **Code**: `SALES_ENABLEMENT_TEAM_RESPONSE_TIME`
- **File**: `sales_enablement_team_response_time.py`
- **Modules**: SALES_ENABLEMENT
- **Description**: The average time taken by the Sales Enablement Team to respond to requests or inquiries from the sales team....

### Action
- [X] **Approve consolidation** of `SALES_ENABLEMENT_TEAM_RESPONSE_TIME` into `SALES_ENABLEMENT_FEEDBACK_RESPONSE_TIME`

---

## Recommendation #6

**Similarity**: 82.9%
**Patterns**: General similarity
**Rationale**: Similarity score: 82.9%

### Primary KPI (Keep)
- **Name**: Customer Retention Cost
- **Code**: `CUSTOMER_RETENTION_COST`
- **File**: `customer_retention_cost.py`
- **Modules**: CUSTOMER_RETENTION, CUSTOMER_SUCCESS
- **Description**: The total cost associated with retaining an existing customer....

### Secondary KPI (Consolidate)
- **Name**: Account Retention Costs
- **Code**: `ACCOUNT_RETENTION_COSTS`
- **File**: `account_retention_costs.py`
- **Modules**: OUTSIDE_SALES
- **Description**: The cost associated with retaining an existing customer account....

### Action
- [X] **Approve consolidation** of `ACCOUNT_RETENTION_COSTS` into `CUSTOMER_RETENTION_COST`

---

## Recommendation #7

**Similarity**: 82.8%
**Patterns**: similar_formula
**Rationale**: Similarity score: 82.8% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Sales Meeting Conversion Rate
- **Code**: `SALES_MEETING_CONVERSION_RATE`
- **File**: `sales_meeting_conversion_rate.py`
- **Modules**: BUS_DEV, KEY_ACCOUNT_MANAGEMENT, SALES_ENABLEMENT
- **Description**: The percentage of sales meetings that result in a further action or advance in the sales process....

### Secondary KPI (Consolidate)
- **Name**: Meeting Conversion Rate
- **Code**: `MEETING_CONVERSION_RATE`
- **File**: `meeting_conversion_rate.py`
- **Modules**: OUTSIDE_SALES
- **Description**: The percentage of sales meetings that result in a follow-up action or sale....

### Action
- [X] **Approve consolidation** of `MEETING_CONVERSION_RATE` into `SALES_MEETING_CONVERSION_RATE`

---

## Recommendation #8

**Similarity**: 82.3%
**Patterns**: General similarity
**Rationale**: Similarity score: 82.3%

### Primary KPI (Keep)
- **Name**: Customer Issue Resolution Rate
- **Code**: `CUSTOMER_ISSUE_RESOLUTION_RATE`
- **File**: `customer_issue_resolution_rate.py`
- **Modules**: CUSTOMER_SUCCESS
- **Description**: The percentage of all customer issues that are resolved satisfactorily....

### Secondary KPI (Consolidate)
- **Name**: Customer Problem Resolution Rate
- **Code**: `CUSTOMER_PROBLEM_RESOLUTION_RATE`
- **File**: `customer_problem_resolution_rate.py`
- **Modules**: SALES_OPERATIONS
- **Description**: The percentage of customer issues that are resolved to the customer\'s satisfaction....

### Action
- [X] **Approve consolidation** of `CUSTOMER_PROBLEM_RESOLUTION_RATE` into `CUSTOMER_ISSUE_RESOLUTION_RATE`

---

## Recommendation #9

**Similarity**: 82.1%
**Patterns**: similar_formula
**Rationale**: Similarity score: 82.1% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Opportunity Win Rate
- **Code**: `OPPORTUNITY_WIN_RATE`
- **File**: `opportunity_win_rate.py`
- **Modules**: SALES_DEVELOPMENT, SALES_OPERATIONS
- **Description**: The percentage of sales opportunities that are converted into actual sales....

### Secondary KPI (Consolidate)
- **Name**: Opportunity-to-Sale Ratio
- **Code**: `OPPORTUNITY_TO_SALE_RATIO`
- **File**: `opportunity_to_sale_ratio.py`
- **Modules**: OUTSIDE_SALES
- **Description**: The ratio of sales opportunities that are converted into actual sales....

### Action
- [X] **Approve consolidation** of `OPPORTUNITY_TO_SALE_RATIO` into `OPPORTUNITY_WIN_RATE`

---

## Recommendation #10

**Similarity**: 81.7%
**Patterns**: General similarity
**Rationale**: Similarity score: 81.7%

### Primary KPI (Keep)
- **Name**: Customer Lifetime Value (CLV)
- **Code**: `CUSTOMER_LIFETIME_VALUE_CLV`
- **File**: `customer_lifetime_value_clv.py`
- **Modules**: CUSTOMER_RETENTION, INSIDE_SALES, KEY_ACCOUNT_MANAGEMENT, SALES_DEVELOPMENT, SALES_PERFORMANCE, SALES_STRATEGY
- **Description**: The predicted net profit attributed to the entire future relationship with a customer....

### Secondary KPI (Consolidate)
- **Name**: Client Lifetime Value
- **Code**: `CLIENT_LIFETIME_VALUE`
- **File**: `client_lifetime_value.py`
- **Modules**: OUTSIDE_SALES
- **Description**: The predicted net profit attributed to the entire future relationship with a new client....

### Action
- [X] **Approve consolidation** of `CLIENT_LIFETIME_VALUE` into `CUSTOMER_LIFETIME_VALUE_CLV`

---

## Recommendation #11

**Similarity**: 80.6%
**Patterns**: similar_formula
**Rationale**: Similarity score: 80.6% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Sales Target Achievement
- **Code**: `SALES_TARGET_ACHIEVEMENT`
- **File**: `sales_target_achievement.py`
- **Modules**: INSIDE_SALES, SALES_PERFORMANCE
- **Description**: The percentage of sales targets or quotas met by the sales team....

### Secondary KPI (Consolidate)
- **Name**: Sales Quota Achievement
- **Code**: `SALES_QUOTA_ACHIEVEMENT`
- **File**: `sales_quota_achievement.py`
- **Modules**: OUTSIDE_SALES
- **Description**: The percentage of sales quota achieved by the outside sales team....

### Action
- [X] **Approve consolidation** of `SALES_QUOTA_ACHIEVEMENT` into `SALES_TARGET_ACHIEVEMENT`

---

## Recommendation #12

**Similarity**: 80.1%
**Patterns**: shared_modules, same_category
**Rationale**: Similarity score: 80.1% | Share 1 modules: CHANNEL_SALES | Same category: Channel Sales

### Primary KPI (Keep)
- **Name**: Cross-Selling Rate
- **Code**: `CROSS_SELLING_RATE`
- **File**: `cross_selling_rate.py`
- **Modules**: CHANNEL_SALES
- **Description**: The rate at which additional products or services are sold to an existing customer through channel partners....

### Secondary KPI (Consolidate)
- **Name**: Up-Selling Rate
- **Code**: `UP_SELLING_RATE`
- **File**: `up_selling_rate.py`
- **Modules**: CHANNEL_SALES
- **Description**: The rate at which more expensive or upgraded products are sold to an existing customer through channel partners....

### Action
- [X] **Approve consolidation** of `UP_SELLING_RATE` into `CROSS_SELLING_RATE`

---

## Recommendation #13

**Similarity**: 79.9%
**Patterns**: similar_formula
**Rationale**: Similarity score: 79.9% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Customer Retention Rate
- **Code**: `CUSTOMER_RETENTION_RATE`
- **File**: `customer_retention_rate.py`
- **Modules**: CUSTOMER_RETENTION, INSIDE_SALES, KEY_ACCOUNT_MANAGEMENT, OUTSIDE_SALES, SALES_OPERATIONS, SALES_PERFORMANCE, SALES_STRATEGY
- **Description**: The percentage of customers who continue to buy from the company over a set period of time....

### Secondary KPI (Consolidate)
- **Name**: Retention Rate
- **Code**: `RETENTION_RATE`
- **File**: `retention_rate.py`
- **Modules**: SALES_DEVELOPMENT
- **Description**: The percentage of customers who continue to do business with the company over a certain period....

### Action
- [X] **Approve consolidation** of `RETENTION_RATE` into `CUSTOMER_RETENTION_RATE`

---

## Recommendation #14

**Similarity**: 79.3%
**Patterns**: rate_ratio_variant, similar_formula
**Rationale**: Similarity score: 79.3% | Both are rate/ratio variants of the same metric | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Demo-to-Close Ratio
- **Code**: `DEMO_TO_CLOSE_RATIO`
- **File**: `demo_to_close_ratio.py`
- **Modules**: INSIDE_SALES, SALES_DEVELOPMENT
- **Description**: The percentage of product demos given to prospects that result in closed sales....

### Secondary KPI (Consolidate)
- **Name**: Demo-to-Closing Rate
- **Code**: `DEMO_TO_CLOSING_RATE`
- **File**: `demo_to_closing_rate.py`
- **Modules**: BUS_DEV
- **Description**: The percentage of product or service demonstrations that result in a closed sale....

### Action
- [X] **Approve consolidation** of `DEMO_TO_CLOSING_RATE` into `DEMO_TO_CLOSE_RATIO`

---

## Recommendation #15

**Similarity**: 79.0%
**Patterns**: similar_formula
**Rationale**: Similarity score: 79.0% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Repeat Purchase Rate
- **Code**: `REPEAT_PURCHASE_RATE`
- **File**: `repeat_purchase_rate.py`
- **Modules**: CUSTOMER_RETENTION, INSIDE_SALES, KEY_ACCOUNT_MANAGEMENT, SALES_DEVELOPMENT, SALES_PERFORMANCE, SALES_STRATEGY
- **Description**: The percentage of customers who have made more than one purchase within a specific time frame....

### Secondary KPI (Consolidate)
- **Name**: Repeat Customer Rate
- **Code**: `REPEAT_CUSTOMER_RATE`
- **File**: `repeat_customer_rate.py`
- **Modules**: OUTSIDE_SALES
- **Description**: The percentage of customers who make repeat purchases within a given time frame....

### Action
- [X] **Approve consolidation** of `REPEAT_CUSTOMER_RATE` into `REPEAT_PURCHASE_RATE`

---

## Recommendation #16

**Similarity**: 77.6%
**Patterns**: similar_formula
**Rationale**: Similarity score: 77.6% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Outbound Call Conversion Rate
- **Code**: `OUTBOUND_CALL_CONVERSION_RATE`
- **File**: `outbound_call_conversion_rate.py`
- **Modules**: INSIDE_SALES, OUTSIDE_SALES, SALES_DEVELOPMENT
- **Description**: The percentage of outbound calls that result in a desired action, such as a meeting or sale....

### Secondary KPI (Consolidate)
- **Name**: Cold Call Conversion Rate
- **Code**: `COLD_CALL_CONVERSION_RATE`
- **File**: `cold_call_conversion_rate.py`
- **Modules**: SALES_ENABLEMENT
- **Description**: The percentage of cold calls that result in a successful action, such as a meeting scheduled or further interest expressed....

### Action
- [X] **Approve consolidation** of `COLD_CALL_CONVERSION_RATE` into `OUTBOUND_CALL_CONVERSION_RATE`

---

## Recommendation #17

**Similarity**: 76.2%
**Patterns**: shared_modules, same_category
**Rationale**: Similarity score: 76.2% | Share 1 modules: CUSTOMER_SUCCESS | Same category: Customer Success

### Primary KPI (Keep)
- **Name**: Customer Goal Achievement Rate
- **Code**: `CUSTOMER_GOAL_ACHIEVEMENT_RATE`
- **File**: `customer_goal_achievement_rate.py`
- **Modules**: CUSTOMER_SUCCESS
- **Description**: The rate at which customers achieve their desired outcomes or goals with the company\'s products or services....

### Secondary KPI (Consolidate)
- **Name**: Customer Incident Rate
- **Code**: `CUSTOMER_INCIDENT_RATE`
- **File**: `customer_incident_rate.py`
- **Modules**: CUSTOMER_SUCCESS
- **Description**: The frequency at which customers encounter issues or problems with the company\'s products or services....

### Action
- [ ] **Approve consolidation** of `CUSTOMER_INCIDENT_RATE` into `CUSTOMER_GOAL_ACHIEVEMENT_RATE`

---

## Recommendation #18

**Similarity**: 76.0%
**Patterns**: General similarity
**Rationale**: Similarity score: 76.0%

### Primary KPI (Keep)
- **Name**: Sales Forecast Accuracy
- **Code**: `SALES_FORECAST_ACCURACY`
- **File**: `sales_forecast_accuracy.py`
- **Modules**: INSIDE_SALES, KEY_ACCOUNT_MANAGEMENT, OUTSIDE_SALES, SALES_DEVELOPMENT, SALES_ENABLEMENT, SALES_OPERATIONS, SALES_PERFORMANCE, SALES_STRATEGY, SALES_TRAINING_COACHING
- **Description**: The accuracy of the sales team\'s revenue forecasts....

### Secondary KPI (Consolidate)
- **Name**: Revenue Forecast Accuracy
- **Code**: `REVENUE_FORECAST_ACCURACY`
- **File**: `revenue_forecast_accuracy.py`
- **Modules**: BUS_DEV
- **Description**: The accuracy of the sales team's revenue forecasts compared to actual revenue results....

### Action
- [X] **Approve consolidation** of `REVENUE_FORECAST_ACCURACY` into `SALES_FORECAST_ACCURACY`

---

## Recommendation #19

**Similarity**: 75.1%
**Patterns**: shared_modules, similar_formula
**Rationale**: Similarity score: 75.1% | Share 4 modules: INSIDE_SALES, SALES_OPERATIONS, SALES_PERFORMANCE | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Customer Retention Rate
- **Code**: `CUSTOMER_RETENTION_RATE`
- **File**: `customer_retention_rate.py`
- **Modules**: CUSTOMER_RETENTION, INSIDE_SALES, KEY_ACCOUNT_MANAGEMENT, OUTSIDE_SALES, SALES_OPERATIONS, SALES_PERFORMANCE, SALES_STRATEGY
- **Description**: The percentage of customers who continue to buy from the company over a set period of time....

### Secondary KPI (Consolidate)
- **Name**: Customer Churn Rate
- **Code**: `CUSTOMER_CHURN_RATE`
- **File**: `customer_churn_rate.py`
- **Modules**: INSIDE_SALES, OUTSIDE_SALES, SALES_OPERATIONS, SALES_PERFORMANCE
- **Description**: The percentage of customers who stop doing business with the company over a given period....

### Action
- [ ] **Approve consolidation** of `CUSTOMER_CHURN_RATE` into `CUSTOMER_RETENTION_RATE`

---

## Recommendation #20

**Similarity**: 75.0%
**Patterns**: same_category
**Rationale**: Similarity score: 75.0% | Same category: Business Development

### Primary KPI (Keep)
- **Name**: Lead Response Time
- **Code**: `LEAD_RESPONSE_TIME`
- **File**: `lead_response_time.py`
- **Modules**: BUS_DEV, INSIDE_SALES, KEY_ACCOUNT_MANAGEMENT, OUTSIDE_SALES, SALES_DEVELOPMENT, SALES_ENABLEMENT, SALES_OPERATIONS, SALES_PERFORMANCE, SALES_STRATEGY, SALES_TRAINING_COACHING
- **Description**: The time it takes for a sales representative to respond to a new lead....

### Secondary KPI (Consolidate)
- **Name**: Sales Team Response Time
- **Code**: `SALES_TEAM_RESPONSE_TIME`
- **File**: `sales_team_response_time.py`
- **Modules**: BUS_DEV, SALES_PERFORMANCE
- **Description**: The average time it takes for a sales representative to follow up on a lead or customer inquiry....

### Action
- [X] **Approve consolidation** of `SALES_TEAM_RESPONSE_TIME` into `LEAD_RESPONSE_TIME`

---

## Recommendation #21

**Similarity**: 74.4%
**Patterns**: General similarity
**Rationale**: Similarity score: 74.4%

### Primary KPI (Keep)
- **Name**: Follow-up Contact Rate
- **Code**: `FOLLOW_UP_CONTACT_RATE`
- **File**: `follow_up_contact_rate.py`
- **Modules**: INSIDE_SALES, OUTSIDE_SALES
- **Description**: The frequency at which the sales team follows up with leads and prospects....

### Secondary KPI (Consolidate)
- **Name**: Rate of Follow-Up Contact
- **Code**: `RATE_OF_FOLLOW_UP_CONTACT`
- **File**: `rate_of_follow_up_contact.py`
- **Modules**: SALES_OPERATIONS
- **Description**: The frequency at which sales representatives follow up with leads....

### Action
- [X] **Approve consolidation** of `RATE_OF_FOLLOW_UP_CONTACT` into `FOLLOW_UP_CONTACT_RATE`

---

## Recommendation #22

**Similarity**: 74.2%
**Patterns**: General similarity
**Rationale**: Similarity score: 74.2%

### Primary KPI (Keep)
- **Name**: Customer Support Ticket Resolution Time
- **Code**: `CUSTOMER_SUPPORT_TICKET_RESOLUTION_TIME`
- **File**: `customer_support_ticket_resolution_time.py`
- **Modules**: BUS_DEV
- **Description**: The average time it takes for the sales or support team to resolve customer issues or support tickets....

### Secondary KPI (Consolidate)
- **Name**: Sales Support Ticket Resolution Time
- **Code**: `SALES_SUPPORT_TICKET_RESOLUTION_TIME`
- **File**: `sales_support_ticket_resolution_time.py`
- **Modules**: SALES_OPERATIONS
- **Description**: The average time taken to resolve sales-related support tickets....

### Action
- [X] **Approve consolidation** of `SALES_SUPPORT_TICKET_RESOLUTION_TIME` into `CUSTOMER_SUPPORT_TICKET_RESOLUTION_TIME`

---

## Recommendation #23

**Similarity**: 74.2%
**Patterns**: similar_formula
**Rationale**: Similarity score: 74.2% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Revenue per Sales Representative
- **Code**: `REVENUE_PER_SALES_REPRESENTATIVE`
- **File**: `revenue_per_sales_representative.py`
- **Modules**: BUS_DEV, SALES_DEVELOPMENT, SALES_OPERATIONS, SALES_STRATEGY
- **Description**: The amount of revenue generated by each sales representative, indicating their individual productivity and contribution to the team....

### Secondary KPI (Consolidate)
- **Name**: Sales per Representative
- **Code**: `SALES_PER_REPRESENTATIVE`
- **File**: `sales_per_representative.py`
- **Modules**: SALES_PERFORMANCE
- **Description**: The average amount of sales revenue generated by each sales representative, indicating individual performance....

### Action
- [X] **Approve consolidation** of `SALES_PER_REPRESENTATIVE` into `REVENUE_PER_SALES_REPRESENTATIVE`

---

## Recommendation #24

**Similarity**: 73.9%
**Patterns**: similar_formula
**Rationale**: Similarity score: 73.9% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Customer Education Engagement Rate
- **Code**: `CUSTOMER_EDUCATION_ENGAGEMENT_RATE`
- **File**: `customer_education_engagement_rate.py`
- **Modules**: CUSTOMER_RETENTION, CUSTOMER_SUCCESS
- **Description**: The engagement level of customers with educational content or training provided by the company....

### Secondary KPI (Consolidate)
- **Name**: Customer Education Completion Rate
- **Code**: `CUSTOMER_EDUCATION_COMPLETION_RATE`
- **File**: `customer_education_completion_rate.py`
- **Modules**: CUSTOMER_SUCCESS
- **Description**: The rate at which customers complete educational programs or training offered by the company....

### Action
- [X] **Approve consolidation** of `CUSTOMER_EDUCATION_COMPLETION_RATE` into `CUSTOMER_EDUCATION_ENGAGEMENT_RATE`

---

## Recommendation #25

**Similarity**: 73.4%
**Patterns**: General similarity
**Rationale**: Similarity score: 73.4%

### Primary KPI (Keep)
- **Name**: Conversion Rate
- **Code**: `CONVERSION_RATE`
- **File**: `conversion_rate.py`
- **Modules**: BUS_DEV, INSIDE_SALES, OUTSIDE_SALES, SALES_DEVELOPMENT, SALES_STRATEGY
- **Description**: The percentage of leads that convert into paying customers....

### Secondary KPI (Consolidate)
- **Name**: Lead Conversion Rate
- **Code**: `LEAD_CONVERSION_RATE`
- **File**: `lead_conversion_rate.py`
- **Modules**: CHANNEL_SALES, SALES_OPERATIONS, SALES_PERFORMANCE
- **Description**: The percentage of leads generated by channel partners that convert to sales....

### Action
- [X] **Approve consolidation** of `CONVERSION_RATE` into `LEAD_CONVERSION_RATE`

---

## Recommendation #26

**Similarity**: 72.8%
**Patterns**: General similarity
**Rationale**: Similarity score: 72.8%

### Primary KPI (Keep)
- **Name**: Sales by Region
- **Code**: `SALES_BY_REGION`
- **File**: `sales_by_region.py`
- **Modules**: SALES_OPERATIONS, SALES_PERFORMANCE
- **Description**: The amount of sales generated in each geographic region....

### Secondary KPI (Consolidate)
- **Name**: Sales by Region/Area
- **Code**: `SALES_BY_REGIONAREA`
- **File**: `sales_by_regionarea.py`
- **Modules**: SALES_DEVELOPMENT
- **Description**: The amount of sales generated in specific regions or areas, useful for geographic performance analysis....

### Action
- [X] **Approve consolidation** of `SALES_BY_REGIONAREA` into `SALES_BY_REGION`

---

## Recommendation #27

**Similarity**: 72.7%
**Patterns**: shared_modules, same_category
**Rationale**: Similarity score: 72.7% | Share 1 modules: SALES_ENABLEMENT | Same category: Sales Enablement

### Primary KPI (Keep)
- **Name**: Sales Coaching Effectiveness Rate
- **Code**: `SALES_COACHING_EFFECTIVENESS_RATE`
- **File**: `sales_coaching_effectiveness_rate.py`
- **Modules**: SALES_ENABLEMENT
- **Description**: The effectiveness of sales coaching programs provided by the sales enablement team in terms of improving sales skills and performance....

### Secondary KPI (Consolidate)
- **Name**: Sales Content Effectiveness Rate
- **Code**: `SALES_CONTENT_EFFECTIVENESS_RATE`
- **File**: `sales_content_effectiveness_rate.py`
- **Modules**: SALES_ENABLEMENT
- **Description**: The effectiveness of sales content created by the sales enablement team in terms of generating leads, closing deals, and achieving sales targets....

### Action
- [ ] **Approve consolidation** of `SALES_CONTENT_EFFECTIVENESS_RATE` into `SALES_COACHING_EFFECTIVENESS_RATE`

---

## Recommendation #28

**Similarity**: 72.7%
**Patterns**: similar_formula
**Rationale**: Similarity score: 72.7% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Sales per Rep
- **Code**: `SALES_PER_REP`
- **File**: `sales_per_rep.py`
- **Modules**: OUTSIDE_SALES
- **Description**: The average sales revenue generated by each sales representative....

### Secondary KPI (Consolidate)
- **Name**: Sales per Representative
- **Code**: `SALES_PER_REPRESENTATIVE`
- **File**: `sales_per_representative.py`
- **Modules**: SALES_PERFORMANCE
- **Description**: The average amount of sales revenue generated by each sales representative, indicating individual performance....

### Action
- [ ] **Approve consolidation** of `SALES_PER_REPRESENTATIVE` into `SALES_PER_REP`

---

## Recommendation #29

**Similarity**: 72.6%
**Patterns**: same_category, similar_formula
**Rationale**: Similarity score: 72.6% | Same category: Sales Operations | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Sales by Region
- **Code**: `SALES_BY_REGION`
- **File**: `sales_by_region.py`
- **Modules**: SALES_OPERATIONS, SALES_PERFORMANCE
- **Description**: The amount of sales generated in each geographic region....

### Secondary KPI (Consolidate)
- **Name**: Sales by Product Line
- **Code**: `SALES_BY_PRODUCT_LINE`
- **File**: `sales_by_product_line.py`
- **Modules**: SALES_OPERATIONS
- **Description**: The amount of sales generated by each product line....

### Action
- [ ] **Approve consolidation** of `SALES_BY_PRODUCT_LINE` into `SALES_BY_REGION`

---

## Recommendation #30

**Similarity**: 72.6%
**Patterns**: similar_formula
**Rationale**: Similarity score: 72.6% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Sales Rep Retention Rate
- **Code**: `SALES_REP_RETENTION_RATE`
- **File**: `sales_rep_retention_rate.py`
- **Modules**: SALES_TRAINING_COACHING
- **Description**: The percentage of sales reps who remain with the company over a specific period. A higher retention rate indicates effective training and coaching....

### Secondary KPI (Consolidate)
- **Name**: Sales Retention Rate
- **Code**: `SALES_RETENTION_RATE`
- **File**: `sales_retention_rate.py`
- **Modules**: SALES_ENABLEMENT
- **Description**: The percentage of sales representatives who remain with the company over a given period, indicating the impact of sales enablement on job satisfaction....

### Action
- [ ] **Approve consolidation** of `SALES_RETENTION_RATE` into `SALES_REP_RETENTION_RATE`

---

## Recommendation #31

**Similarity**: 72.5%
**Patterns**: similar_formula
**Rationale**: Similarity score: 72.5% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Sales Process Adherence Rate
- **Code**: `SALES_PROCESS_ADHERENCE_RATE`
- **File**: `sales_process_adherence_rate.py`
- **Modules**: SALES_OPERATIONS
- **Description**: The percentage of sales reps following the prescribed sales process....

### Secondary KPI (Consolidate)
- **Name**: Sales Process Compliance Rate
- **Code**: `SALES_PROCESS_COMPLIANCE_RATE`
- **File**: `sales_process_compliance_rate.py`
- **Modules**: SALES_ENABLEMENT
- **Description**: The percentage of sales reps who are following the defined sales process as established by the sales enablement team....

### Action
- [ ] **Approve consolidation** of `SALES_PROCESS_COMPLIANCE_RATE` into `SALES_PROCESS_ADHERENCE_RATE`

---

## Recommendation #32

**Similarity**: 72.4%
**Patterns**: similar_formula
**Rationale**: Similarity score: 72.4% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Customer Churn Rate
- **Code**: `CUSTOMER_CHURN_RATE`
- **File**: `customer_churn_rate.py`
- **Modules**: INSIDE_SALES, OUTSIDE_SALES, SALES_OPERATIONS, SALES_PERFORMANCE
- **Description**: The percentage of customers who stop doing business with the company over a given period....

### Secondary KPI (Consolidate)
- **Name**: Partner Churn Rate
- **Code**: `PARTNER_CHURN_RATE`
- **File**: `partner_churn_rate.py`
- **Modules**: CHANNEL_SALES
- **Description**: The rate at which channel partners cease doing business with the company over a specific period....

### Action
- [ ] **Approve consolidation** of `PARTNER_CHURN_RATE` into `CUSTOMER_CHURN_RATE`

---

## Recommendation #33

**Similarity**: 72.4%
**Patterns**: General similarity
**Rationale**: Similarity score: 72.4%

### Primary KPI (Keep)
- **Name**: Customer Onboarding Success Rate
- **Code**: `CUSTOMER_ONBOARDING_SUCCESS_RATE`
- **File**: `customer_onboarding_success_rate.py`
- **Modules**: INSIDE_SALES, SALES_DEVELOPMENT
- **Description**: The success rate of bringing new customers up to speed with the product or service....

### Secondary KPI (Consolidate)
- **Name**: Customer Enablement Success Rate
- **Code**: `CUSTOMER_ENABLEMENT_SUCCESS_RATE`
- **File**: `customer_enablement_success_rate.py`
- **Modules**: CUSTOMER_SUCCESS
- **Description**: The success rate of customer enablement efforts, assessing how well customers are equipped to use the product or service....

### Action
- [ ] **Approve consolidation** of `CUSTOMER_ENABLEMENT_SUCCESS_RATE` into `CUSTOMER_ONBOARDING_SUCCESS_RATE`

---

## Recommendation #34

**Similarity**: 72.3%
**Patterns**: General similarity
**Rationale**: Similarity score: 72.3%

### Primary KPI (Keep)
- **Name**: Lead Conversion Time
- **Code**: `LEAD_CONVERSION_TIME`
- **File**: `lead_conversion_time.py`
- **Modules**: INSIDE_SALES
- **Description**: The average time it takes to convert a lead into a sale, reflecting the team’s sales cycle efficiency....

### Secondary KPI (Consolidate)
- **Name**: Sales Conversion Time
- **Code**: `SALES_CONVERSION_TIME`
- **File**: `sales_conversion_time.py`
- **Modules**: SALES_PERFORMANCE
- **Description**: The average amount of time it takes a lead to become a sale, indicating the efficiency of the sales process....

### Action
- [ ] **Approve consolidation** of `SALES_CONVERSION_TIME` into `LEAD_CONVERSION_TIME`

---

## Recommendation #35

**Similarity**: 71.9%
**Patterns**: rate_ratio_variant
**Rationale**: Similarity score: 71.9% | Both are rate/ratio variants of the same metric

### Primary KPI (Keep)
- **Name**: Opportunity-to-Close Rate
- **Code**: `OPPORTUNITY_TO_CLOSE_RATE`
- **File**: `opportunity_to_close_rate.py`
- **Modules**: BUS_DEV
- **Description**: The percentage of sales opportunities that are converted into actual sales, showing the effectiveness of the sales team's closing abilities....

### Secondary KPI (Consolidate)
- **Name**: Opportunity-to-Sale Ratio
- **Code**: `OPPORTUNITY_TO_SALE_RATIO`
- **File**: `opportunity_to_sale_ratio.py`
- **Modules**: OUTSIDE_SALES
- **Description**: The ratio of sales opportunities that are converted into actual sales....

### Action
- [ ] **Approve consolidation** of `OPPORTUNITY_TO_SALE_RATIO` into `OPPORTUNITY_TO_CLOSE_RATE`

---

## Recommendation #36

**Similarity**: 71.6%
**Patterns**: similar_formula
**Rationale**: Similarity score: 71.6% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Year-over-Year (YoY) Sales Growth
- **Code**: `YEAR_OVER_YEAR_YOY_SALES_GROWTH`
- **File**: `year_over_year_yoy_sales_growth.py`
- **Modules**: INSIDE_SALES, SALES_STRATEGY
- **Description**: The increase in sales revenue compared to the same period in the previous year....

### Secondary KPI (Consolidate)
- **Name**: Sales Growth Year-over-Year
- **Code**: `SALES_GROWTH_YEAR_OVER_YEAR`
- **File**: `sales_growth_year_over_year.py`
- **Modules**: SALES_DEVELOPMENT
- **Description**: The percentage increase in sales compared to the same period in the previous year....

### Action
- [ ] **Approve consolidation** of `SALES_GROWTH_YEAR_OVER_YEAR` into `YEAR_OVER_YEAR_YOY_SALES_GROWTH`

---

## Recommendation #37

**Similarity**: 71.2%
**Patterns**: General similarity
**Rationale**: Similarity score: 71.2%

### Primary KPI (Keep)
- **Name**: Sales Efficiency
- **Code**: `SALES_EFFICIENCY`
- **File**: `sales_efficiency.py`
- **Modules**: OUTSIDE_SALES
- **Description**: The ratio of revenue generated to the cost of sales and marketing efforts....

### Secondary KPI (Consolidate)
- **Name**: Sales Operational Efficiency
- **Code**: `SALES_OPERATIONAL_EFFICIENCY`
- **File**: `sales_operational_efficiency.py`
- **Modules**: SALES_OPERATIONS
- **Description**: The ratio of revenue generated to operational costs within the sales department....

### Action
- [ ] **Approve consolidation** of `SALES_OPERATIONAL_EFFICIENCY` into `SALES_EFFICIENCY`

---

## Recommendation #38

**Similarity**: 71.1%
**Patterns**: General similarity
**Rationale**: Similarity score: 71.1%

### Primary KPI (Keep)
- **Name**: Average Issue Resolution Time
- **Code**: `AVERAGE_ISSUE_RESOLUTION_TIME`
- **File**: `average_issue_resolution_time.py`
- **Modules**: CUSTOMER_RETENTION
- **Description**: The average time taken to resolve customer issues or complaints....

### Secondary KPI (Consolidate)
- **Name**: Sales Support Ticket Resolution Time
- **Code**: `SALES_SUPPORT_TICKET_RESOLUTION_TIME`
- **File**: `sales_support_ticket_resolution_time.py`
- **Modules**: SALES_OPERATIONS
- **Description**: The average time taken to resolve sales-related support tickets....

### Action
- [ ] **Approve consolidation** of `SALES_SUPPORT_TICKET_RESOLUTION_TIME` into `AVERAGE_ISSUE_RESOLUTION_TIME`

---

## Recommendation #39

**Similarity**: 71.1%
**Patterns**: similar_formula
**Rationale**: Similarity score: 71.1% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Customer Problem Resolution Time
- **Code**: `CUSTOMER_PROBLEM_RESOLUTION_TIME`
- **File**: `customer_problem_resolution_time.py`
- **Modules**: KEY_ACCOUNT_MANAGEMENT
- **Description**: The time it takes to resolve a customer’s issue or problem....

### Secondary KPI (Consolidate)
- **Name**: Average Issue Resolution Time
- **Code**: `AVERAGE_ISSUE_RESOLUTION_TIME`
- **File**: `average_issue_resolution_time.py`
- **Modules**: CUSTOMER_RETENTION
- **Description**: The average time taken to resolve customer issues or complaints....

### Action
- [ ] **Approve consolidation** of `AVERAGE_ISSUE_RESOLUTION_TIME` into `CUSTOMER_PROBLEM_RESOLUTION_TIME`

---

## Recommendation #40

**Similarity**: 71.1%
**Patterns**: General similarity
**Rationale**: Similarity score: 71.1%

### Primary KPI (Keep)
- **Name**: Channel Partner Performance
- **Code**: `CHANNEL_PARTNER_PERFORMANCE`
- **File**: `channel_partner_performance.py`
- **Modules**: SALES_OPERATIONS
- **Description**: The performance metrics of each channel partner in terms of sales volume and effectiveness....

### Secondary KPI (Consolidate)
- **Name**: Channel Partner Performance Scorecard
- **Code**: `CHANNEL_PARTNER_PERFORMANCE_SCORECARD`
- **File**: `channel_partner_performance_scorecard.py`
- **Modules**: CHANNEL_SALES
- **Description**: The performance of individual channel partners in areas such as sales growth, market share, and customer satisfaction....

### Action
- [ ] **Approve consolidation** of `CHANNEL_PARTNER_PERFORMANCE_SCORECARD` into `CHANNEL_PARTNER_PERFORMANCE`

---

## Recommendation #41

**Similarity**: 71.0%
**Patterns**: similar_formula
**Rationale**: Similarity score: 71.0% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Sales Training Completion Rate
- **Code**: `SALES_TRAINING_COMPLETION_RATE`
- **File**: `sales_training_completion_rate.py`
- **Modules**: BUS_DEV, INSIDE_SALES, SALES_ENABLEMENT
- **Description**: The percentage of sales representatives who have completed mandatory sales training programs....

### Secondary KPI (Consolidate)
- **Name**: Sales Training Attendance Rate
- **Code**: `SALES_TRAINING_ATTENDANCE_RATE`
- **File**: `sales_training_attendance_rate.py`
- **Modules**: SALES_ENABLEMENT
- **Description**: The percentage of eligible sales representatives who attend scheduled sales training sessions....

### Action
- [ ] **Approve consolidation** of `SALES_TRAINING_ATTENDANCE_RATE` into `SALES_TRAINING_COMPLETION_RATE`

---

## Recommendation #42

**Similarity**: 71.0%
**Patterns**: similar_formula
**Rationale**: Similarity score: 71.0% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Service Level Agreement (SLA) Compliance Rate
- **Code**: `SERVICE_LEVEL_AGREEMENT_SLA_COMPLIANCE_RATE`
- **File**: `service_level_agreement_sla_compliance_rate.py`
- **Modules**: CUSTOMER_SUCCESS, KEY_ACCOUNT_MANAGEMENT
- **Description**: The rate at which the customer success team adheres to the agreed-upon service levels in SLAs with customers....

### Secondary KPI (Consolidate)
- **Name**: Service Level Agreement (SLA) Performance
- **Code**: `SERVICE_LEVEL_AGREEMENT_SLA_PERFORMANCE`
- **File**: `service_level_agreement_sla_performance.py`
- **Modules**: CUSTOMER_RETENTION
- **Description**: The rate at which a company meets the service expectations as outlined in SLAs with the customer....

### Action
- [ ] **Approve consolidation** of `SERVICE_LEVEL_AGREEMENT_SLA_PERFORMANCE` into `SERVICE_LEVEL_AGREEMENT_SLA_COMPLIANCE_RATE`

---

## Recommendation #43

**Similarity**: 70.7%
**Patterns**: same_category
**Rationale**: Similarity score: 70.7% | Same category: Customer Retention

### Primary KPI (Keep)
- **Name**: Customer Feedback Response Rate
- **Code**: `CUSTOMER_FEEDBACK_RESPONSE_RATE`
- **File**: `customer_feedback_response_rate.py`
- **Modules**: CUSTOMER_RETENTION, CUSTOMER_SUCCESS
- **Description**: The percentage of customers who provide feedback when asked....

### Secondary KPI (Consolidate)
- **Name**: Customer Winback Rate
- **Code**: `CUSTOMER_WINBACK_RATE`
- **File**: `customer_winback_rate.py`
- **Modules**: CUSTOMER_RETENTION
- **Description**: The percentage of former customers who have been reacquired....

### Action
- [ ] **Approve consolidation** of `CUSTOMER_WINBACK_RATE` into `CUSTOMER_FEEDBACK_RESPONSE_RATE`

---

## Recommendation #44

**Similarity**: 70.6%
**Patterns**: similar_formula
**Rationale**: Similarity score: 70.6% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Proposal Conversion Rate
- **Code**: `PROPOSAL_CONVERSION_RATE`
- **File**: `proposal_conversion_rate.py`
- **Modules**: SALES_DEVELOPMENT, SALES_OPERATIONS
- **Description**: The percentage of proposals or quotes that result in a sale....

### Secondary KPI (Consolidate)
- **Name**: Sales Conversion Rate
- **Code**: `SALES_CONVERSION_RATE`
- **File**: `sales_conversion_rate.py`
- **Modules**: KEY_ACCOUNT_MANAGEMENT, SALES_OPERATIONS
- **Description**: The percentage of opportunities that are converted to closed deals....

### Action
- [ ] **Approve consolidation** of `SALES_CONVERSION_RATE` into `PROPOSAL_CONVERSION_RATE`

---

## Recommendation #45

**Similarity**: 70.6%
**Patterns**: similar_formula
**Rationale**: Similarity score: 70.6% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Average Revenue per Unit (ARPU)
- **Code**: `AVERAGE_REVENUE_PER_UNIT_ARPU`
- **File**: `average_revenue_per_unit_arpu.py`
- **Modules**: BUS_DEV, SALES_PERFORMANCE
- **Description**: The average revenue generated per unit sold, which helps assess the value of a company's products or services....

### Secondary KPI (Consolidate)
- **Name**: Average Revenue Per User (ARPU)
- **Code**: `AVERAGE_REVENUE_PER_USER_ARPU`
- **File**: `average_revenue_per_user_arpu.py`
- **Modules**: CUSTOMER_RETENTION
- **Description**: The average revenue generated from each active customer or user....

### Action
- [ ] **Approve consolidation** of `AVERAGE_REVENUE_PER_USER_ARPU` into `AVERAGE_REVENUE_PER_UNIT_ARPU`

---

## Recommendation #46

**Similarity**: 70.6%
**Patterns**: General similarity
**Rationale**: Similarity score: 70.6%

### Primary KPI (Keep)
- **Name**: Upsell/cross-sell Ratio
- **Code**: `UPSELLCROSS_SELL_RATIO`
- **File**: `upsellcross_sell_ratio.py`
- **Modules**: KEY_ACCOUNT_MANAGEMENT
- **Description**: The ratio of additional products or services sold to existing key accounts....

### Secondary KPI (Consolidate)
- **Name**: Cross-Selling Rate
- **Code**: `CROSS_SELLING_RATE`
- **File**: `cross_selling_rate.py`
- **Modules**: CHANNEL_SALES
- **Description**: The rate at which additional products or services are sold to an existing customer through channel partners....

### Action
- [ ] **Approve consolidation** of `CROSS_SELLING_RATE` into `UPSELLCROSS_SELL_RATIO`

---

## Recommendation #47

**Similarity**: 70.4%
**Patterns**: similar_formula
**Rationale**: Similarity score: 70.4% | Similar calculation formulas

### Primary KPI (Keep)
- **Name**: Sales Pipeline Velocity
- **Code**: `SALES_PIPELINE_VELOCITY`
- **File**: `sales_pipeline_velocity.py`
- **Modules**: SALES_OPERATIONS
- **Description**: The time it takes for a lead to move through the sales pipeline and convert into a sale....

### Secondary KPI (Consolidate)
- **Name**: Pipeline Velocity
- **Code**: `PIPELINE_VELOCITY`
- **File**: `pipeline_velocity.py`
- **Modules**: OUTSIDE_SALES
- **Description**: The speed at which deals move through the sales pipeline....

### Action
- [ ] **Approve consolidation** of `PIPELINE_VELOCITY` into `SALES_PIPELINE_VELOCITY`

---

## Recommendation #48

**Similarity**: 70.4%
**Patterns**: General similarity
**Rationale**: Similarity score: 70.4%

### Primary KPI (Keep)
- **Name**: Prospect Engagement Score
- **Code**: `PROSPECT_ENGAGEMENT_SCORE`
- **File**: `prospect_engagement_score.py`
- **Modules**: SALES_DEVELOPMENT, SALES_ENABLEMENT
- **Description**: A measure of how involved and interested prospects are during sales interactions....

### Secondary KPI (Consolidate)
- **Name**: Prospect Engagement Level
- **Code**: `PROSPECT_ENGAGEMENT_LEVEL`
- **File**: `prospect_engagement_level.py`
- **Modules**: INSIDE_SALES
- **Description**: The level of interaction and interest shown by prospects during the sales process....

### Action
- [ ] **Approve consolidation** of `PROSPECT_ENGAGEMENT_LEVEL` into `PROSPECT_ENGAGEMENT_SCORE`

---

## Recommendation #49

**Similarity**: 70.4%
**Patterns**: shared_modules, same_category
**Rationale**: Similarity score: 70.4% | Share 1 modules: OUTSIDE_SALES | Same category: Outside Sales

### Primary KPI (Keep)
- **Name**: Number of Sales Calls
- **Code**: `NUMBER_OF_SALES_CALLS`
- **File**: `number_of_sales_calls.py`
- **Modules**: OUTSIDE_SALES
- **Description**: The total number of sales-related calls made by the outside sales team....

### Secondary KPI (Consolidate)
- **Name**: Sales Volume
- **Code**: `SALES_VOLUME`
- **File**: `sales_volume.py`
- **Modules**: OUTSIDE_SALES
- **Description**: The total number of sales made by the outside sales team....

### Action
- [ ] **Approve consolidation** of `SALES_VOLUME` into `NUMBER_OF_SALES_CALLS`

---

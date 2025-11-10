"""
Account Retention Costs KPI

The cost associated with retaining an existing customer account.
"""

from analytics_models import KPI

ACCOUNT_RETENTION_COSTS = KPI(
    name="Account Retention Costs",
    code="ACCOUNT_RETENTION_COSTS",
    category="Outside Sales",
    
    # Core Definition
    description="The cost associated with retaining an existing customer account.",
    kpi_definition="The cost associated with retaining an existing customer account.",
    expected_business_insights="Reveals the investment required to retain clients, helping assess the balance between retention efforts and customer value.",
    measurement_approach="Considers all expenses associated with keeping an existing customer, including support, marketing, and relationship management costs.",
    
    # Formula
    formula="Total Costs to Retain Customers / Total Number of Retained Customers",
    calculation_formula="Total Costs to Retain Customers / Total Number of Retained Customers",
    
    # Analysis
    trend_analysis="""
    * Increasing account retention costs may indicate difficulties in maintaining customer loyalty or increased competition.
    * Decreasing costs could signal improved customer satisfaction and loyalty, as well as more efficient account management processes.
    """,
    diagnostic_questions="""
    * Are there specific customer segments or products with higher retention costs?
    * How do our account retention costs compare with industry benchmarks or with our historical data?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Implement customer loyalty programs to incentivize repeat purchases and reduce churn.
    * Invest in customer relationship management (CRM) systems to better track and manage customer interactions and needs.
    * Provide additional training and resources to sales teams to improve customer retention and account management skills.
    """,
    visualization_suggestions="""
    * Line charts showing the trend of account retention costs over time.
    * Pie charts comparing retention costs across different customer segments or product categories.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * High account retention costs can impact profitability and indicate inefficiencies in customer management.
    * Significant fluctuations in retention costs may point to inconsistent customer experiences or market volatility.
    """,
    tracking_tools="""
    * CRM software like Salesforce or HubSpot for tracking customer interactions and managing accounts.
    * Customer analytics tools to identify patterns and behaviors that impact retention costs.
    """,
    integration_points="""
    * Integrate account retention cost data with sales performance metrics to understand the relationship between customer retention and sales efforts.
    * Link retention cost analysis with marketing data to assess the impact of promotional activities on customer loyalty.
    """,
    change_impact_analysis="""
    * Reducing account retention costs can lead to improved profitability and long-term customer value.
    * However, cutting costs without considering customer satisfaction may lead to increased churn and reduced revenue in the long run.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["OUTSIDE_SALES"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Account", "Account Penetration", "Account Plan", "Account Risk", "Customer", "Customer Advocacy Program", "Customer Cohort", "Customer Community", "Customer Education", "Customer Feedback", "Customer Goal", "Customer Health Record", "Customer Journey", "Customer Onboarding", "Customer Segment", "Customer Success Manager", "Key Account", "Key Account Manager", "Renewal Management", "Sale", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program", "Support Ticket"]
    }
)

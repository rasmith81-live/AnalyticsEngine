"""
Retention Rate KPI

The percentage of customers who continue to do business with the company over a certain period.
"""

from analytics_models import KPI

RETENTION_RATE = KPI(
    name="Retention Rate",
    code="RETENTION_RATE",
    category="Sales Development",
    
    # Core Definition
    description="The percentage of customers who continue to do business with the company over a certain period.",
    kpi_definition="The percentage of customers who continue to do business with the company over a certain period.",
    expected_business_insights="Indicates customer satisfaction and the effectiveness of customer retention strategies.",
    measurement_approach="Measures the percentage of customers who continue to do business with a company over a given period.",
    
    # Formula
    formula="((Number of Customers at End of Period - Number of New Customers during Period) / Number of Customers at Start of Period) * 100",
    calculation_formula="((Number of Customers at End of Period - Number of New Customers during Period) / Number of Customers at Start of Period) * 100",
    
    # Analysis
    trend_analysis="""
    * An increasing retention rate may indicate improved customer satisfaction and loyalty.
    * A decreasing rate could signal issues with product quality, customer service, or competitive pressures.
    """,
    diagnostic_questions="""
    * What factors have contributed to the changes in our retention rate?
    * Are there specific customer segments or product lines that are experiencing higher or lower retention?
    """,
    
    # Action & Visualization
    actionable_tips="""
    * Invest in customer relationship management (CRM) systems to better understand and engage with customers.
    * Implement loyalty programs or incentives to encourage repeat business.
    * Conduct regular customer feedback surveys to identify areas for improvement.
    """,
    visualization_suggestions="""
    * Line charts showing retention rate trends over time.
    * Cohort analysis to track retention rates for different customer cohorts.
    """,
    
    # Risk & Integration
    risk_warnings="""
    * Low retention rates can lead to increased customer acquisition costs and reduced overall revenue.
    * High retention rates without corresponding growth may indicate a lack of new customer acquisition.
    """,
    tracking_tools="""
    * Customer analytics platforms like Google Analytics or Kissmetrics to track customer behavior and retention.
    * CRM systems such as Salesforce or HubSpot for managing customer relationships and communications.
    """,
    integration_points="""
    * Integrate retention rate data with marketing automation platforms to tailor messaging and offers to different customer segments.
    * Link retention rate with sales performance metrics to identify potential areas for improvement in the sales process.
    """,
    change_impact_analysis="""
    * Improving retention rates can lead to increased customer lifetime value and overall revenue.
    * However, focusing solely on retention may neglect the need for new customer acquisition and market expansion.
    """,
    
    is_active=True,
    metadata_={
        "modules": ["SALES_DEVELOPMENT"],
        "source": "kpidepot.com",
        "import_date": "2025-11-07",
        "required_objects": ["Customer", "Quarterly Business Review", "Sales Activity", "Sales Appointment", "Sales Assessment", "Sales Call", "Sales Coaching Session", "Sales Content", "Sales Dashboard", "Sales Email", "Sales Forecast", "Sales Playbook", "Sales Process Workflow", "Sales Quota", "Sales Representative", "Sales Team", "Sales Territory", "Sales Training Program"]
    }
)

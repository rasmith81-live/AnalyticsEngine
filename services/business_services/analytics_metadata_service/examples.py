"""
Example usage of Analytics Models

This file demonstrates how to use the analytics hierarchy models
in various scenarios with the ValueChain layer.
"""

from datetime import datetime
from typing import List
import uuid

# Import database models
from .db_models import Industry, ValueChain, Module, ObjectModel, ObjectAttribute, Object, KPI

# Import Pydantic schemas
from .schemas import (
    IndustryCreate,
    ValueChainCreate,
    ModuleCreate,
    ObjectModelCreate,
    ObjectAttributeCreate,
    ObjectCreate,
    KPICreate,
    IndustryRead,
)

# Import utilities
from .utils import (
    calculate_kpi_status,
    calculate_kpi_variance,
    build_hierarchy_dict,
    get_kpi_summary,
)


# ============================================================================
# Example 1: Creating a Complete Hierarchy
# ============================================================================

def example_create_financial_services_hierarchy():
    """
    Example: Create a complete hierarchy for Financial Services industry.
    """
    
    # Step 1: Create Industry
    industry = Industry(
        name="Financial Services",
        code="FIN_SVC",
        description="Financial services and banking analytics",
        is_active=True,
        metadata_={
            "sector": "Finance",
            "region": "North America"
        }
    )
    
    # Step 2: Create Modules
    risk_module = Module(
        industry_id=industry.id,  # Will be set after industry is saved
        name="Risk Management",
        code="RISK_MGMT",
        description="Risk assessment and management analytics",
        display_order=1,
        is_active=True
    )
    
    portfolio_module = Module(
        industry_id=industry.id,
        name="Portfolio Management",
        code="PORT_MGMT",
        description="Investment portfolio analytics",
        display_order=2,
        is_active=True
    )
    
    # Step 3: Create Object Models
    credit_risk_model = ObjectModel(
        module_id=risk_module.id,
        name="Credit Risk Assessment",
        code="CREDIT_RISK",
        description="Credit risk evaluation model",
        display_order=1,
        schema_definition={
            "fields": [
                {"name": "borrower_id", "type": "string"},
                {"name": "credit_score", "type": "integer"},
                {"name": "debt_to_income", "type": "float"},
                {"name": "default_probability", "type": "float"}
            ]
        }
    )
    
    # Step 4: Create Objects
    borrower_obj = Object(
        object_model_id=credit_risk_model.id,
        name="Borrower ABC123",
        code="BORR_ABC123",
        description="Individual borrower profile",
        data_values={
            "borrower_id": "ABC123",
            "credit_score": 720,
            "debt_to_income": 0.35,
            "default_probability": 0.02
        }
    )
    
    # Step 5: Create KPIs
    default_rate_kpi = KPI(
        object_model_id=credit_risk_model.id,
        name="Default Rate",
        code="DEFAULT_RATE",
        description="Percentage of loans in default",
        calculation_formula="(defaulted_loans / total_loans) * 100",
        unit_of_measure="percentage",
        target_value=2.0,
        current_value=1.5,
        threshold_warning=3.0,
        threshold_critical=5.0,
        category="Risk",
        display_order=1
    )
    
    return {
        "industry": industry,
        "modules": [risk_module, portfolio_module],
        "object_models": [credit_risk_model],
        "objects": [borrower_obj],
        "kpis": [default_rate_kpi]
    }


# ============================================================================
# Example 2: Using Pydantic Schemas for API
# ============================================================================

def example_api_create_industry():
    """
    Example: Create industry using Pydantic schemas (for API endpoints).
    """
    
    # Create request schema
    industry_create = IndustryCreate(
        name="Healthcare",
        code="HEALTH",
        description="Healthcare and medical analytics",
        is_active=True,
        metadata_={
            "sector": "Healthcare",
            "compliance": "HIPAA"
        }
    )
    
    # Convert to database model
    industry = Industry(**industry_create.model_dump())
    
    # After saving to database, convert to read schema
    industry_read = IndustryRead.model_validate(industry)
    
    return industry_read


# ============================================================================
# Example 3: Working with KPIs
# ============================================================================

def example_kpi_monitoring():
    """
    Example: Monitor KPI status and calculate variance.
    """
    
    # Create a KPI
    revenue_kpi = KPI(
        object_model_id=1,
        name="Monthly Revenue",
        code="MONTHLY_REV",
        description="Total monthly revenue",
        calculation_formula="SUM(sales)",
        unit_of_measure="USD",
        target_value=1000000.0,
        current_value=950000.0,
        threshold_warning=800000.0,
        threshold_critical=600000.0,
        category="Financial"
    )
    
    # Calculate status
    status = calculate_kpi_status(
        revenue_kpi.current_value,
        revenue_kpi.target_value,
        revenue_kpi.threshold_warning,
        revenue_kpi.threshold_critical
    )
    
    # Calculate variance
    variance = calculate_kpi_variance(
        revenue_kpi.current_value,
        revenue_kpi.target_value
    )
    
    return {
        "kpi": revenue_kpi,
        "status": status,
        "variance": variance["variance"],
        "variance_percentage": variance["variance_percentage"]
    }


# ============================================================================
# Example 4: Building Complete Hierarchy
# ============================================================================

def example_build_hierarchy():
    """
    Example: Build a complete hierarchy dictionary.
    """
    
    # Assume we have an industry with all relationships loaded
    industry = Industry(
        id=1,
        name="Retail",
        code="RETAIL",
        description="Retail analytics",
        is_active=True
    )
    
    # Build hierarchy dictionary
    hierarchy = build_hierarchy_dict(
        industry,
        include_modules=True,
        include_object_models=True,
        include_objects=True,
        include_kpis=True
    )
    
    return hierarchy


# ============================================================================
# Example 5: E-commerce Analytics Hierarchy
# ============================================================================

def example_ecommerce_analytics():
    """
    Example: Complete e-commerce analytics hierarchy.
    """
    
    # Industry
    ecommerce = Industry(
        name="E-Commerce",
        code="ECOMM",
        description="E-commerce platform analytics"
    )
    
    # Module: Customer Analytics
    customer_module = Module(
        name="Customer Analytics",
        code="CUST_ANALYTICS",
        description="Customer behavior and engagement analytics",
        display_order=1
    )
    
    # Object Model: Customer Segments
    segment_model = ObjectModel(
        name="Customer Segments",
        code="CUST_SEG",
        description="Customer segmentation model",
        schema_definition={
            "fields": [
                {"name": "segment_name", "type": "string"},
                {"name": "customer_count", "type": "integer"},
                {"name": "avg_order_value", "type": "float"},
                {"name": "lifetime_value", "type": "float"}
            ]
        }
    )
    
    # Object: Premium Segment
    premium_segment = Object(
        name="Premium Customers",
        code="SEG_PREMIUM",
        data_values={
            "segment_name": "Premium",
            "customer_count": 5000,
            "avg_order_value": 250.00,
            "lifetime_value": 5000.00
        }
    )
    
    # KPIs for Customer Segments
    kpis = [
        KPI(
            name="Customer Acquisition Cost",
            code="CAC",
            calculation_formula="marketing_spend / new_customers",
            unit_of_measure="USD",
            target_value=50.0,
            current_value=45.0,
            threshold_warning=60.0,
            threshold_critical=75.0,
            category="Acquisition",
            display_order=1
        ),
        KPI(
            name="Customer Lifetime Value",
            code="CLV",
            calculation_formula="avg_order_value * purchase_frequency * customer_lifespan",
            unit_of_measure="USD",
            target_value=5000.0,
            current_value=5200.0,
            threshold_warning=4000.0,
            threshold_critical=3000.0,
            category="Value",
            display_order=2
        ),
        KPI(
            name="Churn Rate",
            code="CHURN",
            calculation_formula="(churned_customers / total_customers) * 100",
            unit_of_measure="percentage",
            target_value=5.0,
            current_value=4.2,
            threshold_warning=7.0,
            threshold_critical=10.0,
            category="Retention",
            display_order=3
        ),
    ]
    
    # Get KPI summary
    summary = get_kpi_summary(kpis)
    
    return {
        "industry": ecommerce,
        "module": customer_module,
        "object_model": segment_model,
        "object": premium_segment,
        "kpis": kpis,
        "kpi_summary": summary
    }


# ============================================================================
# Example 6: Manufacturing Analytics
# ============================================================================

def example_manufacturing_analytics():
    """
    Example: Manufacturing industry analytics hierarchy.
    """
    
    # Industry
    manufacturing = Industry(
        name="Manufacturing",
        code="MFG",
        description="Manufacturing operations analytics"
    )
    
    # Module: Production
    production_module = Module(
        name="Production Analytics",
        code="PROD_ANALYTICS",
        description="Production line performance analytics",
        display_order=1
    )
    
    # Object Model: Production Line
    production_line_model = ObjectModel(
        name="Production Line",
        code="PROD_LINE",
        description="Production line performance model",
        schema_definition={
            "fields": [
                {"name": "line_id", "type": "string"},
                {"name": "capacity", "type": "integer"},
                {"name": "current_output", "type": "integer"},
                {"name": "downtime_hours", "type": "float"}
            ]
        }
    )
    
    # Object: Assembly Line 1
    assembly_line = Object(
        name="Assembly Line 1",
        code="LINE_001",
        data_values={
            "line_id": "LINE_001",
            "capacity": 1000,
            "current_output": 950,
            "downtime_hours": 2.5
        }
    )
    
    # KPIs
    kpis = [
        KPI(
            name="Overall Equipment Effectiveness",
            code="OEE",
            calculation_formula="availability * performance * quality",
            unit_of_measure="percentage",
            target_value=85.0,
            current_value=82.5,
            threshold_warning=75.0,
            threshold_critical=65.0,
            category="Efficiency",
            display_order=1
        ),
        KPI(
            name="Defect Rate",
            code="DEFECT_RATE",
            calculation_formula="(defective_units / total_units) * 100",
            unit_of_measure="percentage",
            target_value=2.0,
            current_value=1.8,
            threshold_warning=3.0,
            threshold_critical=5.0,
            category="Quality",
            display_order=2
        ),
        KPI(
            name="Production Throughput",
            code="THROUGHPUT",
            calculation_formula="units_produced / time_period",
            unit_of_measure="units/hour",
            target_value=100.0,
            current_value=95.0,
            threshold_warning=80.0,
            threshold_critical=60.0,
            category="Production",
            display_order=3
        ),
    ]
    
    return {
        "industry": manufacturing,
        "module": production_module,
        "object_model": production_line_model,
        "object": assembly_line,
        "kpis": kpis
    }


# ============================================================================
# Example 7: CQRS Command/Query Pattern
# ============================================================================

def example_cqrs_pattern():
    """
    Example: Using CQRS pattern for commands and queries.
    """
    from .schemas import CreateIndustryCommand, GetIndustryQuery
    
    # Create Command
    create_command = CreateIndustryCommand(
        industry=IndustryCreate(
            name="Technology",
            code="TECH",
            description="Technology sector analytics"
        ),
        command_id=str(uuid.uuid4())
    )
    
    # Query
    get_query = GetIndustryQuery(
        industry_id=1,
        include_modules=True,
        query_id=str(uuid.uuid4())
    )
    
    return {
        "command": create_command,
        "query": get_query
    }


# ============================================================================
# Main Example Runner
# ============================================================================

if __name__ == "__main__":
    """
    Run examples to demonstrate usage.
    Note: These examples show the structure but won't execute
    without a database connection.
    """
    
    print("Analytics Models Examples")
    print("=" * 50)
    
    print("\n1. Financial Services Hierarchy")
    fin_hierarchy = example_create_financial_services_hierarchy()
    print(f"Created industry: {fin_hierarchy['industry'].name}")
    print(f"Modules: {len(fin_hierarchy['modules'])}")
    print(f"KPIs: {len(fin_hierarchy['kpis'])}")
    
    print("\n2. E-Commerce Analytics")
    ecomm = example_ecommerce_analytics()
    print(f"Industry: {ecomm['industry'].name}")
    print(f"KPI Summary: {ecomm['kpi_summary']}")
    
    print("\n3. Manufacturing Analytics")
    mfg = example_manufacturing_analytics()
    print(f"Industry: {mfg['industry'].name}")
    print(f"Production KPIs: {len(mfg['kpis'])}")
    
    print("\n4. KPI Monitoring")
    kpi_monitor = example_kpi_monitoring()
    print(f"KPI Status: {kpi_monitor['status']}")
    print(f"Variance: {kpi_monitor['variance']}")
    print(f"Variance %: {kpi_monitor['variance_percentage']:.2f}%")

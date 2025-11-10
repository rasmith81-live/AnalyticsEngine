"""
ObjectAttribute Examples

Demonstrates how to define object attributes and create KPIs that reference them.
"""

from analytics_models import (
    Industry,
    Module,
    ObjectModel,
    ObjectAttribute,
    Object,
    KPI
)


# ============================================================================
# Example 1: Sales Transaction Model
# ============================================================================

def create_sales_transaction_model():
    """Create a sales transaction model with attributes and KPIs."""
    
    # Create hierarchy
    retail_industry = Industry(
        name="Retail",
        code="RETAIL",
        description="Retail industry"
    )
    
    sales_module = Module(
        name="Sales Management",
        code="SALES_MGMT",
        description="Sales tracking and analytics"
    )
    sales_module.industries.append(retail_industry)
    
    # Create ObjectModel
    sales_txn_model = ObjectModel(
        name="Sales Transaction",
        code="SALES_TXN",
        description="Individual sales transaction record"
    )
    sales_txn_model.modules.append(sales_module)
    
    # Define Attributes (like database table columns)
    attributes = [
        ObjectAttribute(
            object_model_id=sales_txn_model.id,
            name="Revenue",
            code="REVENUE",
            description="Total revenue from the transaction",
            data_type="float",
            is_required=True,
            validation_rules={
                "min": 0,
                "precision": 2
            },
            display_order=1
        ),
        ObjectAttribute(
            object_model_id=sales_txn_model.id,
            name="Cost",
            code="COST",
            description="Total cost of goods sold",
            data_type="float",
            is_required=True,
            validation_rules={
                "min": 0,
                "precision": 2
            },
            display_order=2
        ),
        ObjectAttribute(
            object_model_id=sales_txn_model.id,
            name="Quantity",
            code="QUANTITY",
            description="Number of units sold",
            data_type="integer",
            is_required=True,
            validation_rules={
                "min": 1
            },
            display_order=3
        ),
        ObjectAttribute(
            object_model_id=sales_txn_model.id,
            name="Transaction Date",
            code="TXN_DATE",
            description="Date of the transaction",
            data_type="date",
            is_required=True,
            display_order=4
        ),
        ObjectAttribute(
            object_model_id=sales_txn_model.id,
            name="Customer Type",
            code="CUSTOMER_TYPE",
            description="Type of customer",
            data_type="string",
            is_required=False,
            validation_rules={
                "enum": ["retail", "wholesale", "enterprise"]
            },
            display_order=5
        ),
    ]
    
    # Create KPIs that reference attributes
    profit_margin_kpi = KPI(
        name="Profit Margin",
        code="PROFIT_MARGIN",
        description="Percentage of revenue remaining as profit",
        
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
        
        expected_business_insights="""
        - Pricing effectiveness
        - Cost control efficiency
        - Product profitability
        - Competitive positioning
        """,
        
        target_value=40.0,
        threshold_warning=30.0,
        threshold_critical=20.0,
        
        category="Profitability"
    )
    profit_margin_kpi.object_models.append(sales_txn_model)
    
    avg_revenue_per_unit_kpi = KPI(
        name="Average Revenue Per Unit",
        code="AVG_REVENUE_PER_UNIT",
        description="Average selling price per unit",
        
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
        """,
        
        category="Pricing"
    )
    avg_revenue_per_unit_kpi.object_models.append(sales_txn_model)
    
    cost_ratio_kpi = KPI(
        name="Cost Ratio",
        code="COST_RATIO",
        description="Percentage of revenue consumed by costs",
        
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
        threshold_critical=80.0,
        
        category="Cost Management"
    )
    cost_ratio_kpi.object_models.append(sales_txn_model)
    
    # Create sample objects (transaction instances)
    transaction_1 = Object(
        name="Transaction #TXN-2024-001",
        code="TXN_2024_001",
        description="Enterprise customer purchase",
        data_values={
            "REVENUE": 100000.00,
            "COST": 60000.00,
            "QUANTITY": 500,
            "TXN_DATE": "2024-01-15",
            "CUSTOMER_TYPE": "enterprise"
        }
    )
    transaction_1.object_models.append(sales_txn_model)
    
    transaction_2 = Object(
        name="Transaction #TXN-2024-002",
        code="TXN_2024_002",
        description="Retail customer purchase",
        data_values={
            "REVENUE": 5000.00,
            "COST": 3500.00,
            "QUANTITY": 25,
            "TXN_DATE": "2024-01-16",
            "CUSTOMER_TYPE": "retail"
        }
    )
    transaction_2.object_models.append(sales_txn_model)
    
    return {
        "industry": retail_industry,
        "module": sales_module,
        "object_model": sales_txn_model,
        "attributes": attributes,
        "kpis": [profit_margin_kpi, avg_revenue_per_unit_kpi, cost_ratio_kpi],
        "objects": [transaction_1, transaction_2]
    }


# ============================================================================
# Example 2: Customer Account Model
# ============================================================================

def create_customer_account_model():
    """Create a customer account model with financial attributes."""
    
    # Create ObjectModel
    account_model = ObjectModel(
        name="Customer Account",
        code="CUST_ACCT",
        description="Customer account with financial metrics"
    )
    
    # Define Attributes
    attributes = [
        ObjectAttribute(
            object_model_id=account_model.id,
            name="Account Balance",
            code="ACCOUNT_BALANCE",
            data_type="float",
            is_required=True,
            validation_rules={"precision": 2},
            display_order=1
        ),
        ObjectAttribute(
            object_model_id=account_model.id,
            name="Credit Limit",
            code="CREDIT_LIMIT",
            data_type="float",
            is_required=True,
            validation_rules={"min": 0, "precision": 2},
            display_order=2
        ),
        ObjectAttribute(
            object_model_id=account_model.id,
            name="Total Purchases",
            code="TOTAL_PURCHASES",
            data_type="float",
            is_required=True,
            validation_rules={"min": 0, "precision": 2},
            display_order=3
        ),
        ObjectAttribute(
            object_model_id=account_model.id,
            name="Payment Count",
            code="PAYMENT_COUNT",
            data_type="integer",
            is_required=True,
            validation_rules={"min": 0},
            display_order=4
        ),
        ObjectAttribute(
            object_model_id=account_model.id,
            name="Account Status",
            code="ACCOUNT_STATUS",
            data_type="string",
            is_required=True,
            validation_rules={
                "enum": ["active", "suspended", "closed"]
            },
            display_order=5
        ),
    ]
    
    # Create KPIs
    credit_utilization_kpi = KPI(
        name="Credit Utilization",
        code="CREDIT_UTILIZATION",
        
        formula="Credit Utilization = Account Balance / Credit Limit * 100",
        calculation_formula="ACCOUNT_BALANCE / CREDIT_LIMIT * 100",
        
        attribute_references={
            "account_balance": "ACCOUNT_BALANCE",
            "credit_limit": "CREDIT_LIMIT"
        },
        
        unit_of_measure="percentage",
        
        kpi_definition="""
        Credit Utilization measures the percentage of available credit being used.
        High utilization may indicate credit risk.
        """,
        
        target_value=30.0,
        threshold_warning=70.0,
        threshold_critical=90.0,
        
        category="Credit Risk"
    )
    credit_utilization_kpi.object_models.append(account_model)
    
    avg_purchase_value_kpi = KPI(
        name="Average Purchase Value",
        code="AVG_PURCHASE_VALUE",
        
        formula="Average Purchase = Total Purchases / Payment Count",
        calculation_formula="TOTAL_PURCHASES / PAYMENT_COUNT",
        
        attribute_references={
            "total_purchases": "TOTAL_PURCHASES",
            "payment_count": "PAYMENT_COUNT"
        },
        
        unit_of_measure="USD",
        
        kpi_definition="""
        Average Purchase Value measures the average transaction size per payment.
        Helps identify high-value customers.
        """,
        
        category="Customer Value"
    )
    avg_purchase_value_kpi.object_models.append(account_model)
    
    # Create sample objects
    account_1 = Object(
        name="Account #ACC-001",
        code="ACC_001",
        data_values={
            "ACCOUNT_BALANCE": 5000.00,
            "CREDIT_LIMIT": 10000.00,
            "TOTAL_PURCHASES": 25000.00,
            "PAYMENT_COUNT": 12,
            "ACCOUNT_STATUS": "active"
        }
    )
    account_1.object_models.append(account_model)
    
    return {
        "object_model": account_model,
        "attributes": attributes,
        "kpis": [credit_utilization_kpi, avg_purchase_value_kpi],
        "objects": [account_1]
    }


# ============================================================================
# Example 3: Product Inventory Model
# ============================================================================

def create_product_inventory_model():
    """Create a product inventory model with stock attributes."""
    
    inventory_model = ObjectModel(
        name="Product Inventory",
        code="PROD_INV",
        description="Product inventory tracking"
    )
    
    # Define Attributes
    attributes = [
        ObjectAttribute(
            object_model_id=inventory_model.id,
            name="Units in Stock",
            code="UNITS_IN_STOCK",
            data_type="integer",
            is_required=True,
            validation_rules={"min": 0},
            display_order=1
        ),
        ObjectAttribute(
            object_model_id=inventory_model.id,
            name="Reorder Point",
            code="REORDER_POINT",
            data_type="integer",
            is_required=True,
            validation_rules={"min": 0},
            display_order=2
        ),
        ObjectAttribute(
            object_model_id=inventory_model.id,
            name="Units Sold This Month",
            code="UNITS_SOLD_MTD",
            data_type="integer",
            is_required=True,
            validation_rules={"min": 0},
            display_order=3
        ),
        ObjectAttribute(
            object_model_id=inventory_model.id,
            name="Unit Cost",
            code="UNIT_COST",
            data_type="float",
            is_required=True,
            validation_rules={"min": 0, "precision": 2},
            display_order=4
        ),
        ObjectAttribute(
            object_model_id=inventory_model.id,
            name="Unit Price",
            code="UNIT_PRICE",
            data_type="float",
            is_required=True,
            validation_rules={"min": 0, "precision": 2},
            display_order=5
        ),
    ]
    
    # Create KPIs
    stock_coverage_kpi = KPI(
        name="Stock Coverage Ratio",
        code="STOCK_COVERAGE",
        
        formula="Stock Coverage = Units in Stock / Reorder Point",
        calculation_formula="UNITS_IN_STOCK / REORDER_POINT",
        
        attribute_references={
            "units_in_stock": "UNITS_IN_STOCK",
            "reorder_point": "REORDER_POINT"
        },
        
        unit_of_measure="ratio",
        
        kpi_definition="""
        Stock Coverage Ratio indicates how many times the current stock exceeds
        the reorder point. Values below 1 indicate need to reorder.
        """,
        
        target_value=2.0,
        threshold_warning=1.0,
        threshold_critical=0.5,
        
        category="Inventory Management"
    )
    stock_coverage_kpi.object_models.append(inventory_model)
    
    inventory_value_kpi = KPI(
        name="Inventory Value",
        code="INVENTORY_VALUE",
        
        formula="Inventory Value = Units in Stock * Unit Cost",
        calculation_formula="UNITS_IN_STOCK * UNIT_COST",
        
        attribute_references={
            "units_in_stock": "UNITS_IN_STOCK",
            "unit_cost": "UNIT_COST"
        },
        
        unit_of_measure="USD",
        
        kpi_definition="""
        Inventory Value measures the total cost value of current stock.
        Important for financial reporting and working capital management.
        """,
        
        category="Financial"
    )
    inventory_value_kpi.object_models.append(inventory_model)
    
    unit_margin_kpi = KPI(
        name="Unit Margin",
        code="UNIT_MARGIN",
        
        formula="Unit Margin = (Unit Price - Unit Cost) / Unit Price * 100",
        calculation_formula="(UNIT_PRICE - UNIT_COST) / UNIT_PRICE * 100",
        
        attribute_references={
            "unit_price": "UNIT_PRICE",
            "unit_cost": "UNIT_COST"
        },
        
        unit_of_measure="percentage",
        
        kpi_definition="""
        Unit Margin measures the profit margin per unit sold.
        Indicates product profitability.
        """,
        
        target_value=40.0,
        threshold_warning=25.0,
        threshold_critical=15.0,
        
        category="Profitability"
    )
    unit_margin_kpi.object_models.append(inventory_model)
    
    # Create sample object
    product_1 = Object(
        name="Product #PROD-001",
        code="PROD_001",
        data_values={
            "UNITS_IN_STOCK": 500,
            "REORDER_POINT": 200,
            "UNITS_SOLD_MTD": 150,
            "UNIT_COST": 25.00,
            "UNIT_PRICE": 45.00
        }
    )
    product_1.object_models.append(inventory_model)
    
    return {
        "object_model": inventory_model,
        "attributes": attributes,
        "kpis": [stock_coverage_kpi, inventory_value_kpi, unit_margin_kpi],
        "objects": [product_1]
    }


# ============================================================================
# Usage Example
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("ObjectAttribute Examples")
    print("=" * 80)
    
    # Example 1: Sales Transaction
    print("\n1. Sales Transaction Model")
    print("-" * 80)
    sales_data = create_sales_transaction_model()
    print(f"Created: {sales_data['object_model'].name}")
    print(f"Attributes: {len(sales_data['attributes'])}")
    for attr in sales_data['attributes']:
        print(f"  - {attr.name} ({attr.code}): {attr.data_type}")
    print(f"KPIs: {len(sales_data['kpis'])}")
    for kpi in sales_data['kpis']:
        print(f"  - {kpi.name}: {kpi.calculation_formula}")
        print(f"    References: {kpi.attribute_references}")
    
    # Example 2: Customer Account
    print("\n2. Customer Account Model")
    print("-" * 80)
    account_data = create_customer_account_model()
    print(f"Created: {account_data['object_model'].name}")
    print(f"Attributes: {len(account_data['attributes'])}")
    for attr in account_data['attributes']:
        print(f"  - {attr.name} ({attr.code}): {attr.data_type}")
    print(f"KPIs: {len(account_data['kpis'])}")
    for kpi in account_data['kpis']:
        print(f"  - {kpi.name}: {kpi.calculation_formula}")
    
    # Example 3: Product Inventory
    print("\n3. Product Inventory Model")
    print("-" * 80)
    inventory_data = create_product_inventory_model()
    print(f"Created: {inventory_data['object_model'].name}")
    print(f"Attributes: {len(inventory_data['attributes'])}")
    for attr in inventory_data['attributes']:
        print(f"  - {attr.name} ({attr.code}): {attr.data_type}")
    print(f"KPIs: {len(inventory_data['kpis'])}")
    for kpi in inventory_data['kpis']:
        print(f"  - {kpi.name}: {kpi.calculation_formula}")
    
    print("\n" + "=" * 80)
    print("Examples completed successfully!")
    print("=" * 80)

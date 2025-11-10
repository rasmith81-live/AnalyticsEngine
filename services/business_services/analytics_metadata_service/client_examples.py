"""
Client Authorization Examples

Demonstrates how to set up clients, roles, and permissions with row-level
security and attribute masking.
"""

from analytics_models import (
    Client,
    ClientRole,
    ClientModulePermission,
    RoleObjectModelPermission,
    RoleObjectPermission,
    RoleKPIPermission,
    RoleAttributePermission,
    Module,
    ObjectModel,
    Object,
    KPI,
    ObjectAttribute
)


# ============================================================================
# Example 1: Multi-Tenant Setup with Module Access Control
# ============================================================================

def create_multi_tenant_setup():
    """Create multiple clients with different module access."""
    
    # Assume modules already exist
    sales_module = Module(name="Sales Management", code="SALES")
    finance_module = Module(name="Finance", code="FINANCE")
    hr_module = Module(name="Human Resources", code="HR")
    marketing_module = Module(name="Marketing", code="MARKETING")
    
    # Client 1: ACME Corp - Full access
    acme_corp = Client(
        name="ACME Corporation",
        code="ACME",
        description="Enterprise client with full access",
        contact_email="admin@acme.com",
        contact_phone="+1-555-0100",
        config={
            "max_users": 100,
            "features": ["advanced_analytics", "custom_reports", "api_access"],
            "subscription_tier": "enterprise"
        }
    )
    
    # ACME can access Sales, Finance, and Marketing (NOT HR)
    acme_sales_perm = ClientModulePermission(
        client_id=acme_corp.id,
        module_id=sales_module.id,
        can_view=True,
        can_create=True,
        can_update=True,
        can_delete=True
    )
    
    acme_finance_perm = ClientModulePermission(
        client_id=acme_corp.id,
        module_id=finance_module.id,
        can_view=True,
        can_create=True,
        can_update=True,
        can_delete=False  # Can't delete financial records
    )
    
    acme_marketing_perm = ClientModulePermission(
        client_id=acme_corp.id,
        module_id=marketing_module.id,
        can_view=True,
        can_create=True,
        can_update=True,
        can_delete=True
    )
    
    # Client 2: TechStart Inc - Limited access
    techstart = Client(
        name="TechStart Inc",
        code="TECHSTART",
        description="Startup client with basic access",
        contact_email="admin@techstart.io",
        contact_phone="+1-555-0200",
        config={
            "max_users": 25,
            "features": ["basic_analytics"],
            "subscription_tier": "starter"
        }
    )
    
    # TechStart can only access Sales (read-only)
    techstart_sales_perm = ClientModulePermission(
        client_id=techstart.id,
        module_id=sales_module.id,
        can_view=True,
        can_create=False,
        can_update=False,
        can_delete=False
    )
    
    return {
        "clients": [acme_corp, techstart],
        "modules": [sales_module, finance_module, hr_module, marketing_module],
        "permissions": [
            acme_sales_perm, acme_finance_perm, acme_marketing_perm,
            techstart_sales_perm
        ]
    }


# ============================================================================
# Example 2: Role-Based Access Control
# ============================================================================

def create_role_hierarchy():
    """Create roles with different permission levels."""
    
    acme_corp = Client(name="ACME Corporation", code="ACME")
    
    # Role 1: Administrator - Full access
    admin_role = ClientRole(
        client_id=acme_corp.id,
        name="Administrator",
        code="ADMIN",
        description="Full administrative access to all resources",
        permissions={
            "is_admin": True,
            "can_manage_users": True,
            "can_manage_roles": True,
            "can_export_data": True,
            "can_configure_system": True
        }
    )
    
    # Role 2: Sales Manager - Sales data access
    sales_mgr_role = ClientRole(
        client_id=acme_corp.id,
        name="Sales Manager",
        code="SALES_MGR",
        description="Manage sales data and view sales KPIs",
        permissions={
            "is_admin": False,
            "can_export_data": True,
            "can_view_reports": True
        }
    )
    
    # Role 3: Analyst - Read-only access
    analyst_role = ClientRole(
        client_id=acme_corp.id,
        name="Data Analyst",
        code="ANALYST",
        description="Read-only access for data analysis",
        permissions={
            "is_admin": False,
            "can_export_data": True,
            "can_view_reports": True
        }
    )
    
    # Role 4: Customer Service - Limited access with masking
    cs_role = ClientRole(
        client_id=acme_corp.id,
        name="Customer Service",
        code="CS_REP",
        description="Customer service with masked sensitive data",
        permissions={
            "is_admin": False,
            "can_view_customer_data": True,
            "sensitive_data_masked": True
        }
    )
    
    return {
        "client": acme_corp,
        "roles": [admin_role, sales_mgr_role, analyst_role, cs_role]
    }


# ============================================================================
# Example 3: ObjectModel Permissions
# ============================================================================

def setup_objectmodel_permissions():
    """Set up permissions for object models."""
    
    # Assume roles and object models exist
    admin_role = ClientRole(name="Administrator", code="ADMIN")
    analyst_role = ClientRole(name="Analyst", code="ANALYST")
    
    sales_txn_model = ObjectModel(name="Sales Transaction", code="SALES_TXN")
    customer_model = ObjectModel(name="Customer", code="CUSTOMER")
    product_model = ObjectModel(name="Product", code="PRODUCT")
    
    # Admin: Full access to all object models
    admin_sales_perm = RoleObjectModelPermission(
        role_id=admin_role.id,
        object_model_id=sales_txn_model.id,
        can_view=True,
        can_create=True,
        can_update=True,
        can_delete=True
    )
    
    admin_customer_perm = RoleObjectModelPermission(
        role_id=admin_role.id,
        object_model_id=customer_model.id,
        can_view=True,
        can_create=True,
        can_update=True,
        can_delete=True
    )
    
    # Analyst: Read-only access
    analyst_sales_perm = RoleObjectModelPermission(
        role_id=analyst_role.id,
        object_model_id=sales_txn_model.id,
        can_view=True,
        can_create=False,
        can_update=False,
        can_delete=False
    )
    
    analyst_customer_perm = RoleObjectModelPermission(
        role_id=analyst_role.id,
        object_model_id=customer_model.id,
        can_view=True,
        can_create=False,
        can_update=False,
        can_delete=False
    )
    
    return {
        "permissions": [
            admin_sales_perm, admin_customer_perm,
            analyst_sales_perm, analyst_customer_perm
        ]
    }


# ============================================================================
# Example 4: Row-Level Security
# ============================================================================

def setup_row_level_security():
    """Set up row-level security with data filters."""
    
    # Regional managers can only see their region's data
    west_mgr_role = ClientRole(
        name="Regional Manager - West",
        code="REGIONAL_MGR_WEST"
    )
    
    east_mgr_role = ClientRole(
        name="Regional Manager - East",
        code="REGIONAL_MGR_EAST"
    )
    
    # Assume sales transactions exist
    sales_txn_1 = Object(name="Transaction #001", code="TXN_001")
    sales_txn_2 = Object(name="Transaction #002", code="TXN_002")
    
    # West Manager: Can only see US-WEST region data
    west_perm_1 = RoleObjectPermission(
        role_id=west_mgr_role.id,
        object_id=sales_txn_1.id,
        can_view=True,
        can_update=True,
        can_delete=False,
        row_filter={
            "attribute_filters": {
                "REGION": {"eq": "US-WEST"},
                "STATUS": {"ne": "cancelled"}
            },
            "logic": "AND"
        },
        config={
            "description": "West region sales data only"
        }
    )
    
    # East Manager: Can only see US-EAST region data
    east_perm_1 = RoleObjectPermission(
        role_id=east_mgr_role.id,
        object_id=sales_txn_1.id,
        can_view=True,
        can_update=True,
        can_delete=False,
        row_filter={
            "attribute_filters": {
                "REGION": {"eq": "US-EAST"},
                "STATUS": {"ne": "cancelled"}
            },
            "logic": "AND"
        },
        config={
            "description": "East region sales data only"
        }
    )
    
    # Enterprise Account Manager: Can only see enterprise customers
    enterprise_mgr_role = ClientRole(
        name="Enterprise Account Manager",
        code="ENTERPRISE_MGR"
    )
    
    enterprise_perm = RoleObjectPermission(
        role_id=enterprise_mgr_role.id,
        object_id=sales_txn_1.id,
        can_view=True,
        can_update=True,
        can_delete=False,
        row_filter={
            "attribute_filters": {
                "CUSTOMER_TYPE": {"eq": "enterprise"},
                "REVENUE": {"gte": 50000}
            },
            "logic": "AND"
        },
        config={
            "description": "Enterprise customers with revenue >= $50K"
        }
    )
    
    return {
        "roles": [west_mgr_role, east_mgr_role, enterprise_mgr_role],
        "permissions": [west_perm_1, east_perm_1, enterprise_perm]
    }


# ============================================================================
# Example 5: Attribute-Level Security with Masking
# ============================================================================

def setup_attribute_masking():
    """Set up attribute-level security with data masking."""
    
    cs_role = ClientRole(
        name="Customer Service",
        code="CS_REP"
    )
    
    finance_role = ClientRole(
        name="Finance Analyst",
        code="FINANCE_ANALYST"
    )
    
    # Assume attributes exist
    customer_name_attr = ObjectAttribute(name="Customer Name", code="CUSTOMER_NAME")
    email_attr = ObjectAttribute(name="Email", code="EMAIL")
    phone_attr = ObjectAttribute(name="Phone", code="PHONE")
    ssn_attr = ObjectAttribute(name="SSN", code="SSN")
    credit_card_attr = ObjectAttribute(name="Credit Card", code="CREDIT_CARD")
    salary_attr = ObjectAttribute(name="Salary", code="SALARY")
    
    # Customer Service: Can see name and email, but sensitive data is masked
    
    # Name: No masking
    cs_name_perm = RoleAttributePermission(
        role_id=cs_role.id,
        attribute_id=customer_name_attr.id,
        can_view=True,
        can_update=False,
        is_masked=False
    )
    
    # Email: No masking
    cs_email_perm = RoleAttributePermission(
        role_id=cs_role.id,
        attribute_id=email_attr.id,
        can_view=True,
        can_update=False,
        is_masked=False
    )
    
    # Phone: Partial masking (show last 4 digits)
    cs_phone_perm = RoleAttributePermission(
        role_id=cs_role.id,
        attribute_id=phone_attr.id,
        can_view=True,
        can_update=False,
        is_masked=True,
        mask_type="partial",
        config={
            "mask_pattern": "***-***-{last4}",
            "description": "Show last 4 digits only"
        }
    )
    
    # SSN: Full masking
    cs_ssn_perm = RoleAttributePermission(
        role_id=cs_role.id,
        attribute_id=ssn_attr.id,
        can_view=True,
        can_update=False,
        is_masked=True,
        mask_type="full",
        config={
            "mask_pattern": "***-**-****",
            "description": "Completely hidden"
        }
    )
    
    # Credit Card: Partial masking (show last 4 digits)
    cs_cc_perm = RoleAttributePermission(
        role_id=cs_role.id,
        attribute_id=credit_card_attr.id,
        can_view=True,
        can_update=False,
        is_masked=True,
        mask_type="partial",
        config={
            "mask_pattern": "****-****-****-{last4}",
            "description": "Show last 4 digits only"
        }
    )
    
    # Salary: No access (attribute not granted)
    # CS role cannot see salary at all
    
    # Finance Analyst: Can see all data unmasked
    
    finance_ssn_perm = RoleAttributePermission(
        role_id=finance_role.id,
        attribute_id=ssn_attr.id,
        can_view=True,
        can_update=False,
        is_masked=False  # No masking for finance
    )
    
    finance_salary_perm = RoleAttributePermission(
        role_id=finance_role.id,
        attribute_id=salary_attr.id,
        can_view=True,
        can_update=True,
        is_masked=False
    )
    
    return {
        "roles": [cs_role, finance_role],
        "permissions": [
            cs_name_perm, cs_email_perm, cs_phone_perm, cs_ssn_perm, cs_cc_perm,
            finance_ssn_perm, finance_salary_perm
        ]
    }


# ============================================================================
# Example 6: KPI Access Control
# ============================================================================

def setup_kpi_permissions():
    """Set up KPI access permissions by role."""
    
    exec_role = ClientRole(name="Executive", code="EXECUTIVE")
    sales_mgr_role = ClientRole(name="Sales Manager", code="SALES_MGR")
    analyst_role = ClientRole(name="Analyst", code="ANALYST")
    
    # Assume KPIs exist
    revenue_kpi = KPI(name="Total Revenue", code="REVENUE")
    profit_margin_kpi = KPI(name="Profit Margin", code="PROFIT_MARGIN")
    cac_kpi = KPI(name="Customer Acquisition Cost", code="CAC")
    employee_cost_kpi = KPI(name="Employee Cost", code="EMPLOYEE_COST")
    churn_rate_kpi = KPI(name="Churn Rate", code="CHURN_RATE")
    
    # Executive: Can see ALL KPIs and update them
    exec_kpis = [revenue_kpi, profit_margin_kpi, cac_kpi, employee_cost_kpi, churn_rate_kpi]
    exec_permissions = []
    for kpi in exec_kpis:
        exec_permissions.append(RoleKPIPermission(
            role_id=exec_role.id,
            kpi_id=kpi.id,
            can_view=True,
            can_update=True
        ))
    
    # Sales Manager: Can see sales-related KPIs (read-only)
    sales_kpis = [revenue_kpi, cac_kpi, churn_rate_kpi]
    sales_permissions = []
    for kpi in sales_kpis:
        sales_permissions.append(RoleKPIPermission(
            role_id=sales_mgr_role.id,
            kpi_id=kpi.id,
            can_view=True,
            can_update=False  # Read-only
        ))
    
    # Analyst: Can see operational KPIs (read-only)
    analyst_kpis = [revenue_kpi, profit_margin_kpi, churn_rate_kpi]
    analyst_permissions = []
    for kpi in analyst_kpis:
        analyst_permissions.append(RoleKPIPermission(
            role_id=analyst_role.id,
            kpi_id=kpi.id,
            can_view=True,
            can_update=False
        ))
    
    # Note: Employee Cost KPI is hidden from Sales Manager and Analyst
    
    return {
        "roles": [exec_role, sales_mgr_role, analyst_role],
        "permissions": exec_permissions + sales_permissions + analyst_permissions
    }


# ============================================================================
# Example 7: Complete Multi-Tenant Scenario
# ============================================================================

def create_complete_scenario():
    """Create a complete multi-tenant scenario with all permission types."""
    
    # Create client
    retail_corp = Client(
        name="Retail Corporation",
        code="RETAIL_CORP",
        description="Large retail chain",
        contact_email="admin@retailcorp.com",
        config={
            "max_users": 500,
            "features": ["advanced_analytics", "custom_reports", "api_access"],
            "subscription_tier": "enterprise",
            "regions": ["US-WEST", "US-EAST", "US-CENTRAL"]
        }
    )
    
    # Grant module access
    sales_module = Module(name="Sales", code="SALES")
    inventory_module = Module(name="Inventory", code="INVENTORY")
    
    retail_sales_perm = ClientModulePermission(
        client_id=retail_corp.id,
        module_id=sales_module.id,
        can_view=True,
        can_create=True,
        can_update=True,
        can_delete=True
    )
    
    retail_inventory_perm = ClientModulePermission(
        client_id=retail_corp.id,
        module_id=inventory_module.id,
        can_view=True,
        can_create=True,
        can_update=True,
        can_delete=False
    )
    
    # Create roles
    store_mgr_role = ClientRole(
        client_id=retail_corp.id,
        name="Store Manager",
        code="STORE_MGR",
        description="Manages individual store operations",
        permissions={
            "can_view_store_data": True,
            "can_manage_inventory": True,
            "region_restricted": True
        }
    )
    
    regional_dir_role = ClientRole(
        client_id=retail_corp.id,
        name="Regional Director",
        code="REGIONAL_DIR",
        description="Oversees multiple stores in a region",
        permissions={
            "can_view_regional_data": True,
            "can_view_all_stores": True,
            "region_restricted": True
        }
    )
    
    # Set up ObjectModel permissions
    sales_txn_model = ObjectModel(name="Sales Transaction", code="SALES_TXN")
    
    store_mgr_om_perm = RoleObjectModelPermission(
        role_id=store_mgr_role.id,
        object_model_id=sales_txn_model.id,
        can_view=True,
        can_create=True,
        can_update=True,
        can_delete=False
    )
    
    # Set up row-level security (store manager can only see their store)
    sales_txn_obj = Object(name="Transaction #001", code="TXN_001")
    
    store_mgr_obj_perm = RoleObjectPermission(
        role_id=store_mgr_role.id,
        object_id=sales_txn_obj.id,
        can_view=True,
        can_update=True,
        can_delete=False,
        row_filter={
            "attribute_filters": {
                "STORE_ID": {"eq": "STORE_001"},  # Only their store
                "STATUS": {"ne": "cancelled"}
            }
        }
    )
    
    # Regional director can see all stores in their region
    regional_dir_obj_perm = RoleObjectPermission(
        role_id=regional_dir_role.id,
        object_id=sales_txn_obj.id,
        can_view=True,
        can_update=False,
        can_delete=False,
        row_filter={
            "attribute_filters": {
                "REGION": {"eq": "US-WEST"},  # All stores in region
                "STATUS": {"ne": "cancelled"}
            }
        }
    )
    
    # Set up KPI permissions
    daily_sales_kpi = KPI(name="Daily Sales", code="DAILY_SALES")
    inventory_turnover_kpi = KPI(name="Inventory Turnover", code="INV_TURNOVER")
    
    # Store manager can see store-level KPIs
    store_mgr_sales_kpi_perm = RoleKPIPermission(
        role_id=store_mgr_role.id,
        kpi_id=daily_sales_kpi.id,
        can_view=True,
        can_update=False
    )
    
    # Regional director can see all KPIs
    regional_dir_sales_kpi_perm = RoleKPIPermission(
        role_id=regional_dir_role.id,
        kpi_id=daily_sales_kpi.id,
        can_view=True,
        can_update=True
    )
    
    regional_dir_inv_kpi_perm = RoleKPIPermission(
        role_id=regional_dir_role.id,
        kpi_id=inventory_turnover_kpi.id,
        can_view=True,
        can_update=True
    )
    
    return {
        "client": retail_corp,
        "roles": [store_mgr_role, regional_dir_role],
        "module_permissions": [retail_sales_perm, retail_inventory_perm],
        "objectmodel_permissions": [store_mgr_om_perm],
        "object_permissions": [store_mgr_obj_perm, regional_dir_obj_perm],
        "kpi_permissions": [
            store_mgr_sales_kpi_perm,
            regional_dir_sales_kpi_perm,
            regional_dir_inv_kpi_perm
        ]
    }


# ============================================================================
# Usage Example
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("Client Authorization Examples")
    print("=" * 80)
    
    # Example 1: Multi-tenant setup
    print("\n1. Multi-Tenant Setup")
    print("-" * 80)
    tenant_data = create_multi_tenant_setup()
    print(f"Created {len(tenant_data['clients'])} clients")
    print(f"Created {len(tenant_data['modules'])} modules")
    print(f"Created {len(tenant_data['permissions'])} module permissions")
    
    # Example 2: Role hierarchy
    print("\n2. Role Hierarchy")
    print("-" * 80)
    role_data = create_role_hierarchy()
    print(f"Created {len(role_data['roles'])} roles for {role_data['client'].name}")
    for role in role_data['roles']:
        print(f"  - {role.name} ({role.code})")
    
    # Example 3: Row-level security
    print("\n3. Row-Level Security")
    print("-" * 80)
    rls_data = setup_row_level_security()
    print(f"Created {len(rls_data['roles'])} roles with row-level security")
    for perm in rls_data['permissions']:
        print(f"  - Role {perm.role_id}: {perm.row_filter}")
    
    # Example 4: Attribute masking
    print("\n4. Attribute Masking")
    print("-" * 80)
    masking_data = setup_attribute_masking()
    print(f"Created {len(masking_data['permissions'])} attribute permissions")
    masked_count = sum(1 for p in masking_data['permissions'] if p.is_masked)
    print(f"  - {masked_count} attributes with masking enabled")
    
    # Example 5: KPI permissions
    print("\n5. KPI Permissions")
    print("-" * 80)
    kpi_data = setup_kpi_permissions()
    print(f"Created {len(kpi_data['permissions'])} KPI permissions")
    for role in kpi_data['roles']:
        role_perms = [p for p in kpi_data['permissions'] if p.role_id == role.id]
        print(f"  - {role.name}: {len(role_perms)} KPIs")
    
    print("\n" + "=" * 80)
    print("Examples completed successfully!")
    print("=" * 80)

"""
Seed script to create base value chains and modules in the metadata database.
"""

import asyncio
import httpx

METADATA_SERVICE_URL = "http://127.0.0.1:8020"

VALUE_CHAINS = [
    {
        "kind": "value_chain_pattern_definition",
        "code": "supply_chain",
        "name": "Supply Chain",
        "description": "Supply chain management including procurement, logistics, and inventory",
        "domain": "company"
    },
    {
        "kind": "value_chain_pattern_definition",
        "code": "sales_marketing",
        "name": "Sales & Marketing",
        "description": "Sales operations, marketing campaigns, and customer acquisition",
        "domain": "company"
    },
    {
        "kind": "value_chain_pattern_definition",
        "code": "finance_accounting",
        "name": "Finance & Accounting",
        "description": "Financial operations, accounting, and treasury management",
        "domain": "company"
    },
    {
        "kind": "value_chain_pattern_definition",
        "code": "human_resources",
        "name": "Human Resources",
        "description": "HR operations, talent management, and workforce planning",
        "domain": "company"
    },
    {
        "kind": "value_chain_pattern_definition",
        "code": "operations",
        "name": "Operations",
        "description": "Core business operations and process management",
        "domain": "company"
    }
]

# Modules with their value chain assignments (for relationship creation only)
MODULES = [
    # Supply Chain modules (business_process_definition)
    {"kind": "business_process_definition", "code": "procurement", "name": "Procurement", "process_type": "core", "_value_chain": "supply_chain"},
    {"kind": "business_process_definition", "code": "inventory_management", "name": "Inventory Management", "process_type": "core", "_value_chain": "supply_chain"},
    {"kind": "business_process_definition", "code": "logistics", "name": "Logistics", "process_type": "core", "_value_chain": "supply_chain"},
    {"kind": "business_process_definition", "code": "warehouse_management", "name": "Warehouse Management", "process_type": "core", "_value_chain": "supply_chain"},
    {"kind": "business_process_definition", "code": "supplier_management", "name": "Supplier Management", "process_type": "core", "_value_chain": "supply_chain"},
    
    # Sales & Marketing modules
    {"kind": "business_process_definition", "code": "sales_operations", "name": "Sales Operations", "process_type": "core", "_value_chain": "sales_marketing"},
    {"kind": "business_process_definition", "code": "marketing_campaigns", "name": "Marketing Campaigns", "process_type": "core", "_value_chain": "sales_marketing"},
    {"kind": "business_process_definition", "code": "customer_acquisition", "name": "Customer Acquisition", "process_type": "core", "_value_chain": "sales_marketing"},
    {"kind": "business_process_definition", "code": "sales_training", "name": "Sales Training & Coaching", "process_type": "support", "_value_chain": "sales_marketing"},
    
    # Finance & Accounting modules
    {"kind": "business_process_definition", "code": "accounts_receivable", "name": "Accounts Receivable", "process_type": "core", "_value_chain": "finance_accounting"},
    {"kind": "business_process_definition", "code": "accounts_payable", "name": "Accounts Payable", "process_type": "core", "_value_chain": "finance_accounting"},
    {"kind": "business_process_definition", "code": "financial_reporting", "name": "Financial Reporting", "process_type": "core", "_value_chain": "finance_accounting"},
    {"kind": "business_process_definition", "code": "treasury", "name": "Treasury", "process_type": "core", "_value_chain": "finance_accounting"},
    
    # Human Resources modules
    {"kind": "business_process_definition", "code": "talent_acquisition", "name": "Talent Acquisition", "process_type": "core", "_value_chain": "human_resources"},
    {"kind": "business_process_definition", "code": "performance_management", "name": "Performance Management", "process_type": "core", "_value_chain": "human_resources"},
    {"kind": "business_process_definition", "code": "compensation_benefits", "name": "Compensation & Benefits", "process_type": "core", "_value_chain": "human_resources"},
    
    # Operations modules
    {"kind": "business_process_definition", "code": "production", "name": "Production", "process_type": "core", "_value_chain": "operations"},
    {"kind": "business_process_definition", "code": "quality_management", "name": "Quality Management", "process_type": "core", "_value_chain": "operations"},
    {"kind": "business_process_definition", "code": "maintenance", "name": "Maintenance", "process_type": "support", "_value_chain": "operations"},
]


async def seed_metadata():
    """Seed value chains and modules."""
    async with httpx.AsyncClient(timeout=30.0) as client:
        # Create value chains
        print("Creating value chains...")
        for vc in VALUE_CHAINS:
            try:
                response = await client.post(
                    f"{METADATA_SERVICE_URL}/api/v1/metadata/definitions",
                    json=vc,
                    params={"created_by": "system"}
                )
                if response.status_code == 201:
                    print(f"  ✅ Created: {vc['code']}")
                elif response.status_code == 409:
                    print(f"  ⏭️  Already exists: {vc['code']}")
                else:
                    print(f"  ❌ Failed: {vc['code']} - {response.status_code}: {response.text}")
            except Exception as e:
                print(f"  ❌ Error: {vc['code']} - {e}")
        
        # Create modules (without embedded value_chain - relationships handle this)
        print("\nCreating modules...")
        for mod in MODULES:
            # Extract value_chain for relationship, don't include in definition
            value_chain = mod.pop("_value_chain", None)
            mod["_value_chain"] = value_chain  # Keep for relationship creation
            
            # Create definition without _value_chain
            definition = {k: v for k, v in mod.items() if not k.startswith("_")}
            
            try:
                response = await client.post(
                    f"{METADATA_SERVICE_URL}/api/v1/metadata/definitions",
                    json=definition,
                    params={"created_by": "system"}
                )
                if response.status_code == 201:
                    print(f"  ✅ Created: {mod['code']}")
                elif response.status_code == 409:
                    print(f"  ⏭️  Already exists: {mod['code']}")
                else:
                    print(f"  ❌ Failed: {mod['code']} - {response.status_code}: {response.text}")
            except Exception as e:
                print(f"  ❌ Error: {mod['code']} - {e}")
        
        # Create relationships between modules and value chains
        print("\nCreating module-value chain relationships...")
        for mod in MODULES:
            value_chain = mod.get("_value_chain")
            if not value_chain:
                continue
            try:
                response = await client.post(
                    f"{METADATA_SERVICE_URL}/api/v1/metadata/relationships",
                    json={
                        "from_entity_code": mod["code"],
                        "to_entity_code": value_chain,
                        "relationship_type": "belongs_to"
                    },
                    params={"created_by": "system"}
                )
                if response.status_code in (200, 201):
                    print(f"  ✅ {mod['code']} -> {value_chain}")
                elif response.status_code == 409:
                    print(f"  ⏭️  Already exists: {mod['code']} -> {value_chain}")
                else:
                    print(f"  ❌ Failed: {mod['code']} -> {value_chain} - {response.status_code}")
            except Exception as e:
                print(f"  ❌ Error: {mod['code']} -> {value_chain} - {e}")
        
        print("\n✅ Seeding complete!")


if __name__ == "__main__":
    asyncio.run(seed_metadata())

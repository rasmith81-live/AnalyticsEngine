"""
Analyze SCOR Object Model Gaps

Compares required objects from SCOR KPIs against existing object models
to identify which need to be created.
"""

from pathlib import Path
import re

# Required objects from SCOR KPIs
SCOR_REQUIRED_OBJECTS = {
    "AccountsPayable",
    "AccountsReceivable",
    "Activity",
    "Asset",
    "Capacity",
    "Cost",
    "CostCenter",
    "Delivery",
    "Emission",
    "Employee",
    "Energy",
    "Inventory",
    "Invoice",
    "Material",
    "Order",
    "OrderLine",
    "Payment",
    "Product",
    "Production",
    "Receipt",
    "Revenue",
    "SafetyIncident",
    "Shipment",
    "Supplier",
    "Transportation",
    "WorkHours"
}

def get_existing_objects(object_models_dir: Path) -> set:
    """Get list of existing object model codes."""
    existing = set()
    
    for file_path in object_models_dir.glob("*.py"):
        if file_path.name in ['__init__.py', 'registry.py']:
            continue
            
        # Read file and extract code
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Look for ObjectModel code parameter
            match = re.search(r'code\s*=\s*["\']([A-Z_]+)["\']', content)
            if match:
                code = match.group(1)
                # Convert to PascalCase for comparison
                pascal_case = ''.join(word.capitalize() for word in code.split('_'))
                existing.add(pascal_case)
        except Exception as e:
            print(f"[WARN] Could not parse {file_path.name}: {e}")
    
    return existing

def main():
    """Analyze object model gaps."""
    
    print("=" * 80)
    print("SCOR OBJECT MODEL GAP ANALYSIS")
    print("=" * 80)
    print()
    
    # Get existing objects
    project_root = Path(__file__).parent.parent.parent
    object_models_dir = project_root / 'services' / 'business_services' / 'analytics_models' / 'definitions' / 'object_models'
    
    existing_objects = get_existing_objects(object_models_dir)
    
    print(f"[INFO] Required by SCOR KPIs: {len(SCOR_REQUIRED_OBJECTS)} objects")
    print(f"[INFO] Existing in system: {len(existing_objects)} objects")
    print()
    
    # Find gaps
    missing_objects = SCOR_REQUIRED_OBJECTS - existing_objects
    existing_required = SCOR_REQUIRED_OBJECTS & existing_objects
    
    # Display results
    print("=" * 80)
    print(f"EXISTING OBJECTS ({len(existing_required)})")
    print("=" * 80)
    for obj in sorted(existing_required):
        print(f"  ✅ {obj}")
    print()
    
    print("=" * 80)
    print(f"MISSING OBJECTS ({len(missing_objects)})")
    print("=" * 80)
    for obj in sorted(missing_objects):
        print(f"  ❌ {obj}")
    print()
    
    # Coverage stats
    coverage = (len(existing_required) / len(SCOR_REQUIRED_OBJECTS)) * 100
    print("=" * 80)
    print("COVERAGE STATISTICS")
    print("=" * 80)
    print(f"Coverage: {coverage:.1f}%")
    print(f"Existing: {len(existing_required)}/{len(SCOR_REQUIRED_OBJECTS)}")
    print(f"Missing: {len(missing_objects)}/{len(SCOR_REQUIRED_OBJECTS)}")
    print()
    
    # Priority categorization
    print("=" * 80)
    print("PRIORITY CATEGORIZATION")
    print("=" * 80)
    print()
    
    # High Priority - Core supply chain objects
    high_priority = {
        "Order", "OrderLine", "Shipment", "Delivery", "Inventory",
        "Product", "Supplier", "Cost", "Revenue"
    }
    high_missing = missing_objects & high_priority
    
    print(f"HIGH PRIORITY ({len(high_missing)}):")
    print("Core supply chain objects needed for basic SCOR metrics")
    for obj in sorted(high_missing):
        print(f"  🔴 {obj}")
    print()
    
    # Medium Priority - Financial and operational
    medium_priority = {
        "Invoice", "Payment", "Receipt", "AccountsPayable", "AccountsReceivable",
        "Production", "Material", "Asset", "CostCenter", "Activity"
    }
    medium_missing = missing_objects & medium_priority
    
    print(f"MEDIUM PRIORITY ({len(medium_missing)}):")
    print("Financial and operational objects for advanced metrics")
    for obj in sorted(medium_missing):
        print(f"  🟡 {obj}")
    print()
    
    # Low Priority - Specialized metrics
    low_priority = {
        "Capacity", "Energy", "Emission", "Transportation",
        "Employee", "WorkHours", "SafetyIncident"
    }
    low_missing = missing_objects & low_priority
    
    print(f"LOW PRIORITY ({len(low_missing)}):")
    print("Specialized objects for agility, environmental, and social metrics")
    for obj in sorted(low_missing):
        print(f"  🟢 {obj}")
    print()
    
    # Next steps
    print("=" * 80)
    print("RECOMMENDED NEXT STEPS")
    print("=" * 80)
    print()
    print("1. Create HIGH PRIORITY objects first (core supply chain)")
    print("   These enable: Perfect Order Fulfillment, Cycle Time, COGS")
    print()
    print("2. Create MEDIUM PRIORITY objects (financial/operational)")
    print("   These enable: Cash-to-Cash, ROWC, Total SC Cost")
    print()
    print("3. Create LOW PRIORITY objects (specialized)")
    print("   These enable: Agility, Environmental, Social metrics")
    print()
    print("4. For each new object:")
    print("   a. Create object_models/{name}.py with table_schema")
    print("   b. Extract JSON schema")
    print("   c. Manually add to db_models.py")
    print("   d. Create Alembic migration")
    print()
    print("=" * 80)
    
    # Save report
    report_path = project_root / 'services' / 'business_services' / 'analytics_models' / 'SCOR_OBJECT_GAP_ANALYSIS.md'
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# SCOR Object Model Gap Analysis\n\n")
        f.write(f"**Generated**: {Path(__file__).name}\n\n")
        f.write(f"## Summary\n\n")
        f.write(f"- **Required**: {len(SCOR_REQUIRED_OBJECTS)} objects\n")
        f.write(f"- **Existing**: {len(existing_required)} objects ({coverage:.1f}%)\n")
        f.write(f"- **Missing**: {len(missing_objects)} objects\n\n")
        
        f.write(f"## Existing Objects ({len(existing_required)})\n\n")
        for obj in sorted(existing_required):
            f.write(f"- ✅ {obj}\n")
        f.write("\n")
        
        f.write(f"## Missing Objects by Priority\n\n")
        
        f.write(f"### 🔴 HIGH PRIORITY ({len(high_missing)})\n")
        f.write("Core supply chain objects\n\n")
        for obj in sorted(high_missing):
            f.write(f"- {obj}\n")
        f.write("\n")
        
        f.write(f"### 🟡 MEDIUM PRIORITY ({len(medium_missing)})\n")
        f.write("Financial and operational objects\n\n")
        for obj in sorted(medium_missing):
            f.write(f"- {obj}\n")
        f.write("\n")
        
        f.write(f"### 🟢 LOW PRIORITY ({len(low_missing)})\n")
        f.write("Specialized metrics objects\n\n")
        for obj in sorted(low_missing):
            f.write(f"- {obj}\n")
        f.write("\n")
        
        f.write("## Implementation Plan\n\n")
        f.write("1. Create HIGH PRIORITY objects (enables core metrics)\n")
        f.write("2. Create MEDIUM PRIORITY objects (enables financial metrics)\n")
        f.write("3. Create LOW PRIORITY objects (enables specialized metrics)\n")
    
    print(f"[INFO] Report saved to: {report_path}")
    print()
    
    return len(missing_objects) == 0

if __name__ == '__main__':
    import sys
    success = main()
    sys.exit(0 if success else 1)

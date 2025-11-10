"""
Script to consolidate rate/ratio KPI variants into base KPIs.
Automates the consolidation process for remaining rate/ratio duplicates.
"""

import re
from pathlib import Path

# Define consolidations to perform
CONSOLIDATIONS = [
    {
        'base_file': 'revenue_growth.py',
        'delete_file': 'revenue_growth_rate.py',
        'base_code': 'REVENUE_GROWTH',
        'delete_code': 'REVENUE_GROWTH_RATE',
        'base_modules': ['CHANNEL_SALES'],
        'add_modules': ['SALES_PERFORMANCE'],
        'name': 'Revenue Growth'
    },
    {
        'base_file': 'sales_growth.py',
        'delete_file': 'sales_growth_rate.py',
        'base_code': 'SALES_GROWTH',
        'delete_code': 'SALES_GROWTH_RATE',
        'base_modules': ['BUS_DEV', 'KEY_ACCOUNT_MANAGEMENT', 'SALES_STRATEGY'],
        'add_modules': ['SALES_OPERATIONS'],
        'name': 'Sales Growth'
    },
    {
        'base_file': 'sales_forecast_accuracy.py',
        'delete_file': 'sales_forecast_accuracy_rate.py',
        'base_code': 'SALES_FORECAST_ACCURACY',
        'delete_code': 'SALES_FORECAST_ACCURACY_RATE',
        'base_modules': ['INSIDE_SALES', 'KEY_ACCOUNT_MANAGEMENT', 'OUTSIDE_SALES', 'SALES_DEVELOPMENT', 'SALES_OPERATIONS', 'SALES_PERFORMANCE', 'SALES_STRATEGY', 'SALES_TRAINING_COACHING'],
        'add_modules': ['SALES_ENABLEMENT'],
        'name': 'Sales Forecast Accuracy'
    },
    {
        'base_file': 'sales_target_achievement.py',
        'delete_file': 'sales_target_achievement_rate.py',
        'base_code': 'SALES_TARGET_ACHIEVEMENT',
        'delete_code': 'SALES_TARGET_ACHIEVEMENT_RATE',
        'base_modules': ['INSIDE_SALES'],
        'add_modules': ['SALES_PERFORMANCE'],
        'name': 'Sales Target Achievement'
    },
    {
        'base_file': 'sales_meeting_conversion_rate.py',
        'delete_file': 'sales_meeting_conversion_ratio.py',
        'base_code': 'SALES_MEETING_CONVERSION_RATE',
        'delete_code': 'SALES_MEETING_CONVERSION_RATIO',
        'base_modules': ['KEY_ACCOUNT_MANAGEMENT', 'SALES_ENABLEMENT'],
        'add_modules': ['BUS_DEV'],
        'name': 'Sales Meeting Conversion Rate'
    },
    {
        'base_file': 'new_customer_rate.py',
        'delete_file': 'new_customer_ratio.py',
        'base_code': 'NEW_CUSTOMER_RATE',
        'delete_code': 'NEW_CUSTOMER_RATIO',
        'base_modules': ['SALES_OPERATIONS'],
        'add_modules': ['OUTSIDE_SALES'],
        'name': 'New Customer Rate'
    }
]

def main():
    kpi_dir = Path('kpis')
    
    print("=" * 80)
    print("CONSOLIDATING RATE/RATIO KPI VARIANTS")
    print("=" * 80)
    print()
    
    for consolidation in CONSOLIDATIONS:
        print(f"\nProcessing: {consolidation['name']}")
        print("-" * 60)
        
        base_path = kpi_dir / consolidation['base_file']
        delete_path = kpi_dir / consolidation['delete_file']
        
        # Check if files exist
        if not base_path.exists():
            print(f"  ❌ Base file not found: {consolidation['base_file']}")
            continue
        
        if not delete_path.exists():
            print(f"  ⚠️  Delete file not found (may already be deleted): {consolidation['delete_file']}")
            continue
        
        # Read base file
        with open(base_path, 'r', encoding='utf-8') as f:
            base_content = f.read()
        
        # Read delete file
        with open(delete_path, 'r', encoding='utf-8') as f:
            delete_content = f.read()
        
        # Extract modules from delete file
        delete_modules_match = re.search(r'"modules":\s*\[([^\]]+)\]', delete_content)
        if delete_modules_match:
            delete_modules_str = delete_modules_match.group(1)
            print(f"  Found modules in delete file: {delete_modules_str}")
        
        # Update modules in base file
        all_modules = consolidation['base_modules'] + consolidation['add_modules']
        all_modules_unique = sorted(list(set(all_modules)))
        modules_str = ', '.join([f'"{m}"' for m in all_modules_unique])
        
        # Update metadata in base file
        metadata_pattern = r'(metadata_=\{[^}]*"modules":\s*\[)[^\]]+(\][^}]*\})'
        updated_content = re.sub(
            metadata_pattern,
            f'\\1{modules_str}\\2',
            base_content
        )
        
        # Add replaces field if not present
        if '"replaces"' not in updated_content:
            # Add before closing brace of metadata
            updated_content = re.sub(
                r'(\s+)(}[\s\n]*\)[\s\n]*$)',
                f'\\1    "replaces": ["{consolidation["delete_code"]}"]\\n\\1\\2',
                updated_content
            )
        
        # Write updated base file
        with open(base_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"  ✅ Updated {consolidation['base_file']}")
        print(f"  📝 Modules: {modules_str}")
        print(f"  🗑️  Ready to delete: {consolidation['delete_file']}")
    
    print("\n" + "=" * 80)
    print("CONSOLIDATION SUMMARY")
    print("=" * 80)
    print(f"\nTotal consolidations: {len(CONSOLIDATIONS)}")
    print("\nFiles to delete:")
    for consolidation in CONSOLIDATIONS:
        delete_path = kpi_dir / consolidation['delete_file']
        if delete_path.exists():
            print(f"  - {consolidation['delete_file']}")
    
    print("\n⚠️  NOTE: Files have been updated but not deleted.")
    print("Review the changes, then run the delete commands manually.")

if __name__ == '__main__':
    main()

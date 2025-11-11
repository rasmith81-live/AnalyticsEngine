"""
Regenerate Sample Data for All KPIs

This script regenerates the sample_data field for all KPIs based on their
formulas, using the enhanced formula-aware generation logic.
"""

import sys
from pathlib import Path

# Add parent directory to path to import from validate_and_enhance_kpis
sys.path.insert(0, str(Path(__file__).parent))

from validate_and_enhance_kpis import (
    load_kpi, write_kpi_file, generate_sample_data,
    KPIS_DIR, create_backup
)

def main():
    """Main execution function."""
    print("\n🔄 Regenerating Sample Data for All KPIs")
    print("=" * 70)
    print(f"📁 KPIs Directory: {KPIS_DIR}\n")
    
    # Create backup
    print("📦 Creating backup...")
    create_backup()
    
    # Get all KPI files
    kpi_files = sorted([f for f in KPIS_DIR.glob("*.py") 
                       if f.name not in ['__init__.py', 'base_kpi.py']])
    
    print(f"\n🔄 Processing {len(kpi_files)} KPI files...\n")
    
    regenerated_count = 0
    errors = 0
    
    for file_path in kpi_files:
        print(f"Processing: {file_path.name}")
        
        # Load KPI
        kpi = load_kpi(file_path)
        if not kpi:
            errors += 1
            print(f"  ✗ Failed to load")
            continue
        
        # Regenerate sample data
        try:
            kpi['sample_data'] = generate_sample_data(kpi)
            
            # Write updated KPI
            write_kpi_file(kpi, file_path)
            regenerated_count += 1
            print(f"  ✓ Sample data regenerated")
            
        except Exception as e:
            errors += 1
            print(f"  ✗ Error: {e}")
    
    # Summary
    print(f"\n📊 Summary:")
    print(f"  Total KPIs: {len(kpi_files)}")
    print(f"  ✓ Regenerated: {regenerated_count}")
    print(f"  ✗ Errors: {errors}")
    
    print(f"\n🎉 Sample data regeneration complete!")


if __name__ == "__main__":
    main()

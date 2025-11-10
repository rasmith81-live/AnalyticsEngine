"""
Fix the comma placement in KPI metadata.
Move comma from separate line to end of preceding line.
"""

import re
from pathlib import Path

def fix_comma_issue(file_path):
    """Fix the comma placement - move it to end of preceding line."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Pattern 1: find lines ending without comma, followed by line with just comma and whitespace
    # Example: "replaces": ["FOO"]\n    ,\n        "required_objects":
    # Should be: "replaces": ["FOO"],\n        "required_objects":
    pattern1 = r'(\[[^\]]*\])(\s*\n\s*)\,(\s*\n\s*)"required_objects":'
    content = re.sub(pattern1, r'\1,\3"required_objects":', content)
    
    # Pattern 2: for cases where there's a string value before the comma
    # Example: "import_date": "2025-11-07"\n    ,\n        "required_objects":
    # Should be: "import_date": "2025-11-07",\n        "required_objects":
    pattern2 = r'("[^"]*")(\s*\n\s*)\,(\s*\n\s*)"required_objects":'
    content = re.sub(pattern2, r'\1,\3"required_objects":', content)
    
    # Pattern 3: for cases where there's a number before the comma
    # Example: "some_value": 123\n    ,\n        "required_objects":
    pattern3 = r'(\d+)(\s*\n\s*)\,(\s*\n\s*)"required_objects":'
    content = re.sub(pattern3, r'\1,\3"required_objects":', content)
    
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def main():
    kpi_dir = Path('kpis')
    kpi_files = list(kpi_dir.glob('*.py'))
    
    print("=" * 80)
    print("FIXING COMMA ISSUES IN KPI METADATA")
    print("=" * 80)
    print(f"\nTotal KPI files: {len(kpi_files)}")
    print()
    
    fixed_count = 0
    
    for file_path in sorted(kpi_files):
        try:
            if fix_comma_issue(file_path):
                fixed_count += 1
                if fixed_count <= 20:
                    print(f"✅ Fixed: {file_path.name}")
        except Exception as e:
            print(f"❌ Error in {file_path.name}: {str(e)}")
    
    if fixed_count > 20:
        print(f"... and {fixed_count - 20} more files fixed")
    
    print("\n" + "=" * 80)
    print(f"✅ Fixed: {fixed_count} files")
    print("=" * 80)

if __name__ == '__main__':
    main()

"""
Verify that all KPI metadata is properly formatted.
"""

import re
from pathlib import Path

def check_formatting(file_path):
    """Check for formatting issues in KPI file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # Check for standalone comma lines
    if re.search(r'^\s+,\s*$', content, re.MULTILINE):
        issues.append("Standalone comma line found")
    
    # Check for required_objects field
    if '"required_objects"' not in content and file_path.name not in ['__init__.py', 'registry.py']:
        issues.append("Missing required_objects field")
    
    return issues

def main():
    kpi_dir = Path('kpis')
    kpi_files = list(kpi_dir.glob('*.py'))
    
    print("=" * 80)
    print("VERIFYING KPI METADATA FORMATTING")
    print("=" * 80)
    print(f"\nTotal KPI files: {len(kpi_files)}")
    print()
    
    files_with_issues = []
    
    for file_path in sorted(kpi_files):
        issues = check_formatting(file_path)
        if issues:
            files_with_issues.append((file_path.name, issues))
    
    if files_with_issues:
        print(f"❌ Found {len(files_with_issues)} files with issues:\n")
        for filename, issues in files_with_issues[:20]:
            print(f"  {filename}:")
            for issue in issues:
                print(f"    - {issue}")
        
        if len(files_with_issues) > 20:
            print(f"\n  ... and {len(files_with_issues) - 20} more files")
    else:
        print("✅ All KPI files are properly formatted!")
        print(f"   - No standalone comma lines")
        print(f"   - All files have required_objects field")
    
    print("\n" + "=" * 80)
    print(f"Total files checked: {len(kpi_files)}")
    print(f"Files with issues: {len(files_with_issues)}")
    print(f"Clean files: {len(kpi_files) - len(files_with_issues)}")
    print("=" * 80)

if __name__ == '__main__':
    main()

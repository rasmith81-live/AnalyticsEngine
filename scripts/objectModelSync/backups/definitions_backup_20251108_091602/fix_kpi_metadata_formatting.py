"""
Fix formatting issues in KPI metadata after adding required_objects.
"""

import re
from pathlib import Path

def fix_metadata_formatting(file_path):
    """Fix metadata formatting issues."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to find metadata with formatting issues
    # Look for cases where there's a comma before required_objects
    pattern = r'(metadata_=\{[^}]*?)(\s*,\s*)(}[\s\n]*,[\s\n]*"required_objects":)'
    
    def fix_format(match):
        metadata_start = match.group(1)
        closing_and_required = match.group(3)
        
        # Remove the extra comma and closing brace, then add proper formatting
        return metadata_start + ',\n        "required_objects":'
    
    updated_content = re.sub(pattern, fix_format, content)
    
    # Also fix the pattern where required_objects is outside the metadata dict
    pattern2 = r'(metadata_=\{[^}]*?)(}[\s\n]*)(,[\s\n]*"required_objects": \[[^\]]*\][\s\n]*})'
    
    def fix_format2(match):
        metadata_content = match.group(1)
        required_objects = match.group(3)
        
        # Remove the closing brace from metadata_content if it ends with one
        metadata_content = metadata_content.rstrip()
        if metadata_content.endswith(','):
            metadata_content = metadata_content[:-1]
        
        # Extract required_objects content
        req_obj_match = re.search(r'"required_objects": (\[[^\]]*\])', required_objects)
        if req_obj_match:
            req_obj_content = req_obj_match.group(1)
            return f'{metadata_content},\n        "required_objects": {req_obj_content}\n    }}'
        
        return match.group(0)
    
    updated_content = re.sub(pattern2, fix_format2, updated_content, flags=re.DOTALL)
    
    if updated_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        return True
    
    return False

def main():
    kpi_dir = Path('kpis')
    kpi_files = list(kpi_dir.glob('*.py'))
    
    print("=" * 80)
    print("FIXING KPI METADATA FORMATTING")
    print("=" * 80)
    print(f"\nTotal KPI files: {len(kpi_files)}")
    print()
    
    fixed_count = 0
    
    for file_path in sorted(kpi_files):
        try:
            if fix_metadata_formatting(file_path):
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

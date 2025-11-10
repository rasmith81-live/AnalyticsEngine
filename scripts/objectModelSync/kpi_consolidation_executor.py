"""
KPI Consolidation Executor

Reads the approved recommendations from the markdown file and executes
the consolidations by:
1. Merging metadata (modules, aggregation_methods, etc.)
2. Merging UML schemas
3. Merging definitions where appropriate
4. Adding 'replaces' field
5. Deleting the secondary KPI file
"""

import re
import json
from pathlib import Path
from datetime import datetime
import shutil

class KPIConsolidationExecutor:
    """Executes approved KPI consolidations."""
    
    def __init__(self, config):
        self.config = config
        self.kpis_dir = Path(config['paths']['kpis_dir'])
        self.output_dir = Path(config['paths']['output_dir'])
        self.backup_dir = Path(config['paths']['backup_dir'])
        self.results = {
            'consolidated': [],
            'errors': [],
            'files_deleted': []
        }
    
    def load_approved_recommendations(self):
        """Load and parse approved recommendations from markdown."""
        md_file = self.output_dir / 'kpi_consolidation_recommendations.md'
        json_file = self.output_dir / 'kpi_consolidation_recommendations.json'
        
        if not md_file.exists() or not json_file.exists():
            raise FileNotFoundError("Recommendations files not found. Run kpi_consolidation_analyzer.py first.")
        
        # Load JSON data
        with open(json_file, 'r', encoding='utf-8') as f:
            all_recommendations = json.load(f)
        
        # Parse markdown for approvals
        with open(md_file, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Find checked boxes
        approved = []
        for rec in all_recommendations:
            # Look for checked box for this recommendation
            pattern = rf'\[x\].*{re.escape(rec["secondary_kpi"]["code"])}.*into.*{re.escape(rec["primary_kpi"]["code"])}'
            if re.search(pattern, md_content, re.IGNORECASE):
                approved.append(rec)
        
        return approved
    
    def create_backup(self):
        """Create backup before consolidation."""
        if not self.config['sync_options']['create_backups']:
            return None
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = self.backup_dir / f"consolidation_backup_{timestamp}"
        
        try:
            shutil.copytree(self.kpis_dir, backup_path)
            return backup_path
        except Exception as e:
            print(f"  Warning: Backup failed: {e}")
            return None
    
    def load_kpi_file(self, kpi_file):
        """Load KPI file content."""
        file_path = self.kpis_dir / kpi_file
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def extract_metadata_section(self, content):
        """Extract metadata section from KPI."""
        pattern = r'metadata_=\{([^}]+)\}'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            return match.group(1)
        return None
    
    def extract_field_list(self, content, field_name):
        """Extract a list field from metadata."""
        pattern = rf'"{field_name}":\s*\[([^\]]+)\]'
        match = re.search(pattern, content)
        if match:
            items_str = match.group(1)
            return [item.strip().strip('"') for item in items_str.split(',')]
        return []
    
    def merge_modules(self, primary_content, secondary_content):
        """Merge modules from both KPIs."""
        primary_modules = set(self.extract_field_list(primary_content, 'modules'))
        secondary_modules = set(self.extract_field_list(secondary_content, 'modules'))
        
        merged = sorted(list(primary_modules | secondary_modules))
        return merged
    
    def merge_aggregation_methods(self, primary_content, secondary_content):
        """Merge aggregation methods."""
        primary_agg = set(self.extract_field_list(primary_content, 'aggregation_methods'))
        secondary_agg = set(self.extract_field_list(secondary_content, 'aggregation_methods'))
        
        if not primary_agg and not secondary_agg:
            return None
        
        merged = sorted(list(primary_agg | secondary_agg))
        if not merged:
            merged = ["average", "median", "sum", "min", "max", "count"]
        
        return merged
    
    def merge_time_periods(self, primary_content, secondary_content):
        """Merge time periods."""
        primary_periods = set(self.extract_field_list(primary_content, 'time_periods'))
        secondary_periods = set(self.extract_field_list(secondary_content, 'time_periods'))
        
        if not primary_periods and not secondary_periods:
            return None
        
        merged = sorted(list(primary_periods | secondary_periods))
        if not merged:
            merged = ["daily", "weekly", "monthly", "quarterly", "annually", "custom"]
        
        return merged
    
    def add_replaces_field(self, content, secondary_code):
        """Add or update replaces field."""
        # Check if replaces already exists
        existing_replaces = self.extract_field_list(content, 'replaces')
        
        if secondary_code not in existing_replaces:
            existing_replaces.append(secondary_code)
        
        replaces_str = ', '.join([f'"{code}"' for code in sorted(existing_replaces)])
        
        # Check if replaces field exists
        if '"replaces"' in content:
            # Update existing
            pattern = r'"replaces":\s*\[[^\]]*\]'
            content = re.sub(pattern, f'"replaces": [{replaces_str}]', content)
        else:
            # Add new
            metadata_pattern = r'(metadata_=\{[^}]*?)(}[\s\n]*\))'
            
            def add_field(match):
                metadata_content = match.group(1)
                closing = match.group(2)
                
                metadata_content = metadata_content.rstrip()
                if metadata_content.endswith(','):
                    metadata_content = metadata_content[:-1]
                
                new_field = f',\n        "replaces": [{replaces_str}]'
                
                return metadata_content + new_field + closing
            
            content = re.sub(metadata_pattern, add_field, content, flags=re.DOTALL)
        
        return content
    
    def update_metadata_field(self, content, field_name, values):
        """Update or add a metadata field."""
        if values is None:
            return content
        
        values_str = ', '.join([f'"{v}"' for v in values])
        
        # Check if field exists
        if f'"{field_name}"' in content:
            # Update existing
            pattern = rf'"{field_name}":\s*\[[^\]]*\]'
            content = re.sub(pattern, f'"{field_name}": [{values_str}]', content)
        else:
            # Add new
            metadata_pattern = r'(metadata_=\{[^}]*?)(}[\s\n]*\))'
            
            def add_field(match):
                metadata_content = match.group(1)
                closing = match.group(2)
                
                metadata_content = metadata_content.rstrip()
                if metadata_content.endswith(','):
                    metadata_content = metadata_content[:-1]
                
                new_field = f',\n        "{field_name}": [{values_str}]'
                
                return metadata_content + new_field + closing
            
            content = re.sub(metadata_pattern, add_field, content, flags=re.DOTALL)
        
        return content
    
    def consolidate_kpi_pair(self, recommendation):
        """Consolidate a single KPI pair."""
        primary_file = recommendation['primary_kpi']['file']
        secondary_file = recommendation['secondary_kpi']['file']
        secondary_code = recommendation['secondary_kpi']['code']
        
        print(f"\n  Consolidating: {secondary_file} → {primary_file}")
        
        try:
            # Load both files
            primary_content = self.load_kpi_file(primary_file)
            secondary_content = self.load_kpi_file(secondary_file)
            
            # Merge metadata
            merged_modules = self.merge_modules(primary_content, secondary_content)
            merged_agg = self.merge_aggregation_methods(primary_content, secondary_content)
            merged_periods = self.merge_time_periods(primary_content, secondary_content)
            
            # Update primary KPI
            updated_content = primary_content
            updated_content = self.update_metadata_field(updated_content, 'modules', merged_modules)
            updated_content = self.update_metadata_field(updated_content, 'aggregation_methods', merged_agg)
            updated_content = self.update_metadata_field(updated_content, 'time_periods', merged_periods)
            updated_content = self.add_replaces_field(updated_content, secondary_code)
            
            # Write updated primary KPI
            if not self.config['sync_options']['dry_run']:
                primary_path = self.kpis_dir / primary_file
                with open(primary_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
            
            # Delete secondary KPI
            if not self.config['sync_options']['dry_run']:
                secondary_path = self.kpis_dir / secondary_file
                secondary_path.unlink()
                self.results['files_deleted'].append(secondary_file)
            
            self.results['consolidated'].append({
                'primary': primary_file,
                'secondary': secondary_file,
                'modules_merged': len(merged_modules),
                'secondary_code': secondary_code
            })
            
            print(f"    ✅ Merged {len(merged_modules)} modules")
            print(f"    ✅ Added to replaces: {secondary_code}")
            if not self.config['sync_options']['dry_run']:
                print(f"    ✅ Deleted: {secondary_file}")
            
            return True
        
        except Exception as e:
            error_msg = f"Error consolidating {secondary_file}: {str(e)}"
            print(f"    ❌ {error_msg}")
            self.results['errors'].append(error_msg)
            return False
    
    def execute_consolidations(self):
        """Execute all approved consolidations."""
        print("=" * 80)
        print("KPI CONSOLIDATION EXECUTOR")
        print("=" * 80)
        print()
        
        if self.config['sync_options']['dry_run']:
            print("⚠️  DRY RUN MODE - No files will be modified")
            print()
        
        print("Step 1: Loading approved recommendations...")
        try:
            approved = self.load_approved_recommendations()
            print(f"  Found {len(approved)} approved consolidations")
        except FileNotFoundError as e:
            print(f"  ❌ {e}")
            return self.results
        
        if not approved:
            print("\n  No consolidations approved. Check boxes in recommendations file.")
            return self.results
        
        print()
        print("Step 2: Creating backup...")
        backup_path = self.create_backup()
        if backup_path:
            print(f"  ✅ Backup created: {backup_path}")
        
        print()
        print("Step 3: Executing consolidations...")
        
        for rec in approved:
            self.consolidate_kpi_pair(rec)
        
        print()
        print("=" * 80)
        print("CONSOLIDATION SUMMARY")
        print("=" * 80)
        print(f"Approved: {len(approved)}")
        print(f"Consolidated: {len(self.results['consolidated'])}")
        print(f"Files deleted: {len(self.results['files_deleted'])}")
        print(f"Errors: {len(self.results['errors'])}")
        
        if self.results['errors']:
            print("\nErrors:")
            for error in self.results['errors']:
                print(f"  - {error}")
        
        if self.results['files_deleted']:
            print("\nDeleted files:")
            for file in self.results['files_deleted'][:10]:
                print(f"  - {file}")
            if len(self.results['files_deleted']) > 10:
                print(f"  ... and {len(self.results['files_deleted']) - 10} more")
        
        print("=" * 80)
        
        # Save execution report
        self.save_execution_report()
        
        return self.results
    
    def save_execution_report(self):
        """Save execution report."""
        report_file = self.output_dir / 'kpi_consolidation_execution_report.json'
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'dry_run': self.config['sync_options']['dry_run'],
            'summary': {
                'consolidated': len(self.results['consolidated']),
                'files_deleted': len(self.results['files_deleted']),
                'errors': len(self.results['errors'])
            },
            'consolidations': self.results['consolidated'],
            'files_deleted': self.results['files_deleted'],
            'errors': self.results['errors']
        }
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n📄 Execution report saved to: {report_file}")

def run_consolidation_execution(config):
    """Run KPI consolidation execution."""
    executor = KPIConsolidationExecutor(config)
    return executor.execute_consolidations()

if __name__ == '__main__':
    import json
    
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    run_consolidation_execution(config)

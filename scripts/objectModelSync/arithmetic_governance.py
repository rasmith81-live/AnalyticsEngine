"""
Arithmetic Governance Script

Reviews all KPIs and identifies those with arithmetic modifiers in their names
(average, mean, median, max, min, sum, count, total, rate, ratio, percentage).

Removes the arithmetic modifier from the name and definitions, and places it
as metadata following the design pattern of abstracting modifiers.

UPDATED: Now works with dictionary-based definitions.
"""

import re
import json
from pathlib import Path
from collections import defaultdict
from definition_loader import load_all_kpis, load_definition_file, update_definition_field, add_definition_field

# Arithmetic modifiers to detect and abstract
# Note: rate, ratio, and percentage are EXCLUDED as they represent comparative calculations
ARITHMETIC_MODIFIERS = {
    'average': {'type': 'aggregation', 'method': 'average'},
    'avg': {'type': 'aggregation', 'method': 'average'},
    'mean': {'type': 'aggregation', 'method': 'mean'},
    'median': {'type': 'aggregation', 'method': 'median'},
    'max': {'type': 'aggregation', 'method': 'max'},
    'maximum': {'type': 'aggregation', 'method': 'max'},
    'min': {'type': 'aggregation', 'method': 'min'},
    'minimum': {'type': 'aggregation', 'method': 'min'},
    'sum': {'type': 'aggregation', 'method': 'sum'},
    'total': {'type': 'aggregation', 'method': 'sum'},
    'count': {'type': 'aggregation', 'method': 'count'},
}

# Standard metadata to add
STANDARD_AGGREGATION_METHODS = ["average", "median", "sum", "min", "max", "count"]
STANDARD_TIME_PERIODS = ["daily", "weekly", "monthly", "quarterly", "annually", "custom"]

class ArithmeticGovernance:
    """Manages arithmetic modifier governance for KPIs."""
    
    def __init__(self, config):
        self.config = config
        self.kpis_dir = Path(config['paths']['kpis_dir'])
        self.results = {
            'analyzed': 0,
            'with_modifiers': [],
            'updated': 0,
            'errors': [],
            'dry_run': config['sync_options']['dry_run']
        }
    
    def detect_arithmetic_modifier(self, text):
        """Detect arithmetic modifiers in text."""
        text_lower = text.lower()
        detected = []
        
        for modifier, info in ARITHMETIC_MODIFIERS.items():
            # Check for modifier as whole word
            pattern = r'\b' + re.escape(modifier) + r'\b'
            if re.search(pattern, text_lower):
                detected.append({
                    'modifier': modifier,
                    'type': info['type'],
                    'method': info['method']
                })
        
        return detected
    
    def extract_kpi_data(self, kpi_file):
        """Extract KPI data from file."""
        with open(kpi_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        data = {'content': content}
        
        # Extract key fields
        fields = ['code', 'name', 'description', 'kpi_definition', 'formula', 
                  'calculation_formula', 'category']
        
        for field in fields:
            # Try simple string match
            pattern = rf'{field}="([^"]+)"'
            match = re.search(pattern, content)
            if match:
                data[field] = match.group(1)
            else:
                # Try triple-quoted string
                pattern = rf'{field}="""(.*?)"""'
                match = re.search(pattern, content, re.DOTALL)
                if match:
                    data[field] = match.group(1)
        
        # Extract existing metadata
        metadata_match = re.search(r'metadata_=\{([^}]+)\}', content, re.DOTALL)
        if metadata_match:
            data['has_metadata'] = True
            
            # Check for existing aggregation_methods
            agg_match = re.search(r'"aggregation_methods":\s*\[([^\]]+)\]', content)
            data['has_aggregation_methods'] = bool(agg_match)
            
            # Check for existing time_periods
            time_match = re.search(r'"time_periods":\s*\[([^\]]+)\]', content)
            data['has_time_periods'] = bool(time_match)
        else:
            data['has_metadata'] = False
            data['has_aggregation_methods'] = False
            data['has_time_periods'] = False
        
        return data
    
    def remove_modifier_from_text(self, text, modifier):
        """Remove arithmetic modifier from text."""
        if not text:
            return text
        
        # Patterns to try
        patterns = [
            # "Average Deal Size" -> "Deal Size"
            (r'\b' + re.escape(modifier) + r'\s+', ''),
            # "Deal Size Average" -> "Deal Size"
            (r'\s+' + re.escape(modifier) + r'\b', ''),
            # "Deal_Size_Average" -> "Deal_Size"
            (r'_' + re.escape(modifier) + r'\b', ''),
        ]
        
        result = text
        for pattern, replacement in patterns:
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)
        
        # Clean up extra spaces
        result = re.sub(r'\s+', ' ', result).strip()
        
        return result
    
    def generate_base_name(self, original_name, modifiers):
        """Generate base name by removing all modifiers."""
        base_name = original_name
        
        for mod_info in modifiers:
            base_name = self.remove_modifier_from_text(base_name, mod_info['modifier'])
        
        return base_name
    
    def generate_base_code(self, original_code, modifiers):
        """Generate base code by removing all modifiers."""
        base_code = original_code
        
        for mod_info in modifiers:
            modifier_upper = mod_info['modifier'].upper()
            # Remove modifier from code
            base_code = re.sub(r'_?' + re.escape(modifier_upper) + r'_?', '_', base_code, flags=re.IGNORECASE)
        
        # Clean up underscores
        base_code = re.sub(r'_+', '_', base_code)
        base_code = base_code.strip('_')
        
        return base_code
    
    def update_kpi_content(self, kpi_data, modifiers):
        """Update KPI content to abstract arithmetic modifiers."""
        content = kpi_data['content']
        original_name = kpi_data.get('name', '')
        original_code = kpi_data.get('code', '')
        
        # Generate base name and code
        base_name = self.generate_base_name(original_name, modifiers)
        base_code = self.generate_base_code(original_code, modifiers)
        
        # Update name
        if original_name and base_name != original_name:
            content = content.replace(f'name="{original_name}"', f'name="{base_name}"')
        
        # Update code
        if original_code and base_code != original_code:
            content = content.replace(f'code="{original_code}"', f'code="{base_code}"')
            # Also update the KPI variable name
            content = content.replace(f'{original_code} = KPI(', f'{base_code} = KPI(')
        
        # Update description and definition to remove modifiers
        for field in ['description', 'kpi_definition']:
            if field in kpi_data:
                original_text = kpi_data[field]
                updated_text = original_text
                
                for mod_info in modifiers:
                    # Make description more generic
                    updated_text = self.remove_modifier_from_text(updated_text, mod_info['modifier'])
                
                # Add note about aggregation flexibility
                if updated_text != original_text:
                    if 'can be aggregated' not in updated_text.lower():
                        updated_text += " This metric can be aggregated using various methods (average, median, sum, min, max, count) and filtered by time period."
                    
                    # Replace in content
                    content = content.replace(f'{field}="{original_text}"', f'{field}="{updated_text}"')
        
        # Add or update metadata
        if not kpi_data['has_aggregation_methods']:
            # Add aggregation_methods
            metadata_pattern = r'(metadata_=\{[^}]*?)(}[\s\n]*\))'
            
            def add_aggregation(match):
                metadata_content = match.group(1)
                closing = match.group(2)
                
                metadata_content = metadata_content.rstrip()
                if metadata_content.endswith(','):
                    metadata_content = metadata_content[:-1]
                
                agg_str = ', '.join([f'"{m}"' for m in STANDARD_AGGREGATION_METHODS])
                new_field = f',\n        "aggregation_methods": [{agg_str}]'
                
                return metadata_content + new_field + closing
            
            content = re.sub(metadata_pattern, add_aggregation, content, flags=re.DOTALL)
        
        if not kpi_data['has_time_periods']:
            # Add time_periods
            metadata_pattern = r'(metadata_=\{[^}]*?)(}[\s\n]*\))'
            
            def add_time_periods(match):
                metadata_content = match.group(1)
                closing = match.group(2)
                
                metadata_content = metadata_content.rstrip()
                if metadata_content.endswith(','):
                    metadata_content = metadata_content[:-1]
                
                time_str = ', '.join([f'"{t}"' for t in STANDARD_TIME_PERIODS])
                new_field = f',\n        "time_periods": [{time_str}]'
                
                return metadata_content + new_field + closing
            
            content = re.sub(metadata_pattern, add_time_periods, content, flags=re.DOTALL)
        
        return content, base_name, base_code
    
    def analyze_kpi(self, kpi_file):
        """Analyze a single KPI for arithmetic modifiers."""
        try:
            kpi_data = self.extract_kpi_data(kpi_file)
            
            # Check name for modifiers
            name = kpi_data.get('name', '')
            code = kpi_data.get('code', '')
            
            if not name:
                return None
            
            modifiers = self.detect_arithmetic_modifier(name)
            
            if modifiers:
                return {
                    'file': kpi_file.name,
                    'original_name': name,
                    'original_code': code,
                    'modifiers': modifiers,
                    'kpi_data': kpi_data
                }
            
            return None
        
        except Exception as e:
            self.results['errors'].append({
                'file': kpi_file.name,
                'error': str(e)
            })
            return None
    
    def update_kpi_file(self, kpi_file, kpi_info):
        """Update a KPI file to abstract arithmetic modifiers."""
        try:
            updated_content, base_name, base_code = self.update_kpi_content(
                kpi_info['kpi_data'],
                kpi_info['modifiers']
            )
            
            if not self.config['sync_options']['dry_run']:
                with open(kpi_file, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
            
            return {
                'file': kpi_file.name,
                'original_name': kpi_info['original_name'],
                'base_name': base_name,
                'original_code': kpi_info['original_code'],
                'base_code': base_code,
                'modifiers_removed': [m['modifier'] for m in kpi_info['modifiers']]
            }
        
        except Exception as e:
            self.results['errors'].append({
                'file': kpi_file.name,
                'error': str(e)
            })
            return None
    
    def run_governance(self):
        """Run arithmetic governance on all KPIs."""
        print("=" * 80)
        print("ARITHMETIC GOVERNANCE - KPI MODIFIER ABSTRACTION")
        print("=" * 80)
        print()
        
        if self.config['sync_options']['dry_run']:
            print("⚠️  DRY RUN MODE - No files will be modified")
            print()
        
        print("Step 1: Analyzing all KPIs for arithmetic modifiers...")
        
        kpi_files = list(self.kpis_dir.glob('*.py'))
        
        for kpi_file in kpi_files:
            if kpi_file.name in ['__init__.py', 'registry.py']:
                continue
            
            self.results['analyzed'] += 1
            
            kpi_info = self.analyze_kpi(kpi_file)
            
            if kpi_info:
                self.results['with_modifiers'].append(kpi_info)
        
        print(f"  Analyzed: {self.results['analyzed']} KPIs")
        print(f"  Found with modifiers: {len(self.results['with_modifiers'])}")
        print()
        
        if not self.results['with_modifiers']:
            print("✅ No KPIs with arithmetic modifiers found!")
            return self.results
        
        print("Step 2: Updating KPIs to abstract modifiers...")
        print()
        
        updated_kpis = []
        
        for kpi_info in self.results['with_modifiers']:
            kpi_file = self.kpis_dir / kpi_info['file']
            
            result = self.update_kpi_file(kpi_file, kpi_info)
            
            if result:
                updated_kpis.append(result)
                self.results['updated'] += 1
                
                if self.results['updated'] <= 20:
                    print(f"✅ {result['file']}")
                    print(f"   {result['original_name']} → {result['base_name']}")
                    print(f"   Modifiers: {', '.join(result['modifiers_removed'])}")
                    print()
        
        if self.results['updated'] > 20:
            print(f"... and {self.results['updated'] - 20} more KPIs updated")
        
        print()
        print("=" * 80)
        print("GOVERNANCE SUMMARY")
        print("=" * 80)
        print(f"Total KPIs analyzed: {self.results['analyzed']}")
        print(f"KPIs with modifiers: {len(self.results['with_modifiers'])}")
        print(f"KPIs updated: {self.results['updated']}")
        print(f"Errors: {len(self.results['errors'])}")
        
        if self.results['errors']:
            print("\nErrors encountered:")
            for error in self.results['errors']:
                print(f"  - {error['file']}: {error['error']}")
        
        print("=" * 80)
        
        # Save detailed report
        self.save_report(updated_kpis)
        
        return self.results
    
    def save_report(self, updated_kpis):
        """Save governance report."""
        output_dir = Path(self.config['paths']['output_dir'])
        output_dir.mkdir(parents=True, exist_ok=True)
        
        report_file = output_dir / 'arithmetic_governance_report.json'
        
        report = {
            'summary': {
                'analyzed': self.results['analyzed'],
                'with_modifiers': len(self.results['with_modifiers']),
                'updated': self.results['updated'],
                'errors': len(self.results['errors']),
                'dry_run': self.results['dry_run']
            },
            'kpis_with_modifiers': [
                {
                    'file': kpi['file'],
                    'original_name': kpi['original_name'],
                    'modifiers': [m['modifier'] for m in kpi['modifiers']]
                }
                for kpi in self.results['with_modifiers']
            ],
            'updated_kpis': updated_kpis,
            'errors': self.results['errors']
        }
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n📄 Detailed report saved to: {report_file}")
        
        # Also create markdown report
        self.save_markdown_report(updated_kpis, output_dir)
    
    def save_markdown_report(self, updated_kpis, output_dir):
        """Save markdown report."""
        report_file = output_dir / 'arithmetic_governance_report.md'
        
        lines = []
        lines.append("# Arithmetic Governance Report")
        lines.append(f"\n**Date**: {Path().cwd()}")
        lines.append(f"**Mode**: {'DRY RUN' if self.results['dry_run'] else 'LIVE UPDATE'}")
        lines.append("\n---\n")
        
        lines.append("## Summary")
        lines.append(f"\n- **Total KPIs Analyzed**: {self.results['analyzed']}")
        lines.append(f"- **KPIs with Modifiers**: {len(self.results['with_modifiers'])}")
        lines.append(f"- **KPIs Updated**: {self.results['updated']}")
        lines.append(f"- **Errors**: {len(self.results['errors'])}")
        
        if updated_kpis:
            lines.append("\n## Updated KPIs\n")
            
            for kpi in updated_kpis:
                lines.append(f"### {kpi['file']}")
                lines.append(f"- **Original Name**: {kpi['original_name']}")
                lines.append(f"- **Base Name**: {kpi['base_name']}")
                lines.append(f"- **Original Code**: {kpi['original_code']}")
                lines.append(f"- **Base Code**: {kpi['base_code']}")
                lines.append(f"- **Modifiers Removed**: {', '.join(kpi['modifiers_removed'])}")
                lines.append("")
        
        if self.results['errors']:
            lines.append("\n## Errors\n")
            for error in self.results['errors']:
                lines.append(f"- **{error['file']}**: {error['error']}")
        
        lines.append("\n---\n")
        lines.append(f"\n**Status**: {'✅ Complete' if not self.results['errors'] else '⚠️ Completed with errors'}")
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        print(f"📄 Markdown report saved to: {report_file}")

def run_arithmetic_governance(config):
    """Run arithmetic governance."""
    governance = ArithmeticGovernance(config)
    return governance.run_governance()

if __name__ == '__main__':
    import json
    
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    run_arithmetic_governance(config)

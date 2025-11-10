"""
KPI Consolidation Analyzer

Analyzes all KPIs to identify overlapping metrics that should be considered
for consolidation. Generates a recommendations markdown file with checkboxes
for user approval.

UPDATED: Now works with dictionary-based definitions.
"""

import re
import json
import shutil
from pathlib import Path
from collections import defaultdict
from difflib import SequenceMatcher
from datetime import datetime
from definition_loader import load_all_kpis

class KPIConsolidationAnalyzer:
    """Analyzes KPIs for consolidation opportunities."""
    
    def __init__(self, config):
        self.config = config
        self.kpis_dir = Path(config['paths']['kpis_dir'])
        self.output_dir = Path(config['paths']['output_dir'])
        self.kpis = {}
        self.recommendations = []
        
    def archive_old_reports(self):
        """Archive existing consolidation reports before creating new ones."""
        # Create archive directory
        archive_dir = self.output_dir / "archive"
        archive_dir.mkdir(exist_ok=True)
        
        # Generate timestamp for archive
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Files to archive
        files_to_archive = [
            self.output_dir / "kpi_consolidation_recommendations.md",
            self.output_dir / "kpi_consolidation_execution_report.json"
        ]
        
        archived_count = 0
        for file_path in files_to_archive:
            if file_path.exists():
                # Create archived filename with timestamp
                archive_name = f"{file_path.stem}_{timestamp}{file_path.suffix}"
                archive_path = archive_dir / archive_name
                
                # Move file to archive
                shutil.move(str(file_path), str(archive_path))
                print(f"📦 Archived: {file_path.name} → archive/{archive_name}")
                archived_count += 1
        
        if archived_count > 0:
            print(f"✓ Archived {archived_count} old report(s)\n")
        
        return archived_count
        
    def extract_kpi_data(self, kpi_file):
        """Extract comprehensive KPI data."""
        with open(kpi_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        data = {
            'file': kpi_file.name,
            'file_path': str(kpi_file),
            'content': content
        }
        
        # Extract key fields
        fields = ['code', 'name', 'description', 'kpi_definition', 'formula', 
                  'calculation_formula', 'category', 'measurement_approach']
        
        for field in fields:
            pattern = rf'{field}="([^"]+)"'
            match = re.search(pattern, content)
            if match:
                data[field] = match.group(1)
            else:
                pattern = rf'{field}="""(.*?)"""'
                match = re.search(pattern, content, re.DOTALL)
                if match:
                    data[field] = match.group(1)
                else:
                    data[field] = ""
        
        # Extract modules
        modules_match = re.search(r'"modules":\s*\[([^\]]+)\]', content)
        if modules_match:
            modules_str = modules_match.group(1)
            data['modules'] = [m.strip().strip('"') for m in modules_str.split(',')]
        else:
            data['modules'] = []
        
        # Extract aggregation_methods if present
        agg_match = re.search(r'"aggregation_methods":\s*\[([^\]]+)\]', content)
        if agg_match:
            agg_str = agg_match.group(1)
            data['aggregation_methods'] = [a.strip().strip('"') for a in agg_str.split(',')]
        else:
            data['aggregation_methods'] = []
        
        # Extract replaces if present
        replaces_match = re.search(r'"replaces":\s*\[([^\]]+)\]', content)
        if replaces_match:
            replaces_str = replaces_match.group(1)
            data['replaces'] = [r.strip().strip('"') for r in replaces_str.split(',')]
        else:
            data['replaces'] = []
        
        return data
    
    def calculate_similarity(self, text1, text2):
        """Calculate similarity between two texts."""
        if not text1 or not text2:
            return 0.0
        return SequenceMatcher(None, text1.lower(), text2.lower()).ratio()
    
    def normalize_name(self, name):
        """Normalize KPI name for comparison."""
        # Remove common variations
        normalized = name.lower()
        normalized = re.sub(r'\s+', ' ', normalized)
        normalized = normalized.strip()
        return normalized
    
    def find_similar_kpis(self, kpi_data, all_kpis):
        """Find KPIs similar to the given KPI."""
        similar = []
        kpi_name = kpi_data.get('name', '')
        kpi_desc = kpi_data.get('description', '')
        kpi_def = kpi_data.get('kpi_definition', '')
        kpi_code = kpi_data.get('code', '')
        
        for other_code, other_data in all_kpis.items():
            if other_code == kpi_code:
                continue
            
            # Skip if already marked as replaced
            if kpi_code in other_data.get('replaces', []):
                continue
            if other_code in kpi_data.get('replaces', []):
                continue
            
            other_name = other_data.get('name', '')
            other_desc = other_data.get('description', '')
            other_def = other_data.get('kpi_definition', '')
            
            # Calculate similarities
            name_sim = self.calculate_similarity(kpi_name, other_name)
            desc_sim = self.calculate_similarity(kpi_desc, other_desc)
            def_sim = self.calculate_similarity(kpi_def, other_def)
            
            # Weighted average
            overall_sim = (name_sim * 0.4 + desc_sim * 0.3 + def_sim * 0.3)
            
            # High similarity threshold
            if overall_sim > 0.7:
                similar.append({
                    'code': other_code,
                    'data': other_data,
                    'name_similarity': name_sim,
                    'desc_similarity': desc_sim,
                    'def_similarity': def_sim,
                    'overall_similarity': overall_sim
                })
        
        # Sort by similarity
        similar.sort(key=lambda x: x['overall_similarity'], reverse=True)
        
        return similar
    
    def detect_consolidation_patterns(self, kpi1, kpi2):
        """Detect specific consolidation patterns."""
        patterns = []
        
        name1 = kpi1.get('name', '').lower()
        name2 = kpi2.get('name', '').lower()
        
        # Pattern 1: Rate/Ratio variants
        if ('rate' in name1 and 'ratio' in name2) or ('ratio' in name1 and 'rate' in name2):
            base1 = name1.replace('rate', '').replace('ratio', '').strip()
            base2 = name2.replace('rate', '').replace('ratio', '').strip()
            if self.calculate_similarity(base1, base2) > 0.8:
                patterns.append('rate_ratio_variant')
        
        # Pattern 2: Percentage variants
        if ('percentage' in name1 or 'percent' in name1) and ('percentage' in name2 or 'percent' in name2):
            patterns.append('percentage_variant')
        
        # Pattern 3: Same modules
        modules1 = set(kpi1.get('modules', []))
        modules2 = set(kpi2.get('modules', []))
        if modules1 and modules2:
            overlap = len(modules1 & modules2) / len(modules1 | modules2)
            if overlap > 0.5:
                patterns.append('shared_modules')
        
        # Pattern 4: Same category
        if kpi1.get('category') == kpi2.get('category') and kpi1.get('category'):
            patterns.append('same_category')
        
        # Pattern 5: Similar formulas
        formula1 = kpi1.get('formula', '')
        formula2 = kpi2.get('formula', '')
        if formula1 and formula2:
            formula_sim = self.calculate_similarity(formula1, formula2)
            if formula_sim > 0.7:
                patterns.append('similar_formula')
        
        return patterns
    
    def generate_recommendation(self, kpi_data, similar_kpis):
        """Generate consolidation recommendation."""
        if not similar_kpis:
            return None
        
        # Take top similar KPI
        top_similar = similar_kpis[0]
        
        # Detect patterns
        patterns = self.detect_consolidation_patterns(kpi_data, top_similar['data'])
        
        # Determine primary KPI (keep the one with more modules or better name)
        kpi1_modules = len(kpi_data.get('modules', []))
        kpi2_modules = len(top_similar['data'].get('modules', []))
        
        if kpi1_modules >= kpi2_modules:
            primary = kpi_data
            secondary = top_similar['data']
        else:
            primary = top_similar['data']
            secondary = kpi_data
        
        recommendation = {
            'primary_kpi': {
                'code': primary.get('code'),
                'name': primary.get('name'),
                'file': primary.get('file'),
                'modules': primary.get('modules', []),
                'description': primary.get('description', '')[:200] + '...'
            },
            'secondary_kpi': {
                'code': secondary.get('code'),
                'name': secondary.get('name'),
                'file': secondary.get('file'),
                'modules': secondary.get('modules', []),
                'description': secondary.get('description', '')[:200] + '...'
            },
            'similarity_score': top_similar['overall_similarity'],
            'patterns': patterns,
            'rationale': self.generate_rationale(primary, secondary, patterns, top_similar),
            'approved': False
        }
        
        return recommendation
    
    def generate_rationale(self, primary, secondary, patterns, similarity_info):
        """Generate human-readable rationale for consolidation."""
        rationale = []
        
        rationale.append(f"Similarity score: {similarity_info['overall_similarity']:.1%}")
        
        if 'rate_ratio_variant' in patterns:
            rationale.append("Both are rate/ratio variants of the same metric")
        
        if 'percentage_variant' in patterns:
            rationale.append("Both are percentage-based metrics")
        
        if 'shared_modules' in patterns:
            shared = set(primary.get('modules', [])) & set(secondary.get('modules', []))
            rationale.append(f"Share {len(shared)} modules: {', '.join(list(shared)[:3])}")
        
        if 'same_category' in patterns:
            rationale.append(f"Same category: {primary.get('category')}")
        
        if 'similar_formula' in patterns:
            rationale.append("Similar calculation formulas")
        
        return " | ".join(rationale)
    
    def analyze_all_kpis(self):
        """Analyze all KPIs for consolidation opportunities."""
        print("=" * 80)
        print("KPI CONSOLIDATION ANALYZER")
        print("=" * 80)
        print()
        
        print("Step 1: Loading all KPIs...")
        kpi_files = list(self.kpis_dir.glob('*.py'))
        
        for kpi_file in kpi_files:
            if kpi_file.name in ['__init__.py', 'registry.py']:
                continue
            
            try:
                kpi_data = self.extract_kpi_data(kpi_file)
                code = kpi_data.get('code')
                if code:
                    self.kpis[code] = kpi_data
            except Exception as e:
                print(f"  Error loading {kpi_file.name}: {e}")
        
        print(f"  Loaded {len(self.kpis)} KPIs")
        print()
        
        print("Step 2: Analyzing for consolidation opportunities...")
        processed = set()
        
        for kpi_code, kpi_data in self.kpis.items():
            if kpi_code in processed:
                continue
            
            similar_kpis = self.find_similar_kpis(kpi_data, self.kpis)
            
            if similar_kpis:
                recommendation = self.generate_recommendation(kpi_data, similar_kpis)
                
                if recommendation:
                    # Mark both as processed
                    processed.add(recommendation['primary_kpi']['code'])
                    processed.add(recommendation['secondary_kpi']['code'])
                    
                    self.recommendations.append(recommendation)
        
        print(f"  Found {len(self.recommendations)} consolidation opportunities")
        print()
        
        # Sort by similarity score
        self.recommendations.sort(key=lambda x: x['similarity_score'], reverse=True)
        
        return self.recommendations
    
    def generate_markdown_report(self):
        """Generate markdown report with checkboxes."""
        print("Step 3: Generating recommendations report...")
        
        lines = []
        lines.append("# KPI Consolidation Recommendations")
        lines.append(f"\n**Generated**: {Path().cwd()}")
        lines.append(f"**Total Recommendations**: {len(self.recommendations)}")
        lines.append("\n---\n")
        
        lines.append("## Instructions")
        lines.append("\n1. Review each recommendation below")
        lines.append("2. Check the box `[ ]` → `[x]` for recommendations you approve")
        lines.append("3. Save this file")
        lines.append("4. Run `python kpi_consolidation_executor.py` to execute approved consolidations")
        lines.append("\n---\n")
        
        lines.append("## Summary")
        lines.append(f"\n- **Total Opportunities**: {len(self.recommendations)}")
        lines.append(f"- **High Confidence** (>90% similarity): {sum(1 for r in self.recommendations if r['similarity_score'] > 0.9)}")
        lines.append(f"- **Medium Confidence** (70-90% similarity): {sum(1 for r in self.recommendations if 0.7 <= r['similarity_score'] <= 0.9)}")
        lines.append("\n---\n")
        
        for i, rec in enumerate(self.recommendations, 1):
            lines.append(f"## Recommendation #{i}")
            lines.append(f"\n**Similarity**: {rec['similarity_score']:.1%}")
            lines.append(f"**Patterns**: {', '.join(rec['patterns']) if rec['patterns'] else 'General similarity'}")
            lines.append(f"**Rationale**: {rec['rationale']}")
            lines.append("")
            
            lines.append("### Primary KPI (Keep)")
            lines.append(f"- **Name**: {rec['primary_kpi']['name']}")
            lines.append(f"- **Code**: `{rec['primary_kpi']['code']}`")
            lines.append(f"- **File**: `{rec['primary_kpi']['file']}`")
            lines.append(f"- **Modules**: {', '.join(rec['primary_kpi']['modules']) if rec['primary_kpi']['modules'] else 'None'}")
            lines.append(f"- **Description**: {rec['primary_kpi']['description']}")
            lines.append("")
            
            lines.append("### Secondary KPI (Consolidate)")
            lines.append(f"- **Name**: {rec['secondary_kpi']['name']}")
            lines.append(f"- **Code**: `{rec['secondary_kpi']['code']}`")
            lines.append(f"- **File**: `{rec['secondary_kpi']['file']}`")
            lines.append(f"- **Modules**: {', '.join(rec['secondary_kpi']['modules']) if rec['secondary_kpi']['modules'] else 'None'}")
            lines.append(f"- **Description**: {rec['secondary_kpi']['description']}")
            lines.append("")
            
            lines.append("### Action")
            lines.append(f"- [ ] **Approve consolidation** of `{rec['secondary_kpi']['code']}` into `{rec['primary_kpi']['code']}`")
            lines.append("")
            lines.append("---\n")
        
        # Save report
        self.output_dir.mkdir(parents=True, exist_ok=True)
        report_file = self.output_dir / 'kpi_consolidation_recommendations.md'
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        print(f"  Report saved to: {report_file}")
        
        # Also save JSON for executor
        json_file = self.output_dir / 'kpi_consolidation_recommendations.json'
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(self.recommendations, f, indent=2)
        
        print(f"  Data saved to: {json_file}")
        
        return report_file
    
    def run(self):
        """Run the complete analysis."""
        # Archive old reports first
        print("=" * 80)
        print("ARCHIVING OLD REPORTS")
        print("=" * 80)
        self.archive_old_reports()
        
        # Run analysis
        self.analyze_all_kpis()
        report_file = self.generate_markdown_report()
        
        print()
        print("=" * 80)
        print("ANALYSIS COMPLETE")
        print("=" * 80)
        print(f"Found {len(self.recommendations)} consolidation opportunities")
        print(f"\nNext steps:")
        print(f"1. Review: {report_file}")
        print(f"2. Approve: Check boxes for recommendations you approve")
        print(f"3. Execute: Run `python kpi_consolidation_executor.py`")
        print("=" * 80)
        
        return self.recommendations

def run_consolidation_analysis(config):
    """Run KPI consolidation analysis."""
    analyzer = KPIConsolidationAnalyzer(config)
    return analyzer.run()

if __name__ == '__main__':
    import json
    
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    run_consolidation_analysis(config)

"""
Analyze KPI files to identify potential duplicates that should be consolidated.
"""

import re
from pathlib import Path
from collections import defaultdict

def extract_kpi_info(file_path):
    """Extract basic info from KPI file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract KPI code
    code_match = re.search(r'code="([^"]+)"', content)
    code = code_match.group(1) if code_match else None
    
    # Extract description
    desc_match = re.search(r'description="([^"]+)"', content)
    description = desc_match.group(1) if desc_match else None
    
    # Extract formula
    formula_match = re.search(r'formula="([^"]+)"', content)
    formula = formula_match.group(1) if formula_match else None
    
    # Extract modules
    modules_match = re.search(r'"modules":\s*\[([^\]]+)\]', content)
    modules = modules_match.group(1) if modules_match else None
    
    return {
        'file': file_path.name,
        'code': code,
        'description': description,
        'formula': formula,
        'modules': modules
    }

def normalize_name(name):
    """Remove common modifiers to get base concept."""
    # Remove file extension
    base = name.replace('.py', '')
    
    # Remove common modifiers
    modifiers = [
        'average_', '_average',
        'total_', '_total',
        'mean_', '_mean',
        'sum_', '_sum',
        'median_', '_median',
        'monthly_', '_monthly',
        'quarterly_', '_quarterly',
        'annual_', '_annual', 'annually_', '_annually',
        'yearly_', '_yearly',
        'daily_', '_daily',
        'weekly_', '_weekly',
        '_per_', '_rate', '_ratio', '_percentage'
    ]
    
    normalized = base
    for modifier in modifiers:
        normalized = normalized.replace(modifier, '_')
    
    # Clean up multiple underscores
    normalized = re.sub(r'_+', '_', normalized)
    normalized = normalized.strip('_')
    
    return normalized

def find_duplicate_groups():
    """Find groups of KPIs that might be duplicates."""
    kpi_dir = Path('kpis')
    kpi_files = list(kpi_dir.glob('*.py'))
    
    # Group by normalized name
    groups = defaultdict(list)
    for file in kpi_files:
        normalized = normalize_name(file.name)
        groups[normalized].append(file)
    
    # Filter to only groups with multiple files
    duplicate_groups = {k: v for k, v in groups.items() if len(v) > 1}
    
    return duplicate_groups

def analyze_specific_patterns():
    """Analyze specific known patterns."""
    kpi_dir = Path('kpis')
    
    patterns = {
        'Deal Size': [
            'deal_size.py',
            'average_deal_size.py',
            'deal_size_average.py'  # Already deleted
        ],
        'Sales Cycle': [
            'sales_cycle_length.py',
            'sales_cycle_time.py'
        ],
        'Revenue Per Account': [
            'average_revenue_per_account_arpa.py',
            'average_revenue_per_user_arpu.py',
            'average_revenue_per_unit_arpu.py'
        ],
        'Order/Purchase Value': [
            'average_order_value_aov.py',
            'average_purchase_value.py'
        ],
        'Profit Margin': [
            'profit_margin_per_sale.py',
            'average_profit_margin_per_sale.py'
        ],
        'Lead Response Time': [
            'lead_response_time.py',
            'average_lead_response_time.py'
        ],
        'Issue Resolution Time': [
            'average_issue_resolution_time.py',
            'partner_support_ticket_resolution_time.py',
            'sales_support_ticket_resolution_time.py'
        ]
    }
    
    results = {}
    for concept, files in patterns.items():
        existing = []
        for file_name in files:
            file_path = kpi_dir / file_name
            if file_path.exists():
                info = extract_kpi_info(file_path)
                existing.append(info)
        
        if len(existing) > 1:
            results[concept] = existing
    
    return results

def main():
    print("=" * 80)
    print("KPI DUPLICATE ANALYSIS")
    print("=" * 80)
    print()
    
    # Find duplicate groups by normalized name
    print("1. GROUPS WITH SIMILAR BASE NAMES")
    print("-" * 80)
    duplicate_groups = find_duplicate_groups()
    
    if duplicate_groups:
        for base_name, files in sorted(duplicate_groups.items()):
            print(f"\n**{base_name.upper().replace('_', ' ')}**")
            for file in sorted(files, key=lambda x: x.name):
                info = extract_kpi_info(file)
                print(f"  - {file.name}")
                print(f"    Code: {info['code']}")
                if info['modules']:
                    print(f"    Modules: {info['modules']}")
    else:
        print("No duplicate groups found by name normalization.")
    
    print("\n\n")
    print("2. SPECIFIC KNOWN DUPLICATE PATTERNS")
    print("-" * 80)
    
    specific_duplicates = analyze_specific_patterns()
    
    for concept, kpis in specific_duplicates.items():
        print(f"\n**{concept}**")
        for kpi in kpis:
            print(f"  - {kpi['file']}")
            print(f"    Code: {kpi['code']}")
            print(f"    Description: {kpi['description'][:80]}...")
            if kpi['modules']:
                print(f"    Modules: {kpi['modules']}")
            print()
    
    print("\n\n")
    print("3. ALL KPIs WITH 'AVERAGE' PREFIX")
    print("-" * 80)
    
    kpi_dir = Path('kpis')
    average_kpis = sorted([f.stem for f in kpi_dir.glob('average_*.py')])
    
    for i, kpi in enumerate(average_kpis, 1):
        print(f"{i:2}. {kpi}")
    
    print(f"\nTotal: {len(average_kpis)} KPIs with 'average' prefix")
    
    print("\n\n")
    print("=" * 80)
    print("CONSOLIDATION RECOMMENDATIONS")
    print("=" * 80)
    print()
    print("HIGH PRIORITY (Clear Duplicates):")
    print("  1. ✅ Deal Size + Deal Size Average → Deal Size (COMPLETED)")
    print("  2. Sales Cycle Length + Sales Cycle Time → Sales Cycle Duration")
    print("  3. Average Deal Size (Channel) → Deal Size (add CHANNEL_SALES module)")
    print("  4. Profit Margin Per Sale + Average Profit Margin Per Sale → Profit Margin Per Sale")
    print()
    print("MEDIUM PRIORITY (Similar Concepts):")
    print("  5. Average Order Value + Average Purchase Value → Transaction Value")
    print("  6. Lead Response Time + Average Lead Response Time → Lead Response Time")
    print()
    print("LOW PRIORITY (Different Contexts):")
    print("  7. Revenue Per Account/User/Unit - Keep separate (different denominators)")
    print("  8. Resolution Time variants - Keep separate (different contexts)")
    print()

if __name__ == '__main__':
    main()

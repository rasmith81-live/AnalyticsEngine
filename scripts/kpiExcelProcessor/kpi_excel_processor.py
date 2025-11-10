"""
KPI Excel/CSV Processor
Generates KPI Python files from Excel/CSV templates with proper abstraction of arithmetic modifiers and time periods.

UPDATED: Now generates dictionary-based definitions for analytics_metadata_service.
"""

import pandas as pd
import os
import sys
import re
from pathlib import Path
from typing import List, Dict, Set
import argparse


class KPIExcelProcessor:
    """Process Excel/CSV files and generate KPI Python files."""
    
    def __init__(self, excel_path: str, module_name: str, value_chain: str, output_dir: str = None):
        self.excel_path = excel_path
        self.module_name = module_name.upper()
        self.value_chain = value_chain.upper()
        
        # Default output directory - Updated to analytics_metadata_service
        if output_dir is None:
            base_path = Path(__file__).parent.parent.parent / "services" / "business_services" / "analytics_metadata_service" / "definitions"
            self.output_dir = base_path / "kpis"
            self.modules_dir = base_path / "modules"
            self.value_chains_dir = base_path / "value_chains"
        else:
            self.output_dir = Path(output_dir)
            self.modules_dir = Path(output_dir).parent / "modules"
            self.value_chains_dir = Path(output_dir).parent / "value_chains"
        
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.modules_dir.mkdir(parents=True, exist_ok=True)
        self.value_chains_dir.mkdir(parents=True, exist_ok=True)
        
        # Arithmetic modifiers to abstract
        self.arithmetic_modifiers = [
            'average', 'mean', 'median', 'sum', 'total', 
            'min', 'minimum', 'max', 'maximum', 'count'
        ]
        
        # Time periods to abstract
        self.time_periods = [
            'daily', 'weekly', 'monthly', 'quarterly', 
            'annually', 'yearly', 'custom'
        ]
        
        # Common objects in formulas
        self.object_keywords = {
            'order': 'Order',
            'purchase order': 'PurchaseOrder',
            'po': 'PurchaseOrder',
            'supplier': 'Supplier',
            'vendor': 'Supplier',
            'contract': 'Contract',
            'invoice': 'Invoice',
            'payment': 'Payment',
            'product': 'Product',
            'item': 'Product',
            'inventory': 'Inventory',
            'stock': 'Inventory',
            'warehouse': 'Warehouse',
            'customer': 'Customer',
            'employee': 'Employee',
            'buyer': 'Employee',
            'staff': 'Employee',
            'lead': 'Lead',
            'opportunity': 'Opportunity',
            'deal': 'Deal',
            'ticket': 'SupportTicket',
            'support ticket': 'SupportTicket',
            'shipment': 'Shipment',
            'delivery': 'Delivery',
            'return': 'Return',
            'defect': 'Defect',
            'quality': 'QualityMetric'
        }
    
    def load_data(self) -> pd.DataFrame:
        """Load Excel or CSV file."""
        file_ext = os.path.splitext(self.excel_path)[1].lower()
        
        try:
            if file_ext == '.csv':
                df = pd.read_csv(self.excel_path)
            elif file_ext in ['.xlsx', '.xls']:
                df = pd.read_excel(self.excel_path)
            else:
                raise ValueError(f"Unsupported file format: {file_ext}")
            
            print(f"✓ Loaded {len(df)} KPIs from {os.path.basename(self.excel_path)}")
            return df
        except Exception as e:
            print(f"✗ Error loading file: {e}")
            sys.exit(1)
    
    def clean_text(self, text: str) -> str:
        """Clean and normalize text."""
        if pd.isna(text):
            return ""
        return str(text).strip().replace('\n', ' ').replace('\r', ' ')
    
    def generate_code_name(self, kpi_name: str) -> str:
        """Generate a code name from KPI name."""
        # Remove special characters and convert to uppercase with underscores
        code = re.sub(r'[^\w\s-]', '', kpi_name)
        code = re.sub(r'[-\s]+', '_', code)
        code = code.upper()
        
        # Remove common prefixes if present
        for prefix in ['AVERAGE_', 'TOTAL_', 'MEAN_', 'MEDIAN_']:
            if code.startswith(prefix):
                code = code[len(prefix):]
        
        return code
    
    def generate_class_name(self, kpi_name: str) -> str:
        """Generate a Python class name from KPI name."""
        # Remove special characters
        name = re.sub(r'[^\w\s-]', '', kpi_name)
        # Split on spaces and hyphens, capitalize each word
        words = re.split(r'[-\s]+', name)
        class_name = ''.join(word.capitalize() for word in words if word)
        
        # Remove arithmetic modifiers from class name
        for modifier in ['Average', 'Total', 'Mean', 'Median', 'Sum', 'Min', 'Max', 'Count']:
            if class_name.startswith(modifier):
                class_name = class_name[len(modifier):]
        
        return class_name
    
    def generate_file_name(self, kpi_name: str) -> str:
        """Generate a Python file name from KPI name."""
        # Remove special characters and convert to lowercase with underscores
        name = re.sub(r'[^\w\s-]', '', kpi_name)
        name = re.sub(r'[-\s]+', '_', name)
        name = name.lower()
        
        # Remove arithmetic modifiers from file name
        for modifier in ['average_', 'total_', 'mean_', 'median_', 'sum_', 'min_', 'max_', 'count_']:
            if name.startswith(modifier):
                name = name[len(modifier):]
        
        return f"{name}.py"
    
    def extract_required_objects(self, kpi_name: str, definition: str, formula: str) -> List[str]:
        """Extract required objects from KPI name, definition, and formula."""
        objects = set()
        
        # Combine all text for analysis
        combined_text = f"{kpi_name} {definition} {formula}".lower()
        
        # Search for object keywords
        for keyword, object_name in self.object_keywords.items():
            if keyword in combined_text:
                objects.add(object_name)
        
        return sorted(list(objects))
    
    def determine_aggregation_methods(self, kpi_name: str, definition: str, formula: str) -> List[str]:
        """Determine appropriate aggregation methods based on KPI characteristics."""
        combined_text = f"{kpi_name} {definition} {formula}".lower()
        
        methods = []
        
        # Check for specific modifiers in text
        if any(word in combined_text for word in ['average', 'mean']):
            methods.append('average')
        if any(word in combined_text for word in ['total', 'sum']):
            methods.append('sum')
        if 'median' in combined_text:
            methods.append('median')
        if any(word in combined_text for word in ['minimum', 'min']):
            methods.append('min')
        if any(word in combined_text for word in ['maximum', 'max']):
            methods.append('max')
        if 'count' in combined_text or 'number of' in combined_text:
            methods.append('count')
        
        # Default aggregation methods if none found
        if not methods:
            if 'rate' in combined_text or 'percentage' in combined_text or '%' in formula:
                methods = ['average']
            elif 'time' in combined_text or 'cycle' in combined_text:
                methods = ['average', 'min', 'max']
            else:
                methods = ['average', 'sum']
        
        return methods
    
    def determine_time_periods(self, kpi_name: str, definition: str) -> List[str]:
        """Determine appropriate time periods based on KPI characteristics."""
        combined_text = f"{kpi_name} {definition}".lower()
        
        # Check for specific time periods mentioned
        mentioned_periods = []
        for period in self.time_periods:
            if period in combined_text:
                mentioned_periods.append(period)
        
        # If specific periods mentioned, use those
        if mentioned_periods:
            return mentioned_periods
        
        # Default time periods based on KPI type
        if any(word in combined_text for word in ['daily', 'day-to-day', 'real-time']):
            return ['daily', 'weekly', 'monthly']
        elif any(word in combined_text for word in ['strategic', 'long-term', 'annual']):
            return ['quarterly', 'annually']
        else:
            # Most common default
            return ['daily', 'weekly', 'monthly', 'quarterly', 'annually']
    
    def generate_kpi_file(self, row: pd.Series) -> Dict[str, str]:
        """Generate a single KPI Python file."""
        # Extract data from row
        kpi_name = self.clean_text(row.get('KPI', ''))
        definition = self.clean_text(row.get('Definition', ''))
        formula = self.clean_text(row.get('Standard Formula', ''))
        
        if not kpi_name:
            return None
        
        # Generate names
        code_name = self.generate_code_name(kpi_name)
        class_name = self.generate_class_name(kpi_name)
        file_name = self.generate_file_name(kpi_name)
        
        # Extract metadata
        required_objects = self.extract_required_objects(kpi_name, definition, formula)
        aggregation_methods = self.determine_aggregation_methods(kpi_name, definition, formula)
        time_periods = self.determine_time_periods(kpi_name, definition)
        
        # Determine category from module name
        category = self.module_name.replace('_', ' ').title()
        
        # Generate Python code - Dictionary format
        code = f'''"""
{kpi_name}

{definition}
"""

{code_name} = {{
    "code": "{code_name}",
    "name": "{kpi_name}",
    "display_name": "{kpi_name}",
    "description": "{definition}",
    "formula": "{formula}",
    "category": "{category}",
    "modules": ["{self.module_name}"],
    "module_code": "{self.module_name}",
    "required_objects": {required_objects},
    "aggregation_methods": {aggregation_methods},
    "time_periods": {time_periods},
    "is_active": True,
    "metadata_": {{
        "source": "excel_processor",
        "value_chain": "{self.value_chain}"
    }}
}}
'''
        
        return {
            'file_name': file_name,
            'code': code,
            'kpi_name': kpi_name,
            'code_name': code_name
        }
    
    def process_all(self) -> List[Dict[str, str]]:
        """Process all KPIs from the Excel/CSV file."""
        df = self.load_data()
        
        results = []
        skipped = []
        
        print(f"\n{'='*80}")
        print(f"Processing KPIs for Module: {self.module_name} | Value Chain: {self.value_chain}")
        print(f"{'='*80}\n")
        
        for idx, row in df.iterrows():
            try:
                result = self.generate_kpi_file(row)
                if result:
                    # Write file
                    file_path = self.output_dir / result['file_name']
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(result['code'])
                    
                    results.append(result)
                    print(f"✓ [{idx+1:3d}] {result['kpi_name'][:60]:<60} → {result['file_name']}")
                else:
                    skipped.append(idx + 1)
            except Exception as e:
                print(f"✗ [{idx+1:3d}] Error: {e}")
                skipped.append(idx + 1)
        
        print(f"\n{'='*80}")
        print(f"✓ Successfully created {len(results)} KPI files")
        if skipped:
            print(f"⚠ Skipped {len(skipped)} rows: {skipped}")
        print(f"{'='*80}\n")
        
        return results
    
    def generate_summary_report(self, results: List[Dict[str, str]]) -> str:
        """Generate a summary report of processed KPIs."""
        # Calculate path relative to this script's location
        script_dir = Path(__file__).parent
        report_path = script_dir.parent / "objectModelSync" / f"{self.module_name}_KPI_PROCESSING_SUMMARY.md"
        
        report = f"""# {self.module_name.replace('_', ' ').title()} Module KPI Processing Summary

**Source File**: `{self.excel_path}`  
**Module**: {self.module_name}  
**Value Chain**: {self.value_chain}  
**Total KPIs**: {len(results)}  
**Date**: {pd.Timestamp.now().strftime('%B %d, %Y')}

---

## KPIs Created

"""
        
        for idx, result in enumerate(results, 1):
            report += f"{idx}. **{result['kpi_name']}** - `{result['code_name']}`\n"
        
        report += f"""
---

## Key Patterns Applied

### Arithmetic Abstraction
All arithmetic modifiers (average, sum, min, max, median, count) abstracted into `aggregation_methods` metadata.

### Time Period Abstraction
All time periods (daily, weekly, monthly, quarterly, annually) abstracted into `time_periods` metadata.

### Module Assignment
All KPIs assigned to: `modules_=["{self.module_name}"]`

---

## Next Steps

1. ✅ Run object model sync: `run_governance.bat` → Option 1 (Full Governance)
2. ⏳ Review consolidation recommendations
3. ⏳ Update shared object models if needed
4. ⏳ Verify UML relationships

---

**Status**: {len(results)} KPIs created successfully  
**Output Directory**: `{self.output_dir}`
"""
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"📄 Summary report created: {report_path}")
        return str(report_path)
    
    def create_or_update_value_chain(self) -> str:
        """Create or update value chain definition file."""
        value_chain_file = self.value_chains_dir / f"{self.value_chain.lower()}.py"
        
        # Check if file exists
        if value_chain_file.exists():
            print(f"ℹ Value chain '{self.value_chain}' already exists: {value_chain_file}")
            return str(value_chain_file)
        
        # Map value chain codes to display names
        value_chain_names = {
            'SUPPLY_CHAIN': 'Supply Chain Management',
            'REVENUE': 'Revenue Generation',
            'CUSTOMER_EXPERIENCE': 'Customer Experience',
            'OPERATIONS': 'Operations Management',
            'FINANCE': 'Financial Management'
        }
        
        display_name = value_chain_names.get(self.value_chain, self.value_chain.replace('_', ' ').title())
        
        # Generate value chain file content - Dictionary format
        content = f'''"""
{display_name} Value Chain

Auto-generated by KPI Excel Processor
"""

{self.value_chain} = {{
    "code": "{self.value_chain}",
    "name": "{display_name}",
    "display_name": "{display_name}",
    "description": "{display_name} operations and optimization",
    "display_order": 1,
    "is_active": True,
    "metadata_": {{
        "category": "cross_industry",
        "industries": ["RETAIL", "MANUFACTURING"],
        "modules": []  # Will be populated by governance suite
    }}
}}
'''
        
        with open(value_chain_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Created value chain definition: {value_chain_file}")
        return str(value_chain_file)
    
    def create_or_update_module(self, kpi_codes: List[str], object_models: Set[str]) -> str:
        """Create or update module definition file."""
        module_file = self.modules_dir / f"{self.module_name.lower()}.py"
        
        # Generate module display name
        display_name = self.module_name.replace('_', ' ').title()
        
        # Check if file exists
        if module_file.exists():
            print(f"ℹ Module '{self.module_name}' already exists, updating KPI list...")
            
            # Read existing file
            with open(module_file, 'r', encoding='utf-8') as f:
                existing_content = f.read()
            
            # Extract existing associated_kpis list
            import re
            kpi_pattern = r'"associated_kpis":\s*\[(.*?)\]'
            match = re.search(kpi_pattern, existing_content, re.DOTALL)
            
            if match:
                # Parse existing KPIs
                existing_kpis_str = match.group(1)
                existing_kpis = [k.strip().strip('"\'') for k in existing_kpis_str.split(',') if k.strip()]
                
                # Merge with new KPIs (avoid duplicates)
                all_kpis = sorted(list(set(existing_kpis + kpi_codes)))
                
                # Format KPI list - include ALL KPIs for complete mapping
                kpi_list_str = ',\n            '.join([f'"{kpi}"' for kpi in all_kpis])
                
                # Replace KPI list in content
                new_kpi_section = f'"associated_kpis": [\n            {kpi_list_str}\n        ]'
                updated_content = re.sub(kpi_pattern, new_kpi_section, existing_content, flags=re.DOTALL)
                
                with open(module_file, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                
                print(f"✓ Updated module definition with {len(all_kpis)} KPIs: {module_file}")
                return str(module_file)
        
        # Create new module file - Dictionary format
        # Include ALL KPIs for complete mapping
        kpi_list_str = ',\n            '.join([f'"{kpi}"' for kpi in kpi_codes])
        
        # Include ALL object models for complete mapping
        all_objects = sorted(list(object_models))
        object_list_str = ', '.join([f'"{obj.upper()}"' for obj in all_objects])
        
        content = f'''"""
{display_name} Module

Auto-generated by KPI Excel Processor
"""

{self.module_name} = {{
    "code": "{self.module_name}",
    "name": "{display_name}",
    "display_name": "{display_name}",
    "description": "{display_name} analytics and performance tracking",
    "display_order": 1,
    "is_active": True,
    "value_chains": ["{self.value_chain}"],
    "metadata_": {{
        "industries": ["RETAIL", "MANUFACTURING"],
        "associated_object_models": [{object_list_str}],
        "associated_kpis": [
            {kpi_list_str}
        ]
    }}
}}
'''
        
        with open(module_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Created module definition: {module_file}")
        return str(module_file)


def main():
    """Main entry point for command-line usage."""
    parser = argparse.ArgumentParser(
        description='Generate KPI Python files from Excel/CSV templates',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python kpi_excel_processor.py --file "C:\\path\\to\\kpis.csv" --module SOURCING --chain SUPPLY_CHAIN
  python kpi_excel_processor.py -f kpis.xlsx -m SALES -c REVENUE
  python kpi_excel_processor.py -f kpis.csv -m CUSTOMER_SERVICE -c CUSTOMER_EXPERIENCE -o ./custom_output
        """
    )
    
    parser.add_argument(
        '-f', '--file',
        required=True,
        help='Path to Excel (.xlsx, .xls) or CSV (.csv) file containing KPI data'
    )
    
    parser.add_argument(
        '-m', '--module',
        required=True,
        help='Module name to assign (e.g., SOURCING, SALES, CUSTOMER_SERVICE)'
    )
    
    parser.add_argument(
        '-c', '--chain',
        required=True,
        help='Value chain to assign (e.g., SUPPLY_CHAIN, REVENUE, CUSTOMER_EXPERIENCE)'
    )
    
    parser.add_argument(
        '-o', '--output',
        default=None,
        help='Output directory for generated KPI files (default: auto-detect)'
    )
    
    args = parser.parse_args()
    
    # Validate file exists
    if not os.path.exists(args.file):
        print(f"✗ Error: File not found: {args.file}")
        sys.exit(1)
    
    # Process KPIs
    processor = KPIExcelProcessor(
        excel_path=args.file,
        module_name=args.module,
        value_chain=args.chain,
        output_dir=args.output
    )
    
    results = processor.process_all()
    
    if results:
        # Collect all KPI codes and object models
        kpi_codes = [r['code_name'].lower() for r in results]
        all_objects = set()
        for result in results:
            # Extract objects from the generated code
            code_lines = result['code'].split('\n')
            for line in code_lines:
                if 'required_objects=' in line:
                    # Extract object list from the line
                    import ast
                    try:
                        start = line.index('[')
                        end = line.index(']') + 1
                        objects_str = line[start:end]
                        objects = ast.literal_eval(objects_str)
                        all_objects.update(objects)
                    except:
                        pass
        
        # Create or update value chain and module
        print(f"\n{'='*80}")
        print("Creating/Updating Module and Value Chain Definitions")
        print(f"{'='*80}\n")
        
        processor.create_or_update_value_chain()
        processor.create_or_update_module(kpi_codes, all_objects)
        
        # Generate summary report
        processor.generate_summary_report(results)
        
        print(f"\n{'='*80}")
        print(f"✓ All done! Created {len(results)} KPI files for {args.module} module.")
        print(f"✓ Module and value chain definitions updated")
        print(f"{'='*80}")
        print(f"\n💡 Next step: Run governance suite to sync object models")
        print(f"   Command: cd scripts\\objectModelSync && run_governance.bat")
    else:
        print("\n✗ No KPIs were processed.")
        sys.exit(1)


if __name__ == '__main__':
    main()

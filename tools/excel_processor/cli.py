import argparse
import sys
from .processor import KPIExcelProcessor

def main():
    parser = argparse.ArgumentParser(description="Analytics Engine - KPI Excel Processor")
    parser.add_argument("input_file", help="Path to the Excel file containing KPI definitions")
    parser.add_argument("--output-dir", default="./output/definitions", help="Directory to save generated JSON definitions")
    parser.add_argument("--code-file", default=None, help="Optional: Path to save generated Python code registry")
    
    args = parser.parse_args()
    
    print(f"Processing file: {args.input_file}")
    
    processor = KPIExcelProcessor()
    
    try:
        kpis = processor.parse_file(args.input_file)
        print(f"Found {len(kpis)} valid KPIs.")
        
        processor.generate_definitions(kpis, args.output_dir)
        
        if args.code_file:
            processor.generate_python_code(kpis, args.code_file)
            
        print("Processing complete.")
        sys.exit(0)
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

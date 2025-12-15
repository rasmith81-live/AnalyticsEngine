import pandas as pd
from typing import List, Dict, Any
import json
import os
import re

class KPIExcelProcessor:
    """
    Parses Excel and CSV files to extract KPI definitions and generates metadata artifacts.
    """

    # Updated column mapping based on "kpidepot.com-sales-training-and-coaching.csv"
    REQUIRED_COLUMNS = ['KPI', 'Definition', 'Standard Formula']

    def parse_file(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Reads the Excel/CSV file and returns a list of KPI definition dictionaries.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        try:
            if file_path.endswith('.csv'):
                df = pd.read_csv(file_path)
            else:
                df = pd.read_excel(file_path)
        except Exception as e:
            raise ValueError(f"Failed to read file: {e}")

        # Normalize columns (strip whitespace)
        df.columns = [c.strip() for c in df.columns]

        # Validate columns
        missing_cols = [col for col in self.REQUIRED_COLUMNS if col not in df.columns]
        if missing_cols:
            # Fallback to old format if new columns aren't present
            if 'Code' in df.columns and 'Name' in df.columns:
                return self._parse_legacy_format(df, file_path)
            raise ValueError(f"Missing required columns: {missing_cols}")

        kpis = []
        for _, row in df.iterrows():
            # Generate code from KPI name (slugify)
            kpi_name = str(row['KPI']).strip()
            kpi_code = re.sub(r'[^a-zA-Z0-9]', '_', kpi_name).upper()

            kpi = {
                "kind": "metric_definition",
                "code": kpi_code,
                "name": kpi_name,
                "description": str(row['Definition']).strip() if pd.notna(row['Definition']) else None,
                "formula": str(row['Standard Formula']).strip() if pd.notna(row['Standard Formula']) else None,
                # Map extra fields to metadata
                "metadata": {
                    "source_file": os.path.basename(file_path),
                    "business_insights": str(row.get('Business Insights', '')),
                    "measurement_approach": str(row.get('Measurement Approach', '')),
                    "visualization_suggestions": str(row.get('Visualization Suggestions', ''))
                }
            }
            if self._validate_kpi(kpi):
                kpis.append(kpi)
            else:
                print(f"Skipping invalid KPI row: {kpi_name}")
        
        return kpis

    def _parse_legacy_format(self, df: pd.DataFrame, file_path: str) -> List[Dict[str, Any]]:
        """
        Parses the legacy Excel format (Code, Name, Description, Formula).
        """
        kpis = []
        for _, row in df.iterrows():
            kpi = {
                "kind": "metric_definition",
                "code": str(row['Code']).strip(),
                "name": str(row['Name']).strip(),
                "description": str(row['Description']).strip() if pd.notna(row['Description']) else None,
                "formula": str(row['Formula']).strip() if pd.notna(row['Formula']) else None,
                "metadata": {
                    "source_file": os.path.basename(file_path)
                }
            }
            if self._validate_kpi(kpi):
                kpis.append(kpi)
        return kpis

    def _validate_kpi(self, kpi: Dict[str, Any]) -> bool:
        """
        Basic validation logic.
        """
        if not kpi['code'] or not kpi['name']:
            return False
        # Check basic formula safety (no obvious injection)
        if kpi['formula'] and any(x in kpi['formula'] for x in ['import', 'exec', 'eval']):
            return False
        return True

    def generate_definitions(self, kpis: List[Dict[str, Any]], output_dir: str):
        """
        Generates JSON definition files for each KPI.
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for kpi in kpis:
            file_name = f"{kpi['code'].lower()}.json"
            file_path = os.path.join(output_dir, file_name)
            
            try:
                with open(file_path, 'w') as f:
                    json.dump(kpi, f, indent=4)
                print(f"Generated: {file_path}")
            except Exception as e:
                print(f"Failed to write {file_name}: {e}")

    def generate_python_code(self, kpis: List[Dict[str, Any]], output_file: str):
        """
        Generates a Python file containing the KPI logic (Prototype).
        """
        lines = [
            "# Auto-generated KPI Definitions",
            "from typing import Dict, Any",
            "",
            "KPI_REGISTRY = {"
        ]
        
        for kpi in kpis:
            lines.append(f'    "{kpi["code"]}": {{')
            lines.append(f'        "name": "{kpi["name"]}",')
            lines.append(f'        "formula": "{kpi["formula"]}",')
            lines.append('    },')
        
        lines.append("}")
        
        with open(output_file, 'w') as f:
            f.write("\n".join(lines))
        print(f"Generated Python code: {output_file}")

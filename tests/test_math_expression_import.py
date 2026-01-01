"""
Test for Math Expression Generation During Import

Validates that the metadata ingestion service correctly generates
mathematical expressions from natural language KPI formulas.

Usage:
    python tests/test_math_expression_import.py
"""

import asyncio
import httpx
import json
import os
import sys
import tempfile
import time
from typing import Dict, Any, List, Optional
from dataclasses import dataclass

# Configuration
INGESTION_SERVICE_URL = os.getenv("INGESTION_SERVICE_URL", "http://127.0.0.1:8025")
METADATA_SERVICE_URL = os.getenv("METADATA_SERVICE_URL", "http://127.0.0.1:8020")
REQUEST_TIMEOUT = 60.0


@dataclass
class TestResult:
    """Container for test results."""
    name: str
    passed: bool = False
    error: Optional[str] = None
    details: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.details is None:
            self.details = {}
    
    def __repr__(self):
        status = "✅ PASS" if self.passed else "❌ FAIL"
        return f"{status} {self.name}"


# Test KPIs with various formula patterns
TEST_KPIS = [
    {
        "name": "Order Fulfillment Rate",
        "formula": "(Number of Orders Fulfilled On Time / Total Number of Orders) * 100",
        "description": "Percentage of orders fulfilled on time",
        "expected_pattern": "ratio_percentage"  # (A / B) * 100
    },
    {
        "name": "Inventory Turnover",
        "formula": "Cost of Goods Sold / Average Inventory Value",
        "description": "How many times inventory is sold and replaced",
        "expected_pattern": "ratio"  # A / B
    },
    {
        "name": "Average Order Value",
        "formula": "Total Revenue / Number of Orders",
        "description": "Average value per order",
        "expected_pattern": "ratio"
    },
    {
        "name": "Days Sales Outstanding",
        "formula": "(Accounts Receivable / Total Credit Sales) * Number of Days",
        "description": "Average days to collect payment",
        "expected_pattern": "complex"
    },
    {
        "name": "Gross Profit Margin",
        "formula": "((Revenue - Cost of Goods Sold) / Revenue) * 100",
        "description": "Profit as percentage of revenue",
        "expected_pattern": "ratio_percentage"
    }
]


def create_test_csv() -> str:
    """Create a temporary CSV file with test KPIs."""
    import csv
    
    fd, path = tempfile.mkstemp(suffix='.csv')
    with os.fdopen(fd, 'w', newline='', encoding='utf-8') as f:
        # Use the required columns: KPI, Definition, Standard Formula
        writer = csv.DictWriter(f, fieldnames=['KPI', 'Definition', 'Standard Formula'])
        writer.writeheader()
        for kpi in TEST_KPIS:
            writer.writerow({
                'KPI': kpi['name'],
                'Definition': kpi['description'],
                'Standard Formula': kpi['formula']
            })
    return path


class MathExpressionImportTest:
    """Test math expression generation during import."""
    
    def __init__(self):
        self.results: List[TestResult] = []
        self.import_id: Optional[str] = None
        self.preview_data: List[Dict] = []
        
    async def check_service_health(self) -> TestResult:
        """Check if ingestion service is healthy."""
        result = TestResult(name="Ingestion Service Health Check")
        
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.get(f"{INGESTION_SERVICE_URL}/health")
                if response.status_code == 200:
                    result.passed = True
                    result.details = response.json()
                else:
                    result.error = f"Status {response.status_code}"
        except Exception as e:
            result.error = str(e)
        
        return result
    
    async def upload_and_analyze(self) -> TestResult:
        """Upload test CSV - math expressions are extracted during upload."""
        result = TestResult(name="Upload and Extract Math Expressions")
        
        csv_path = create_test_csv()
        
        try:
            async with httpx.AsyncClient(timeout=REQUEST_TIMEOUT) as client:
                # Upload file - this automatically extracts math expressions using spaCy
                with open(csv_path, 'rb') as f:
                    files = {'file': ('test_kpis.csv', f, 'text/csv')}
                    response = await client.post(
                        f"{INGESTION_SERVICE_URL}/import/upload",
                        files=files
                    )
                
                if response.status_code != 200:
                    result.error = f"Upload failed: {response.status_code} - {response.text}"
                    return result
                
                upload_result = response.json()
                self.import_id = upload_result.get("importId")
                self.preview_data = upload_result.get("preview", [])
                
                result.details["import_id"] = self.import_id
                result.details["total_rows"] = upload_result.get("totalRows")
                result.details["valid_rows"] = upload_result.get("validRows")
                result.details["kpi_count"] = len(self.preview_data)
                result.passed = True
                
        except Exception as e:
            result.error = str(e)
        finally:
            # Cleanup temp file
            try:
                os.unlink(csv_path)
            except:
                pass
        
        return result
    
    def validate_math_expressions(self) -> TestResult:
        """Validate that math expressions were generated correctly."""
        result = TestResult(name="Validate Math Expression Generation")
        
        if not self.preview_data:
            result.error = "No preview data available"
            return result
        
        validated = 0
        failed = []
        expression_samples = []
        
        for i, kpi in enumerate(self.preview_data):
            kpi_name = kpi.get("Name", f"KPI {i}")
            formula = kpi.get("Formula", "")
            
            # Get math expression from top level (MathExpression in preview)
            math_expr = kpi.get("MathExpression")
            
            if math_expr:
                validated += 1
                expression_samples.append({
                    "name": kpi_name,
                    "formula": formula[:50] + "..." if len(formula) > 50 else formula,
                    "math_expression": math_expr
                })
            else:
                failed.append({
                    "name": kpi_name,
                    "formula": formula,
                    "error": "No math expression generated"
                })
        
        result.details = {
            "total_kpis": len(self.preview_data),
            "with_math_expression": validated,
            "without_math_expression": len(failed),
            "samples": expression_samples[:3],
            "failures": failed[:3]
        }
        
        # Pass if at least 80% of KPIs have math expressions
        if len(self.preview_data) > 0:
            success_rate = validated / len(self.preview_data)
            result.details["success_rate"] = f"{success_rate * 100:.1f}%"
            result.passed = success_rate >= 0.8
            if not result.passed:
                result.error = f"Only {success_rate * 100:.1f}% of KPIs have math expressions"
        else:
            result.error = "No KPIs in preview data"
        
        return result
    
    def validate_required_objects(self) -> TestResult:
        """Validate that required_objects contains proper entity references."""
        result = TestResult(name="Validate Required Objects (Entities)")
        
        if not self.preview_data:
            result.error = "No preview data available"
            return result
        
        validated = 0
        samples = []
        issues = []
        
        # Stop words that should NOT appear in required_objects
        stop_words = {"of", "by", "the", "a", "an", "to", "from", "in", "on", "at", 
                      "for", "with", "as", "is", "are", "total", "number", "sum", 
                      "count", "average", "avg", "rate", "ratio", "percent", "percentage"}
        
        for kpi in self.preview_data:
            kpi_name = kpi.get("Name", "Unknown")
            required_objs = kpi.get("RequiredObjects", [])
            
            if not required_objs:
                issues.append({"name": kpi_name, "issue": "No required_objects"})
                continue
            
            # Check for stop words in required_objects
            found_stop_words = [w for w in required_objs if w.lower() in stop_words]
            
            if found_stop_words:
                issues.append({
                    "name": kpi_name, 
                    "issue": f"Contains stop words: {found_stop_words}",
                    "all_objects": required_objs
                })
            else:
                validated += 1
                samples.append({
                    "name": kpi_name,
                    "required_objects": required_objs
                })
        
        result.details = {
            "total_kpis": len(self.preview_data),
            "properly_extracted": validated,
            "with_issues": len(issues),
            "samples": samples[:3],
            "issues": issues[:3]
        }
        
        # Pass if at least 80% have proper entity extraction
        if len(self.preview_data) > 0:
            success_rate = validated / len(self.preview_data)
            result.details["success_rate"] = f"{success_rate * 100:.1f}%"
            result.passed = success_rate >= 0.8
            if not result.passed:
                result.error = f"Only {success_rate * 100:.1f}% have properly extracted entities"
        else:
            result.error = "No KPIs in preview data"
        
        return result
    
    def validate_expression_syntax(self) -> TestResult:
        """Validate that generated math expressions have correct syntax."""
        result = TestResult(name="Validate Math Expression Syntax")
        
        valid_syntax = 0
        invalid = []
        
        for kpi in self.preview_data:
            kpi_name = kpi.get("Name", "Unknown")
            math_expr = kpi.get("MathExpression")
            
            if not math_expr:
                continue
            
            # Check for expected patterns in math expression
            has_aggregation = any(agg in math_expr for agg in ["Count(", "Sum(", "Avg(", "Max(", "Min("])
            has_operators = any(op in math_expr for op in ["/", "*", "+", "-"])
            has_parentheses = "(" in math_expr and ")" in math_expr
            
            # Valid if it has aggregations or operators with proper structure
            if has_aggregation or (has_operators and has_parentheses):
                valid_syntax += 1
            else:
                invalid.append({
                    "name": kpi_name,
                    "expression": math_expr,
                    "issue": "Missing aggregation functions or operators"
                })
        
        total_with_expr = sum(1 for k in self.preview_data if k.get("MathExpression"))
        
        result.details = {
            "total_with_expression": total_with_expr,
            "valid_syntax": valid_syntax,
            "invalid_syntax": len(invalid),
            "invalid_samples": invalid[:3]
        }
        
        if total_with_expr > 0:
            success_rate = valid_syntax / total_with_expr
            result.details["syntax_success_rate"] = f"{success_rate * 100:.1f}%"
            result.passed = success_rate >= 0.7
            if not result.passed:
                result.error = f"Only {success_rate * 100:.1f}% have valid syntax"
        else:
            result.passed = True
            result.details["note"] = "No expressions to validate"
        
        return result
    
    async def run_all_tests(self) -> bool:
        """Run all tests and return overall success."""
        print("\n" + "=" * 70)
        print("MATH EXPRESSION IMPORT VALIDATION TEST")
        print("=" * 70)
        
        # Health check
        print("\n📋 Phase 1: Service Health Check")
        health_result = await self.check_service_health()
        self.results.append(health_result)
        print(f"   {health_result}")
        
        if not health_result.passed:
            print("\n❌ Ingestion service not available. Cannot proceed.")
            return False
        
        # Upload and analyze
        print("\n📋 Phase 2: Upload and Analyze Test KPIs")
        upload_result = await self.upload_and_analyze()
        self.results.append(upload_result)
        print(f"   {upload_result}")
        if upload_result.details:
            print(f"      Import ID: {upload_result.details.get('import_id')}")
            print(f"      KPIs processed: {upload_result.details.get('kpi_count')}")
        
        if not upload_result.passed:
            print(f"\n❌ Upload/Analysis failed: {upload_result.error}")
            return False
        
        # Validate math expressions
        print("\n📋 Phase 3: Validate Math Expression Generation")
        expr_result = self.validate_math_expressions()
        self.results.append(expr_result)
        print(f"   {expr_result}")
        print(f"      KPIs with math expressions: {expr_result.details.get('with_math_expression')}/{expr_result.details.get('total_kpis')}")
        
        if expr_result.details.get("samples"):
            print("\n   📝 Sample Math Expressions:")
            for sample in expr_result.details["samples"]:
                print(f"      • {sample['name']}")
                print(f"        Formula: {sample['formula']}")
                print(f"        Math:    {sample['math_expression']}")
        
        # Validate required_objects
        print("\n📋 Phase 4: Validate Required Objects (Entities)")
        req_obj_result = self.validate_required_objects()
        self.results.append(req_obj_result)
        print(f"   {req_obj_result}")
        print(f"      Properly extracted: {req_obj_result.details.get('properly_extracted')}/{req_obj_result.details.get('total_kpis')}")
        
        if req_obj_result.details.get("samples"):
            print("\n   📝 Sample Required Objects:")
            for sample in req_obj_result.details["samples"]:
                print(f"      • {sample['name']}: {sample['required_objects']}")
        
        if req_obj_result.details.get("issues"):
            print("\n   ⚠️ Issues Found:")
            for issue in req_obj_result.details["issues"]:
                print(f"      • {issue['name']}: {issue['issue']}")
        
        # Validate syntax
        print("\n📋 Phase 5: Validate Math Expression Syntax")
        syntax_result = self.validate_expression_syntax()
        self.results.append(syntax_result)
        print(f"   {syntax_result}")
        
        # Summary
        print("\n" + "=" * 70)
        print("TEST SUMMARY")
        print("=" * 70)
        
        passed = sum(1 for r in self.results if r.passed)
        total = len(self.results)
        
        print(f"\nResults: {passed}/{total} tests passed")
        
        all_passed = all(r.passed for r in self.results)
        
        if all_passed:
            print("\n✅ ALL TESTS PASSED - Math expressions are being generated correctly")
        else:
            print("\n❌ SOME TESTS FAILED")
            for r in self.results:
                if not r.passed:
                    print(f"   - {r.name}: {r.error}")
        
        return all_passed


async def main():
    """Run the test suite."""
    test = MathExpressionImportTest()
    success = await test.run_all_tests()
    return 0 if success else 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)

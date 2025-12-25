"""
Test LLM Connectivity via Entity Resolution Service

Tests LLM integration by calling the batch extraction endpoint
which uses LLM under the hood.
"""

import sys
import httpx
from datetime import datetime

ENTITY_RESOLUTION_URL = "http://127.0.0.1:8012"

def test_llm_via_service():
    """Test LLM by calling the entity resolution service batch extraction."""
    print("\n" + "=" * 60)
    print("  LLM CONNECTIVITY TEST (via Entity Resolution Service)")
    print("=" * 60)
    print(f"  Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Target: {ENTITY_RESOLUTION_URL}")
    print("=" * 60 + "\n")
    
    # Test 1: Health check
    print("📡 Step 1: Health check...")
    try:
        with httpx.Client(timeout=10.0) as client:
            response = client.get(f"{ENTITY_RESOLUTION_URL}/health")
            if response.status_code == 200:
                print(f"   ✅ Service healthy: {response.json()}")
            else:
                print(f"   ❌ Service unhealthy: {response.status_code}")
                return False
    except Exception as e:
        print(f"   ❌ Cannot reach service: {e}")
        return False
    
    # Test 2: Batch entity extraction (uses LLM)
    print("\n📡 Step 2: Batch entity extraction (LLM call)...")
    test_kpis = [
        "Customer Acquisition Cost measures marketing spend divided by new customers",
        "Revenue Growth Rate shows year over year sales increase percentage",
        "Inventory Turnover measures how often stock is sold and replaced"
    ]
    
    try:
        with httpx.Client(timeout=60.0) as client:
            response = client.post(
                f"{ENTITY_RESOLUTION_URL}/api/v1/entity-resolution/semantic/extract-batch",
                json={"kpi_texts": test_kpis}
            )
            
            if response.status_code == 200:
                result = response.json()
                entities = result.get("entities", [])
                count = result.get("count", 0)
                
                print(f"   ✅ LLM Response received")
                print(f"   ✅ Extracted {count} distinct entities: {entities}")
                
                # Check for expected business entities
                expected = {"customer", "revenue", "inventory", "sales", "stock", "marketing"}
                found = set(e.lower() for e in entities)
                matches = expected.intersection(found)
                
                if matches:
                    print(f"   ✅ Found expected entities: {matches}")
                    print("\n" + "=" * 60)
                    print("  🎉 LLM CONNECTIVITY TEST PASSED!")
                    print("=" * 60)
                    return True
                elif entities:
                    print(f"   ⚠️  Got entities but none matched expected: {entities}")
                    print("\n" + "=" * 60)
                    print("  ⚠️  LLM CONNECTED (entities differ from expected)")
                    print("=" * 60)
                    return True
                else:
                    print("   ❌ No entities extracted - LLM may not be configured")
                    print("\n" + "=" * 60)
                    print("  ❌ LLM NOT CONFIGURED OR FAILED")
                    print("=" * 60)
                    return False
            else:
                print(f"   ❌ Request failed: {response.status_code}")
                print(f"   Response: {response.text[:200]}")
                return False
                
    except httpx.TimeoutException:
        print("   ❌ Request timed out (60s)")
        return False
    except Exception as e:
        print(f"   ❌ Error: {type(e).__name__}: {e}")
        return False


if __name__ == "__main__":
    success = test_llm_via_service()
    sys.exit(0 if success else 1)

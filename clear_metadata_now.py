"""Clear metadata database using the service's own configuration."""

import sys
import asyncio
from pathlib import Path

# Add the business_metadata service to path
service_path = Path(__file__).parent / "services" / "business_services" / "business_metadata"
sys.path.insert(0, str(service_path))

# Add backend services to path for database_service
backend_path = Path(__file__).parent / "services" / "backend_services"
sys.path.insert(0, str(backend_path))

async def clear_database():
    """Clear all metadata tables."""
    try:
        from config import settings
        from sqlalchemy.ext.asyncio import create_async_engine
        from sqlalchemy import text
        
        print(f"Connecting to database: {settings.database_url.split('@')[1]}")
        
        # Create engine using service's database URL
        engine = create_async_engine(settings.database_url)
        
        async with engine.begin() as conn:
            print("Clearing metadata tables...")
            
            # Truncate all tables
            await conn.execute(text(
                "TRUNCATE TABLE metadata_definitions, metadata_relationships, metadata_versions CASCADE"
            ))
            
            print("✅ Database cleared successfully!")
            print("   - metadata_definitions: cleared")
            print("   - metadata_relationships: cleared")
            print("   - metadata_versions: cleared")
            print("\nYou can now re-upload your Excel file.")
        
        await engine.dispose()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

if __name__ == "__main__":
    success = asyncio.run(clear_database())
    sys.exit(0 if success else 1)

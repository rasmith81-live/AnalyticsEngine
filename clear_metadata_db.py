"""Script to clear all metadata from the business_metadata database."""

import asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

async def clear_metadata_database():
    """Clear all tables in the metadata database."""
    # Database connection string - analytics_metadata database
    # Note: Update password if different from default
    database_url = "postgresql+asyncpg://postgres:postgres@localhost:5432/analytics_metadata"
    
    engine = create_async_engine(database_url)
    
    try:
        async with engine.begin() as conn:
            print("Clearing metadata database...")
            
            # Truncate all metadata tables
            await conn.execute(text(
                "TRUNCATE TABLE metadata_definitions, metadata_relationships, metadata_versions CASCADE"
            ))
            
            print("✅ Database cleared successfully!")
            print("   - metadata_definitions: cleared")
            print("   - metadata_relationships: cleared")
            print("   - metadata_versions: cleared")
            
    except Exception as e:
        print(f"❌ Error clearing database: {e}")
        raise
    finally:
        await engine.dispose()

if __name__ == "__main__":
    asyncio.run(clear_metadata_database())

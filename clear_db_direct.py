"""Direct database clear without using service config."""

import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text

async def clear_database():
    """Clear all metadata tables."""
    # Use the correct database credentials from .env
    # The business_metadata service uses the multiservice_db database
    database_url = "postgresql+asyncpg://multiservice_user:multiservice_password@localhost:5432/multiservice_db"
    
    print(f"Connecting to multiservice_db database...")
    
    try:
        engine = create_async_engine(database_url, echo=False)
        
        async with engine.begin() as conn:
            print("Clearing metadata tables...")
            
            # Truncate all tables
            await conn.execute(text(
                "TRUNCATE TABLE metadata_definitions, metadata_relationships, metadata_versions CASCADE"
            ))
            
            print("\n✅ Database cleared successfully!")
            print("   - metadata_definitions: cleared")
            print("   - metadata_relationships: cleared")
            print("   - metadata_versions: cleared")
            print("\n📝 You can now re-upload your Excel file without duplicates.")
        
        await engine.dispose()
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nIf you're getting a password error, the database password may be different.")
        print("Check your PostgreSQL configuration or .env files for the correct password.")
        return False

if __name__ == "__main__":
    success = asyncio.run(clear_database())
    exit(0 if success else 1)

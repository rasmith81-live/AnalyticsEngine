import sys
import os
import logging
from typing import List, Tuple, Any
from alembic.runtime.migration import MigrationContext
from alembic.autogenerate import compare_metadata
from sqlalchemy import create_engine, pool

# Add parent directory to path to allow importing app modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.config import get_settings
from app.base_models import Base

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SchemaDetector:
    """Detects schema drift between SQLAlchemy models and the live database."""

    def __init__(self):
        self.settings = get_settings()
        # Use sync URL for Alembic inspection
        self.db_url = self.settings.database_url.replace('+asyncpg', '+psycopg2')
        if '+psycopg2' not in self.db_url and 'postgresql://' in self.db_url:
             self.db_url = self.db_url.replace('postgresql://', 'postgresql+psycopg2://')

    def check_drift(self) -> List[Tuple[Any, ...]]:
        """
        Compares metadata and returns a list of differences.
        """
        logger.info(f"Connecting to database to check for schema drift: {self.db_url.split('@')[-1]}") # Log safe URL part
        
        engine = create_engine(self.db_url, poolclass=pool.NullPool)
        
        try:
            with engine.connect() as connection:
                context = MigrationContext.configure(
                    connection, 
                    opts={
                        'compare_type': True,  # Check column types
                        'compare_server_default': True, # Check defaults
                    }
                )
                
                # Compare the live DB (context) against the Code (Base.metadata)
                diff = compare_metadata(context, Base.metadata)
                
                return diff
        except Exception as e:
            logger.error(f"Failed to check schema drift: {e}")
            raise
        finally:
            engine.dispose()

    def print_report(self, diff: List[Tuple[Any, ...]]) -> bool:
        """
        Prints a human-readable report of the drift.
        Returns True if drift detected, False otherwise.
        """
        if not diff:
            logger.info("✅ No schema drift detected. Database is in sync with models.")
            return False

        logger.warning(f"⚠️  SCHEMA DRIFT DETECTED: {len(diff)} differences found.")
        
        for action in diff:
            # Format the action tuple into a readable string
            # Action tuples structure varies: ('add_table', table), ('remove_column', table, col), etc.
            action_name = action[0]
            if action_name == 'add_table':
                print(f"  [+] Table '{action[1].name}' exists in Code but missing in DB.")
            elif action_name == 'remove_table':
                print(f"  [-] Table '{action[1].name}' exists in DB but missing in Code.")
            elif action_name == 'add_column':
                print(f"  [+] Column '{action[2].name}' missing in DB (Table: {action[1]}).")
            elif action_name == 'remove_column':
                print(f"  [-] Column '{action[2].name}' extra in DB (Table: {action[1]}).")
            elif action_name == 'modify_type':
                print(f"  [~] Column '{action[2]}' type mismatch (Table: {action[1]}). Code: {action[5]}, DB: {action[4]}")
            else:
                print(f"  [?] {action}")

        return True

def main():
    detector = SchemaDetector()
    try:
        diff = detector.check_drift()
        has_drift = detector.print_report(diff)
        
        if has_drift:
            sys.exit(1) # Fail build
        else:
            sys.exit(0) # Pass build
            
    except Exception as e:
        logger.critical(f"Schema detection crashed: {e}")
        sys.exit(2) # System error

if __name__ == "__main__":
    main()

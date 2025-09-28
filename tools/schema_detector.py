import argparse
import logging
import os
import sys
from importlib import import_module

from alembic.config import Config
from alembic.runtime.migration import MigrationContext
from alembic import autogenerate
from alembic.script import ScriptDirectory
from sqlalchemy import create_engine

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

# Exit codes
EXIT_CODE_CHANGES_DETECTED = 0
EXIT_CODE_ERROR = 1
EXIT_CODE_NO_CHANGES = 2

def get_project_root():
    """Get the project root directory."""
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def main():
    """Main function to detect schema drift."""
    parser = argparse.ArgumentParser(description='Detects drift between SQLAlchemy models and the database schema.')
    parser.add_argument('--service', required=True, help='The name of the service to check (e.g., database_service).')
    args = parser.parse_args()

    project_root = get_project_root()
    sys.path.insert(0, project_root)

    # 1. Load Alembic configuration
    alembic_cfg = Config(os.path.join(project_root, 'alembic.ini'))
    script = ScriptDirectory.from_config(alembic_cfg)

    # 2. Get database URL from environment (Alembic needs a sync URL)
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        logger.error('DATABASE_URL environment variable is not set.')
        sys.exit(EXIT_CODE_ERROR)
    sync_db_url = db_url.replace('+asyncpg', '+psycopg2')

    # 3. Dynamically import the service's models
    try:
        module_path = f'services.backend_services.{args.service}.app.base_models'
        models_module = import_module(module_path)
        target_metadata = models_module.Base.metadata
        logger.info(f'Successfully imported models from {module_path}')
    except ImportError as e:
        logger.error(f'Failed to import models for service {args.service}: {e}')
        sys.exit(EXIT_CODE_ERROR)

    # 4. Compare metadata
    has_changes = False
    try:
        engine = create_engine(sync_db_url)
        with engine.connect() as connection:
            logger.info('Connected to the database to check for schema differences.')
            # We need a MigrationContext to run the comparison
            opts = {
                'compare_type': True,
                'compare_server_default': True,
            }
            mctx = MigrationContext.configure(connection=connection, opts=opts)

            # The 'autogenerate.compare_metadata' function does the heavy lifting
            diff = autogenerate.compare_metadata(mctx, target_metadata)

            if diff:
                logger.warning('Schema drift detected! The following changes were found:')
                for op in diff:
                    # op is a tuple, e.g., ('add_table', <Table object>)
                    op_type = op[0]
                    details = str(op[1])
                    logger.info(f'  - {op_type}: {details}')
                has_changes = True
            else:
                logger.info('No schema drift detected. Models and database are in sync.')

    except Exception as e:
        logger.error(f'An error occurred during schema comparison: {e}', exc_info=True)
        sys.exit(EXIT_CODE_ERROR)

    # 5. Exit with the appropriate code
    if has_changes:
        logger.info(f'Exiting with code {EXIT_CODE_CHANGES_DETECTED} (changes detected).')
        sys.exit(EXIT_CODE_CHANGES_DETECTED)
    else:
        logger.info(f'Exiting with code {EXIT_CODE_NO_CHANGES} (no changes).')
        sys.exit(EXIT_CODE_NO_CHANGES)

if __name__ == '__main__':
    main()


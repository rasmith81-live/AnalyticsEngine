"""
Object Model Synchronization - Main Orchestrator

Runs the complete synchronization process to ensure all analytics objects
are properly mapped to their associated components.
"""

import sys
import json
import logging
from pathlib import Path
from datetime import datetime
import shutil

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from analyze_objects import analyze_all_objects
from sync_kpi_required_objects import sync_kpi_objects
from sync_object_metadata import sync_object_metadata
from sync_uml_relationships import sync_uml_relationships
from fix_formatting import fix_all_formatting
from validate_integrity import validate_system_integrity
from generate_report import generate_sync_report

class SyncOrchestrator:
    """Orchestrates the complete synchronization process."""
    
    def __init__(self, config_path='config.json'):
        """Initialize orchestrator with configuration."""
        self.config = self.load_config(config_path)
        self.setup_logging()
        self.setup_directories()
        self.results = {
            'start_time': datetime.now(),
            'steps': [],
            'errors': [],
            'warnings': []
        }
    
    def load_config(self, config_path):
        """Load configuration from JSON file."""
        with open(config_path, 'r') as f:
            return json.load(f)
    
    def setup_logging(self):
        """Setup logging configuration."""
        log_dir = Path(self.config['paths']['logs_dir'])
        log_dir.mkdir(parents=True, exist_ok=True)
        
        log_file = log_dir / f"sync_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        
        logging.basicConfig(
            level=getattr(logging, self.config['logging']['level']),
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file),
                logging.StreamHandler() if self.config['logging']['console_output'] else logging.NullHandler()
            ]
        )
        
        self.logger = logging.getLogger(__name__)
        self.logger.info("=" * 80)
        self.logger.info("OBJECT MODEL SYNCHRONIZATION - FULL SYNC")
        self.logger.info("=" * 80)
    
    def setup_directories(self):
        """Create necessary directories."""
        for key, path in self.config['paths'].items():
            if key.endswith('_dir'):
                Path(path).mkdir(parents=True, exist_ok=True)
    
    def create_backup(self):
        """Create timestamped backup of definitions directory."""
        if not self.config['sync_options']['create_backups']:
            self.logger.info("Backups disabled, skipping...")
            return None
        
        self.logger.info("\nStep 0: Creating backup...")
        
        backup_dir = Path(self.config['paths']['backup_dir'])
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = backup_dir / f"definitions_backup_{timestamp}"
        
        definitions_dir = Path(self.config['paths']['definitions_dir'])
        
        try:
            shutil.copytree(definitions_dir, backup_path)
            self.logger.info(f"✅ Backup created: {backup_path}")
            return backup_path
        except Exception as e:
            self.logger.error(f"❌ Backup failed: {e}")
            self.results['errors'].append(f"Backup failed: {e}")
            return None
    
    def run_step(self, step_name, step_function, *args, **kwargs):
        """Run a synchronization step and track results."""
        self.logger.info(f"\n{step_name}")
        self.logger.info("-" * 80)
        
        step_result = {
            'name': step_name,
            'start_time': datetime.now(),
            'success': False,
            'data': None,
            'error': None
        }
        
        try:
            result = step_function(*args, **kwargs)
            step_result['success'] = True
            step_result['data'] = result
            self.logger.info(f"✅ {step_name} completed successfully")
        except Exception as e:
            step_result['error'] = str(e)
            self.logger.error(f"❌ {step_name} failed: {e}")
            self.results['errors'].append(f"{step_name}: {e}")
            
            if self.config['validation']['fail_on_errors']:
                raise
        finally:
            step_result['end_time'] = datetime.now()
            step_result['duration'] = (step_result['end_time'] - step_result['start_time']).total_seconds()
            self.results['steps'].append(step_result)
        
        return step_result
    
    def run_full_sync(self):
        """Execute the complete synchronization process."""
        self.logger.info("\nStarting full synchronization process...")
        
        # Step 0: Create backup
        backup_path = self.create_backup()
        self.results['backup_path'] = str(backup_path) if backup_path else None
        
        # Step 1: Analyze all objects
        analysis_result = self.run_step(
            "Step 1: Analyze Objects",
            analyze_all_objects,
            self.config
        )
        
        # Step 2: Sync KPI required objects
        kpi_sync_result = self.run_step(
            "Step 2: Sync KPI Required Objects",
            sync_kpi_objects,
            self.config,
            analysis_result['data'] if analysis_result['success'] else None
        )
        
        # Step 3: Sync object metadata
        object_sync_result = self.run_step(
            "Step 3: Sync Object Metadata",
            sync_object_metadata,
            self.config,
            analysis_result['data'] if analysis_result['success'] else None
        )
        
        # Step 4: Sync UML relationships
        uml_sync_result = self.run_step(
            "Step 4: Sync UML Relationships",
            sync_uml_relationships,
            self.config
        )
        
        # Step 5: Fix formatting
        format_result = self.run_step(
            "Step 5: Fix Formatting",
            fix_all_formatting,
            self.config
        )
        
        # Step 6: Validate integrity
        validation_result = self.run_step(
            "Step 6: Validate Integrity",
            validate_system_integrity,
            self.config
        )
        
        # Step 7: Generate report
        report_result = self.run_step(
            "Step 7: Generate Report",
            generate_sync_report,
            self.config,
            self.results
        )
        
        # Finalize
        self.results['end_time'] = datetime.now()
        self.results['total_duration'] = (self.results['end_time'] - self.results['start_time']).total_seconds()
        
        self.print_summary()
        
        return self.results
    
    def print_summary(self):
        """Print synchronization summary."""
        self.logger.info("\n" + "=" * 80)
        self.logger.info("SYNCHRONIZATION SUMMARY")
        self.logger.info("=" * 80)
        
        successful_steps = sum(1 for step in self.results['steps'] if step['success'])
        total_steps = len(self.results['steps'])
        
        self.logger.info(f"Total Steps: {total_steps}")
        self.logger.info(f"Successful: {successful_steps}")
        self.logger.info(f"Failed: {total_steps - successful_steps}")
        self.logger.info(f"Errors: {len(self.results['errors'])}")
        self.logger.info(f"Warnings: {len(self.results['warnings'])}")
        self.logger.info(f"Duration: {self.results['total_duration']:.2f} seconds")
        
        if self.results['errors']:
            self.logger.error("\nErrors encountered:")
            for error in self.results['errors']:
                self.logger.error(f"  - {error}")
        
        if self.results['warnings']:
            self.logger.warning("\nWarnings:")
            for warning in self.results['warnings']:
                self.logger.warning(f"  - {warning}")
        
        self.logger.info("\n" + "=" * 80)
        
        if successful_steps == total_steps:
            self.logger.info("✅ SYNCHRONIZATION COMPLETED SUCCESSFULLY")
        else:
            self.logger.warning("⚠️  SYNCHRONIZATION COMPLETED WITH ERRORS")
        
        self.logger.info("=" * 80)

def main():
    """Main entry point."""
    try:
        orchestrator = SyncOrchestrator()
        results = orchestrator.run_full_sync()
        
        # Exit with appropriate code
        if results['errors'] and orchestrator.config['validation']['fail_on_errors']:
            sys.exit(1)
        else:
            sys.exit(0)
    
    except Exception as e:
        logging.error(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()

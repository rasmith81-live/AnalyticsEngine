
import asyncio
import logging
import uuid
import sys
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime
from pydantic import BaseModel

# Add backend services to path
backend_services_path = Path(__file__).parent.parent.parent.parent / "backend_services"
sys.path.insert(0, str(backend_services_path))

from database_service.app.messaging_client import MessagingClient

logger = logging.getLogger(__name__)

class IngestionJob(BaseModel):
    job_id: str
    connection_id: str
    target_entity: str
    schedule: str  # Cron expression or "immediate"
    status: str
    last_run: Optional[datetime] = None

class DataExtractor:
    """
    Responsible for fetching data from the Connector Service.
    """
    def __init__(self, connector_service_url: str):
        self.connector_url = connector_service_url

    async def extract_data(self, connection_id: str, query_config: Dict[str, Any]) -> List[Dict[str, Any]]:
        # In a real impl, this calls Connector Service to get a stream or batch of data
        logger.info(f"Extracting data from connection {connection_id}")
        return [{"id": 1, "data": "mock"}]

class PipelineOrchestrator:
    """
    Manages ingestion jobs and execution flow.
    """
    def __init__(self, messaging_client: Optional[MessagingClient] = None):
        self.jobs: Dict[str, IngestionJob] = {}
        self.extractor = DataExtractor("http://connector_service")
        self.messaging_client = messaging_client
        
    async def create_job(self, job: IngestionJob) -> str:
        if not job.job_id:
            job.job_id = str(uuid.uuid4())
        self.jobs[job.job_id] = job
        logger.info(f"Created ingestion job {job.job_id}")
        return job.job_id
        
    async def run_job(self, job_id: str):
        job = self.jobs.get(job_id)
        if not job:
            raise ValueError(f"Job {job_id} not found")
            
        job.status = "RUNNING"
        logger.info(f"Running job {job_id}")
        
        try:
            # 1. Extract
            data = await self.extractor.extract_data(job.connection_id, {})
            
            # 2. Transform (Transformation Engine integration would be here)
            
            # 3. Load (Publish to Ingestion Events for Database Service)
            if self.messaging_client:
                await self.messaging_client.publish_event(
                    event_type="data.ingestion.completed",
                    payload={
                        "job_id": job_id,
                        "target_entity": job.target_entity,
                        "rows_ingested": len(data),
                        "timestamp": datetime.utcnow().isoformat()
                    },
                    correlation_id=job_id
                )
                logger.info(f"Published data.ingestion.completed event for job {job_id}")
            
            job.status = "COMPLETED"
            job.last_run = datetime.utcnow()
        except Exception as e:
            job.status = "FAILED"
            logger.error(f"Job {job_id} failed: {e}")
            
        return job.status

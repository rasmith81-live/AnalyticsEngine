from fastapi import Depends
from ..core.config import settings
from ..clients.messaging import MessagingClient
from ..clients.metadata_client import MetadataServiceClient
from ..clients.calculation_client import CalculationEngineClient
from ..clients.config_client import DemoConfigServiceClient
from ..clients.connector_client import ConnectorServiceClient
from ..clients.ingestion_client import IngestionServiceClient
from ..clients.entity_resolution_client import EntityResolutionServiceClient
from ..clients.conversation_client import ConversationServiceClient
from ..clients.metadata_ingestion_client import MetadataIngestionServiceClient

def get_messaging_client() -> MessagingClient:
    return MessagingClient()

def get_metadata_client() -> MetadataServiceClient:
    service_url = settings.SERVICE_REGISTRY["business_metadata_service"]["url"]
    return MetadataServiceClient(service_url)

def get_calculation_client() -> CalculationEngineClient:
    service_url = settings.SERVICE_REGISTRY["calculation_engine_service"]["url"]
    return CalculationEngineClient(service_url)

def get_config_client() -> DemoConfigServiceClient:
    service_url = settings.SERVICE_REGISTRY["demo_config_service"]["url"]
    return DemoConfigServiceClient(service_url)

def get_connector_client() -> ConnectorServiceClient:
    service_url = settings.SERVICE_REGISTRY["connector_service"]["url"]
    return ConnectorServiceClient(service_url)

def get_ingestion_client() -> IngestionServiceClient:
    service_url = settings.SERVICE_REGISTRY["ingestion_service"]["url"]
    return IngestionServiceClient(service_url)

def get_entity_resolution_client() -> EntityResolutionServiceClient:
    service_url = settings.SERVICE_REGISTRY["entity_resolution_service"]["url"]
    return EntityResolutionServiceClient(service_url)

def get_conversation_client() -> ConversationServiceClient:
    service_url = settings.SERVICE_REGISTRY["conversation_service"]["url"]
    return ConversationServiceClient(service_url)

def get_metadata_ingestion_client() -> MetadataIngestionServiceClient:
    service_url = settings.SERVICE_REGISTRY["metadata_ingestion_service"]["url"]
    return MetadataIngestionServiceClient(service_url)

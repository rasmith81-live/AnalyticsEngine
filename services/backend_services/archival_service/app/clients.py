from app.config import settings
from app.lakehouse_client import LakehouseClient
from app.messaging_client import MessagingClient

# Initialize LakehouseClient with settings
lakehouse_client = LakehouseClient(
    storage_account=settings.storage_account,
    container_name=settings.container_name,
    connection_string=settings.storage_connection_string
)

# Initialize MessagingClient with settings
messaging_client = MessagingClient(
    redis_url=settings.redis_url,
    service_name=settings.service_name
)

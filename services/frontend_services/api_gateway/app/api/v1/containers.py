"""
Container Management API Router.

Provides endpoints for managing Docker containers (restart, rebuild).
"""

import logging
import asyncio
from typing import Optional
from fastapi import APIRouter, HTTPException, status

logger = logging.getLogger(__name__)

router = APIRouter()

# Map service names to their Docker Compose service names
SERVICE_NAME_MAP = {
    "messaging_service": "messaging_service",
    "database_service": "database_service",
    "archival_service": "archival_service",
    "observability_service": "observability_service",
    "business_metadata_service": "business_metadata",
    "calculation_engine_service": "calculation_engine_service",
    "conversation_service": "conversation_service",
    "demo_config_service": "demo_config_service",
    "connector_service": "connector_service",
    "ingestion_service": "ingestion_service",
    "entity_resolution_service": "entity_resolution_service",
    "metadata_ingestion_service": "metadata_ingestion_service",
    "systems_monitor": "systems_monitor",
    "data_simulator_service": "data_simulator_service",
    "machine_learning_service": "machine_learning_service",
    "data_governance_service": "data_governance_service",
}


async def run_docker_command(command: str) -> tuple[bool, str]:
    """
    Run a Docker Compose command asynchronously.
    
    Args:
        command: The docker-compose command to run
        
    Returns:
        Tuple of (success, output)
    """
    try:
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd="/app"  # Working directory in container
        )
        stdout, stderr = await asyncio.wait_for(process.communicate(), timeout=300)
        
        if process.returncode == 0:
            return True, stdout.decode()
        else:
            return False, stderr.decode()
    except asyncio.TimeoutError:
        return False, "Command timed out after 5 minutes"
    except Exception as e:
        return False, str(e)


@router.post("/{service_name}/restart")
async def restart_container(service_name: str):
    """
    Restart a service container.
    
    Args:
        service_name: Name of the service to restart
        
    Returns:
        Status of the restart operation
    """
    docker_service = SERVICE_NAME_MAP.get(service_name)
    if not docker_service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Unknown service: {service_name}"
        )
    
    logger.info(f"Restarting container: {docker_service}")
    
    # Use docker-compose restart
    command = f"docker-compose restart {docker_service}"
    success, output = await run_docker_command(command)
    
    if success:
        logger.info(f"Successfully restarted {docker_service}")
        return {
            "success": True,
            "service": service_name,
            "action": "restart",
            "message": f"Container {docker_service} restarted successfully"
        }
    else:
        logger.error(f"Failed to restart {docker_service}: {output}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to restart container: {output}"
        )


@router.post("/{service_name}/rebuild")
async def rebuild_container(service_name: str):
    """
    Rebuild a service container with no cache.
    
    Args:
        service_name: Name of the service to rebuild
        
    Returns:
        Status of the rebuild operation
    """
    docker_service = SERVICE_NAME_MAP.get(service_name)
    if not docker_service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Unknown service: {service_name}"
        )
    
    logger.info(f"Rebuilding container (no cache): {docker_service}")
    
    # Use docker-compose up with build and no-cache
    command = f"docker-compose up -d --build --no-cache {docker_service}"
    success, output = await run_docker_command(command)
    
    if success:
        logger.info(f"Successfully rebuilt {docker_service}")
        return {
            "success": True,
            "service": service_name,
            "action": "rebuild",
            "message": f"Container {docker_service} rebuilt successfully (no cache)"
        }
    else:
        logger.error(f"Failed to rebuild {docker_service}: {output}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to rebuild container: {output}"
        )


@router.get("/{service_name}/status")
async def get_container_status(service_name: str):
    """
    Get the status of a service container.
    
    Args:
        service_name: Name of the service
        
    Returns:
        Container status information
    """
    docker_service = SERVICE_NAME_MAP.get(service_name)
    if not docker_service:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Unknown service: {service_name}"
        )
    
    command = f"docker-compose ps --format json {docker_service}"
    success, output = await run_docker_command(command)
    
    if success:
        return {
            "success": True,
            "service": service_name,
            "status": output
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get container status: {output}"
        )

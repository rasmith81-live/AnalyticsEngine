"""
Command-line interface for the Archival Service.

This module provides CLI commands for managing the archival process,
including checking status, retrieving statistics, and triggering archival operations.
"""

import asyncio
import json
import logging
import sys
from datetime import datetime
from typing import Dict, List, Optional, Any

import click
import httpx
from pydantic import BaseModel

from .config import settings
from .management import (
    ArchivalManager,
    ArchivalStats,
    RetentionStatus,
    TableRetentionStatus,
    get_archival_manager,
    close_archival_manager
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)


class CliContext(BaseModel):
    """CLI context for sharing state between commands."""
    database_url: str
    archival_url: str
    timeout: int = 30
    manager: Optional[ArchivalManager] = None
    
    class Config:
        arbitrary_types_allowed = True


async def get_manager(ctx: CliContext) -> ArchivalManager:
    """Get or create an ArchivalManager instance.
    
    Args:
        ctx: CLI context.
        
    Returns:
        ArchivalManager: The archival manager instance.
    """
    if ctx.manager is None:
        ctx.manager = get_archival_manager(
            database_service_url=ctx.database_url,
            archival_service_url=ctx.archival_url,
            timeout=ctx.timeout
        )
    return ctx.manager


async def close_manager(ctx: CliContext):
    """Close the ArchivalManager instance.
    
    Args:
        ctx: CLI context.
    """
    if ctx.manager is not None:
        await close_archival_manager()
        ctx.manager = None


def format_json(data: Any) -> str:
    """Format data as pretty JSON.
    
    Args:
        data: Data to format.
        
    Returns:
        str: Formatted JSON string.
    """
    if isinstance(data, BaseModel):
        data = data.model_dump()
    return json.dumps(data, indent=2, default=str)


@click.group()
@click.option(
    "--database-url",
    default=settings.database_service_url,
    help="Database service URL."
)
@click.option(
    "--archival-url",
    default=f"http://{settings.host}:{settings.port}",
    help="Archival service URL."
)
@click.option(
    "--timeout",
    default=30,
    help="Request timeout in seconds."
)
@click.pass_context
def cli(ctx, database_url: str, archival_url: str, timeout: int):
    """Archival Service CLI.
    
    This CLI provides commands for managing the archival process.
    """
    ctx.obj = CliContext(
        database_url=database_url,
        archival_url=archival_url,
        timeout=timeout
    )


@cli.command("status")
@click.pass_obj
def status(ctx_obj: CliContext):
    """Get the current retention status for all hypertables."""
    async def run():
        try:
            manager = await get_manager(ctx_obj)
            retention = await manager.get_retention_status()
            click.echo(format_json(retention))
        except Exception as e:
            click.echo(f"Error: {str(e)}", err=True)
            sys.exit(1)
        finally:
            await close_manager(ctx_obj)
    
    asyncio.run(run())


@cli.command("stats")
@click.pass_obj
def stats(ctx_obj: CliContext):
    """Get statistics about the archival process."""
    async def run():
        try:
            manager = await get_manager(ctx_obj)
            stats = await manager.calculate_archival_stats()
            click.echo(format_json(stats))
        except Exception as e:
            click.echo(f"Error: {str(e)}", err=True)
            sys.exit(1)
        finally:
            await close_manager(ctx_obj)
    
    asyncio.run(run())


@cli.command("health")
@click.pass_obj
def health(ctx_obj: CliContext):
    """Get health status of both the Database Service and Archival Service."""
    async def run():
        try:
            manager = await get_manager(ctx_obj)
            health_status = await manager.get_health_status()
            click.echo(format_json(health_status))
        except Exception as e:
            click.echo(f"Error: {str(e)}", err=True)
            sys.exit(1)
        finally:
            await close_manager(ctx_obj)
    
    asyncio.run(run())


@cli.command("trigger")
@click.argument("table_name")
@click.pass_obj
def trigger(ctx_obj: CliContext, table_name: str):
    """Manually trigger archival for a specific table."""
    async def run():
        try:
            manager = await get_manager(ctx_obj)
            response = await manager.trigger_archival(table_name)
            click.echo(format_json(response))
        except Exception as e:
            click.echo(f"Error: {str(e)}", err=True)
            sys.exit(1)
        finally:
            await close_manager(ctx_obj)
    
    asyncio.run(run())


@cli.command("metrics")
@click.pass_obj
def metrics(ctx_obj: CliContext):
    """Get archival metrics from the Archival Service."""
    async def run():
        try:
            manager = await get_manager(ctx_obj)
            metrics = await manager.get_archival_metrics()
            click.echo(format_json(metrics))
        except Exception as e:
            click.echo(f"Error: {str(e)}", err=True)
            sys.exit(1)
        finally:
            await close_manager(ctx_obj)
    
    asyncio.run(run())


if __name__ == "__main__":
    cli()

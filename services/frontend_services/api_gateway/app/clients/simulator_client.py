"""Client for the Data Simulator Service."""

import httpx
from typing import Any, Dict, List, Optional
import os


SIMULATOR_SERVICE_URL = os.getenv("SIMULATOR_SERVICE_URL", "http://localhost:8007")


class SimulatorClient:
    """HTTP client for the Data Simulator Service."""
    
    def __init__(self, base_url: str = SIMULATOR_SERVICE_URL):
        self.base_url = base_url
        self.timeout = 30.0
    
    async def list_kpis(self) -> List[Dict[str, Any]]:
        """List all available KPIs."""
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(f"{self.base_url}/kpis")
            response.raise_for_status()
            return response.json()
    
    async def get_kpi(self, kpi_code: str) -> Dict[str, Any]:
        """Get a specific KPI."""
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(f"{self.base_url}/kpis/{kpi_code}")
            response.raise_for_status()
            return response.json()
    
    async def get_kpi_entities(self, kpi_code: str) -> Dict[str, Any]:
        """Get entities required for a KPI."""
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(f"{self.base_url}/kpis/{kpi_code}/entities")
            response.raise_for_status()
            return response.json()
    
    async def list_simulations(self) -> List[Dict[str, Any]]:
        """List all simulations."""
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(f"{self.base_url}/simulations")
            response.raise_for_status()
            return response.json()
    
    async def create_simulation(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new simulation."""
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(f"{self.base_url}/simulations", json=config)
            response.raise_for_status()
            return response.json()
    
    async def get_simulation(self, simulation_id: str) -> Dict[str, Any]:
        """Get a specific simulation."""
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(f"{self.base_url}/simulations/{simulation_id}")
            response.raise_for_status()
            return response.json()
    
    async def start_simulation(self, simulation_id: str) -> Dict[str, Any]:
        """Start a simulation."""
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(f"{self.base_url}/simulations/{simulation_id}/start")
            response.raise_for_status()
            return response.json()
    
    async def pause_simulation(self, simulation_id: str) -> Dict[str, Any]:
        """Pause a simulation."""
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(f"{self.base_url}/simulations/{simulation_id}/pause")
            response.raise_for_status()
            return response.json()
    
    async def resume_simulation(self, simulation_id: str) -> Dict[str, Any]:
        """Resume a simulation."""
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(f"{self.base_url}/simulations/{simulation_id}/resume")
            response.raise_for_status()
            return response.json()
    
    async def stop_simulation(self, simulation_id: str) -> Dict[str, Any]:
        """Stop a simulation."""
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.post(f"{self.base_url}/simulations/{simulation_id}/stop")
            response.raise_for_status()
            return response.json()
    
    async def delete_simulation(self, simulation_id: str) -> None:
        """Delete a simulation."""
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.delete(f"{self.base_url}/simulations/{simulation_id}")
            response.raise_for_status()
    
    async def get_simulation_ticks(
        self, 
        simulation_id: str, 
        limit: int = 100,
        offset: int = 0
    ) -> Dict[str, Any]:
        """Get simulation ticks."""
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(
                f"{self.base_url}/simulations/{simulation_id}/ticks",
                params={"limit": limit, "offset": offset}
            )
            response.raise_for_status()
            return response.json()
    
    async def get_simulation_data(
        self,
        simulation_id: str,
        entity_type: str,
        limit: int = 100
    ) -> Dict[str, Any]:
        """Get simulation entity data."""
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.get(
                f"{self.base_url}/simulations/{simulation_id}/data/{entity_type}",
                params={"limit": limit}
            )
            response.raise_for_status()
            return response.json()


simulator_client = SimulatorClient()

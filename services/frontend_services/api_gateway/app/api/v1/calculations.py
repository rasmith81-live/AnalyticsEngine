
from typing import Dict, Any
from fastapi import APIRouter, Depends
from ...clients.calculation_client import CalculationEngineClient
from ...api.dependencies import get_calculation_client

router = APIRouter()

@router.post("/calculate")
async def calculate_kpi(
    params: Dict[str, Any],
    client: CalculationEngineClient = Depends(get_calculation_client)
):
    return await client.calculate_kpi(params)

@router.post("/calculate/batch")
async def calculate_batch(
    params: Dict[str, Any],
    client: CalculationEngineClient = Depends(get_calculation_client)
):
    return await client.calculate_batch(params)

@router.post("/calculate/dashboard")
async def calculate_dashboard(
    config: Dict[str, Any],
    client: CalculationEngineClient = Depends(get_calculation_client)
):
    return await client.calculate_dashboard(config)

@router.post("/batch/schedule")
async def schedule_batch_job(
    job_config: Dict[str, Any],
    client: CalculationEngineClient = Depends(get_calculation_client)
):
    return await client.schedule_batch_job(job_config)

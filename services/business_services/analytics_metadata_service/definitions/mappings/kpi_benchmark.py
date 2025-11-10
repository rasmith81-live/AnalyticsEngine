"""
KPI to Benchmark Mappings

Defines which benchmarks belong to which KPIs.
"""

from ..kpis.registry import get_kpi
from ..benchmarks.registry import get_benchmark


KPI_BENCHMARK_MAP = {
    # Add mappings as benchmarks are created
}


def setup_kpi_benchmark_relationships():
    """Associate benchmarks with KPIs based on mappings."""
    for kpi_code, benchmark_codes in KPI_BENCHMARK_MAP.items():
        kpi = get_kpi(kpi_code)
        if kpi:
            for bench_code in benchmark_codes:
                benchmark = get_benchmark(bench_code)
                if benchmark:
                    # Store benchmark reference in KPI metadata
                    if not kpi.metadata_:
                        kpi.metadata_ = {}
                    if 'benchmarks' not in kpi.metadata_:
                        kpi.metadata_['benchmarks'] = []
                    if bench_code not in kpi.metadata_['benchmarks']:
                        kpi.metadata_['benchmarks'].append(bench_code)

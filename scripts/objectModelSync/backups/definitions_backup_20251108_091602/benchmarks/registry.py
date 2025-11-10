"""
Benchmark Registry

Automatically discovers and registers all benchmark definitions.
"""

from analytics_models import Benchmark
from ..base_registry import BaseRegistry


class BenchmarkRegistry(BaseRegistry):
    """Registry for all benchmarks."""
    
    def __init__(self):
        super().__init__(
            entity_class=Benchmark,
            module_path='definitions.benchmarks'
        )


# Create singleton instance
benchmarks = BenchmarkRegistry()


# Convenience functions
def get_benchmark(code: str) -> Benchmark:
    """Get benchmark by code."""
    return benchmarks.get(code)


def get_all_benchmarks() -> list[Benchmark]:
    """Get all benchmarks."""
    return benchmarks.get_all()


def list_benchmark_codes() -> list[str]:
    """List all benchmark codes."""
    return benchmarks.list_codes()

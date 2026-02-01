"""Statistical calculations for simulation results.

Provides confidence intervals, hypothesis testing, and
statistical analysis of simulation output.
"""

import math
import statistics
from typing import Dict, List, Optional, Tuple


class SimulationStatistics:
    """Statistical analysis utilities for simulation results."""
    
    @staticmethod
    def confidence_interval(
        data: List[float],
        confidence: float = 0.95
    ) -> Tuple[float, float]:
        """
        Calculate confidence interval for a sample.
        
        Args:
            data: Sample data
            confidence: Confidence level (default 0.95 for 95%)
            
        Returns:
            Tuple of (lower_bound, upper_bound)
        """
        if not data:
            return (0.0, 0.0)
        
        n = len(data)
        mean = statistics.mean(data)
        
        if n < 2:
            return (mean, mean)
        
        std_err = statistics.stdev(data) / math.sqrt(n)
        
        # Use t-distribution critical value approximation
        # For large n, approaches z-score
        if n >= 30:
            # Z-score for common confidence levels
            z_scores = {
                0.90: 1.645,
                0.95: 1.96,
                0.99: 2.576
            }
            z = z_scores.get(confidence, 1.96)
        else:
            # Rough t-distribution approximation for small samples
            z = 2.0 + (0.1 * (30 - n) / 30)
        
        margin = z * std_err
        return (mean - margin, mean + margin)
    
    @staticmethod
    def calculate_replication_statistics(
        replication_results: List[Dict[str, float]]
    ) -> Dict[str, Dict[str, float]]:
        """
        Calculate statistics across multiple replications.
        
        Args:
            replication_results: List of result dicts from each replication
            
        Returns:
            Dict with mean, std, ci_lower, ci_upper for each metric
        """
        if not replication_results:
            return {}
        
        # Collect values for each metric
        metrics: Dict[str, List[float]] = {}
        for result in replication_results:
            for key, value in result.items():
                if isinstance(value, (int, float)):
                    if key not in metrics:
                        metrics[key] = []
                    metrics[key].append(float(value))
        
        # Calculate statistics for each metric
        stats = {}
        for metric, values in metrics.items():
            if values:
                mean = statistics.mean(values)
                std = statistics.stdev(values) if len(values) > 1 else 0
                ci = SimulationStatistics.confidence_interval(values)
                
                stats[metric] = {
                    "mean": mean,
                    "std": std,
                    "ci_lower": ci[0],
                    "ci_upper": ci[1],
                    "min": min(values),
                    "max": max(values),
                    "n": len(values)
                }
        
        return stats
    
    @staticmethod
    def compare_scenarios(
        baseline_results: List[float],
        scenario_results: List[float],
        alpha: float = 0.05
    ) -> Dict[str, any]:
        """
        Compare two scenarios using statistical tests.
        
        Args:
            baseline_results: Results from baseline scenario
            scenario_results: Results from comparison scenario
            alpha: Significance level
            
        Returns:
            Dict with comparison results including p-value and significance
        """
        if not baseline_results or not scenario_results:
            return {"error": "Insufficient data"}
        
        baseline_mean = statistics.mean(baseline_results)
        scenario_mean = statistics.mean(scenario_results)
        
        # Calculate difference
        difference = scenario_mean - baseline_mean
        percent_change = (difference / baseline_mean * 100) if baseline_mean != 0 else 0
        
        # Pooled standard error (simplified)
        n1, n2 = len(baseline_results), len(scenario_results)
        if n1 > 1 and n2 > 1:
            s1 = statistics.stdev(baseline_results)
            s2 = statistics.stdev(scenario_results)
            pooled_se = math.sqrt((s1**2 / n1) + (s2**2 / n2))
            
            # t-statistic
            t_stat = difference / pooled_se if pooled_se > 0 else 0
            
            # Approximate p-value (two-tailed)
            # Using normal approximation for simplicity
            p_value = 2 * (1 - SimulationStatistics._normal_cdf(abs(t_stat)))
        else:
            t_stat = 0
            p_value = 1.0
        
        return {
            "baseline_mean": baseline_mean,
            "scenario_mean": scenario_mean,
            "difference": difference,
            "percent_change": percent_change,
            "t_statistic": t_stat,
            "p_value": p_value,
            "significant": p_value < alpha,
            "alpha": alpha
        }
    
    @staticmethod
    def _normal_cdf(x: float) -> float:
        """Approximate cumulative distribution function for standard normal."""
        # Approximation using error function
        return 0.5 * (1 + math.erf(x / math.sqrt(2)))
    
    @staticmethod
    def calculate_utilization(
        busy_time: float,
        total_time: float,
        capacity: int = 1
    ) -> float:
        """
        Calculate resource utilization.
        
        Args:
            busy_time: Total time resource was busy
            total_time: Total simulation time
            capacity: Resource capacity
            
        Returns:
            Utilization percentage (0-100)
        """
        if total_time <= 0 or capacity <= 0:
            return 0.0
        
        return min(100.0, (busy_time / (total_time * capacity)) * 100)
    
    @staticmethod
    def detect_bottleneck(
        utilizations: Dict[str, float],
        threshold: float = 80.0
    ) -> List[str]:
        """
        Detect bottleneck resources based on utilization.
        
        Args:
            utilizations: Dict of resource_id -> utilization %
            threshold: Utilization threshold for bottleneck detection
            
        Returns:
            List of resource IDs identified as bottlenecks
        """
        bottlenecks = [
            resource_id
            for resource_id, util in utilizations.items()
            if util >= threshold
        ]
        return sorted(bottlenecks, key=lambda r: utilizations[r], reverse=True)
    
    @staticmethod
    def little_law_validation(
        avg_wip: float,
        throughput: float,
        avg_cycle_time: float,
        tolerance: float = 0.1
    ) -> Dict[str, any]:
        """
        Validate simulation using Little's Law: L = λW
        
        Args:
            avg_wip: Average work in process
            throughput: Average throughput (λ)
            avg_cycle_time: Average cycle time (W)
            tolerance: Acceptable deviation
            
        Returns:
            Validation result
        """
        expected_wip = throughput * avg_cycle_time
        deviation = abs(avg_wip - expected_wip) / expected_wip if expected_wip > 0 else 0
        
        return {
            "observed_wip": avg_wip,
            "expected_wip": expected_wip,
            "deviation": deviation,
            "valid": deviation <= tolerance,
            "tolerance": tolerance
        }

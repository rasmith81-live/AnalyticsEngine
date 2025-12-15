from typing import Dict, List, Set, Optional
import logging

logger = logging.getLogger(__name__)

class DependencyGraph:
    """
    Manages dependencies between metrics to determine calculation order.
    """
    def __init__(self):
        # Adjacency list: metric -> list of metrics it depends on
        self.dependencies: Dict[str, Set[str]] = {}
    
    def add_dependency(self, metric: str, depends_on: str):
        """
        Record that 'metric' depends on 'depends_on'.
        """
        if metric not in self.dependencies:
            self.dependencies[metric] = set()
        self.dependencies[metric].add(depends_on)
        
        # Ensure the dependency exists as a key too
        if depends_on not in self.dependencies:
            self.dependencies[depends_on] = set()

    def add_metrics(self, metrics: List[str]):
        """Ensure metrics exist in the graph even if they have no dependencies."""
        for m in metrics:
            if m not in self.dependencies:
                self.dependencies[m] = set()

    def get_calculation_order(self, target_metrics: List[str]) -> List[List[str]]:
        """
        Determine the topological order of calculation layers.
        
        Args:
            target_metrics: List of metrics we want to calculate.
            
        Returns:
            List of sets (layers), where each layer can be calculated in parallel.
            [[independent_metrics], [dependent_layer_1], [dependent_layer_2], ...]
        """
        # Filter graph to only relevant nodes (subgraph)
        relevant_nodes = self._get_relevant_subgraph(target_metrics)
        
        # Topological sort with layering
        # Calculate in-degrees for the relevant subgraph
        in_degree = {node: 0 for node in relevant_nodes}
        for node in relevant_nodes:
            for dep in self.dependencies.get(node, []):
                if dep in relevant_nodes:
                    # Note: self.dependencies is "depends on", so the edge is dep -> node
                    in_degree[node] += 1
        
        # Queue of nodes with 0 in-degree (dependencies satisfied)
        queue = [node for node in relevant_nodes if in_degree[node] == 0]
        
        layers = []
        
        while queue:
            layers.append(queue)
            next_queue = []
            
            for node in queue:
                # Find nodes that depend on this node
                # Since we store 'depends on', we need to scan or iterate
                # This is inefficient for reverse lookup, ideally we'd build the reverse graph too
                # But for now, we iterate through relevant nodes
                for candidate in relevant_nodes:
                    if node in self.dependencies.get(candidate, []):
                        in_degree[candidate] -= 1
                        if in_degree[candidate] == 0:
                            next_queue.append(candidate)
            
            queue = next_queue
            
        # Check for cycles / unvisited nodes
        visited_count = sum(len(layer) for layer in layers)
        if visited_count < len(relevant_nodes):
            raise ValueError("Circular dependency detected or dependencies missing in subgraph")
            
        return layers

    def _get_relevant_subgraph(self, targets: List[str]) -> Set[str]:
        """Identify all metrics needed to calculate targets (transitive closure)."""
        needed = set()
        stack = list(targets)
        
        while stack:
            node = stack.pop()
            if node in needed:
                continue
            needed.add(node)
            
            # Add dependencies of this node to stack
            deps = self.dependencies.get(node, set())
            for dep in deps:
                if dep not in needed:
                    stack.append(dep)
        
        return needed


import logging
from typing import List, Dict, Optional, Set
from ..models import LineageGraph, LineageNode, LineageEdge, NodeType

logger = logging.getLogger(__name__)

class LineageEngine:
    """
    Engine for managing and querying data lineage graph.
    """
    
    def __init__(self):
        # In-memory store for graph (replace with graph DB or relational tables in prod)
        self.nodes: Dict[str, LineageNode] = {}
        self.edges: List[LineageEdge] = []

    def add_node(self, node: LineageNode):
        """Add or update a node in the lineage graph."""
        self.nodes[node.id] = node
        logger.info(f"Added lineage node: {node.name} ({node.type})")

    def add_edge(self, edge: LineageEdge):
        """Add a directed edge representing data flow."""
        # Warn if nodes don't exist (soft validation)
        if edge.source_id not in self.nodes:
            logger.warning(f"Source node {edge.source_id} not found for edge.")
        if edge.target_id not in self.nodes:
            logger.warning(f"Target node {edge.target_id} not found for edge.")
            
        self.edges.append(edge)
        logger.info(f"Added lineage edge: {edge.source_id} -> {edge.target_id}")

    def get_upstream_lineage(self, node_id: str, depth: int = 5) -> LineageGraph:
        """
        Get all upstream nodes (sources) for a given node.
        Trace back where data comes FROM.
        """
        result_nodes = {} # id -> Node
        result_edges = []
        
        current_level_ids = {node_id}
        
        # If starting node exists, add it
        if node_id in self.nodes:
            result_nodes[node_id] = self.nodes[node_id]
        
        for _ in range(depth):
            if not current_level_ids:
                break
                
            next_level_ids = set()
            
            # Find edges where TARGET is in current level (flowing TO current)
            for edge in self.edges:
                if edge.target_id in current_level_ids:
                    result_edges.append(edge)
                    
                    if edge.source_id in self.nodes:
                        result_nodes[edge.source_id] = self.nodes[edge.source_id]
                        next_level_ids.add(edge.source_id)
            
            current_level_ids = next_level_ids
            
        return LineageGraph(nodes=list(result_nodes.values()), edges=result_edges)

    def get_downstream_lineage(self, node_id: str, depth: int = 5) -> LineageGraph:
        """
        Get all downstream nodes (consumers) for a given node.
        Trace where data goes TO.
        """
        result_nodes = {}
        result_edges = []
        
        current_level_ids = {node_id}
        
        # If starting node exists, add it
        if node_id in self.nodes:
            result_nodes[node_id] = self.nodes[node_id]
        
        for _ in range(depth):
            if not current_level_ids:
                break
                
            next_level_ids = set()
            
            # Find edges where SOURCE is in current level (flowing FROM current)
            for edge in self.edges:
                if edge.source_id in current_level_ids:
                    result_edges.append(edge)
                    
                    if edge.target_id in self.nodes:
                        result_nodes[edge.target_id] = self.nodes[edge.target_id]
                        next_level_ids.add(edge.target_id)
            
            current_level_ids = next_level_ids

        return LineageGraph(nodes=list(result_nodes.values()), edges=result_edges)

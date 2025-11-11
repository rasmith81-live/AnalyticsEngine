/**
 * ObjectModelDiagram Component
 * Visualizes object model relationships as a network graph
 */

import { Box, Paper, Typography, Chip, Alert, Tooltip } from '@mui/material';
import { useEffect, useRef, useState } from 'react';
import { parsePlantUML, getGraphStats, type ParsedSchema } from '../utils/plantUmlParser';

interface ObjectModelDiagramProps {
  schemaDefinition: string;
  highlightEntity?: string;
  onEntityClick?: (entityName: string) => void;
}

interface Node {
  id: string;
  x: number;
  y: number;
  vx: number;
  vy: number;
}

interface Link {
  source: string;
  target: string;
  label?: string;
}

export default function ObjectModelDiagram({
  schemaDefinition,
  highlightEntity,
  onEntityClick,
}: ObjectModelDiagramProps) {
  const svgRef = useRef<SVGSVGElement>(null);
  const [schema, setSchema] = useState<ParsedSchema>({ entities: [], relationships: [] });
  const [nodes, setNodes] = useState<Node[]>([]);
  const [links, setLinks] = useState<Link[]>([]);
  const [hoveredNode, setHoveredNode] = useState<string | null>(null);

  // Parse schema on mount or when definition changes
  useEffect(() => {
    if (!schemaDefinition) return;
    
    const parsed = parsePlantUML(schemaDefinition);
    setSchema(parsed);

    // Initialize nodes with simple circular layout
    const nodeCount = parsed.entities.length;
    const radius = Math.min(200, 50 + nodeCount * 10);
    const centerX = 300;
    const centerY = 200;

    const initialNodes: Node[] = parsed.entities.map((entity, i) => {
      const angle = (i / nodeCount) * 2 * Math.PI;
      return {
        id: entity.name,
        x: centerX + radius * Math.cos(angle),
        y: centerY + radius * Math.sin(angle),
        vx: 0,
        vy: 0,
      };
    });

    setNodes(initialNodes);

    // Create links
    const initialLinks: Link[] = parsed.relationships.map(rel => ({
      source: rel.from,
      target: rel.to,
      label: rel.label,
    }));

    setLinks(initialLinks);
  }, [schemaDefinition]);

  // Simple force simulation (very basic)
  useEffect(() => {
    if (nodes.length === 0) return;

    const interval = setInterval(() => {
      setNodes(prevNodes => {
        const newNodes = [...prevNodes];
        
        // Apply forces
        newNodes.forEach((node, i) => {
          // Repulsion between nodes
          newNodes.forEach((other, j) => {
            if (i === j) return;
            const dx = node.x - other.x;
            const dy = node.y - other.y;
            const dist = Math.sqrt(dx * dx + dy * dy) || 1;
            const force = 500 / (dist * dist);
            node.vx += (dx / dist) * force;
            node.vy += (dy / dist) * force;
          });

          // Attraction along links
          links.forEach(link => {
            if (link.source === node.id) {
              const target = newNodes.find(n => n.id === link.target);
              if (target) {
                const dx = target.x - node.x;
                const dy = target.y - node.y;
                const dist = Math.sqrt(dx * dx + dy * dy) || 1;
                const force = dist * 0.01;
                node.vx += (dx / dist) * force;
                node.vy += (dy / dist) * force;
              }
            }
          });

          // Center gravity
          const centerX = 300;
          const centerY = 200;
          node.vx += (centerX - node.x) * 0.001;
          node.vy += (centerY - node.y) * 0.001;

          // Damping
          node.vx *= 0.8;
          node.vy *= 0.8;

          // Update position
          node.x += node.vx;
          node.y += node.vy;

          // Bounds
          node.x = Math.max(50, Math.min(550, node.x));
          node.y = Math.max(50, Math.min(350, node.y));
        });

        return newNodes;
      });
    }, 50);

    // Stop after 3 seconds
    const timeout = setTimeout(() => clearInterval(interval), 3000);

    return () => {
      clearInterval(interval);
      clearTimeout(timeout);
    };
  }, [links]);

  if (!schemaDefinition) {
    return (
      <Alert severity="info">
        No schema definition available for this object model.
      </Alert>
    );
  }

  if (schema.entities.length === 0) {
    return (
      <Alert severity="warning">
        Unable to parse schema definition. The schema may be empty or in an unsupported format.
      </Alert>
    );
  }

  const stats = getGraphStats(schema);

  return (
    <Paper elevation={1} sx={{ p: 2 }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
        <Typography variant="subtitle2" color="text.secondary">
          Relationship Diagram
        </Typography>
        <Box sx={{ display: 'flex', gap: 1 }}>
          <Chip label={`${stats.entityCount} Entities`} size="small" />
          <Chip label={`${stats.relationshipCount} Relationships`} size="small" color="primary" />
        </Box>
      </Box>

      <Box sx={{ bgcolor: 'grey.50', borderRadius: 1, overflow: 'hidden' }}>
        <svg
          ref={svgRef}
          width="600"
          height="400"
          viewBox="0 0 600 400"
          style={{ display: 'block' }}
        >
          {/* Links */}
          <g>
            {links.map((link, i) => {
              const sourceNode = nodes.find(n => n.id === link.source);
              const targetNode = nodes.find(n => n.id === link.target);
              if (!sourceNode || !targetNode) return null;

              const isHighlighted =
                highlightEntity === link.source || highlightEntity === link.target;

              return (
                <line
                  key={i}
                  x1={sourceNode.x}
                  y1={sourceNode.y}
                  x2={targetNode.x}
                  y2={targetNode.y}
                  stroke={isHighlighted ? '#1976d2' : '#ccc'}
                  strokeWidth={isHighlighted ? 2 : 1}
                  opacity={isHighlighted ? 1 : 0.6}
                />
              );
            })}
          </g>

          {/* Nodes */}
          <g>
            {nodes.map(node => {
              const isHighlighted = highlightEntity === node.id;
              const isHovered = hoveredNode === node.id;
              const isConnected = links.some(
                link =>
                  (link.source === highlightEntity && link.target === node.id) ||
                  (link.target === highlightEntity && link.source === node.id)
              );

              return (
                <g key={node.id}>
                  <Tooltip title={node.id} arrow>
                    <circle
                      cx={node.x}
                      cy={node.y}
                      r={isHighlighted ? 12 : isHovered ? 10 : 8}
                      fill={isHighlighted ? '#1976d2' : isConnected ? '#42a5f5' : '#64b5f6'}
                      stroke={isHighlighted ? '#0d47a1' : '#fff'}
                      strokeWidth={2}
                      style={{ cursor: 'pointer' }}
                      onMouseEnter={() => setHoveredNode(node.id)}
                      onMouseLeave={() => setHoveredNode(null)}
                      onClick={() => onEntityClick?.(node.id)}
                    />
                  </Tooltip>
                  <text
                    x={node.x}
                    y={node.y + 20}
                    textAnchor="middle"
                    fontSize="10"
                    fill="#666"
                    style={{ pointerEvents: 'none', userSelect: 'none' }}
                  >
                    {node.id.length > 12 ? node.id.substring(0, 10) + '...' : node.id}
                  </text>
                </g>
              );
            })}
          </g>
        </svg>
      </Box>

      {/* Stats */}
      <Box sx={{ mt: 2, display: 'flex', gap: 1, flexWrap: 'wrap' }}>
        <Typography variant="caption" color="text.secondary">
          Most Connected:
        </Typography>
        {stats.mostConnected.slice(0, 3).map(({ name, degree }) => (
          <Chip
            key={name}
            label={`${name} (${degree})`}
            size="small"
            variant="outlined"
            onClick={() => onEntityClick?.(name)}
          />
        ))}
      </Box>
    </Paper>
  );
}

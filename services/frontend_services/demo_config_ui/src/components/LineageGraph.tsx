import React from 'react';
import ReactFlow, {
  Node,
  Edge,
  Controls,
  Background,
  useNodesState,
  useEdgesState,
  MarkerType,
  ConnectionLineType,
} from 'react-flow-renderer';
import { Box, Typography, useTheme } from '@mui/material';
import { LineageGraph as ILineageGraph, LineageNode } from '../api/governanceApi';

interface LineageGraphProps {
  data: ILineageGraph;
}

const getNodeColor = (type: LineageNode['type']) => {
  switch (type) {
    case 'source': return '#e0e0e0'; // Grey
    case 'ingestion': return '#ffcc80'; // Orange
    case 'process': return '#90caf9'; // Blue
    case 'model': return '#ce93d8'; // Purple
    case 'kpi': return '#a5d6a7'; // Green
    default: return '#eeeeee';
  }
};

const LineageGraph: React.FC<LineageGraphProps> = ({ data }) => {
  const theme = useTheme();

  // Transform API data to React Flow format
  const initialNodes: Node[] = data.nodes.map((node, index) => ({
    id: node.id,
    type: 'default', // Using default for now, could be custom
    data: { label: node.label },
    position: { x: index * 250, y: 100 + (index % 2) * 50 }, // Simple auto-layout
    style: { 
      background: getNodeColor(node.type),
      width: 180,
      border: '1px solid #777',
      borderRadius: '4px',
      fontSize: '12px'
    },
  }));

  const initialEdges: Edge[] = data.edges.map((edge, index) => ({
    id: `e${index}`,
    source: edge.from,
    target: edge.to,
    type: 'smoothstep',
    animated: true,
    style: { stroke: theme.palette.text.secondary },
    markerEnd: {
      type: MarkerType.ArrowClosed,
      color: theme.palette.text.secondary,
    },
  }));

  const [nodes, , onNodesChange] = useNodesState(initialNodes);
  const [edges, , onEdgesChange] = useEdgesState(initialEdges);

  // Re-calculate layout if data changes (simplified)
  React.useEffect(() => {
    // In a real app, we might use dagre for layouting
  }, [data]);

  return (
    <Box sx={{ height: 500, width: '100%', border: '1px solid #ddd', borderRadius: 1 }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        fitView
        attributionPosition="bottom-right"
        connectionLineType={ConnectionLineType.SmoothStep}
      >
        <Controls />
        <Background color="#aaa" gap={16} />
      </ReactFlow>
      <Box sx={{ p: 1, display: 'flex', gap: 2, justifyContent: 'center', borderTop: '1px solid #ddd' }}>
        <LegendItem color="#e0e0e0" label="Source" />
        <LegendItem color="#ffcc80" label="Ingestion" />
        <LegendItem color="#90caf9" label="Process" />
        <LegendItem color="#ce93d8" label="Model" />
        <LegendItem color="#a5d6a7" label="KPI" />
      </Box>
    </Box>
  );
};

const LegendItem = ({ color, label }: { color: string; label: string }) => (
  <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
    <Box sx={{ width: 12, height: 12, borderRadius: '50%', bgcolor: color, border: '1px solid #999' }} />
    <Typography variant="caption">{label}</Typography>
  </Box>
);

export default LineageGraph;

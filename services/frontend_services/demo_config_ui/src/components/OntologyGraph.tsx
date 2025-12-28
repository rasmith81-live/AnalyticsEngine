import { useRef, useCallback, useEffect, useState } from 'react';
import ForceGraph2D from 'react-force-graph-2d';
import { 
  Box, Paper, Typography, Chip, Stack, IconButton, Tooltip, 
  FormControl, InputLabel, Select, MenuItem, Menu, ListItemIcon, ListItemText,
  Dialog, DialogTitle, DialogContent, DialogActions, Button, TextField,
  SelectChangeEvent, Slider
} from '@mui/material';
import {
  ZoomIn as ZoomInIcon,
  ZoomOut as ZoomOutIcon,
  CenterFocusStrong as CenterIcon,
  Add as AddIcon,
  Edit as EditIcon,
  Delete as DeleteIcon,
  Link as LinkIcon
} from '@mui/icons-material';

// Node types and their styling (Neo4j-inspired)
const NODE_STYLES: Record<string, { color: string; size: number; label: string }> = {
  ValueChain: { color: '#F79767', size: 20, label: 'Value Chain' },
  Module: { color: '#DA7194', size: 15, label: 'Module' },
  KPI: { color: '#4C8EDA', size: 10, label: 'KPI' },
  ObjectModel: { color: '#6DCE9E', size: 10, label: 'Object Model' }
};

// Relationship types and their styling
const LINK_STYLES: Record<string, { color: string; width: number }> = {
  BELONGS_TO: { color: '#F79767', width: 2 },
  CONTAINS: { color: '#959AA1', width: 2 },
  HAS_KPI: { color: '#4C8EDA', width: 1.5 },
  USES: { color: '#6DCE9E', width: 1.5 },
  RELATES_TO: { color: '#B8B8B8', width: 1 }
};

// Helper functions for color manipulation
function lightenColor(color: string, percent: number): string {
  const num = parseInt(color.replace('#', ''), 16);
  const amt = Math.round(2.55 * percent);
  const R = Math.min(255, (num >> 16) + amt);
  const G = Math.min(255, ((num >> 8) & 0x00FF) + amt);
  const B = Math.min(255, (num & 0x0000FF) + amt);
  return `#${(0x1000000 + R * 0x10000 + G * 0x100 + B).toString(16).slice(1)}`;
}

function darkenColor(color: string, percent: number): string {
  const num = parseInt(color.replace('#', ''), 16);
  const amt = Math.round(2.55 * percent);
  const R = Math.max(0, (num >> 16) - amt);
  const G = Math.max(0, ((num >> 8) & 0x00FF) - amt);
  const B = Math.max(0, (num & 0x0000FF) - amt);
  return `#${(0x1000000 + R * 0x10000 + G * 0x100 + B).toString(16).slice(1)}`;
}

export interface GraphNode {
  id: string;
  name: string;
  type: 'ValueChain' | 'Module' | 'KPI' | 'ObjectModel';
  description?: string;
  code?: string;
  x?: number;
  y?: number;
  fx?: number;
  fy?: number;
}

export interface GraphLink {
  source: string | GraphNode;
  target: string | GraphNode;
  type: string;
}

export interface GraphData {
  nodes: GraphNode[];
  links: GraphLink[];
}

interface OntologyGraphProps {
  data: GraphData;
  width?: number;
  height?: number;
  valueChains?: { code: string; name: string }[];
  selectedValueChain?: string;
  onValueChainChange?: (code: string) => void;
  onNodeClick?: (node: GraphNode) => void;
  onNodeAdd?: (type: GraphNode['type']) => void;
  onNodeEdit?: (node: GraphNode) => void;
  onNodeDelete?: (node: GraphNode) => void;
  onLinkAdd?: (source: GraphNode, target: GraphNode, type: string) => void;
  onLinkDelete?: (link: GraphLink) => void;
}

export default function OntologyGraph({ 
  data, 
  width = 800, 
  height = 600,
  valueChains = [],
  selectedValueChain = '',
  onValueChainChange,
  onNodeClick,
  onNodeAdd,
  onNodeEdit,
  onNodeDelete,
  onLinkAdd
}: OntologyGraphProps) {
  const graphRef = useRef<any>();
  const [selectedNode, setSelectedNode] = useState<GraphNode | null>(null);
  const [hoveredNode, setHoveredNode] = useState<GraphNode | null>(null);
  
  // Context menu state
  const [contextMenu, setContextMenu] = useState<{ x: number; y: number; node?: GraphNode; link?: GraphLink } | null>(null);
  
  // Add node dialog state
  const [addNodeDialog, setAddNodeDialog] = useState<{ open: boolean; type: GraphNode['type'] }>({ open: false, type: 'Module' });
  const [newNodeForm, setNewNodeForm] = useState({ code: '', name: '', description: '' });
  
  // Add link dialog state
  const [addLinkDialog, setAddLinkDialog] = useState<{ open: boolean; sourceNode?: GraphNode }>({ open: false });
  const [newLinkForm, setNewLinkForm] = useState({ targetId: '', type: 'CONTAINS' });
  
  // Link distance state for edge length control
  const [linkDistance, setLinkDistance] = useState<number>(100);
  
  // Font size state for node labels
  const [labelFontSize, setLabelFontSize] = useState<number>(12);

  // Center graph on mount
  useEffect(() => {
    if (graphRef.current && data.nodes.length > 0) {
      setTimeout(() => {
        graphRef.current?.zoomToFit(400, 50);
      }, 500);
    }
  }, [data]);

  // Apply link distance when it changes
  useEffect(() => {
    if (graphRef.current) {
      const linkForce = graphRef.current.d3Force('link');
      if (linkForce) {
        linkForce.distance(linkDistance);
        graphRef.current.d3ReheatSimulation();
      }
    }
  }, [linkDistance]);

  // Handle node click
  const handleNodeClick = useCallback((node: any) => {
    setSelectedNode(node as GraphNode);
    if (onNodeClick) {
      onNodeClick(node as GraphNode);
    }
  }, [onNodeClick]);

  // Custom node rendering - Neo4j style circles with labels
  const nodeCanvasObject = useCallback((node: any, ctx: CanvasRenderingContext2D, globalScale: number) => {
    // Guard against undefined coordinates during initial render
    if (node.x === undefined || node.y === undefined || !isFinite(node.x) || !isFinite(node.y)) {
      return;
    }
    
    const style = NODE_STYLES[node.type] || NODE_STYLES.ObjectModel;
    const size = style.size;
    const isSelected = selectedNode?.id === node.id;
    const isHovered = hoveredNode?.id === node.id;
    
    // Draw node circle with gradient for 3D effect
    ctx.beginPath();
    ctx.arc(node.x, node.y, size, 0, 2 * Math.PI);
    
    const gradient = ctx.createRadialGradient(
      node.x - size / 3, node.y - size / 3, 0,
      node.x, node.y, size
    );
    gradient.addColorStop(0, lightenColor(style.color, 30));
    gradient.addColorStop(1, style.color);
    ctx.fillStyle = gradient;
    ctx.fill();
    
    // Border
    ctx.strokeStyle = isSelected ? '#FFD700' : isHovered ? '#FFFFFF' : darkenColor(style.color, 20);
    ctx.lineWidth = isSelected ? 3 : isHovered ? 2 : 1;
    ctx.stroke();
    
    // Draw label below node
    const label = node.name || node.id;
    const fontSize = Math.max(labelFontSize / globalScale, 4);
    ctx.font = `${fontSize}px Sans-Serif`;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    
    const textWidth = ctx.measureText(label).width;
    const labelY = node.y + size + fontSize;
    
    // Label background
    ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
    ctx.fillRect(
      node.x - textWidth / 2 - 2,
      labelY - fontSize / 2 - 1,
      textWidth + 4,
      fontSize + 2
    );
    
    // Label text
    ctx.fillStyle = '#FFFFFF';
    ctx.fillText(label, node.x, labelY);
  }, [selectedNode, hoveredNode, labelFontSize]);

  // Zoom controls
  const handleZoomIn = () => graphRef.current?.zoom(graphRef.current.zoom() * 1.3, 300);
  const handleZoomOut = () => graphRef.current?.zoom(graphRef.current.zoom() / 1.3, 300);
  const handleCenter = () => graphRef.current?.zoomToFit(400, 50);

  // Handle right-click context menu
  const handleNodeRightClick = useCallback((node: any, event: MouseEvent) => {
    event.preventDefault();
    setContextMenu({ x: event.clientX, y: event.clientY, node: node as GraphNode });
  }, []);

  const handleCloseContextMenu = () => setContextMenu(null);

  // Handle value chain filter change
  const handleFilterChange = (event: SelectChangeEvent<string>) => {
    if (onValueChainChange) {
      onValueChainChange(event.target.value);
    }
  };

  return (
    <Box sx={{ position: 'relative' }}>
      {/* Filter and Legend Panel */}
      <Paper sx={{ position: 'absolute', top: 8, left: 8, p: 1.5, zIndex: 10, backgroundColor: 'rgba(255,255,255,0.95)', minWidth: 180 }}>
        {/* Value Chain Filter */}
        {valueChains.length > 0 && (
          <FormControl size="small" fullWidth sx={{ mb: 1.5 }}>
            <InputLabel id="vc-filter-label">Filter by Value Chain</InputLabel>
            <Select
              labelId="vc-filter-label"
              value={selectedValueChain}
              label="Filter by Value Chain"
              onChange={handleFilterChange}
            >
              <MenuItem value=""><em>All Value Chains</em></MenuItem>
              {valueChains.map(vc => (
                <MenuItem key={vc.code} value={vc.code}>{vc.name}</MenuItem>
              ))}
            </Select>
          </FormControl>
        )}
        
        {/* Legend */}
        <Typography variant="caption" sx={{ fontWeight: 'bold', display: 'block', mb: 0.5 }}>Legend</Typography>
        <Stack direction="column" spacing={0.5} sx={{ mb: 2 }}>
          {Object.entries(NODE_STYLES).map(([type, style]) => (
            <Stack key={type} direction="row" alignItems="center" spacing={1}>
              <Box sx={{ 
                width: 12, 
                height: 12, 
                borderRadius: '50%', 
                backgroundColor: style.color,
                border: `1px solid ${darkenColor(style.color, 20)}`
              }} />
              <Typography variant="caption">{style.label}</Typography>
            </Stack>
          ))}
        </Stack>
        
        {/* Edge Length Slider */}
        <Typography variant="caption" sx={{ fontWeight: 'bold', display: 'block', mb: 0.5 }}>Edge Length: {linkDistance}px</Typography>
        <Slider
          size="small"
          value={linkDistance}
          onChange={(_, value) => setLinkDistance(value as number)}
          min={30}
          max={300}
          step={10}
          valueLabelDisplay="auto"
          sx={{ mb: 2 }}
        />
        
        {/* Font Size Slider */}
        <Typography variant="caption" sx={{ fontWeight: 'bold', display: 'block', mb: 0.5 }}>Label Size: {labelFontSize}px</Typography>
        <Slider
          size="small"
          value={labelFontSize}
          onChange={(_, value) => setLabelFontSize(value as number)}
          min={6}
          max={24}
          step={1}
          valueLabelDisplay="auto"
        />
      </Paper>

      {/* Zoom Controls and Add Button */}
      <Paper sx={{ position: 'absolute', top: 8, right: 8, zIndex: 10, display: 'flex', flexDirection: 'column' }}>
        <Tooltip title="Zoom In" placement="left">
          <IconButton size="small" onClick={handleZoomIn}><ZoomInIcon /></IconButton>
        </Tooltip>
        <Tooltip title="Zoom Out" placement="left">
          <IconButton size="small" onClick={handleZoomOut}><ZoomOutIcon /></IconButton>
        </Tooltip>
        <Tooltip title="Fit to View" placement="left">
          <IconButton size="small" onClick={handleCenter}><CenterIcon /></IconButton>
        </Tooltip>
        {onNodeAdd && (
          <Tooltip title="Add Node" placement="left">
            <IconButton size="small" onClick={() => setAddNodeDialog({ open: true, type: 'Module' })} color="primary">
              <AddIcon />
            </IconButton>
          </Tooltip>
        )}
      </Paper>

      {/* Selected Node Info */}
      {selectedNode && (
        <Paper sx={{ position: 'absolute', bottom: 8, left: 8, p: 1.5, zIndex: 10, maxWidth: 300, backgroundColor: 'rgba(255,255,255,0.95)' }}>
          <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 0.5 }}>
            <Stack direction="row" alignItems="center" spacing={1}>
              <Box sx={{ 
                width: 16, 
                height: 16, 
                borderRadius: '50%', 
                backgroundColor: NODE_STYLES[selectedNode.type]?.color || '#888'
              }} />
              <Typography variant="subtitle2">{selectedNode.name}</Typography>
            </Stack>
            <Stack direction="row" spacing={0.5}>
              {onNodeEdit && (
                <IconButton size="small" onClick={() => onNodeEdit(selectedNode)} title="Edit">
                  <EditIcon fontSize="small" />
                </IconButton>
              )}
              {onNodeDelete && (
                <IconButton size="small" onClick={() => onNodeDelete(selectedNode)} color="error" title="Delete">
                  <DeleteIcon fontSize="small" />
                </IconButton>
              )}
            </Stack>
          </Stack>
          <Chip label={selectedNode.type} size="small" sx={{ mb: 0.5 }} />
          {selectedNode.code && (
            <Typography variant="caption" display="block" color="text.secondary">
              Code: {selectedNode.code}
            </Typography>
          )}
          {selectedNode.description && (
            <Typography variant="caption" display="block" color="text.secondary" sx={{ mt: 0.5 }}>
              {selectedNode.description}
            </Typography>
          )}
          {onLinkAdd && (
            <Button 
              size="small" 
              startIcon={<LinkIcon />} 
              sx={{ mt: 1 }}
              onClick={() => setAddLinkDialog({ open: true, sourceNode: selectedNode })}
            >
              Add Relationship
            </Button>
          )}
        </Paper>
      )}

      {/* Graph */}
      <ForceGraph2D
        ref={graphRef}
        graphData={data}
        width={width}
        height={height}
        nodeCanvasObject={nodeCanvasObject}
        nodeCanvasObjectMode={() => 'replace'}
        nodePointerAreaPaint={(node: any, color, ctx) => {
          const size = NODE_STYLES[node.type]?.size || 10;
          ctx.fillStyle = color;
          ctx.beginPath();
          ctx.arc(node.x, node.y, size + 5, 0, 2 * Math.PI);
          ctx.fill();
        }}
        linkColor={(link: any) => LINK_STYLES[link.type]?.color || '#B8B8B8'}
        linkWidth={(link: any) => LINK_STYLES[link.type]?.width || 1}
        linkDirectionalArrowLength={6}
        linkDirectionalArrowRelPos={1}
        onNodeClick={handleNodeClick}
        onNodeRightClick={handleNodeRightClick}
        onNodeHover={(node: any) => setHoveredNode(node as GraphNode | null)}
        onNodeDragEnd={(node: any) => {
          // Fix node position after drag - persists in current session
          node.fx = node.x;
          node.fy = node.y;
        }}
        enableNodeDrag={true}
        cooldownTicks={100}
        d3AlphaDecay={0.02}
        d3VelocityDecay={0.2}
        backgroundColor="#1a1a2e"
      />

      {/* Context Menu */}
      <Menu
        open={contextMenu !== null}
        onClose={handleCloseContextMenu}
        anchorReference="anchorPosition"
        anchorPosition={contextMenu ? { top: contextMenu.y, left: contextMenu.x } : undefined}
      >
        {contextMenu?.node && (
          <>
            {onNodeEdit && (
              <MenuItem onClick={() => { onNodeEdit(contextMenu.node!); handleCloseContextMenu(); }}>
                <ListItemIcon><EditIcon fontSize="small" /></ListItemIcon>
                <ListItemText>Edit Node</ListItemText>
              </MenuItem>
            )}
            {onLinkAdd && (
              <MenuItem onClick={() => { setAddLinkDialog({ open: true, sourceNode: contextMenu.node }); handleCloseContextMenu(); }}>
                <ListItemIcon><LinkIcon fontSize="small" /></ListItemIcon>
                <ListItemText>Add Relationship</ListItemText>
              </MenuItem>
            )}
            {onNodeDelete && (
              <MenuItem onClick={() => { onNodeDelete(contextMenu.node!); handleCloseContextMenu(); }}>
                <ListItemIcon><DeleteIcon fontSize="small" color="error" /></ListItemIcon>
                <ListItemText>Delete Node</ListItemText>
              </MenuItem>
            )}
          </>
        )}
      </Menu>

      {/* Add Node Dialog */}
      <Dialog open={addNodeDialog.open} onClose={() => setAddNodeDialog({ ...addNodeDialog, open: false })} maxWidth="sm" fullWidth>
        <DialogTitle>Add New Node</DialogTitle>
        <DialogContent>
          <Stack spacing={2} sx={{ mt: 1 }}>
            <FormControl fullWidth size="small">
              <InputLabel>Node Type</InputLabel>
              <Select
                value={addNodeDialog.type}
                label="Node Type"
                onChange={(e) => setAddNodeDialog({ ...addNodeDialog, type: e.target.value as GraphNode['type'] })}
              >
                <MenuItem value="ValueChain">Value Chain</MenuItem>
                <MenuItem value="Module">Module</MenuItem>
                <MenuItem value="KPI">KPI</MenuItem>
                <MenuItem value="ObjectModel">Object Model</MenuItem>
              </Select>
            </FormControl>
            <TextField
              label="Code"
              value={newNodeForm.code}
              onChange={(e) => setNewNodeForm({ ...newNodeForm, code: e.target.value })}
              fullWidth
              size="small"
              helperText="Unique identifier (e.g., my_module)"
            />
            <TextField
              label="Name"
              value={newNodeForm.name}
              onChange={(e) => setNewNodeForm({ ...newNodeForm, name: e.target.value })}
              fullWidth
              size="small"
            />
            <TextField
              label="Description"
              value={newNodeForm.description}
              onChange={(e) => setNewNodeForm({ ...newNodeForm, description: e.target.value })}
              fullWidth
              size="small"
              multiline
              rows={2}
            />
          </Stack>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setAddNodeDialog({ ...addNodeDialog, open: false })}>Cancel</Button>
          <Button 
            variant="contained" 
            onClick={() => {
              if (onNodeAdd) {
                onNodeAdd(addNodeDialog.type);
              }
              setAddNodeDialog({ ...addNodeDialog, open: false });
              setNewNodeForm({ code: '', name: '', description: '' });
            }}
            disabled={!newNodeForm.code || !newNodeForm.name}
          >
            Add
          </Button>
        </DialogActions>
      </Dialog>

      {/* Add Link Dialog */}
      <Dialog open={addLinkDialog.open} onClose={() => setAddLinkDialog({ open: false })} maxWidth="sm" fullWidth>
        <DialogTitle>Add Relationship from "{addLinkDialog.sourceNode?.name}"</DialogTitle>
        <DialogContent>
          <Stack spacing={2} sx={{ mt: 1 }}>
            <FormControl fullWidth size="small">
              <InputLabel>Relationship Type</InputLabel>
              <Select
                value={newLinkForm.type}
                label="Relationship Type"
                onChange={(e) => setNewLinkForm({ ...newLinkForm, type: e.target.value })}
              >
                <MenuItem value="CONTAINS">CONTAINS</MenuItem>
                <MenuItem value="HAS_KPI">HAS_KPI</MenuItem>
                <MenuItem value="USES">USES</MenuItem>
                <MenuItem value="RELATES_TO">RELATES_TO</MenuItem>
              </Select>
            </FormControl>
            <FormControl fullWidth size="small">
              <InputLabel>Target Node</InputLabel>
              <Select
                value={newLinkForm.targetId}
                label="Target Node"
                onChange={(e) => setNewLinkForm({ ...newLinkForm, targetId: e.target.value })}
              >
                {data.nodes
                  .filter(n => n.id !== addLinkDialog.sourceNode?.id)
                  .map(n => (
                    <MenuItem key={n.id} value={n.id}>
                      <Stack direction="row" alignItems="center" spacing={1}>
                        <Box sx={{ 
                          width: 10, 
                          height: 10, 
                          borderRadius: '50%', 
                          backgroundColor: NODE_STYLES[n.type]?.color || '#888'
                        }} />
                        <span>{n.name} ({n.type})</span>
                      </Stack>
                    </MenuItem>
                  ))}
              </Select>
            </FormControl>
          </Stack>
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setAddLinkDialog({ open: false })}>Cancel</Button>
          <Button 
            variant="contained" 
            onClick={() => {
              if (onLinkAdd && addLinkDialog.sourceNode && newLinkForm.targetId) {
                const targetNode = data.nodes.find(n => n.id === newLinkForm.targetId);
                if (targetNode) {
                  onLinkAdd(addLinkDialog.sourceNode, targetNode, newLinkForm.type);
                }
              }
              setAddLinkDialog({ open: false });
              setNewLinkForm({ targetId: '', type: 'CONTAINS' });
            }}
            disabled={!newLinkForm.targetId}
          >
            Add Relationship
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
}

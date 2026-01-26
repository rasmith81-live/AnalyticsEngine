import { useState, useEffect, useCallback, useRef } from 'react';
import { ArrowLeft, RefreshCw, ZoomIn, ZoomOut, Maximize2 } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

interface ServiceNode {
  id: string;
  name: string;
  status: 'healthy' | 'unhealthy' | 'unknown';
  x: number;
  y: number;
  layer: string;
}

interface TrafficLink {
  source: string;
  target: string;
  value: number;
  type: string;
}

interface TrafficData {
  nodes: ServiceNode[];
  links: TrafficLink[];
  timestamp: string;
  source?: string;
}

const STATS_URL = '/api/v1/observability/stats/traffic';

const layerColors: Record<string, string> = {
  infrastructure: '#3b82f6',
  platform: '#8b5cf6',
  gateway: '#f59e0b',
  business: '#10b981',
  frontend: '#ec4899',
  unknown: '#6b7280',
};

const statusColors: Record<string, string> = {
  healthy: '#22c55e',
  unhealthy: '#ef4444',
  unknown: '#9ca3af',
};

export default function ServiceTrafficPage() {
  const navigate = useNavigate();
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [trafficData, setTrafficData] = useState<TrafficData | null>(null);
  const [loading, setLoading] = useState(true);
  const [zoom, setZoom] = useState(1);
  const [autoRefresh, setAutoRefresh] = useState(true);
  const [selectedNode, setSelectedNode] = useState<ServiceNode | null>(null);

  const defaultPositions: Record<string, { x: number; y: number; layer: string }> = {
    // Frontend services (top) - includes UI
    demo_config_ui: { x: 100, y: 50, layer: 'frontend' },
    demo_config_service: { x: 250, y: 50, layer: 'frontend' },
    data_simulator_service: { x: 550, y: 50, layer: 'frontend' },
    // Gateway layer
    api_gateway: { x: 400, y: 130, layer: 'gateway' },
    // Platform layer
    observability_service: { x: 400, y: 210, layer: 'platform' },
    // Business services
    ingestion_service: { x: 100, y: 310, layer: 'business' },
    archival_service: { x: 250, y: 310, layer: 'business' },
    connector_service: { x: 400, y: 310, layer: 'business' },
    calculation_engine_service: { x: 550, y: 310, layer: 'business' },
    machine_learning_service: { x: 700, y: 310, layer: 'business' },
    conversation_service: { x: 100, y: 400, layer: 'business' },
    data_governance_service: { x: 250, y: 400, layer: 'business' },
    entity_resolution_service: { x: 400, y: 400, layer: 'business' },
    metadata_ingestion_service: { x: 550, y: 400, layer: 'business' },
    business_metadata: { x: 700, y: 400, layer: 'business' },
    // Infrastructure (bottom)
    messaging_service: { x: 400, y: 520, layer: 'infrastructure' },
    database_service: { x: 200, y: 520, layer: 'infrastructure' },
    redis: { x: 600, y: 520, layer: 'infrastructure' },
  };

  const fetchTrafficData = useCallback(async () => {
    try {
      const response = await fetch(STATS_URL);
      if (response.ok) {
        const data = await response.json();
        
        // If nodes are empty, generate them from links
        if (!data.nodes || data.nodes.length === 0) {
          const serviceIds = new Set<string>();
          data.links?.forEach((link: TrafficLink) => {
            serviceIds.add(link.source);
            serviceIds.add(link.target);
          });
          
          data.nodes = Array.from(serviceIds).map(id => {
            const pos = defaultPositions[id] || { x: 400, y: 300, layer: 'unknown' };
            return {
              id,
              name: id.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase()),
              status: 'healthy' as const,
              x: pos.x,
              y: pos.y,
              layer: pos.layer,
            };
          });
        }
        
        setTrafficData(data);
      }
    } catch (error) {
      console.error('Error fetching traffic data:', error);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchTrafficData();
    
    if (autoRefresh) {
      const interval = setInterval(fetchTrafficData, 2000);
      return () => clearInterval(interval);
    }
  }, [fetchTrafficData, autoRefresh]);

  const drawDiagram = useCallback(() => {
    const canvas = canvasRef.current;
    if (!canvas || !trafficData) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const width = canvas.width;
    const height = canvas.height;

    ctx.clearRect(0, 0, width, height);
    ctx.save();
    
    const offsetX = (width - 800 * zoom) / 2;
    const offsetY = 20;
    ctx.translate(offsetX, offsetY);
    ctx.scale(zoom, zoom);

    ctx.fillStyle = '#1e293b';
    ctx.fillRect(-20, -20, 840, 620);

    ctx.strokeStyle = '#334155';
    ctx.setLineDash([5, 5]);
    const layers = [
      { y: 30, label: 'Frontend Services' },
      { y: 110, label: 'Gateway Layer' },
      { y: 190, label: 'Platform Layer' },
      { y: 280, label: 'Business Services' },
      { y: 490, label: 'Infrastructure Layer' },
    ];
    
    layers.forEach(layer => {
      ctx.beginPath();
      ctx.moveTo(0, layer.y);
      ctx.lineTo(800, layer.y);
      ctx.stroke();
      
      ctx.fillStyle = '#64748b';
      ctx.font = '10px system-ui';
      ctx.fillText(layer.label, 10, layer.y - 5);
    });
    ctx.setLineDash([]);

    const nodePositions = new Map<string, { x: number; y: number }>();
    trafficData.nodes.forEach(node => {
      nodePositions.set(node.id, { x: node.x, y: node.y });
    });

    trafficData.links.forEach(link => {
      const sourcePos = nodePositions.get(link.source);
      const targetPos = nodePositions.get(link.target);
      
      if (sourcePos && targetPos) {
        const intensity = Math.min(1, link.value / 200);
        const lineWidth = 1 + intensity * 4;
        
        // Different colors for HTTP vs message traffic
        const isHttp = link.type === 'http';
        const baseColor = isHttp ? '236, 72, 153' : '59, 130, 246'; // pink for HTTP, blue for messages
        
        ctx.beginPath();
        ctx.strokeStyle = `rgba(${baseColor}, ${0.3 + intensity * 0.5})`;
        ctx.lineWidth = lineWidth;
        
        const midX = (sourcePos.x + targetPos.x) / 2;
        const midY = (sourcePos.y + targetPos.y) / 2 - 20;
        
        ctx.moveTo(sourcePos.x, sourcePos.y);
        ctx.quadraticCurveTo(midX, midY, targetPos.x, targetPos.y);
        ctx.stroke();

        const t = 0.7;
        const arrowX = (1-t)*(1-t)*sourcePos.x + 2*(1-t)*t*midX + t*t*targetPos.x;
        const arrowY = (1-t)*(1-t)*sourcePos.y + 2*(1-t)*t*midY + t*t*targetPos.y;
        
        const angle = Math.atan2(targetPos.y - midY, targetPos.x - midX);
        const arrowSize = 6 + intensity * 4;
        
        ctx.beginPath();
        ctx.fillStyle = `rgba(${baseColor}, ${0.5 + intensity * 0.5})`;
        ctx.moveTo(arrowX, arrowY);
        ctx.lineTo(
          arrowX - arrowSize * Math.cos(angle - Math.PI / 6),
          arrowY - arrowSize * Math.sin(angle - Math.PI / 6)
        );
        ctx.lineTo(
          arrowX - arrowSize * Math.cos(angle + Math.PI / 6),
          arrowY - arrowSize * Math.sin(angle + Math.PI / 6)
        );
        ctx.closePath();
        ctx.fill();

        if (link.value > 50) {
          ctx.fillStyle = '#94a3b8';
          ctx.font = '9px system-ui';
          ctx.fillText(`${link.value}/s`, midX - 15, midY - 5);
        }
      }
    });

    trafficData.nodes.forEach(node => {
      const x = node.x;
      const y = node.y;
      const radius = 25;

      const gradient = ctx.createRadialGradient(x, y, 0, x, y, radius);
      gradient.addColorStop(0, layerColors[node.layer] || layerColors.unknown);
      gradient.addColorStop(1, '#1e293b');
      
      ctx.beginPath();
      ctx.arc(x, y, radius + 3, 0, Math.PI * 2);
      ctx.fillStyle = statusColors[node.status];
      ctx.fill();

      ctx.beginPath();
      ctx.arc(x, y, radius, 0, Math.PI * 2);
      ctx.fillStyle = gradient;
      ctx.fill();
      
      ctx.strokeStyle = layerColors[node.layer] || layerColors.unknown;
      ctx.lineWidth = 2;
      ctx.stroke();

      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 8px system-ui';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      
      const shortName = node.name
        .replace(' Service', '')
        .replace('_service', '')
        .split(' ')
        .map(w => w.substring(0, 6))
        .join('\n');
      
      const lines = shortName.split('\n');
      lines.forEach((line, i) => {
        ctx.fillText(line, x, y - 4 + i * 10);
      });
    });

    ctx.restore();
  }, [trafficData, zoom]);

  useEffect(() => {
    drawDiagram();
  }, [drawDiagram]);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const handleResize = () => {
      canvas.width = canvas.offsetWidth;
      canvas.height = canvas.offsetHeight;
      drawDiagram();
    };

    handleResize();
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, [drawDiagram]);

  const handleCanvasClick = (e: React.MouseEvent<HTMLCanvasElement>) => {
    if (!trafficData || !canvasRef.current) return;
    
    const canvas = canvasRef.current;
    const rect = canvas.getBoundingClientRect();
    const offsetX = (canvas.width - 800 * zoom) / 2;
    const x = (e.clientX - rect.left - offsetX) / zoom;
    const y = (e.clientY - rect.top - 20) / zoom;

    const clickedNode = trafficData.nodes.find(node => {
      const dx = node.x - x;
      const dy = node.y - y;
      return Math.sqrt(dx * dx + dy * dy) < 25;
    });

    setSelectedNode(clickedNode || null);
  };

  return (
    <div className="min-h-screen bg-slate-900 text-white">
      <div className="border-b border-slate-700 bg-slate-800">
        <div className="max-w-7xl mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4">
              <button
                onClick={() => navigate('/system-monitor')}
                className="p-2 hover:bg-slate-700 rounded-lg transition-colors"
              >
                <ArrowLeft className="w-5 h-5" />
              </button>
              <div>
                <h1 className="text-xl font-bold">Service Traffic Monitor</h1>
                <p className="text-sm text-slate-400">Real-time message flow between services</p>
              </div>
            </div>
            
            <div className="flex items-center gap-2">
              <button
                onClick={() => setZoom(z => Math.max(0.5, z - 0.1))}
                className="p-2 hover:bg-slate-700 rounded-lg"
                title="Zoom Out"
              >
                <ZoomOut className="w-5 h-5" />
              </button>
              <span className="text-sm text-slate-400 w-12 text-center">{Math.round(zoom * 100)}%</span>
              <button
                onClick={() => setZoom(z => Math.min(2, z + 0.1))}
                className="p-2 hover:bg-slate-700 rounded-lg"
                title="Zoom In"
              >
                <ZoomIn className="w-5 h-5" />
              </button>
              <button
                onClick={() => setZoom(1)}
                className="p-2 hover:bg-slate-700 rounded-lg"
                title="Reset Zoom"
              >
                <Maximize2 className="w-5 h-5" />
              </button>
              <div className="w-px h-6 bg-slate-600 mx-2" />
              <label className="flex items-center gap-2 cursor-pointer">
                <input
                  type="checkbox"
                  checked={autoRefresh}
                  onChange={(e) => setAutoRefresh(e.target.checked)}
                  className="rounded border-slate-600"
                />
                <span className="text-sm">Auto-refresh</span>
              </label>
              <button
                onClick={fetchTrafficData}
                disabled={loading}
                className="p-2 hover:bg-slate-700 rounded-lg disabled:opacity-50"
                title="Refresh"
              >
                <RefreshCw className={`w-5 h-5 ${loading ? 'animate-spin' : ''}`} />
              </button>
            </div>
          </div>
        </div>
      </div>

      <div className="flex">
        <div className="flex-1 p-4">
          <div className="bg-slate-800 rounded-lg border border-slate-700 h-[calc(100vh-140px)] relative">
            {loading && !trafficData ? (
              <div className="absolute inset-0 flex items-center justify-center">
                <RefreshCw className="w-8 h-8 animate-spin text-blue-500" />
              </div>
            ) : (
              <canvas
                ref={canvasRef}
                className="w-full h-full cursor-crosshair"
                onClick={handleCanvasClick}
              />
            )}
          </div>
        </div>

        <div className="w-72 border-l border-slate-700 bg-slate-800 p-4">
          <h3 className="font-semibold mb-4">Legend</h3>
          
          <div className="space-y-4">
            <div>
              <h4 className="text-sm text-slate-400 mb-2">Service Layers</h4>
              <div className="space-y-1">
                {Object.entries(layerColors).map(([layer, color]) => (
                  <div key={layer} className="flex items-center gap-2 text-sm">
                    <div className="w-3 h-3 rounded-full" style={{ backgroundColor: color }} />
                    <span className="capitalize">{layer}</span>
                  </div>
                ))}
              </div>
            </div>
            
            <div>
              <h4 className="text-sm text-slate-400 mb-2">Health Status</h4>
              <div className="space-y-1">
                {Object.entries(statusColors).map(([status, color]) => (
                  <div key={status} className="flex items-center gap-2 text-sm">
                    <div className="w-3 h-3 rounded-full border-2" style={{ borderColor: color }} />
                    <span className="capitalize">{status}</span>
                  </div>
                ))}
              </div>
            </div>

            <div>
              <h4 className="text-sm text-slate-400 mb-2">Traffic Types</h4>
              <div className="space-y-1">
                <div className="flex items-center gap-2 text-sm">
                  <div className="w-8 h-1 rounded" style={{ backgroundColor: 'rgb(59, 130, 246)' }} />
                  <span>Message Traffic</span>
                </div>
                <div className="flex items-center gap-2 text-sm">
                  <div className="w-8 h-1 rounded" style={{ backgroundColor: 'rgb(236, 72, 153)' }} />
                  <span>HTTP Traffic</span>
                </div>
              </div>
            </div>

            <div>
              <h4 className="text-sm text-slate-400 mb-2">Traffic Intensity</h4>
              <div className="flex items-center gap-2">
                <div className="h-1 w-full bg-gradient-to-r from-blue-900 to-blue-400 rounded" />
              </div>
              <div className="flex justify-between text-xs text-slate-500 mt-1">
                <span>Low</span>
                <span>High</span>
              </div>
            </div>
          </div>

          {selectedNode && (
            <div className="mt-6 p-3 bg-slate-700 rounded-lg">
              <h4 className="font-semibold mb-2">{selectedNode.name}</h4>
              <div className="space-y-1 text-sm">
                <div className="flex justify-between">
                  <span className="text-slate-400">Status:</span>
                  <span className={selectedNode.status === 'healthy' ? 'text-green-400' : 'text-red-400'}>
                    {selectedNode.status}
                  </span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-400">Layer:</span>
                  <span className="capitalize">{selectedNode.layer}</span>
                </div>
                {trafficData && (
                  <>
                    <div className="flex justify-between">
                      <span className="text-slate-400">Incoming:</span>
                      <span>
                        {trafficData.links
                          .filter(l => l.target === selectedNode.id)
                          .reduce((sum, l) => sum + l.value, 0)}/s
                      </span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-slate-400">Outgoing:</span>
                      <span>
                        {trafficData.links
                          .filter(l => l.source === selectedNode.id)
                          .reduce((sum, l) => sum + l.value, 0)}/s
                      </span>
                    </div>
                  </>
                )}
              </div>
            </div>
          )}

          {trafficData && (
            <div className="mt-6 space-y-1">
              <div className="flex items-center gap-2">
                <div className={`w-2 h-2 rounded-full ${trafficData.source?.includes('prometheus') || trafficData.source === 'real_time' ? 'bg-green-500 animate-pulse' : 'bg-yellow-500'}`} />
                <span className="text-xs text-slate-400">
                  {trafficData.source?.includes('prometheus') || trafficData.source === 'real_time' ? 'Real-time data' : 'Baseline estimates'}
                </span>
              </div>
              <div className="text-xs text-slate-500">
                Last updated: {new Date(trafficData.timestamp).toLocaleTimeString()}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

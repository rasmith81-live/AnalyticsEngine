import { useState } from 'react';
import { CheckCircle, X } from 'lucide-react';
import KPITreeView from '../components/KPITreeView';
import KPIDetailPreview from '../components/KPIDetailPreview';
import KPISampleVisualization from '../components/KPISampleVisualization';
import DeriveCustomKPIModal from '../components/DeriveCustomKPIModal';
import ResizableSplitPanel from '../components/ResizableSplitPanel';
import KPICartBadge from '../components/KPICartBadge';
import { useCart } from '../contexts/CartContext';
import type { KPI } from '../types';

export default function ConfigPage() {
  const { selectedKPIs, toggleCart, addToCart, removeFromCart, clearCart, currentViewKPI, setCurrentViewKPI } = useCart();
  const [deriveModalOpen, setDeriveModalOpen] = useState(false);
  const [deriveBaseKPI, setDeriveBaseKPI] = useState<string | null>(null);
  const [saveSuccess, setSaveSuccess] = useState(false);

  const handleKPIToggleCart = (kpiCode: string) => {
    toggleCart(kpiCode);
  };

  const handleKPIViewDetails = (kpiCode: string) => {
    setCurrentViewKPI(kpiCode);
  };

  const handleAddToCart = (kpiCode: string) => {
    addToCart(kpiCode);
  };

  const handleRemoveKPI = (kpiCode: string) => {
    removeFromCart(kpiCode);
  };

  const handleClearAll = () => {
    if (window.confirm(`Are you sure you want to clear all ${selectedKPIs.length} selected KPIs?`)) {
      clearCart();
    }
  };

  const handleSaveConfiguration = () => {
    const config = {
      selectedKPIs,
      savedAt: new Date().toISOString(),
    };
    localStorage.setItem('kpi_configuration', JSON.stringify(config));
    setSaveSuccess(true);
    console.log('Configuration saved:', config);
  };

  const handleDeriveCustomKPI = (kpiCode: string) => {
    setDeriveBaseKPI(kpiCode);
    setDeriveModalOpen(true);
  };

  const handleSaveCustomKPI = (customKPI: Partial<KPI>) => {
    console.log('Custom KPI created:', customKPI);
    if (customKPI.code) {
      handleAddToCart(customKPI.code);
    }
  };

  return (
    <div className="h-[calc(100vh-100px)] w-full flex flex-col overflow-hidden animate-fade-in">
      {/* Page Header with Cart Badge */}
      <div className="px-4 py-3 border-b theme-border theme-card-bg">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold theme-text-title">KPI Configuration</h1>
            <p className="text-sm theme-text-muted">Browse KPIs, view details, and add to your cart</p>
          </div>
          <KPICartBadge
            selectedKPIs={selectedKPIs}
            onRemoveKPI={handleRemoveKPI}
            onClearAll={handleClearAll}
            onSaveConfiguration={handleSaveConfiguration}
            onViewKPI={setCurrentViewKPI}
            currentViewKPI={currentViewKPI}
          />
        </div>
      </div>

      {/* Resizable Split Panel */}
      <div className="flex-1 min-h-0 mt-4 px-4 overflow-hidden">
        <ResizableSplitPanel
          defaultLeftWidth={55}
          minLeftWidth={35}
          minRightWidth={25}
          leftPanel={
            <div className="h-full overflow-hidden">
              <KPITreeView
                onKPIToggleCart={handleKPIToggleCart}
                onKPIViewDetails={handleKPIViewDetails}
                selectedKPIs={selectedKPIs}
                currentViewKPI={currentViewKPI}
              />
            </div>
          }
          rightPanel={
            <div className="h-full flex flex-col gap-4 pl-4 overflow-hidden min-w-0">
              {/* Top: KPI Details */}
              <div className="flex-1 min-h-0">
                <KPIDetailPreview
                  kpiCode={currentViewKPI}
                  onAddToCart={handleAddToCart}
                  onDeriveCustomKPI={handleDeriveCustomKPI}
                  isInCart={currentViewKPI ? selectedKPIs.includes(currentViewKPI) : false}
                />
              </div>
              
              {/* Bottom: Sample Visualization */}
              {currentViewKPI && (
                <div className="h-[280px]">
                  <KPISampleVisualization kpiCode={currentViewKPI} />
                </div>
              )}
            </div>
          }
        />
      </div>

      {/* Custom KPI Derivation Modal */}
      <DeriveCustomKPIModal
        open={deriveModalOpen}
        baseKPICode={deriveBaseKPI}
        onClose={() => setDeriveModalOpen(false)}
        onSave={handleSaveCustomKPI}
      />

      {/* Success Notification */}
      {saveSuccess && (
        <div className="fixed bottom-6 left-1/2 -translate-x-1/2 z-50">
          <div className="flex items-center gap-3 px-4 py-3 rounded-xl bg-green-500/20 border border-green-500/30 text-green-400 shadow-lg">
            <CheckCircle className="w-5 h-5" />
            <span>Configuration saved successfully!</span>
            <button onClick={() => setSaveSuccess(false)} className="p-1 hover:bg-green-500/20 rounded">
              <X className="w-4 h-4" />
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

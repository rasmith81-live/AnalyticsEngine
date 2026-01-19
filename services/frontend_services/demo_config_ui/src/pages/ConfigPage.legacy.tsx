import { Typography, Box, Alert, Snackbar, AppBar, Toolbar } from '@mui/material';
import { useState } from 'react';
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
    // Toggle KPI in cart via checkbox
    toggleCart(kpiCode);
  };

  const handleKPIViewDetails = (kpiCode: string) => {
    // Show KPI details in the right panel preview
    setCurrentViewKPI(kpiCode);
  };

  const handleAddToCart = (kpiCode: string) => {
    // Add to cart from detail view button
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
    // TODO: Implement save to backend via configApi
    // For now, just save to localStorage
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
    // TODO: Save to backend via configApi
    console.log('Custom KPI created:', customKPI);
    // Add to cart
    if (customKPI.code) {
      handleAddToCart(customKPI.code);
    }
  };

  return (
    <Box sx={{ 
      height: 'calc(100vh - 100px)', 
      width: '100vw',
      maxWidth: '100%',
      display: 'flex', 
      flexDirection: 'column',
      overflow: 'hidden'
    }}>
      {/* Page Header with Cart Badge */}
      <AppBar position="static" color="default" elevation={0} sx={{ bgcolor: 'background.paper', borderBottom: 1, borderColor: 'divider' }}>
        <Toolbar sx={{ minWidth: 0, px: 2 }}>
          <Box sx={{ flexGrow: 1 }}>
            <Typography variant="h5" gutterBottom sx={{ mb: 0 }}>
              KPI Configuration
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Browse KPIs, view details, and add to your cart
            </Typography>
          </Box>
          <KPICartBadge
            selectedKPIs={selectedKPIs}
            onRemoveKPI={handleRemoveKPI}
            onClearAll={handleClearAll}
            onSaveConfiguration={handleSaveConfiguration}
            onViewKPI={setCurrentViewKPI}
            currentViewKPI={currentViewKPI}
          />
        </Toolbar>
      </AppBar>

      {/* Resizable Split Panel */}
      <Box sx={{ flex: 1, minHeight: 0, mt: 2, px: 2, overflow: 'hidden' }}>
        <ResizableSplitPanel
          defaultLeftWidth={55}
          minLeftWidth={35}
          minRightWidth={25}
          leftPanel={
            <Box sx={{ height: '100%', overflow: 'hidden' }}>
              <KPITreeView
                onKPIToggleCart={handleKPIToggleCart}
                onKPIViewDetails={handleKPIViewDetails}
                selectedKPIs={selectedKPIs}
                currentViewKPI={currentViewKPI}
              />
            </Box>
          }
          rightPanel={
            <Box sx={{ height: '100%', display: 'flex', flexDirection: 'column', gap: 2, pl: 2, overflow: 'hidden', minWidth: 0 }}>
              {/* Top: KPI Details */}
              <Box sx={{ flex: 1, minHeight: 0 }}>
                <KPIDetailPreview
                  kpiCode={currentViewKPI}
                  onAddToCart={handleAddToCart}
                  onDeriveCustomKPI={handleDeriveCustomKPI}
                  isInCart={currentViewKPI ? selectedKPIs.includes(currentViewKPI) : false}
                />
              </Box>
              
              {/* Bottom: Sample Visualization */}
              {currentViewKPI && (
                <Box sx={{ height: 280 }}>
                  <KPISampleVisualization kpiCode={currentViewKPI} />
                </Box>
              )}
            </Box>
          }
        />
      </Box>

      {/* Custom KPI Derivation Modal */}
      <DeriveCustomKPIModal
        open={deriveModalOpen}
        baseKPICode={deriveBaseKPI}
        onClose={() => setDeriveModalOpen(false)}
        onSave={handleSaveCustomKPI}
      />

      {/* Success Notification */}
      <Snackbar
        open={saveSuccess}
        autoHideDuration={3000}
        onClose={() => setSaveSuccess(false)}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
      >
        <Alert severity="success" onClose={() => setSaveSuccess(false)}>
          Configuration saved successfully!
        </Alert>
      </Snackbar>
    </Box>
  );
}

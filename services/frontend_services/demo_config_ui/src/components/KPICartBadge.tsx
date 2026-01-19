/**
 * KPICartBadge Component
 * Cart badge for header showing KPI count with dropdown
 */

import { useState, useRef, useEffect } from 'react';
import {
  ShoppingCart,
  Trash2,
  Trash,
  Save,
  Eye,
  GitBranch,
} from 'lucide-react';
import { useNavigate } from 'react-router-dom';
import { Button } from './ui/Button';
import { cn } from '../lib/utils';
import { useKPIDetails } from '../hooks/useKPIDetails';

interface KPICartBadgeProps {
  selectedKPIs: string[];
  onRemoveKPI: (kpiCode: string) => void;
  onClearAll: () => void;
  onSaveConfiguration: () => void;
  onViewKPI: (kpiCode: string) => void;
  currentViewKPI: string | null;
}

export default function KPICartBadge({
  selectedKPIs,
  onRemoveKPI,
  onClearAll,
  onSaveConfiguration,
  onViewKPI,
  currentViewKPI,
}: KPICartBadgeProps) {
  const navigate = useNavigate();
  const [isOpen, setIsOpen] = useState(false);
  const popoverRef = useRef<HTMLDivElement>(null);
  const buttonRef = useRef<HTMLButtonElement>(null);
  const { data: kpiDetails } = useKPIDetails(selectedKPIs);

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (
        popoverRef.current &&
        !popoverRef.current.contains(event.target as Node) &&
        buttonRef.current &&
        !buttonRef.current.contains(event.target as Node)
      ) {
        setIsOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  const getKPIDisplayName = (kpiCode: string): string => {
    const kpi = kpiDetails?.find((k) => k.code === kpiCode);
    return kpi?.display_name || kpi?.name || kpiCode;
  };

  const getTotalRequiredObjects = (): number => {
    if (!kpiDetails) return 0;
    const uniqueObjects = new Set<string>();
    kpiDetails.forEach((kpi) => {
      kpi.required_objects?.forEach((obj) => uniqueObjects.add(obj));
    });
    return uniqueObjects.size;
  };

  return (
    <div className="relative">
      <button
        ref={buttonRef}
        onClick={() => setIsOpen(!isOpen)}
        className="relative p-2 rounded-lg hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800 transition-colors"
        title="View KPI Cart"
      >
        <ShoppingCart className="w-5 h-5 theme-text" />
        {selectedKPIs.length > 0 && (
          <span className="absolute -top-1 -right-1 w-5 h-5 rounded-full bg-red-500 text-white text-xs flex items-center justify-center font-bold">
            {selectedKPIs.length}
          </span>
        )}
      </button>

      {isOpen && (
        <div
          ref={popoverRef}
          className="absolute right-0 top-full mt-2 w-[350px] max-h-[500px] rounded-xl theme-card-bg border theme-border shadow-2xl z-50 overflow-hidden"
        >
          {/* Header */}
          <div className="p-3 bg-alpha-500 text-white flex items-center justify-between">
            <h3 className="font-semibold">KPI Cart</h3>
            {selectedKPIs.length > 0 && (
              <button
                onClick={() => { onClearAll(); setIsOpen(false); }}
                className="p-1 hover:bg-white/20 rounded"
                title="Clear All"
              >
                <Trash className="w-4 h-4" />
              </button>
            )}
          </div>

          {/* Empty State */}
          {selectedKPIs.length === 0 ? (
            <div className="p-8 text-center">
              <ShoppingCart className="w-12 h-12 mx-auto theme-text-muted opacity-30 mb-2" />
              <p className="theme-text-muted">Your cart is empty</p>
              <p className="text-xs theme-text-muted">Select KPIs to add them to your cart</p>
            </div>
          ) : (
            <>
              {/* Summary Stats */}
              <div className="p-3 theme-card-bg border-b theme-border">
                <div className="flex justify-between text-sm mb-1">
                  <span className="theme-text-muted">Total KPIs:</span>
                  <span className="font-semibold theme-text">{selectedKPIs.length}</span>
                </div>
                <div className="flex justify-between text-sm">
                  <span className="theme-text-muted">Required Objects:</span>
                  <span className="font-semibold theme-text">{getTotalRequiredObjects()}</span>
                </div>
              </div>

              {/* KPI List */}
              <div className="max-h-[250px] overflow-y-auto divide-y theme-border">
                {selectedKPIs.map((kpiCode) => (
                  <div
                    key={kpiCode}
                    className={cn(
                      "p-3 flex items-center gap-2 cursor-pointer hover:bg-alpha-faded-50 dark:hover:bg-alpha-faded-900 transition-colors",
                      currentViewKPI === kpiCode && "bg-alpha-500/10"
                    )}
                    onClick={() => { onViewKPI(kpiCode); setIsOpen(false); }}
                  >
                    <div className="flex-1 min-w-0">
                      <p className="text-sm font-medium theme-text truncate">{getKPIDisplayName(kpiCode)}</p>
                      <p className="text-xs theme-text-muted truncate">{kpiCode}</p>
                    </div>
                    <div className="flex items-center gap-1">
                      <button
                        onClick={(e) => { e.stopPropagation(); onViewKPI(kpiCode); setIsOpen(false); }}
                        className="p-1.5 rounded hover:bg-alpha-faded-100 dark:hover:bg-alpha-faded-800"
                        title="View Details"
                      >
                        <Eye className="w-4 h-4 theme-text-muted" />
                      </button>
                      <button
                        onClick={(e) => { e.stopPropagation(); onRemoveKPI(kpiCode); }}
                        className="p-1.5 rounded hover:bg-red-500/20 text-red-400"
                        title="Remove"
                      >
                        <Trash2 className="w-4 h-4" />
                      </button>
                    </div>
                  </div>
                ))}
              </div>

              {/* Actions */}
              <div className="p-3 border-t theme-border space-y-2">
                <Button
                  variant="outline"
                  className="w-full"
                  onClick={() => { navigate('/required-objects-view', { state: { kpiCodes: selectedKPIs } }); setIsOpen(false); }}
                  disabled={selectedKPIs.length === 0}
                >
                  <GitBranch className="w-4 h-4 mr-2" />
                  View Required Objects
                </Button>
                <Button
                  className="w-full"
                  onClick={() => { onSaveConfiguration(); setIsOpen(false); }}
                >
                  <Save className="w-4 h-4 mr-2" />
                  Save Configuration
                </Button>
              </div>
            </>
          )}
        </div>
      )}
    </div>
  );
}

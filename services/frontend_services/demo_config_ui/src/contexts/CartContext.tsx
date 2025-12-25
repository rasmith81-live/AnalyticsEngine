/**
 * Cart Context - Global state for KPI shopping cart
 * Persists cart state across page navigation
 */

import { createContext, useContext, useState, useEffect, ReactNode } from 'react';

interface CartContextType {
  selectedKPIs: string[];
  addToCart: (kpiCode: string) => void;
  removeFromCart: (kpiCode: string) => void;
  toggleCart: (kpiCode: string) => void;
  clearCart: () => void;
  isInCart: (kpiCode: string) => boolean;
  currentViewKPI: string | null;
  setCurrentViewKPI: (kpiCode: string | null) => void;
  treeExpandedNodes: string[];
  setTreeExpandedNodes: (nodes: string[]) => void;
  treeSearchQuery: string;
  setTreeSearchQuery: (query: string) => void;
}

const CartContext = createContext<CartContextType | undefined>(undefined);

const CART_STORAGE_KEY = 'analytics_kpi_cart';
const TREE_EXPANDED_STORAGE_KEY = 'analytics_tree_expanded';
const TREE_SEARCH_STORAGE_KEY = 'analytics_tree_search';

export function CartProvider({ children }: { children: ReactNode }) {
  // Initialize cart from localStorage
  const [selectedKPIs, setSelectedKPIs] = useState<string[]>(() => {
    try {
      const stored = localStorage.getItem(CART_STORAGE_KEY);
      return stored ? JSON.parse(stored) : [];
    } catch (error) {
      console.error('Error loading cart from localStorage:', error);
      return [];
    }
  });

  // Start with no KPI selected - user must explicitly click to view details
  const [currentViewKPI, setCurrentViewKPIState] = useState<string | null>(null);

  // Initialize tree expanded nodes from localStorage
  const [treeExpandedNodes, setTreeExpandedNodesState] = useState<string[]>(() => {
    try {
      const stored = localStorage.getItem(TREE_EXPANDED_STORAGE_KEY);
      return stored ? JSON.parse(stored) : [];
    } catch (error) {
      console.error('Error loading tree expanded nodes from localStorage:', error);
      return [];
    }
  });

  // Initialize tree search query from localStorage
  const [treeSearchQuery, setTreeSearchQueryState] = useState<string>(() => {
    try {
      const stored = localStorage.getItem(TREE_SEARCH_STORAGE_KEY);
      return stored || '';
    } catch (error) {
      console.error('Error loading tree search query from localStorage:', error);
      return '';
    }
  });

  // Persist cart to localStorage whenever it changes
  useEffect(() => {
    try {
      localStorage.setItem(CART_STORAGE_KEY, JSON.stringify(selectedKPIs));
    } catch (error) {
      console.error('Error saving cart to localStorage:', error);
    }
  }, [selectedKPIs]);

  // Note: currentViewKPI is intentionally NOT persisted - always starts fresh

  // Persist tree expanded nodes to localStorage whenever they change
  useEffect(() => {
    try {
      localStorage.setItem(TREE_EXPANDED_STORAGE_KEY, JSON.stringify(treeExpandedNodes));
    } catch (error) {
      console.error('Error saving tree expanded nodes to localStorage:', error);
    }
  }, [treeExpandedNodes]);

  // Persist tree search query to localStorage whenever it changes
  useEffect(() => {
    try {
      if (treeSearchQuery) {
        localStorage.setItem(TREE_SEARCH_STORAGE_KEY, treeSearchQuery);
      } else {
        localStorage.removeItem(TREE_SEARCH_STORAGE_KEY);
      }
    } catch (error) {
      console.error('Error saving tree search query to localStorage:', error);
    }
  }, [treeSearchQuery]);

  const addToCart = (kpiCode: string) => {
    setSelectedKPIs((prev) => {
      if (prev.includes(kpiCode)) {
        return prev;
      }
      return [...prev, kpiCode];
    });
  };

  const removeFromCart = (kpiCode: string) => {
    setSelectedKPIs((prev) => prev.filter((code) => code !== kpiCode));
  };

  const toggleCart = (kpiCode: string) => {
    setSelectedKPIs((prev) => {
      if (prev.includes(kpiCode)) {
        return prev.filter((code) => code !== kpiCode);
      }
      return [...prev, kpiCode];
    });
  };

  const clearCart = () => {
    setSelectedKPIs([]);
  };

  const isInCart = (kpiCode: string) => {
    return selectedKPIs.includes(kpiCode);
  };

  const setCurrentViewKPI = (kpiCode: string | null) => {
    setCurrentViewKPIState(kpiCode);
  };

  const setTreeExpandedNodes = (nodes: string[]) => {
    setTreeExpandedNodesState(nodes);
  };

  const setTreeSearchQuery = (query: string) => {
    setTreeSearchQueryState(query);
  };

  const value: CartContextType = {
    selectedKPIs,
    addToCart,
    removeFromCart,
    toggleCart,
    clearCart,
    isInCart,
    currentViewKPI,
    setCurrentViewKPI,
    treeExpandedNodes,
    setTreeExpandedNodes,
    treeSearchQuery,
    setTreeSearchQuery,
  };

  return <CartContext.Provider value={value}>{children}</CartContext.Provider>;
}

export function useCart() {
  const context = useContext(CartContext);
  if (context === undefined) {
    throw new Error('useCart must be used within a CartProvider');
  }
  return context;
}

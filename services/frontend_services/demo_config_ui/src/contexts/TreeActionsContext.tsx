/**
 * TreeActionsContext
 * Provides rename, delete, and drag-drop functionality for the KPI tree
 */

import { createContext, useContext, useState, useCallback, ReactNode } from 'react';
import { useQueryClient } from '@tanstack/react-query';
import { metadataApi } from '../api/metadataApi';

type ItemType = 'valueChain' | 'module' | 'kpi';

interface DragItem {
  type: ItemType;
  code: string;
  name: string;
  sourceModuleCode?: string;
  sourceValueChainCode?: string;
}

interface TreeActionsContextType {
  // Rename
  renameItem: (type: ItemType, code: string, currentName: string) => void;
  isRenaming: boolean;
  renameDialogOpen: boolean;
  closeRenameDialog: () => void;
  submitRename: (newName: string) => Promise<void>;
  currentRenameItem: { type: ItemType; code: string; name: string } | null;
  
  // Delete
  deleteItem: (type: ItemType, code: string, name: string) => void;
  isDeleting: boolean;
  deleteDialogOpen: boolean;
  closeDeleteDialog: () => void;
  confirmDelete: () => Promise<void>;
  currentDeleteItem: { type: ItemType; code: string; name: string } | null;
  
  // Drag and Drop
  dragItem: DragItem | null;
  setDragItem: (item: DragItem | null) => void;
  handleDrop: (targetType: ItemType, targetCode: string) => Promise<void>;
  isDragging: boolean;
  
  // Snackbar
  snackbar: { open: boolean; message: string; severity: 'success' | 'error' };
  closeSnackbar: () => void;
}

const TreeActionsContext = createContext<TreeActionsContextType | undefined>(undefined);

export function TreeActionsProvider({ children }: { children: ReactNode }) {
  const queryClient = useQueryClient();
  
  // Rename state
  const [renameDialogOpen, setRenameDialogOpen] = useState(false);
  const [isRenaming, setIsRenaming] = useState(false);
  const [currentRenameItem, setCurrentRenameItem] = useState<{ type: ItemType; code: string; name: string } | null>(null);
  
  // Delete state
  const [deleteDialogOpen, setDeleteDialogOpen] = useState(false);
  const [isDeleting, setIsDeleting] = useState(false);
  const [currentDeleteItem, setCurrentDeleteItem] = useState<{ type: ItemType; code: string; name: string } | null>(null);
  
  // Drag state
  const [dragItem, setDragItem] = useState<DragItem | null>(null);
  
  // Snackbar state
  const [snackbar, setSnackbar] = useState<{ open: boolean; message: string; severity: 'success' | 'error' }>({
    open: false,
    message: '',
    severity: 'success'
  });

  const showSnackbar = (message: string, severity: 'success' | 'error') => {
    setSnackbar({ open: true, message, severity });
  };

  const closeSnackbar = () => {
    setSnackbar(prev => ({ ...prev, open: false }));
  };

  const refreshTree = useCallback(() => {
    queryClient.invalidateQueries({ queryKey: ['valueChainTree'] });
    queryClient.invalidateQueries({ queryKey: ['infiniteKPIs'] });
  }, [queryClient]);

  // Rename handlers
  const renameItem = useCallback((type: ItemType, code: string, currentName: string) => {
    setCurrentRenameItem({ type, code, name: currentName });
    setRenameDialogOpen(true);
  }, []);

  const closeRenameDialog = useCallback(() => {
    setRenameDialogOpen(false);
    setCurrentRenameItem(null);
  }, []);

  const submitRename = useCallback(async (newName: string) => {
    if (!currentRenameItem) return;
    
    setIsRenaming(true);
    try {
      const { type, code } = currentRenameItem;
      
      // Fetch current data and update name
      if (type === 'valueChain') {
        const valueChains = await metadataApi.getValueChains();
        const vc = valueChains.find((v: any) => v.code === code);
        if (vc) {
          await metadataApi.updateValueChain(code, { ...vc, name: newName });
        }
      } else if (type === 'module') {
        const modules = await metadataApi.getModules();
        const mod = modules.find((m: any) => m.code === code) as any;
        if (mod) {
          await metadataApi.updateModule(code, { ...mod, name: newName });
        }
      } else if (type === 'kpi') {
        const kpi = await metadataApi.getKPI(code);
        await metadataApi.updateKPI(code, { ...kpi, name: newName });
      }
      
      showSnackbar(`${type === 'valueChain' ? 'Value Chain' : type === 'module' ? 'Module' : 'KPI'} renamed successfully`, 'success');
      refreshTree();
      closeRenameDialog();
    } catch (error: any) {
      showSnackbar(`Failed to rename: ${error.message}`, 'error');
    } finally {
      setIsRenaming(false);
    }
  }, [currentRenameItem, refreshTree, closeRenameDialog]);

  // Delete handlers
  const deleteItem = useCallback((type: ItemType, code: string, name: string) => {
    setCurrentDeleteItem({ type, code, name });
    setDeleteDialogOpen(true);
  }, []);

  const closeDeleteDialog = useCallback(() => {
    setDeleteDialogOpen(false);
    setCurrentDeleteItem(null);
  }, []);

  const confirmDelete = useCallback(async () => {
    if (!currentDeleteItem) return;
    
    setIsDeleting(true);
    try {
      const { type, code } = currentDeleteItem;
      
      if (type === 'valueChain') {
        await metadataApi.deleteValueChain(code);
      } else if (type === 'module') {
        await metadataApi.deleteModule(code);
      } else if (type === 'kpi') {
        await metadataApi.deleteKPI(code);
      }
      
      showSnackbar(`${type === 'valueChain' ? 'Value Chain' : type === 'module' ? 'Module' : 'KPI'} deleted successfully`, 'success');
      refreshTree();
      closeDeleteDialog();
    } catch (error: any) {
      showSnackbar(`Failed to delete: ${error.message}`, 'error');
    } finally {
      setIsDeleting(false);
    }
  }, [currentDeleteItem, refreshTree, closeDeleteDialog]);

  // Drag and drop handlers
  const handleDrop = useCallback(async (targetType: ItemType, targetCode: string) => {
    if (!dragItem) return;
    
    try {
      // KPI dropped on module
      if (dragItem.type === 'kpi' && targetType === 'module') {
        // Get the target module to find its value chain
        const modules = await metadataApi.getModules();
        const targetModule = modules.find((m: any) => m.code === targetCode) as any;
        const targetValueChain = targetModule?.metadata_?.value_chain || targetModule?.value_chain || '';
        
        await metadataApi.updateKPIRelationship(dragItem.code, targetCode, targetValueChain);
        showSnackbar(`KPI "${dragItem.name}" moved to module`, 'success');
      }
      // Module dropped on value chain
      else if (dragItem.type === 'module' && targetType === 'valueChain') {
        await metadataApi.moveModuleToValueChain(dragItem.code, targetCode);
        showSnackbar(`Module "${dragItem.name}" moved to value chain`, 'success');
      }
      
      refreshTree();
    } catch (error: any) {
      showSnackbar(`Failed to move item: ${error.message}`, 'error');
    } finally {
      setDragItem(null);
    }
  }, [dragItem, refreshTree]);

  const value: TreeActionsContextType = {
    renameItem,
    isRenaming,
    renameDialogOpen,
    closeRenameDialog,
    submitRename,
    currentRenameItem,
    
    deleteItem,
    isDeleting,
    deleteDialogOpen,
    closeDeleteDialog,
    confirmDelete,
    currentDeleteItem,
    
    dragItem,
    setDragItem,
    handleDrop,
    isDragging: dragItem !== null,
    
    snackbar,
    closeSnackbar,
  };

  return (
    <TreeActionsContext.Provider value={value}>
      {children}
    </TreeActionsContext.Provider>
  );
}

export function useTreeActions() {
  const context = useContext(TreeActionsContext);
  if (context === undefined) {
    throw new Error('useTreeActions must be used within a TreeActionsProvider');
  }
  return context;
}

/**
 * TreeActionsDialogs Component
 * Renders the rename and delete dialogs for tree items
 */

import { useState, useEffect } from 'react';
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogContentText,
  DialogActions,
  Button,
  TextField,
  Snackbar,
  Alert,
  CircularProgress
} from '@mui/material';
import { useTreeActions } from '../contexts/TreeActionsContext';

export default function TreeActionsDialogs() {
  const {
    renameDialogOpen,
    closeRenameDialog,
    submitRename,
    currentRenameItem,
    isRenaming,
    
    deleteDialogOpen,
    closeDeleteDialog,
    confirmDelete,
    currentDeleteItem,
    isDeleting,
    
    snackbar,
    closeSnackbar,
  } = useTreeActions();

  const [newName, setNewName] = useState('');

  // Reset name field when dialog opens
  useEffect(() => {
    if (renameDialogOpen && currentRenameItem) {
      setNewName(currentRenameItem.name);
    }
  }, [renameDialogOpen, currentRenameItem]);

  const handleRenameSubmit = async () => {
    if (newName.trim()) {
      await submitRename(newName.trim());
    }
  };

  const getTypeLabel = (type: string) => {
    switch (type) {
      case 'valueChain': return 'Value Chain';
      case 'module': return 'Module';
      case 'kpi': return 'KPI';
      default: return 'Item';
    }
  };

  return (
    <>
      {/* Rename Dialog */}
      <Dialog open={renameDialogOpen} onClose={closeRenameDialog} maxWidth="sm" fullWidth>
        <DialogTitle>
          Rename {currentRenameItem ? getTypeLabel(currentRenameItem.type) : 'Item'}
        </DialogTitle>
        <DialogContent>
          <TextField
            autoFocus
            margin="dense"
            label="New Name"
            fullWidth
            value={newName}
            onChange={(e) => setNewName(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleRenameSubmit()}
            disabled={isRenaming}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={closeRenameDialog} disabled={isRenaming}>
            Cancel
          </Button>
          <Button 
            onClick={handleRenameSubmit} 
            variant="contained" 
            disabled={isRenaming || !newName.trim()}
          >
            {isRenaming ? <CircularProgress size={20} /> : 'Rename'}
          </Button>
        </DialogActions>
      </Dialog>

      {/* Delete Confirmation Dialog */}
      <Dialog open={deleteDialogOpen} onClose={closeDeleteDialog}>
        <DialogTitle>
          Delete {currentDeleteItem ? getTypeLabel(currentDeleteItem.type) : 'Item'}
        </DialogTitle>
        <DialogContent>
          <DialogContentText>
            Are you sure you want to delete "{currentDeleteItem?.name}"? This action cannot be undone.
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={closeDeleteDialog} disabled={isDeleting}>
            Cancel
          </Button>
          <Button 
            onClick={confirmDelete} 
            color="error" 
            variant="contained"
            disabled={isDeleting}
          >
            {isDeleting ? <CircularProgress size={20} /> : 'Delete'}
          </Button>
        </DialogActions>
      </Dialog>

      {/* Snackbar for notifications */}
      <Snackbar
        open={snackbar.open}
        autoHideDuration={4000}
        onClose={closeSnackbar}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
      >
        <Alert severity={snackbar.severity} onClose={closeSnackbar}>
          {snackbar.message}
        </Alert>
      </Snackbar>
    </>
  );
}

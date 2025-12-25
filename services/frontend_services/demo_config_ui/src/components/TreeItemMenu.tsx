/**
 * TreeItemMenu Component
 * Renders the ellipsis dropdown menu for tree items
 */

import { useState, MouseEvent } from 'react';
import { IconButton, Menu, MenuItem, ListItemIcon, ListItemText, Divider } from '@mui/material';
import MoreVertIcon from '@mui/icons-material/MoreVert';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import RefreshIcon from '@mui/icons-material/Refresh';
import { useTreeActions } from '../contexts/TreeActionsContext';

type ItemType = 'valueChain' | 'module' | 'kpi';

interface TreeItemMenuProps {
  type: ItemType;
  code: string;
  name: string;
  onRefresh?: () => void;
}

export default function TreeItemMenu({ type, code, name, onRefresh }: TreeItemMenuProps) {
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);
  const open = Boolean(anchorEl);
  const { renameItem, deleteItem } = useTreeActions();

  const handleClick = (event: MouseEvent<HTMLElement>) => {
    event.stopPropagation();
    setAnchorEl(event.currentTarget);
  };

  const handleClose = (event?: MouseEvent) => {
    event?.stopPropagation();
    setAnchorEl(null);
  };

  const handleRename = (event: MouseEvent) => {
    event.stopPropagation();
    handleClose();
    renameItem(type, code, name);
  };

  const handleDelete = (event: MouseEvent) => {
    event.stopPropagation();
    handleClose();
    deleteItem(type, code, name);
  };

  const handleRefresh = (event: MouseEvent) => {
    event.stopPropagation();
    handleClose();
    onRefresh?.();
  };

  return (
    <>
      <IconButton
        size="small"
        onClick={handleClick}
        sx={{ 
          ml: 1,
          opacity: 0.6,
          '&:hover': { opacity: 1 }
        }}
      >
        <MoreVertIcon fontSize="small" />
      </IconButton>
      <Menu
        anchorEl={anchorEl}
        open={open}
        onClose={() => handleClose()}
        onClick={(e) => e.stopPropagation()}
        transformOrigin={{ horizontal: 'right', vertical: 'top' }}
        anchorOrigin={{ horizontal: 'right', vertical: 'bottom' }}
      >
        {onRefresh && (
          <>
            <MenuItem onClick={handleRefresh}>
              <ListItemIcon>
                <RefreshIcon fontSize="small" />
              </ListItemIcon>
              <ListItemText>Refresh</ListItemText>
            </MenuItem>
            <Divider />
          </>
        )}
        <MenuItem onClick={handleRename}>
          <ListItemIcon>
            <EditIcon fontSize="small" />
          </ListItemIcon>
          <ListItemText>Rename</ListItemText>
        </MenuItem>
        <MenuItem onClick={handleDelete} sx={{ color: 'error.main' }}>
          <ListItemIcon>
            <DeleteIcon fontSize="small" color="error" />
          </ListItemIcon>
          <ListItemText>Delete</ListItemText>
        </MenuItem>
      </Menu>
    </>
  );
}

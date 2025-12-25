/**
 * ImportItemMenu Component
 * Renders the ellipsis dropdown menu for import preview items (KPIs, ontology, relationships)
 * These items are not yet in the metadata store, so this handles local state changes
 */

import { useState, MouseEvent } from 'react';
import { IconButton, Menu, MenuItem, ListItemIcon, ListItemText } from '@mui/material';
import MoreVertIcon from '@mui/icons-material/MoreVert';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';

interface ImportItemMenuProps {
  name: string;
  onRename: (newName: string) => void;
  onDelete: () => void;
}

export default function ImportItemMenu({ name, onRename, onDelete }: ImportItemMenuProps) {
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);
  const open = Boolean(anchorEl);

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
    const newName = prompt('Enter new name:', name);
    if (newName && newName.trim() !== '' && newName !== name) {
      onRename(newName.trim());
    }
  };

  const handleDelete = (event: MouseEvent) => {
    event.stopPropagation();
    handleClose();
    onDelete();
  };

  return (
    <>
      <IconButton
        size="small"
        onClick={handleClick}
        sx={{ 
          ml: 'auto',
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

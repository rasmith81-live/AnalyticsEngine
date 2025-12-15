import React from 'react';
import { useDraggable } from '@dnd-kit/core';
import { Box, Typography, Paper } from '@mui/material';
import DragIndicatorIcon from '@mui/icons-material/DragIndicator';

// Mock Data
const sourceColumns = [
  { id: 'src_col_1', name: 'MATNR (Material)' },
  { id: 'src_col_2', name: 'WERKS (Plant)' },
  { id: 'src_col_3', name: 'LGORT (Storage Loc)' },
  { id: 'src_col_4', name: 'LABST (Stock)' },
];

const DraggableItem = ({ id, name }: { id: string, name: string }) => {
  const { attributes, listeners, setNodeRef, transform } = useDraggable({
    id: id,
  });
  
  const style = transform ? {
    transform: `translate3d(${transform.x}px, ${transform.y}px, 0)`,
  } : undefined;

  return (
    <Paper 
      ref={setNodeRef} 
      style={style} 
      {...listeners} 
      {...attributes}
      sx={{ p: 1, mb: 1, display: 'flex', alignItems: 'center', cursor: 'grab' }}
    >
      <DragIndicatorIcon fontSize="small" sx={{ mr: 1, color: 'grey.500' }} />
      <Typography>{name}</Typography>
    </Paper>
  );
};

const SourceSchemaTree: React.FC = () => {
  return (
    <Box>
      {sourceColumns.map((col) => (
        <DraggableItem key={col.id} id={col.id} name={col.name} />
      ))}
    </Box>
  );
};

export default SourceSchemaTree;

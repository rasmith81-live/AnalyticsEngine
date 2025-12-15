import React from 'react';
import { useDroppable } from '@dnd-kit/core';
import { Box, Typography, Paper, Chip } from '@mui/material';

// Mock Data
const targetAttributes = [
  { id: 'tgt_attr_1', name: 'Product ID', entity: 'Product' },
  { id: 'tgt_attr_2', name: 'Warehouse ID', entity: 'Warehouse' },
  { id: 'tgt_attr_3', name: 'Inventory Qty', entity: 'Inventory' },
];

const DroppableItem = ({ id, name, entity, mappedSource }: { id: string, name: string, entity: string, mappedSource?: string }) => {
  const { setNodeRef, isOver } = useDroppable({
    id: id,
  });

  return (
    <Paper 
      ref={setNodeRef}
      sx={{ 
        p: 2, 
        mb: 2, 
        bgcolor: isOver ? 'action.hover' : 'background.paper',
        borderStyle: 'dashed',
        borderWidth: mappedSource ? 0 : 1,
        borderColor: 'grey.400'
      }}
    >
      <Typography variant="subtitle2" color="primary">{entity}</Typography>
      <Box display="flex" justifyContent="space-between" alignItems="center">
        <Typography variant="body1">{name}</Typography>
        {mappedSource && (
          <Chip label={`Mapped: ${mappedSource}`} color="success" size="small" onDelete={() => {}} />
        )}
      </Box>
    </Paper>
  );
};

interface Props {
  mappings: Record<string, string>;
}

const TargetOntologyTree: React.FC<Props> = ({ mappings }) => {
  return (
    <Box>
      {targetAttributes.map((attr) => (
        <DroppableItem 
          key={attr.id} 
          id={attr.id} 
          name={attr.name} 
          entity={attr.entity}
          mappedSource={mappings[attr.id]}
        />
      ))}
    </Box>
  );
};

export default TargetOntologyTree;

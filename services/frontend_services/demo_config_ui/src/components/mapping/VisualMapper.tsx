import React, { useState } from 'react';
import { DndContext, DragOverlay } from '@dnd-kit/core';
import SourceSchemaTree from './SourceSchemaTree';
import TargetOntologyTree from './TargetOntologyTree';
import { Box, Typography } from '@mui/material';

const VisualMapper: React.FC = () => {
  const [mappings, setMappings] = useState<Record<string, string>>({});

  const handleDragEnd = (event: any) => {
    const { active, over } = event;
    if (over && active.id !== over.id) {
      setMappings((prev) => ({
        ...prev,
        [over.id]: active.id, // Map Target (Key) -> Source (Value)
      }));
    }
  };

  return (
    <DndContext onDragEnd={handleDragEnd}>
      <Box display="flex" height="100%" p={2} gap={2}>
        <Box flex={1} border={1} borderColor="grey.300" borderRadius={1} p={2}>
          <Typography variant="h6" mb={2}>Source Schema (Ingestion)</Typography>
          <SourceSchemaTree />
        </Box>
        
        <Box flex={1} border={1} borderColor="grey.300" borderRadius={1} p={2}>
          <Typography variant="h6" mb={2}>Target Ontology (Business Metadata)</Typography>
          <TargetOntologyTree mappings={mappings} />
        </Box>
      </Box>
    </DndContext>
  );
};

export default VisualMapper;

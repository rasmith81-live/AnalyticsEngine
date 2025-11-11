/**
 * ResizableSplitPanel Component
 * Two-panel layout with draggable divider for resizing
 */

import { Box } from '@mui/material';
import { useState, useRef, useEffect } from 'react';

interface ResizableSplitPanelProps {
  leftPanel: React.ReactNode;
  rightPanel: React.ReactNode;
  defaultLeftWidth?: number; // Percentage (0-100)
  minLeftWidth?: number; // Percentage
  minRightWidth?: number; // Percentage
}

export default function ResizableSplitPanel({
  leftPanel,
  rightPanel,
  defaultLeftWidth = 50,
  minLeftWidth = 20,
  minRightWidth = 20,
}: ResizableSplitPanelProps) {
  const [leftWidth, setLeftWidth] = useState(defaultLeftWidth);
  const [isDragging, setIsDragging] = useState(false);
  const containerRef = useRef<HTMLDivElement>(null);

  const handleMouseDown = (e: React.MouseEvent) => {
    e.preventDefault();
    setIsDragging(true);
  };

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      if (!isDragging || !containerRef.current) return;

      const container = containerRef.current;
      const containerRect = container.getBoundingClientRect();
      const containerWidth = containerRect.width;
      const mouseX = e.clientX - containerRect.left;
      
      // Calculate new left width as percentage
      let newLeftWidth = (mouseX / containerWidth) * 100;
      
      // Apply constraints
      newLeftWidth = Math.max(minLeftWidth, Math.min(100 - minRightWidth, newLeftWidth));
      
      setLeftWidth(newLeftWidth);
    };

    const handleMouseUp = () => {
      setIsDragging(false);
    };

    if (isDragging) {
      document.addEventListener('mousemove', handleMouseMove);
      document.addEventListener('mouseup', handleMouseUp);
      // Prevent text selection while dragging
      document.body.style.userSelect = 'none';
      document.body.style.cursor = 'col-resize';
    }

    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
      document.removeEventListener('mouseup', handleMouseUp);
      document.body.style.userSelect = '';
      document.body.style.cursor = '';
    };
  }, [isDragging, minLeftWidth, minRightWidth]);

  return (
    <Box
      ref={containerRef}
      sx={{
        display: 'flex',
        height: '100%',
        width: '100%',
        position: 'relative',
        overflow: 'hidden',
      }}
    >
      {/* Left Panel */}
      <Box
        sx={{
          width: `${leftWidth}%`,
          height: '100%',
          overflow: 'auto',
          position: 'relative',
        }}
      >
        {leftPanel}
      </Box>

      {/* Draggable Divider */}
      <Box
        onMouseDown={handleMouseDown}
        sx={{
          width: '8px',
          height: '100%',
          cursor: 'col-resize',
          bgcolor: 'divider',
          position: 'relative',
          flexShrink: 0,
          transition: isDragging ? 'none' : 'background-color 0.2s',
          '&:hover': {
            bgcolor: 'primary.main',
          },
          '&::before': {
            content: '""',
            position: 'absolute',
            left: '50%',
            top: '50%',
            transform: 'translate(-50%, -50%)',
            width: '2px',
            height: '40px',
            bgcolor: isDragging ? 'primary.contrastText' : 'grey.400',
            borderRadius: '1px',
          },
          '&::after': {
            content: '""',
            position: 'absolute',
            left: '50%',
            top: '50%',
            transform: 'translate(-50%, calc(-50% + 8px))',
            width: '2px',
            height: '40px',
            bgcolor: isDragging ? 'primary.contrastText' : 'grey.400',
            borderRadius: '1px',
          },
        }}
      />

      {/* Right Panel */}
      <Box
        sx={{
          width: `${100 - leftWidth}%`,
          height: '100%',
          overflow: 'auto',
          position: 'relative',
        }}
      >
        {rightPanel}
      </Box>
    </Box>
  );
}

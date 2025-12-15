
import { Card, CardContent, Typography, Box, Chip, Tooltip } from '@mui/material';
import { TrendingUp, TrendingDown, Remove } from '@mui/icons-material';

interface KPICardProps {
  title: string;
  value: string | number;
  unit?: string;
  trend?: 'up' | 'down' | 'stable';
  trendValue?: string;
  category?: string;
  description?: string;
  onClick?: () => void;
}

export default function KPICard({ 
  title, 
  value, 
  unit, 
  trend, 
  trendValue, 
  category,
  description,
  onClick 
}: KPICardProps) {
  
  const getTrendIcon = () => {
    if (trend === 'up') return <TrendingUp color="success" fontSize="small" />;
    if (trend === 'down') return <TrendingDown color="error" fontSize="small" />;
    return <Remove color="action" fontSize="small" />;
  };

  const getTrendColor = () => {
    if (trend === 'up') return 'success.main';
    if (trend === 'down') return 'error.main';
    return 'text.secondary';
  };

  return (
    <Card 
      variant="outlined" 
      sx={{ 
        height: '100%', 
        cursor: onClick ? 'pointer' : 'default',
        transition: 'transform 0.2s, box-shadow 0.2s',
        '&:hover': onClick ? {
          transform: 'translateY(-2px)',
          boxShadow: 2
        } : {}
      }}
      onClick={onClick}
    >
      <CardContent>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', mb: 1 }}>
          <Tooltip title={description || ''}>
            <Typography variant="subtitle2" color="text.secondary" noWrap sx={{ maxWidth: '70%' }}>
              {title}
            </Typography>
          </Tooltip>
          {category && (
            <Chip label={category} size="small" variant="outlined" sx={{ fontSize: '0.65rem', height: 20 }} />
          )}
        </Box>
        
        <Box sx={{ display: 'flex', alignItems: 'baseline', mb: 1 }}>
          <Typography variant="h4" component="div" fontWeight="bold">
            {value}
          </Typography>
          {unit && (
            <Typography variant="body2" color="text.secondary" sx={{ ml: 0.5 }}>
              {unit}
            </Typography>
          )}
        </Box>
        
        {(trend || trendValue) && (
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
            {getTrendIcon()}
            <Typography variant="caption" color={getTrendColor()} fontWeight="medium">
              {trendValue}
            </Typography>
            <Typography variant="caption" color="text.secondary">
              vs last period
            </Typography>
          </Box>
        )}
      </CardContent>
    </Card>
  );
}

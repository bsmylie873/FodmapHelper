import React from 'react';

type FodmapLevel = 'low' | 'medium' | 'high';

interface FodmapBadgeProps {
  level: FodmapLevel;
  size?: 'sm' | 'md' | 'lg';
  showText?: boolean;
}

const FodmapBadge: React.FC<FodmapBadgeProps> = ({
  level,
  size = 'md',
  showText = true
}) => {
  const colorMap = {
    low: 'bg-green-100 text-green-800 border-green-200',
    medium: 'bg-amber-100 text-amber-800 border-amber-200',
    high: 'bg-red-100 text-red-800 border-red-200'
  };

  const sizeMap = {
    sm: 'text-xs px-2 py-0.5',
    md: 'text-sm px-2.5 py-0.5',
    lg: 'text-base px-3 py-1'
  };

  return (
    <span className={`inline-flex items-center rounded-full border ${colorMap[level]} ${sizeMap[size]}`}>
      <span className={`rounded-full h-2 w-2 mr-1 ${level === 'low' ? 'bg-green-500' : level === 'medium' ? 'bg-amber-500' : 'bg-red-500'}`}></span>
      {showText && <span className="font-medium capitalize">{level}</span>}
    </span>
  );
};

export default FodmapBadge; 
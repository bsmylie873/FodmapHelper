import React from 'react';
import { Link } from 'react-router-dom';
import FodmapBadge from './FodmapBadge';

interface FoodCardProps {
  id: string;
  name: string;
  fodmapLevel: 'low' | 'medium' | 'high';
  category: string;
  servingSize: string;
  imageUrl?: string;
}

const FoodCard: React.FC<FoodCardProps> = ({
  id,
  name,
  fodmapLevel,
  category,
  servingSize,
  imageUrl
}) => {
  return (
    <Link to={`/foods/${id}`} className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-lg transition-shadow duration-300">
      <div className="p-4">
        <div className="flex items-start justify-between">
          <h3 className="text-lg font-medium text-gray-900 mb-1">{name}</h3>
          <FodmapBadge level={fodmapLevel} />
        </div>
        <p className="text-sm text-gray-500 mb-2">{category}</p>
        <div className="text-xs text-gray-600">
          <span className="font-semibold">Serving:</span> {servingSize}
        </div>
      </div>
    </Link>
  );
};

export default FoodCard; 
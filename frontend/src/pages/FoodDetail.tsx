import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import FodmapBadge from '../components/FodmapBadge';

interface Food {
  id: string;
  name: string;
  fodmapLevel: 'low' | 'medium' | 'high';
  category: string;
  servingSize: string;
  description?: string;
  notes?: string;
  alternatives?: string[];
}

const FoodDetail: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const [food, setFood] = useState<Food | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchFood = async () => {
      try {
        const response = await fetch(`/foods/${id}`);
        if (!response.ok) {
          throw new Error('Failed to fetch food details');
        }
        const data = await response.json();
        setFood(data);
      } catch (err) {
        setError('Failed to load food details. Please try again later.');
        console.error('Food detail fetch error:', err);
      } finally {
        setIsLoading(false);
      }
    };

    if (id) {
      fetchFood();
    }
  }, [id]);

  if (isLoading) {
    return <div className="text-center text-gray-600">Loading food details...</div>;
  }

  if (error || !food) {
    return (
      <div className="text-center">
        <div className="text-red-600 mb-4">{error || 'Food not found'}</div>
        <Link to="/foods" className="text-teal-600 hover:text-teal-700">
          Return to Food List
        </Link>
      </div>
    );
  }

  return (
    <div className="max-w-3xl mx-auto">
      <div className="bg-white rounded-lg shadow-md p-6">
        <div className="flex items-start justify-between mb-4">
          <h1 className="text-3xl font-bold text-gray-900">{food.name}</h1>
          <FodmapBadge level={food.fodmapLevel} size="lg" />
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h2 className="text-lg font-semibold text-gray-800 mb-2">Details</h2>
            <dl className="space-y-2">
              <div>
                <dt className="text-sm font-medium text-gray-500">Category</dt>
                <dd className="text-gray-900">
                  <Link to={`/categories/${food.category}`} className="hover:text-teal-600">
                    {food.category}
                  </Link>
                </dd>
              </div>
              <div>
                <dt className="text-sm font-medium text-gray-500">Serving Size</dt>
                <dd className="text-gray-900">{food.servingSize}</dd>
              </div>
            </dl>
          </div>

          {food.description && (
            <div>
              <h2 className="text-lg font-semibold text-gray-800 mb-2">Description</h2>
              <p className="text-gray-600">{food.description}</p>
            </div>
          )}
        </div>

        {food.notes && (
          <div className="mt-6">
            <h2 className="text-lg font-semibold text-gray-800 mb-2">Notes</h2>
            <p className="text-gray-600">{food.notes}</p>
          </div>
        )}

        {food.alternatives && food.alternatives.length > 0 && (
          <div className="mt-6">
            <h2 className="text-lg font-semibold text-gray-800 mb-2">Alternative Options</h2>
            <ul className="list-disc list-inside text-gray-600">
              {food.alternatives.map((alt, index) => (
                <li key={index}>{alt}</li>
              ))}
            </ul>
          </div>
        )}

        <div className="mt-8 pt-6 border-t border-gray-200">
          <Link
            to="/foods"
            className="text-teal-600 hover:text-teal-700 font-medium"
          >
            ← Back to Food List
          </Link>
        </div>
      </div>
    </div>
  );
};

export default FoodDetail; 
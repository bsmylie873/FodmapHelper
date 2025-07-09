import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import FoodCard from '../components/FoodCard';
import SearchBar from '../components/SearchBar';

interface Food {
  id: string;
  name: string;
  fodmapLevel: 'low' | 'medium' | 'high';
  category: string;
  servingSize: string;
}

const FoodList: React.FC = () => {
  const { category } = useParams<{ category?: string }>();
  const [foods, setFoods] = useState<Food[]>([]);
  const [filteredFoods, setFilteredFoods] = useState<Food[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchFoods = async () => {
      try {
        const url = category ? `/foods?category=${category}` : '/foods';
        const response = await fetch(url);
        if (!response.ok) {
          throw new Error('Failed to fetch foods');
        }
        const data = await response.json();
        setFoods(data);
        setFilteredFoods(data);
      } catch (err) {
        setError('Failed to load foods. Please try again later.');
        console.error('Foods fetch error:', err);
      } finally {
        setIsLoading(false);
      }
    };

    fetchFoods();
  }, [category]);

  const handleSearch = (query: string) => {
    const searchTerm = query.toLowerCase();
    const filtered = foods.filter(food =>
      food.name.toLowerCase().includes(searchTerm) ||
      food.category.toLowerCase().includes(searchTerm)
    );
    setFilteredFoods(filtered);
  };

  if (isLoading) {
    return <div className="text-center text-gray-600">Loading foods...</div>;
  }

  if (error) {
    return <div className="text-center text-red-600">{error}</div>;
  }

  return (
    <div>
      <h1 className="text-3xl font-bold text-gray-900 mb-6">
        {category ? `${category} Foods` : 'All Foods'}
      </h1>

      <div className="max-w-2xl mx-auto mb-8">
        <SearchBar
          onSearch={handleSearch}
          placeholder="Filter foods..."
        />
      </div>

      {filteredFoods.length === 0 ? (
        <div className="text-center text-gray-600">
          No foods found. Try adjusting your search.
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredFoods.map((food) => (
            <FoodCard
              key={food.id}
              id={food.id}
              name={food.name}
              fodmapLevel={food.fodmapLevel}
              category={food.category}
              servingSize={food.servingSize}
            />
          ))}
        </div>
      )}
    </div>
  );
};

export default FoodList; 
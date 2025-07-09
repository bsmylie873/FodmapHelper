import React, { useState } from 'react';
import SearchBar from '../components/SearchBar';
import FoodCard from '../components/FoodCard';

interface Food {
  id: string;
  name: string;
  fodmapLevel: 'low' | 'medium' | 'high';
  category: string;
  servingSize: string;
}

const Search: React.FC = () => {
  const [searchResults, setSearchResults] = useState<Food[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSearch = async (query: string) => {
    if (!query.trim()) {
      setSearchResults([]);
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      const response = await fetch(`/foods/search?q=${encodeURIComponent(query)}`);
      if (!response.ok) {
        throw new Error('Failed to fetch search results');
      }
      const data = await response.json();
      setSearchResults(data);
    } catch (err) {
      setError('An error occurred while searching. Please try again.');
      console.error('Search error:', err);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div>
      <h1 className="text-3xl font-bold text-gray-900 mb-6">Search Foods</h1>
      <div className="max-w-2xl mx-auto mb-8">
        <SearchBar onSearch={handleSearch} placeholder="Search for foods..." />
      </div>

      {isLoading && (
        <div className="text-center text-gray-600">Loading...</div>
      )}

      {error && (
        <div className="text-center text-red-600 mb-4">{error}</div>
      )}

      {!isLoading && !error && searchResults.length === 0 && (
        <div className="text-center text-gray-600">
          No results found. Try searching for a different food.
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {searchResults.map((food) => (
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
    </div>
  );
};

export default Search; 
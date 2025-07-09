import React from 'react';
import { Link } from 'react-router-dom';

const Home: React.FC = () => {
  return (
    <div className="text-center">
      <h1 className="text-4xl font-bold text-gray-900 mb-8">
        Welcome to FODMAP Helper
      </h1>
      <p className="text-xl text-gray-600 mb-8">
        Your guide to managing FODMAP-related dietary needs
      </p>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-4xl mx-auto">
        <Link
          to="/foods"
          className="p-6 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow"
        >
          <h2 className="text-xl font-semibold text-gray-900 mb-2">Food List</h2>
          <p className="text-gray-600">Browse our comprehensive database of FODMAP-rated foods</p>
        </Link>
        <Link
          to="/categories"
          className="p-6 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow"
        >
          <h2 className="text-xl font-semibold text-gray-900 mb-2">Categories</h2>
          <p className="text-gray-600">Explore foods by category</p>
        </Link>
        <Link
          to="/search"
          className="p-6 bg-white rounded-lg shadow-md hover:shadow-lg transition-shadow"
        >
          <h2 className="text-xl font-semibold text-gray-900 mb-2">Search</h2>
          <p className="text-gray-600">Find specific foods and their FODMAP ratings</p>
        </Link>
      </div>
    </div>
  );
};

export default Home; 
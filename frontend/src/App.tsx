import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainLayout from './layout/MainLayout';
import Home from './pages/Home';
import FoodList from './pages/FoodList';
import FoodDetail from './pages/FoodDetail';
import Categories from './pages/Categories';
import Search from './pages/Search';
import About from './pages/About';

export function App() {
  return (
    <Router>
      <MainLayout>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/foods" element={<FoodList />} />
          <Route path="/foods/:id" element={<FoodDetail />} />
          <Route path="/categories" element={<Categories />} />
          <Route path="/categories/:category" element={<FoodList />} />
          <Route path="/search" element={<Search />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </MainLayout>
    </Router>
  );
} 
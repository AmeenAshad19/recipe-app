// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes, useNavigate } from 'react-router-dom';
import { Container } from '@mui/material';
import RecipeGallery from './components/RecipeGallery';
import RecipeDetails from './components/RecipeDetails';
import Header from './components/Header';

// Custom hook to get search query from URL query parameters
const useQuery = () => {
    return new URLSearchParams(window.location.search);
};

const App = () => {
    const query = useQuery();
    const searchQuery = query.get('search') || '';
    const navigate = useNavigate();

    const handleSearch = (query) => {
        navigate(`/?search=${query}`);
    };

    return (
        <>
            <Header onSearch={handleSearch} />
            <Container sx={{ mt: 15 }}>
                <Routes>
                    <Route path="/" element={<RecipeGallery searchQuery={searchQuery} />} />
                    <Route path="/recipe/:id" element={<RecipeDetails />} />
                </Routes>
            </Container>
        </>
    );
};

const AppWithRouter = () => (
    <Router>
        <App />
    </Router>
);

export default AppWithRouter;

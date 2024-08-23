import React, { useEffect, useState, useCallback } from 'react';
import { Card, CardContent, CardMedia, Grid, Typography, Button, Link as MuiLink } from '@mui/material';
import axios from 'axios';

const RecipeGallery = ({ searchQuery }) => {
    const [recipes, setRecipes] = useState([]);
    const [searchTerm, setSearchTerm] = useState(searchQuery);

    const fetchRecipes = useCallback(() => {
        const searchParam = searchTerm ? `?search=${searchTerm}` : '';
        // axios.get(`http://127.0.0.1:8000/api/recipes/${searchParam}`)
        const apiUrl = `${process.env.REACT_APP_API_URL}${searchParam}`;
        console.log('Requesting URL:', apiUrl);
        axios.get(apiUrl)
            .then(response => {
                setRecipes(response.data);
            })
            .catch(error => console.error('There was an error fetching the recipes!', error));
    }, [searchTerm]);

    useEffect(() => {
        setSearchTerm(searchQuery);
    }, [searchQuery]);

    useEffect(() => {
        fetchRecipes();
    }, [fetchRecipes]);

    return (
        <>
            <Grid 
                container 
                spacing={4} 
                sx={{ 
                    mt: 2, 
                    minHeight: '50vh', // Ensures container height for vertical centering
                    display: 'flex', 
                    justifyContent: 'center', 
                    alignItems: 'center'
                }}
            >
                {recipes.length > 0 ? (
                    recipes.map(recipe => (
                        <Grid item xs={12} sm={6} md={4} key={recipe.id}>
                            <Card>
                                <CardMedia
                                    component={MuiLink}
                                    href={`/recipe/${recipe.id}`}
                                    sx={{ 
                                        height: 180, 
                                        transition: 'transform 0.3s ease-in-out', // Smooth transition
                                        '&:hover': { 
                                            transform: 'scale(1.05) translateY(-5px)', // Slight zoom and lift effect on hover
                                            cursor: 'pointer'
                                        },  
                                    }}
                                    image={recipe.image_url || 'https://via.placeholder.com/150'}
                                    alt={recipe.title}
                                />
                                <CardContent>
                                    <Typography variant="h6" component="div">
                                        {recipe.title}
                                    </Typography>
                                    <Typography variant="body2" color="text.secondary">
                                        {recipe.description.slice(0, 90)}...
                                    </Typography>
                                    <Button 
                                        variant="contained" 
                                        color="primary" 
                                        sx={{ mt: 1, '&:hover': { backgroundColor: 'primary.dark' } }}  // Styled button with hover effect
                                        href={`/recipe/${recipe.id}`}
                                    >
                                        View Recipe
                                    </Button>
                                </CardContent>
                            </Card>
                        </Grid>
                    ))
                ) : (
                    <Grid item>
                        <Typography variant="h6" align="center">No recipes found</Typography>
                    </Grid>
                )}
            </Grid>
        </>
    );
};

export default RecipeGallery;

// src/components/RecipeDetails.js

import React, { useEffect, useState } from 'react';
import { useParams} from 'react-router-dom';
import { Card, CardMedia, CardContent, Typography, Container, List, ListItem, ListItemText } from '@mui/material';
import axios from 'axios';

const RecipeDetails = () => {
    const { id } = useParams();
    const [recipe, setRecipe] = useState(null);

    useEffect(() => {
        // axios.get(`http://127.0.0.1:8000/api/recipes/${id}/`)
        axios.get(`${process.env.REACT_APP_API_URL}${id}/`)
            .then(response => setRecipe(response.data))
            .catch(error => console.error('There was an error fetching the recipe details!', error));
    }, [id]);

    if (!recipe) return <Typography variant="h6">Loading...</Typography>;

    return (
        <Container>
            <Card sx={{ mt: 3, p: 2 }}>
                <CardMedia
                    component="img"
                    height="300"
                    image={recipe.image_url || 'https://via.placeholder.com/300'}
                    alt={recipe.title}
                />
                <CardContent>
                    <Typography variant="h4" component="div" gutterBottom>
                        {recipe.title}
                    </Typography>
                    <Typography variant="body1" paragraph>
                        {recipe.description}
                    </Typography>

                    {/* Ingredients Section */}
                    <Card sx={{ backgroundColor: '#f5f5dc', p: 2, mt: 2 }}>
                        <Typography variant="h6" component="div" gutterBottom>
                            Ingredients:
                        </Typography>
                        <List sx={{ listStyleType: 'disc', pl: 2 }}>
                            {recipe.ingredients.map((ingredient, index) => (
                                <ListItem key={index} sx={{ display: 'list-item', py: 0.3, pl: 1 }}>
                                    <ListItemText primary={ingredient} />
                                </ListItem>
                            ))}
                        </List>
                    </Card>

                    {/* Instructions Section */}
                    <Card sx={{ backgroundColor: '#f5f5dc', p: 2, mt: 3 }}>
                        <Typography variant="h6" component="div" gutterBottom>
                            Instructions:
                        </Typography>
                        <List sx={{ listStyleType: 'decimal', pl: 4 }}>
                            {recipe.instructions.map((instruction, index) => (
                                <ListItem key={index} sx={{ display: 'list-item', py: 0.3 }}>
                                    <ListItemText primary={instruction} />
                                </ListItem>
                            ))}
                        </List>
                    </Card>
                </CardContent>
            </Card>
        </Container>
    );
};

export default RecipeDetails;

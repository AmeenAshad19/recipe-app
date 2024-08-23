import React, { useState } from 'react';
import { TextField, IconButton, Autocomplete } from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';

const SearchBar = ({ onSearch, placeholder = "Search recipes..." }) => {
    const [query, setQuery] = useState('');
    const [previousQueries, setPreviousQueries] = useState([]);

    const recommendations = ["dessert", "chicken", "indian", "spicy", "snack"];
    const maxPreviousQueries = 3;  // Maximum number of previous searches to display

    // Filter out previous queries that are already in recommendations
    const filteredPreviousQueries = previousQueries.filter(
        (prevQuery) => !recommendations.includes(prevQuery)
    );

    const suggestions = [...recommendations, ...filteredPreviousQueries];

    const handleSearch = () => {
        if (query.trim()) {
            onSearch(query);
            setPreviousQueries(prev => {
                let newQueries = [...prev];
                // Add the query if it's not already in the previous queries list
                if (!newQueries.includes(query)) {
                    newQueries.push(query);
                }
                // Limit to maxPreviousQueries
                if (newQueries.length > maxPreviousQueries) {
                    newQueries = newQueries.slice(-maxPreviousQueries);
                }
                return newQueries;
            });
        }
    };

    return (
        <div style={{ display: 'flex', alignItems: 'center', marginBottom: '16px'}}>
            <Autocomplete
                freeSolo
                options={suggestions}
                onInputChange={(event, newInputValue) => {
                    setQuery(newInputValue);
                }}
                inputValue={query}
                renderInput={(params) => (
                    <TextField
                        {...params}
                        variant="outlined"
                        placeholder={placeholder}
                        size="medium"
                        onKeyPress={(e) => {
                            if (e.key === 'Enter') handleSearch();
                        }}
                        sx={{
                            mr: 1,
                            width: '350px',
                            '& .MuiOutlinedInput-root': {
                                borderRadius: '20px',
                                '& fieldset': {
                                    borderColor: '#ffffff',
                                    borderWidth: '3px',
                                },
                                '&:hover fieldset': {
                                    borderColor: '#ffffff',
                                    borderWidth: '3.3px',
                                },
                                '&.Mui-focused fieldset': {
                                    borderColor: '#ffffff',
                                    borderWidth: '3px',
                                },
                            },
                            '& .MuiInputBase-input': {
                                color: '#ffffff',
                            },
                        }}
                    />
                )}
            />
            <IconButton
                onClick={handleSearch}
                sx={{
                    color: '#ffffff',
                    '& .MuiSvgIcon-root': {
                        fontSize: '2.0rem',
                        fontWeight: 'bold',
                    },
                }}
            >
                <SearchIcon />
            </IconButton>
        </div>
    );
};

export default SearchBar;

// src/components/Header.js
import React from 'react';
import { AppBar, Toolbar, Typography, Container } from '@mui/material';
import SearchBar from './SearchBar';

const Header = ({ onSearch }) => {
    return (
        <AppBar
            position="fixed"
            sx={{
                backgroundColor: '#ff7043',
                boxShadow: '0px 4px 20px rgba(0,0,0,0.2)',
                height: '120px', // Increase height here
                borderBottom: '3px solid #000000', // Black border below header
            }}
        >
            <Toolbar sx={{ height: '100%' }}>
                <Container maxWidth="lg" sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                    <Typography
                        variant="h2"
                        component="div"
                        sx={{
                            flexGrow: 1,
                            fontWeight: 'bold',
                            color: '#ffffff',
                            fontFamily: 'Brush Script MT, cursive',
                            letterSpacing: '0.05em',
                        }}
                    >
                        FlavorFindr
                    </Typography>
                    <SearchBar onSearch={onSearch} />
                </Container>
            </Toolbar>
        </AppBar>
    );
};

export default Header;

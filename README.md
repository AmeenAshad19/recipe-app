# Recipe Finder Web Application

## Project Information

This document provides an overview of the Recipe Finder web application, developed using React.js for the frontend and Django for the backend. The application is hosted on an AWS EC2 instance and showcases a variety of recipes, enabling users to search for and explore different recipes in a user-friendly format.

### Project Links

- **GitHub Repository:** [Recipe App GitHub Repo](https://github.com/AmeenAshad19/recipe-app)
- **Live Application:** [Recipe Finder App](http://65.0.106.92:3000/) on AWS EC2

### Project Overview

- **Frontend (React.js):**
  - **Recipe Search Functionality:** Users can search for recipes using a search bar with auto-suggestions.
    - Example Searches: `dessert`, `indian`, `sweet`
  - **Recipe Gallery:** Visually appealing display of search results, with images, titles, and links to detailed recipes.
  - **Recipe Details Page:** Detailed view with ingredients, preparation steps, and additional information.

- **Backend (Django):**
  - **API Endpoints:**
    - `/api/recipes/` - Retrieves a list of recipes based on search queries.
    - `/api/recipe/<id>/` - Provides detailed information about a specific recipe.
  - **Database:** SQLite3 for storing recipe data.

- **Hosting:**
  - **AWS EC2:** Deployed on an AWS EC2 instance that handles both frontend and backend services.
  - **Frontend:** Served using a Node.js server.
  - **Backend:** Served using Django’s development server.

### Key Features

- **Dynamic Recipe Gallery:** The gallery adapts to search results, displaying them attractively.
- **Search Functionality:** Provides real-time suggestions for recipe searches.
- **Detailed Recipe View:** Comprehensive recipe information, including ingredients and steps.

---

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.x
- pip (Python package installer)
- Node.js
- npm (Node package manager)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/AmeenAshad19/recipe-app.git
   cd recipe-app
   ```

2. **Backend Setup:**

   Navigate to the `backend/` directory:

   ```bash
   cd backend
   ```

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   Apply migrations and create a superuser:

   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

   Run the Django development server:

   ```bash
   python manage.py runserver
   ```

3. **Frontend Setup:**

   Return to the root directory and navigate to the `frontend/` directory:

   ```bash
   cd ..
   cd frontend
   ```

   Install the required Node.js packages:

   ```bash
   npm install
   ```

   Start the React application:

   ```bash
   NODE_OPTIONS=--openssl-legacy-provider npm start
   ```

### Accessing the Application

- **Frontend:** The React application will be running at [http://localhost:3000/](http://localhost:3000/).
- **Backend:** The Django API will be running at [http://localhost:8000/](http://localhost:8000/).

If deployed on AWS, you can access the application at [http://65.0.106.92:3000/](http://65.0.106.92:3000/).
```

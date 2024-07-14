# API Documentation

## Summary
This API, built with Django Rest Framework, provides endpoints for managing movies, reviews, and streaming platforms. It includes functionality for user authentication and registration. The following sections detail the available endpoints, their methods, and expected responses.

## Movies API

### 1. List Movies
- **URL**: `/movies/`
- **Method**: `GET`
- **Description**: Retrieves a list of all movies.
- **Response**:
  - `200 OK`: A list of movies.
  
### 2. Create a Movie
- **URL**: `/movies/`
- **Method**: `POST`
- **Description**: Creaate a new movie.
- **Request Body**:
  - `title` (string): Name of the movie.
  - `genre` (string): Genre of the movie.
  - `storyline` (string): Plot of the movie.
  - `platform_id` (integer): ID of the Streaming Platform of the movie.
  - `active` (boolean): Status of the movie. Default value is false.
- **Response**:
  - `201 Created`: The created Movie.
  - `400 Bad Request`: Invalid input.
  
### 3. Movie Details
- **URL**: `/movies/<int:pk>/`
- **Method**: `GET`
- **Description**: Retrieves details of a specific movie by its ID.
- **Path Parameters**:
  - `pk` (integer): The ID of the movie.
- **Response**:
  - `200 OK`: Details of the specified movie.
  - `404 Not Found`: Movie not found.

## Reviews API

### 1. Create Review for a Movie
- **URL**: `/movies/<int:pk>/reviews-create/`
- **Method**: `POST`
- **Description**: Creates a new review for a specific movie.
- **Path Parameters**:
  - `pk` (integer): The ID of the movie.
- **Request Body**:
  - `text` (string): The content of the review.
  - `rating` (integer): The rating given to the movie.
- **Response**:
  - `201 Created`: The created review.
  - `400 Bad Request`: Invalid input.

### 2. List Reviews for a Movie
- **URL**: `/movies/<int:pk>/reviews/`
- **Method**: `GET`
- **Description**: Retrieves a list of all reviews for a specific movie.
- **Path Parameters**:
  - `pk` (integer): The ID of the movie.
- **Response**:
  - `200 OK`: A list of reviews for the specified movie.
  - `404 Not Found`: Movie not found.

### 3. Review Details
- **URL**: `/movies/<int:pk>/reviews/<int:review_id>/`
- **Method**: `GET`
- **Description**: Retrieves details of a specific review by its ID.
- **Path Parameters**:
  - `pk` (integer): The ID of the movie.
  - `review_id` (integer): The ID of the review.
- **Response**:
  - `200 OK`: Details of the specified review.
  - `404 Not Found`: Review not found.

## Streaming API

### 1. List Streaming Platforms
- **URL**: `/streaming/`
- **Method**: `GET`
- **Description**: Retrieves a list of all streaming platforms.
- **Response**:
  - `200 OK`: A list of streaming platforms.
    
### 2. Create a Streaming Platform
- **URL**: `/streaming/`
- **Method**: `POST`
- **Description**: Creaate a new Streaming Platform
- **Request Body**:
  - `name` (string): Name of the Streaming Platform.
  - `about` (string): Details of the Streaming Platform.
  - `website` (string): URL of the Streaming Platform.
- **Response**:
  - `201 Created`: The created Streaming Platform.
  - `400 Bad Request`: Invalid input.

### 3. Streaming Platform Details
- **URL**: `/streaming/<int:pk>/`
- **Method**: `GET`
- **Description**: Retrieves details of a specific streaming platform by its ID.
- **Path Parameters**:
  - `pk` (integer): The ID of the streaming platform.
- **Response**:
  - `200 OK`: Details of the specified streaming platform.
  - `404 Not Found`: Streaming platform not found.

## Authentication API

### 1. User Login
- **URL**: `/login/`
- **Method**: `POST`
- **Description**: Authenticates a user and returns an authentication token.
- **Request Body**:
  - `username` (string): The username of the user.
  - `password` (string): The password of the user.
- **Response**:
  - `200 OK`: Authentication token.
  - `400 Bad Request`: Invalid credentials.

### 9. User Registration
- **URL**: `/register/`
- **Method**: `POST`
- **Description**: Registers a new user.
- **Request Body**:
  - `username` (string): The desired username.
  - `email` (string): The email address.
  - `password` (string): The desired password.
  - `password2`(string): COnfirm password by entering again.
- **Response**:
  - `201 Created`: User registered successfully.
  - `400 Bad Request`: Invalid input.

### 10. User Logout
- **URL**: `/logout/`
- **Method**: `POST`
- **Description**: Logs out the authenticated user.
- **Response**:
  - `200 OK`: User logged out successfully.
  - `401 Unauthorized`: No user is authenticated.

## General Notes
- **Authentication**: Most endpoints require the user to be authenticated. Ensure to include the authentication token in the request headers.
- **Status Codes**: Each endpoint returns appropriate HTTP status codes to indicate the result of the request.

## Testing:
- Test cases have been added for all endpoints.
- Before making any changes to the project, ensure to add new test cases for the changes.
- Run existing test cases to verify they are working correctly.
- Use the following command to run tests:
  ```sh
  python manage.py test
## How to Use this API

To use this API from the repository, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone <repository-url>
   cd <repository-directory>
2. **Set Up the Virtual Environment:**:
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
3. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
4. **Run Migrations**:
   ```sh
   python manage.py migrate
5. **Start the Development Server**:
   ```sh
   python manage.py runserver
6. **Access the API**:
   - The API will be available at http://127.0.0.1:8000/.
   - Use tools like curl, Postman, or your frontend application to interact with the endpoints.
